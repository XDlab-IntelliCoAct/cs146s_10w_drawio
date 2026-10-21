"""在 run_agent 中实现 Agent 控制循环；测试时可传入预设模型响应。"""
import os
from pathlib import Path
from typing import Callable
from tools import TOOLS, dispatch

MAX_TURNS = 8
MAX_TOOL_CALLS = 12


def local_model(messages: list[dict], tools: list[dict]) -> dict:
    from dotenv import load_dotenv
    from ollama import Client
    load_dotenv(Path(__file__).with_name(".env"))
    client = Client(host=os.getenv("OLLAMA_HOST", "http://127.0.0.1:11434"), timeout=120)
    return client.chat(model=os.getenv("OLLAMA_MODEL", "qwen3:4b-q4_K_M"), messages=messages, tools=tools).message.model_dump()


def run_agent(request: str, model: Callable = local_model) -> dict:
    # TODO: 返回 {answer, stop_reason, events}，记录实际执行过程。
    # 按顺序处理每个工具调用，保存 assistant 消息和工具返回消息。
    # 分别统计模型请求轮数和工具调用次数；修改要求不明确时询问用户。
    # 根据最新工具结果核对最终回答，完成修改后需要复查。
    raise NotImplementedError("请先实现有轮数与调用次数限制的 Agent 循环，以及任务完成判断")


if __name__ == "__main__":
    import json
    request = input("请输入任务: ").strip()
    if not request:
        raise SystemExit("任务不能为空")
    print(json.dumps(run_agent(request), ensure_ascii=False, indent=2))
