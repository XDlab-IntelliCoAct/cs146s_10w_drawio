"""在 MCP 测试客户端中校验 HW2 工具的统一返回格式。"""
import json


def require_success(result) -> dict:
    if result.isError:
        raise RuntimeError("MCP 返回工具执行错误")
    payload = getattr(result, "structuredContent", None)
    if payload is None:
        for block in result.content:
            if getattr(block, "type", None) == "text":
                try:
                    payload = json.loads(block.text)
                    break
                except (ValueError, TypeError):
                    continue
    if not isinstance(payload, dict) or payload.get("ok") is not True:
        raise RuntimeError(f"学生工具未返回成功结果: {payload!r}")
    if not isinstance(payload.get("data"), dict) or payload.get("error") is not None:
        raise RuntimeError("成功结果应为 {ok:true, data:object, error:null}")
    return payload
