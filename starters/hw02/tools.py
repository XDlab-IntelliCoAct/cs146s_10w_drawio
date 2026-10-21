"""实现 HW2 的四种工具；文件解析与写入可调用 shared 中的适配器。"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from shared.diagram_io import apply_operations, read_diagram

WORKSPACE = Path(__file__).resolve().parents[2] / ".runtime/hw02/workspace"
TOOLS: list[dict] = []  # TODO: 定义读取、检查、修改和比较工具的描述及参数。


def read_tool(name: str) -> dict:
    # TODO: 校验工具参数，按统一的 ok/data/error 格式返回结果。
    raise NotImplementedError("read_tool")


def inspect_tool(name: str) -> dict:
    # TODO: 检查各页面的名称和端点引用。
    raise NotImplementedError("inspect_tool")


def apply_tool(name: str, expected_version: str, operations: list[dict]) -> dict:
    # TODO: 校验操作并调用 apply_operations，返回实际修改结果。
    raise NotImplementedError("apply_tool")


def compare_tool(before: dict, after: dict) -> dict:
    # TODO: 按页面与图元标识比较快照，列出变化字段。
    # dispatch 根据模型给出的快照标识，取出程序保存的快照字典。
    raise NotImplementedError("compare_tool")


def dispatch(name: str, arguments: dict) -> dict:
    # TODO: 只分发已注册工具，检查参数，并将异常转换为统一结果。
    # 每次运行单独保存快照表，只向模型提供短标识。
    raise NotImplementedError("dispatch")
