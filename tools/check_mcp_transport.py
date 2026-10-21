"""检查课程提供的 stdio 传输骨架；工具行为由 HW2 完成后另行验证。"""
import asyncio
import sys
from pathlib import Path
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client


async def main():
    server = Path(__file__).resolve().parents[1] / "starters/hw02/mcp_server.py"
    async with stdio_client(StdioServerParameters(command=sys.executable, args=[str(server)])) as (read, write):
        async with ClientSession(read, write) as session:
            await session.initialize()
            result = await session.list_tools()
            names = {t.name for t in result.tools}
            assert {"read_diagram", "inspect_diagram"} <= names, names
            print("MCP 初始化和工具发现通过:", ", ".join(sorted(names)))
            called = await session.call_tool("read_diagram", {"name": "practice.drawio"})
            if called.isError:
                print("工具尚未实现，传输骨架已返回相应错误响应。")
            else:
                print("工具已返回结果，请使用 HW2 客户端和测试核对具体行为。")


if __name__ == "__main__":
    asyncio.run(main())
