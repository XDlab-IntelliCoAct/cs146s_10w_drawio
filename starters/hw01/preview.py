"""读取图表规格，生成 SVG 或 draw.io 预览文件。"""
import argparse
import json
import xml.etree.ElementTree as ET
from pathlib import Path


def render(spec: dict, output: Path) -> None:
    nodes = spec["nodes"]
    ids = [node["id"] for node in nodes]
    if not all(isinstance(i, str) and i and i not in {"0", "1"} for i in ids) or len(set(ids)) != len(ids):
        raise ValueError("节点 ID 必须唯一，且不能使用保留值 0 和 1")
    if any(e["source"] not in ids or e["target"] not in ids for e in spec["edges"]):
        raise ValueError("连接端点必须引用已有节点的 ID")
    if output.suffix == ".drawio":
        root = ET.Element("mxfile")
        page = ET.SubElement(root, "diagram", {"id": "preview", "name": "Preview"})
        graph = ET.SubElement(ET.SubElement(page, "mxGraphModel"), "root")
        ET.SubElement(graph, "mxCell", {"id": "0"})
        ET.SubElement(graph, "mxCell", {"id": "1", "parent": "0"})
        for i, node in enumerate(nodes):
            cell = ET.SubElement(graph, "mxCell", {"id": node["id"], "value": node["label"], "vertex": "1", "parent": "1", "style": "rounded=1;whiteSpace=wrap;html=0;"})
            ET.SubElement(cell, "mxGeometry", {"x": "80", "y": str(40 + i * 100), "width": "220", "height": "50", "as": "geometry"})
        used = set(ids) | {"0", "1"}
        for i, edge in enumerate(spec["edges"]):
            edge_id = f"preview-edge-{i}"
            while edge_id in used:
                edge_id += "-"
            used.add(edge_id)
            cell = ET.SubElement(graph, "mxCell", {"id": edge_id, "value": edge["label"], "source": edge["source"], "target": edge["target"], "edge": "1", "parent": "1"})
            ET.SubElement(cell, "mxGeometry", {"relative": "1", "as": "geometry"})
    elif output.suffix == ".svg":
        root = ET.Element("svg", {"xmlns": "http://www.w3.org/2000/svg", "viewBox": f"0 0 650 {max(140, len(nodes)*100+90)}"})
        positions = {node["id"]: (80, 40 + i*100) for i, node in enumerate(nodes)}
        for edge in spec["edges"]:
            x1, y1 = positions[edge["source"]]
            x2, y2 = positions[edge["target"]]
            ET.SubElement(root, "line", {"x1": str(x1+110), "y1": str(y1+50), "x2": str(x2+110), "y2": str(y2), "stroke": "#475569"})
        for node in nodes:
            x, y = positions[node["id"]]
            ET.SubElement(root, "rect", {"x": str(x), "y": str(y), "width": "220", "height": "50", "fill": "#eff6ff", "stroke": "#2563eb"})
            ET.SubElement(root, "text", {"x": str(x+10), "y": str(y+30), "font-size": "14"}).text = node["label"]
        for i, edge in enumerate(spec["edges"]):
            ET.SubElement(root, "text", {"x": "330", "y": str(30+i*20), "font-size": "12"}).text = f'{edge["source"]} → {edge["target"]}: {edge["label"]}'
        for i, question in enumerate(spec["questions"]):
            ET.SubElement(root, "text", {"x": "20", "y": str(len(nodes)*100+35+i*18), "font-size": "12"}).text = "? " + question
        root.set("viewBox", f"0 0 650 {max(140, len(nodes)*100+70+len(spec['questions'])*18, len(spec['edges'])*20+50)}")
    else:
        raise ValueError("输出文件扩展名应为 .svg 或 .drawio")
    output.parent.mkdir(parents=True, exist_ok=True)
    ET.ElementTree(root).write(output, encoding="utf-8", xml_declaration=True)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="将 JSON 图表规格转换为 SVG 或 draw.io 预览。")
    parser.add_argument("input", type=Path, help="包含 nodes、edges 和 questions 的 JSON 文件")
    parser.add_argument("output", type=Path, help="新建的 .svg 或 .drawio 文件路径")
    args = parser.parse_args()
    if args.input.resolve() == args.output.resolve() or args.output.exists():
        parser.error("请使用新的输出路径，不能覆盖输入或已有文件")
    render(json.loads(args.input.read_text(encoding="utf-8")), args.output)
