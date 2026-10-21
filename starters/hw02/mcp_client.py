"""通过 stdio 连接服务器，发现并调用学生实现的读取与检查工具。"""
import asyncio
import sys
from pathlib import Path
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from shared.tool_result import require_success


async def main():
    server = str(Path(__file__).with_name("mcp_server.py"))
    async with stdio_client(StdioServerParameters(command=sys.executable, args=[server])) as (read, write):
        async with ClientSession(read, write) as session:
            await session.initialize()
            listed = await session.list_tools()
            names = {tool.name for tool in listed.tools}
            assert {"read_diagram", "inspect_diagram"} <= names, names
            for name in ("read_diagram", "inspect_diagram"):
                result = await session.call_tool(name, {"name": "practice.drawio"})
                print(name, result.model_dump_json())
                require_success(result)


if __name__ == "__main__":
    asyncio.run(main())
