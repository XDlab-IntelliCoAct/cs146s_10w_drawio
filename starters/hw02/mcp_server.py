"""MCP 传输骨架，工具实现在 tools.py 中；stdout 只用于协议通信。"""
from mcp.server.fastmcp import FastMCP
from tools import read_tool, inspect_tool

server = FastMCP("cs146s-diagram-lab")


@server.tool()
def read_diagram(name: str) -> dict:
    """读取实验工作区中的未压缩 .drawio 文件。"""
    return read_tool(name)


@server.tool()
def inspect_diagram(name: str) -> dict:
    """检查图表名称和端点引用，不修改文件。"""
    return inspect_tool(name)


if __name__ == "__main__":
    server.run(transport="stdio")
