"""按顺序返回预设模型消息；消息用尽时抛出 replay_exhausted。"""
import argparse
import json
from pathlib import Path
from agent import run_agent


class ReplayModel:
    def __init__(self, messages: list[dict]):
        self.messages = iter(messages)

    def __call__(self, messages: list[dict], tools: list[dict]) -> dict:
        try:
            response = next(self.messages)
        except StopIteration as exc:
            raise RuntimeError("replay_exhausted") from exc
        if "raise" in response:
            raise ConnectionError(response["raise"])
        return response


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="使用预设模型消息测试 Agent 控制流程。")
    parser.add_argument("scenario", type=Path, help="包含 request 和 messages 的 JSON 案例文件")
    args = parser.parse_args()
    case = json.loads(args.scenario.read_text(encoding="utf-8"))
    print(json.dumps(run_agent(case["request"], model=ReplayModel(case["messages"])), ensure_ascii=False, indent=2))
