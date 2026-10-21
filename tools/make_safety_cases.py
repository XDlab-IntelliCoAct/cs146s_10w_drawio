"""在本地生成文件大小、页数、图元数量和解压内容上限附近的测试输入。"""
import argparse
import base64
import copy
import urllib.parse
import xml.etree.ElementTree as ET
import zlib
from pathlib import Path
from make_cases import document, write


def generate(output: Path):
    output.mkdir(parents=True, exist_ok=True)
    if any(output.iterdir()):
        raise FileExistsError("请指定空的输出目录")
    data = ET.tostring(document(), encoding="utf-8")
    for size in (2 * 1024 * 1024, 2 * 1024 * 1024 + 1):
        (output / f"bytes-{size}.drawio").write_bytes(data + b" " * (size - len(data)))
    for count in (20, 21):
        root = ET.Element("mxfile")
        for i in range(count):
            page = copy.deepcopy(document(0).find("diagram"))
            page.set("id", f"page-{i}")
            root.append(page)
        write(root, output / f"pages-{count}.drawio")
    for count in (10000, 10001):
        root = document(5000)
        if count == 10000:
            graph = root.find(".//root")
            graph.remove(graph.findall("mxCell")[-1])
        write(root, output / f"cells-{count}.drawio")
    root = document(0)
    page = root.find("diagram")
    page.remove(page.find("mxGraphModel"))
    expanded = '<mxGraphModel><root><!--' + 'x' * (8 * 1024 * 1024) + '--></root></mxGraphModel>'
    compressor = zlib.compressobj(wbits=-15)
    payload = urllib.parse.quote(expanded, safe="~()*!.'-").encode("utf-8")
    page.text = base64.b64encode(compressor.compress(payload) + compressor.flush()).decode("ascii")
    write(root, output / "expanded-over-limit.drawio")
    for file in sorted(output.iterdir()):
        print(file.name, file.stat().st_size)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", required=True, type=Path, help="保存安全测试输入的空目录")
    args = parser.parse_args()
    generate(args.output)
