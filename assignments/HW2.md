# HW2：构建能够修改并复查图表的本地 Agent

**安排：W2。** 沿用 HW1 的 Ollama 与 Python 环境，在个人课程仓库的 `starters/hw02` 中实现。开始前先读[本周学习](../weeks/week02.md)。

## 本次作业要解决的问题

用户提供图表文件和修改请求，希望程序修改指定内容，并说明实际变化。模型负责提出工具调用，Agent 程序负责检查和执行这些调用，再依据读取、修改和复查结果判断任务是否完成。你将实现这套执行过程，观察模型的选择与文件的实际变化是否一致。

## 开始前

从课程根目录运行：

```powershell
.venv\Scripts\python.exe starters/hw02/prepare.py
```

准备脚本会将 `practice.drawio` 复制到本地工作区。阅读[工具约定](../docs/contracts.md)，并熟悉 [diagram_io.py](../starters/shared/diagram_io.py) 提供的解析和写入方法。在这些方法之上，你需要定义工具参数，实现检查逻辑、调用分发和 Agent 控制循环。

先运行 [W2 的文件修改示例](../weeks/week02.md)，观察读取、改名和拒绝旧版本写入的过程。起始代码中的 `read_tool`、`inspect_tool` 等是 Python 函数名；向模型提供的工具名则在 `TOOLS` 中注册为 `read_diagram`、`inspect_diagram`、`apply_changes`、`compare_changes`。`dispatch` 根据模型请求的工具名调用相应 Python 函数。

## 实现步骤

### 1. 先实现和直接验证工具

在 [tools.py](../starters/hw02/tools.py) 定义工具名称、JSON 参数与说明：

- read_diagram：读取页面、图元和文件版本；
- inspect_diagram：检查空名称与错误端点；
- apply_changes：节点改名、增加连接、调整端点；
- compare_changes：按页面/图元比较前后变化。

四种工具统一使用 `ok`、`data`、`error` 返回结果。程序需要检查是否出现未知参数、类型错误、不存在的 ID，以及超出限制的操作数量。工具描述应说明它适合什么任务、接收什么输入，以及返回结果代表什么。

每次读取或修改文件后，程序保存完整快照，并分配一个短标识。读取和修改工具向模型返回该标识、版本及必要摘要；`compare_changes` 接收 `before` 和 `after` 两个标识，由程序取出保存的快照，再调用 `compare_tool`。模型只选择要比较的快照，完整数据由程序管理。

先直接调用工具函数，验证合法修改、未知节点、连接 ID 重复、重复改成同一名称、空操作和使用旧版本写入等情况。批量修改中任一操作失败时，整个批次都不能写入文件。每次成功修改都保存前后快照，供比较工具使用。

### 2. 实现控制循环

在 [agent.py](../starters/hw02/agent.py) 实现 run_agent(request, model)：

1. 准备用户消息和工具描述；
2. 请求模型并追加原始 assistant 消息；
3. 按顺序处理本轮所有工具调用；
4. 将每次实际执行结果作为 tool 消息回传；
5. 继续下一轮，或根据最终结果结束。

每次请求最多进行 8 轮模型调用和 12 次工具调用尝试，第 13 次工具调用不执行。工具失败后，根据错误类型决定是否允许修正参数并重试；模型服务失败时结束本次请求。无法确定修改对象时，向用户询问。

### 3. 记录每次请求的执行过程

为每条事件保存序号、类型、工具名、参数、执行结果和相关版本，最终返回 `answer`、`stop_reason`、`events`。这份记录应能还原请求怎样经过模型、工具和文件。完成修改后，必须取得检查或比较结果，才能向用户说明任务已完成；用户只询问概念时，可以直接回答。

### 4. 运行六个真实模型任务

使用 [agent-cases.json](../materials/cases/agent-cases.json)。在课程根目录执行：

```powershell
.venv\Scripts\python.exe starters/hw02/agent.py
```

每个会修改文件的案例从新的练习副本开始；保留前一轮结果后重新准备。将用户请求、实际执行的工具调用、文件变化与最终回答放在一起核对。遇到选错工具，保留结果并调整描述后另开一轮。

重新准备时，在课程根目录先将现有 practice.drawio 重命名为自己可辨识的名称，再执行 prepare.py。例如先保存为 A3-after.drawio，再开始 A4；已有同名结果时换一个名称。

六个统一案例完成后，将 HW1 的 chosen.drawio 复制进工作区，用它的真实页面/节点 ID 提出一项改名请求，完成修改与复查。通过这个补充案例，检查工具说明是否足以让模型正确操作另一份图表。

### 5. 用响应注入稳定验证程序

[replay.py](../starters/hw02/replay.py) 接受预设模型消息，例如：

```powershell
.venv\Scripts\python.exe starters/hw02/replay.py materials/cases/replay/multiple-tools.json
```

提供的案例覆盖多工具、未知工具、参数无效、模型不可用和循环上限。再自己构造工具异常、重复写入和版本冲突测试。对每个注入案例，断言调用次数、拒绝结果、文件内容和结束原因；运行轨迹用于解释断言失败的位置。

### 6. 通过 MCP 调用同一工具

完成工具后运行：

```powershell
.venv\Scripts\python.exe starters/hw02/mcp_client.py
```

客户端通过标准输入输出（stdio）连接[服务器骨架](../starters/hw02/mcp_server.py)，完成初始化、工具发现，再调用读取与检查工具。比较返回内容与进程内直接调用的结果。服务器调试信息写到标准错误 `stderr`，标准输出 `stdout` 只用于 MCP 协议消息。

## 提交内容

提交 Agent 程序、四种工具及控制流程测试。在 HW2 报告中整理六个真实模型案例、响应注入测试和 MCP 调用结果，并选取代表性运行记录，解释请求如何执行、何时停止。源码与 `course-notes/HW2.md` 通过个人课程 fork 的 PR 合并到 `practice/main`。

## 完成标准

- 模型一次提出多个工具调用时全部得到相应结果。
- 错误参数和未知工具未执行，旧版本不会覆盖新文件。
- 轮数和调用上限真实生效，服务失败可解释。
- 最终结论对应本次读取、修改和复查。
- 文件修改范围始终在本地工作区；测试输入与临时结果有独立位置。
- MCP 调用实际经过客户端/服务器，并返回自己工具的结果。
