# 使用预设模型响应测试 Agent

真实模型不一定每次返回相同内容，因此难以稳定触发未知工具、错误参数等情况。本练习让模型替身依次返回事先写好的消息，用来测试 Agent 程序如何处理这些响应。

案例保存在 `materials/cases/replay`，包括 `unknown-tool`、`invalid-arguments`、`multiple-tools`、`model-down` 和 `limit`。每份 JSON 中，`request` 是用户请求，`messages` 是预设的模型返回消息。

先用一条没有工具调用的 assistant 消息检查正常结束，再测试多工具调用和错误处理。每个测试分别断言文件内容、调用次数、工具消息回传和 `stop_reason`，并根据运行记录解释执行顺序。

如果出现 `replay_exhausted`，说明 Agent 又请求了一轮响应，但案例没有提供下一条消息。检查这次请求是否符合预期，再决定修正控制循环，还是补充用于验证后续行为的消息。

版本冲突测试可以先读取快照，在副本中通过适配器合法改名一次，再向修改工具传入旧 `version`。未知 ID 和重复连接测试则通过构造 `operations` 完成。具体断言应检查错误原因和文件是否保持原状。
