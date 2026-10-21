"""HW1 实验程序：按 assignments/HW1.md 实现模型调用、评估和批量记录。"""
import argparse
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def generate(case: dict, mode: str, schema: dict) -> str:
    # TODO: 调用 Ollama，三种生成方式使用相同的模型和生成设置。
    # 生成方式为 brief、contract、schema；返回模型的原始内容。
    raise NotImplementedError("请先实现模型调用和三种提示方式")


def evaluate(case: dict, content: str) -> dict:
    # TODO: 分别记录 JSON/Schema 检查、图关系检查及需要人工判断的含义。
    raise NotImplementedError("请先实现解析和评估记录")


def run(split: str) -> None:
    cases = json.loads((ROOT / "materials/cases/prompt-cases.json").read_text(encoding="utf-8"))
    schema = json.loads(Path(__file__).with_name("spec.schema.json").read_text(encoding="utf-8"))
    # TODO: 按 split 选取案例，遍历三种生成方式，每种重复两次。
    # 保存原始输出、耗时、模型配置和错误。
    # 将输出写入 .runtime/hw01，每次运行使用独立 run_id。
    raise NotImplementedError(f"请先实现 {split} 的批量实验；已读取 {len(cases)} 个案例")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--split", choices=["dev", "eval"], required=True)
    args = parser.parse_args()
    run(args.split)
