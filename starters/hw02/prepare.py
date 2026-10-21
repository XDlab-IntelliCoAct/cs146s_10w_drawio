"""将练习图表复制到本地工作区；目标已存在时停止。"""
import shutil
from pathlib import Path

root = Path(__file__).resolve().parents[2]
workspace = root / ".runtime/hw02/workspace"
workspace.mkdir(parents=True, exist_ok=True)
target = workspace / "practice.drawio"
if target.exists():
    raise SystemExit("practice.drawio exists; keep it or rename it before preparing a new exercise")
shutil.copyfile(root / "materials/fixtures/labels.drawio", target)
print(target)
