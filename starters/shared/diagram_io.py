"""HW2 的文件适配器，提供未压缩 mxfile 的解析和受控写入。

学生在此基础上实现工具策略和 Agent 控制。HW3 起在教学项目中
实现产品的数据适配，包括压缩页面处理。
"""
from __future__ import annotations

import hashlib
import os
import tempfile
import xml.etree.ElementTree as ET
from pathlib import Path

MAX_BYTES = 2 * 1024 * 1024


class DiagramError(ValueError):
    pass


def workspace_file(workspace: Path, name: str) -> Path:
    root = workspace.resolve(strict=True)
    if not isinstance(name, str) or not name or Path(name).name != name or any(c in name for c in '/\\<>:"|?*\x00\r\n'):
        raise DiagramError("请提供工作区中的文件名，不包含目录")
    if Path(name).suffix.lower() != ".drawio":
        raise DiagramError("文件扩展名必须为 .drawio")
    candidate = root / name
    if candidate.is_symlink() or (candidate.exists() and candidate.resolve().parent != root):
        raise DiagramError("不接受符号链接或指向工作区外的路径")
    return candidate


def _read(path: Path) -> tuple[bytes, ET.Element]:
    if path.stat().st_size > MAX_BYTES:
        raise DiagramError("输入文件超过 2 MiB 上限")
    data = path.read_bytes()
    if len(data) > MAX_BYTES:
        raise DiagramError("输入文件超过 2 MiB 上限")
    text = data.decode("utf-8-sig")
    if "<!DOCTYPE" in text.upper() or "<!ENTITY" in text.upper():
        raise DiagramError("不接受 DTD 或实体声明")
    try:
        root = ET.fromstring(text)
    except ET.ParseError as exc:
        raise DiagramError(f"XML 格式无效: {exc}") from exc
    if root.tag != "mxfile":
        raise DiagramError("输入必须为未压缩的 mxfile")
    pages = root.findall("diagram")
    if not pages or any(page.find("mxGraphModel/root") is None for page in pages):
        raise DiagramError("每个页面必须包含未压缩的 mxGraphModel")
    return data, root


def _snapshot(data: bytes, root: ET.Element) -> dict:
    pages = []
    for page in root.findall("diagram"):
        cells = [dict(cell.attrib) for cell in page.findall("mxGraphModel/root/mxCell")]
        pages.append({"id": page.get("id"), "name": page.get("name"), "cells": cells})
    return {"version": hashlib.sha256(data).hexdigest(), "pages": pages}


def read_diagram(workspace: Path, name: str) -> dict:
    return _snapshot(*_read(workspace_file(workspace, name)))


def apply_operations(workspace: Path, name: str, expected_version: str, operations: list[dict]) -> dict:
    """在内存副本上完成一批操作，全部成功后替换文件。

    学生实现的工具负责 JSON 参数校验和执行策略；适配器另外检查
    图元引用和文件版本，并在写入失败时保护原文件。
    """
    path = workspace_file(workspace, name)
    data, root = _read(path)
    if hashlib.sha256(data).hexdigest() != expected_version:
        raise DiagramError("version_conflict: 文件已变化，请重新读取")
    if not isinstance(operations, list) or not operations or len(operations) > 20:
        raise DiagramError("每批应包含 1–20 项操作")
    for op in operations:
        if not isinstance(op, dict):
            raise DiagramError("每项操作必须是对象")
        page = next((p for p in root.findall("diagram") if p.get("id") == op.get("page_id")), None)
        if page is None:
            raise DiagramError("找不到 page_id 对应的页面")
        graph = page.find("mxGraphModel/root")
        cells = {c.get("id"): c for c in graph.findall("mxCell")}
        kind = op.get("op")
        cell_id = op.get("cell_id")
        if not isinstance(cell_id, str) or not cell_id or cell_id in {"0", "1"}:
            raise DiagramError("cell_id 无效或使用了结构根节点 ID")
        if kind == "rename_node":
            cell = cells.get(cell_id)
            if cell is None or cell.get("vertex") != "1" or not isinstance(op.get("label"), str):
                raise DiagramError("rename_node 需要已有节点和字符串 label")
            cell.set("value", op["label"])
        elif kind in {"add_edge", "set_endpoints"}:
            for key in ("source", "target"):
                endpoint = cells.get(op.get(key))
                if endpoint is None or endpoint.get("vertex") != "1":
                    raise DiagramError(f"{key} 引用的节点不存在")
            if kind == "add_edge":
                if cell_id in cells:
                    raise DiagramError("cell_id 已存在")
                cell = ET.SubElement(graph, "mxCell", {"id": cell_id, "edge": "1", "parent": "1"})
                ET.SubElement(cell, "mxGeometry", {"relative": "1", "as": "geometry"})
            else:
                cell = cells.get(cell_id)
                if cell is None or cell.get("edge") != "1":
                    raise DiagramError("set_endpoints 只能用于已有连接")
            cell.set("source", op["source"])
            cell.set("target", op["target"])
        else:
            raise DiagramError("未知操作类型")
    output = ET.tostring(root, encoding="utf-8", xml_declaration=True)
    if len(output) > MAX_BYTES:
        raise DiagramError("修改后的文件超过 2 MiB 上限")
    temporary = None
    try:
        with tempfile.NamedTemporaryFile(dir=path.parent, suffix=".tmp", delete=False) as handle:
            temporary = Path(handle.name)
            handle.write(output)
        if hashlib.sha256(path.read_bytes()).hexdigest() != expected_version:
            raise DiagramError("version_conflict: 写入前文件已变化")
        os.replace(temporary, path)
    finally:
        if temporary is not None:
            temporary.unlink(missing_ok=True)
    return read_diagram(workspace, name)
