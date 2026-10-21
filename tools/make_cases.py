"""生成课程人工图表案例和本地性能实验输入。"""
from __future__ import annotations
import argparse
import base64
import copy
import urllib.parse
import xml.etree.ElementTree as ET
import zlib
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def document(nodes=3, prefix="Step"):
    root = ET.Element("mxfile")
    page = ET.SubElement(root, "diagram", {"id": "page-a", "name": "流程 A"})
    graph = ET.SubElement(ET.SubElement(page, "mxGraphModel"), "root")
    ET.SubElement(graph, "mxCell", {"id": "0"})
    ET.SubElement(graph, "mxCell", {"id": "1", "parent": "0"})
    for i in range(nodes):
        cell = ET.SubElement(graph, "mxCell", {"id": f"n{i+1}", "value": f"{prefix} {i+1}", "vertex": "1", "parent": "1", "style": "rounded=1;courseRole=process;"})
        ET.SubElement(cell, "mxGeometry", {"x": str((i%10)*160), "y": str((i//10)*100), "width": "120", "height": "50", "as": "geometry"})
    for i in range(nodes-1):
        cell = ET.SubElement(graph, "mxCell", {"id": f"e{i+1}", "edge": "1", "parent": "1", "source": f"n{i+1}", "target": f"n{i+2}"})
        ET.SubElement(cell, "mxGeometry", {"relative": "1", "as": "geometry"})
    return root


def write(root, target):
    target.parent.mkdir(parents=True, exist_ok=True)
    ET.ElementTree(root).write(target, encoding="utf-8", xml_declaration=True)


def fixtures():
    dest = ROOT / "materials/fixtures"
    normal = document()
    write(normal, dest / "normal.drawio")
    labels = copy.deepcopy(normal)
    labels.find(".//mxCell[@id='n2']").set("value", "   ")
    write(labels, dest / "labels.drawio")
    html = copy.deepcopy(normal)
    cell = html.find(".//mxCell[@id='n2']")
    cell.set("value", "<b>&nbsp;</b>")
    cell.set("style", "html=1;courseRole=process;")
    write(html, dest / "html-label.drawio")
    edge = copy.deepcopy(normal)
    edge.find(".//mxCell[@id='e1']").set("target", "unknown")
    write(edge, dest / "dangling.drawio")
    free = copy.deepcopy(normal)
    del free.find(".//mxCell[@id='e1']").attrib["target"]
    write(free, dest / "free-endpoint.drawio")
    multiple = copy.deepcopy(normal)
    page = copy.deepcopy(labels.find("diagram"))
    page.set("id", "page-b")
    page.set("name", "流程 B")
    multiple.append(page)
    write(multiple, dest / "multi-page.drawio")
    write(document(0), dest / "empty.drawio")
    grouped = copy.deepcopy(normal)
    graph = grouped.find(".//root")
    group = ET.SubElement(graph, "mxCell", {"id": "group-a", "value": "分组", "vertex": "1", "parent": "1", "style": "group;courseRole=container;"})
    ET.SubElement(group, "mxGeometry", {"width": "600", "height": "200", "as": "geometry"})
    grouped.find(".//mxCell[@id='n2']").set("parent", "group-a")
    for id_, style in (("title", "text;courseRole=annotation;"), ("ornament", "shape=image;courseRole=decoration;")):
        c = ET.SubElement(graph, "mxCell", {"id": id_, "value": "", "vertex": "1", "parent": "1", "style": style})
        ET.SubElement(c, "mxGeometry", {"x": "10", "y": "10", "width": "50", "height": "20", "as": "geometry"})
    wrapped = ET.SubElement(graph, "object", {"id": "wrapped", "label": "注释 < > 中文 😀"})
    c = ET.SubElement(wrapped, "mxCell", {"vertex": "1", "parent": "1", "style": "text;courseRole=annotation;"})
    ET.SubElement(c, "mxGeometry", {"width": "200", "height": "30", "as": "geometry"})
    write(grouped, dest / "grouped.drawio")
    compressed = copy.deepcopy(normal)
    page = compressed.find("diagram")
    xml = ET.tostring(page.find("mxGraphModel"), encoding="unicode")
    page.remove(page.find("mxGraphModel"))
    compressor = zlib.compressobj(wbits=-15)
    encoded = urllib.parse.quote(xml, safe="~()*!.'-").encode("utf-8")
    page.text = base64.b64encode(compressor.compress(encoded) + compressor.flush()).decode("ascii")
    write(compressed, dest / "compressed.drawio")
    malicious = copy.deepcopy(normal)
    malicious.find(".//mxCell[@id='n1']").set("value", '<img src=x onerror="window.__course_injected=true">')
    write(malicious, dest / "text-safety.drawio")
    (dest / "invalid.drawio").write_text("<mxfile><diagram>", encoding="utf-8")
    (dest / "external-entity.drawio").write_text('<!DOCTYPE mxfile [<!ENTITY test SYSTEM "https://example.invalid/course">]><mxfile>&test;</mxfile>', encoding="utf-8")
    for filename, source in (("a-normal.drawio", normal), ("b-warning.drawio", labels), ("c-error.drawio", edge)):
        write(source, dest / "batch" / filename)
    (dest / "batch/d-invalid.drawio").write_text("<mxfile>", encoding="utf-8")


def performance(output: Path, with_issues: bool = False):
    output.mkdir(parents=True, exist_ok=True)
    for name, nodes in (("small", 10), ("medium", 500), ("large", 4900)):
        target = output / f"{name}.drawio"
        if target.exists():
            raise FileExistsError(f"目标文件已存在，请先保留或改名保存: {target}")
        root = document(nodes)
        if with_issues:
            for index, cell in enumerate(root.findall(".//mxCell[@vertex='1']"), 1):
                if index % 5 == 0:
                    cell.set("value", "   ")
        write(root, target)
        print(name, "nodes", nodes, "cells", nodes*2+1, "bytes", target.stat().st_size)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--performance", type=Path, help="在指定本地目录生成含 10、500、4900 个节点的性能输入")
    parser.add_argument("--with-issues", action="store_true", help="性能输入中，每五个步骤将一个名称设为空白")
    args = parser.parse_args()
    if args.with_issues and not args.performance:
        parser.error("--with-issues 需要与 --performance 一起使用")
    if args.performance:
        performance(args.performance, with_issues=args.with_issues)
    else:
        fixtures()
