"""在临时副本中演示读取、改名和版本冲突。"""
import shutil
import sys
import tempfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from shared.diagram_io import DiagramError, apply_operations, read_diagram

root = Path(__file__).resolve().parents[2]
parent = root / ".runtime/hw02/adapter-demo"
parent.mkdir(parents=True, exist_ok=True)
with tempfile.TemporaryDirectory(dir=parent) as temporary:
    workspace = Path(temporary)
    shutil.copyfile(root / "materials/fixtures/normal.drawio", workspace / "demo.drawio")
    before = read_diagram(workspace, "demo.drawio")
    operation = {"op": "rename_node", "page_id": "page-a", "cell_id": "n1", "label": "接收资料"}
    after = apply_operations(workspace, "demo.drawio", before["version"], [operation])
    print("读取页面:", before["pages"][0]["id"])
    print("版本是否变化:", before["version"] != after["version"])
    try:
        apply_operations(workspace, "demo.drawio", before["version"], [operation])
    except DiagramError as error:
        print("旧版本写入被拒绝:", error)
    else:
        raise RuntimeError("预期出现版本冲突，但旧版本写入未被拒绝")
