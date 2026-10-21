"""检查本地模型是否可以调用；在课程仓库根目录运行。"""
import os
import time
from pathlib import Path
from dotenv import load_dotenv
from ollama import Client

load_dotenv(Path(__file__).with_name(".env"))
started = time.perf_counter()
try:
    client = Client(host=os.getenv("OLLAMA_HOST", "http://127.0.0.1:11434"), timeout=120)
    model = os.getenv("OLLAMA_MODEL", "qwen3:4b-q4_K_M")
    response = client.chat(model=model, messages=[{"role": "user", "content": "请用一句话解释流程图中的连接。"}])
    if not response.message.content.strip():
        raise ValueError("模型返回了空回答")
    print(f"模型: {model}\n耗时（秒）: {time.perf_counter() - started:.2f}\n{response.message.content}")
except Exception as exc:
    raise SystemExit(f"Model check failed: verify Ollama, model tag and .env. {exc}") from exc
