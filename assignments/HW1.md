# HW1：从自然语言需求到可检查的图表规格

**安排：W1。** 本次作业在个人课程仓库中完成，起始代码位于 `starters/hw01`。开始前，请完成[本周学习](../weeks/week01.md)和[本地模型准备](../docs/setup.md)。

## 本次作业要解决的问题

用户提供一段流程描述，希望模型将它整理成节点、连接和待确认问题。你需要实现三种生成方式，通过同一组案例比较它们的结果，并说明各自容易出现什么错误。本次作业提交实验程序、逐案例结果和分析报告。

## 实现步骤

### 1. 明确规格与判断方法

先阅读[图表规格约定](../docs/contracts.md)和[JSON Schema](../starters/hw01/spec.schema.json)，再手工分析一个开发案例，列出应当保留的步骤、连接关系和待确认问题。根据这份分析，分别为数据结构、图中关系和需求含义设计检查项。

例如，一份 `nodes` 和 `edges` 都为空的输出可以符合字段类型要求，却没有表达用户明确描述的流程。报告中需要分别记录格式检查和内容判断，使这两类结果可以单独分析。

### 2. 完成三种生成方式

在 [prompt_lab.py](../starters/hw01/prompt_lab.py) 实现 generate、evaluate 和 run：

- brief：简短任务提示；
- contract：包含目标、字段、关系与缺失信息处理的提示；
- schema：沿用 contract，并通过 Ollama 的 format 传入 schema。

同一次比较保持模型、上下文、温度和推理设置一致。记录提示版本与配置；请求失败时保存错误，继续处理其他案例。schema 方式见 [Ollama 文档](https://docs.ollama.com/capabilities/structured-outputs)。

实现时，可以先参照 `smoke_test.py` 中的 `Client.chat` 调用完成 `generate`，再用固定 JSON 字符串调试 `evaluate`，最后由 `run` 组织批量实验。程序保存原始输出和自动检查结果；需要人工判断的含义问题填写在报告表中。

### 3. 用开发案例完善实验

开发阶段使用 [prompt-cases.json](../materials/cases/prompt-cases.json) 中标记为 `dev` 的四个案例。每个案例分别采用三种方式生成，每种重复两次，共 24 次调用。完成 `run` 后，在课程仓库根目录执行：

```powershell
.venv\Scripts\python.exe starters/hw01/prompt_lab.py --split dev
```

运行整组实验前，先选一个开发案例，确认程序能够发出请求、保存原始内容、解析输出并记录检查结果，再扩大到三种方式和两次重复。

每次运行建立独立的 .runtime/hw01/run_id 目录，记录 caseId、split、mode、repeat、提示版本、完整模型标签、配置、耗时、原始内容与程序检查结果。把人工含义判断放在结果表中，按 run_id/caseId/mode/repeat 与原始输出对应。run_id 可用你自己确定的日期加序号。

根据开发结果改进一次提示或检查方法，保留改前与改后版本，说明观察如何支持这项改动。

完成修改后，用相同的 `dev` 案例重新运行受影响的生成方式。如果只修改了一种方式，重新运行该方式的四个案例，每个重复两次，共 8 次；其他方式保留相同配置下的原结果。将这些结果用于比较修改前后的变化。

### 4. 冻结方案并运行独立评估

完成开发后固定三种方式的提示与设置，对 eval 四项各重复两次，共 24 次调用：

```powershell
.venv\Scripts\python.exe starters/hw01/prompt_lab.py --split eval
```

评估结果先完整记录再分析。后续若改方案，另开一轮并标明版本，不把不同版本混入同一次比较。

### 5. 从数据与预览解释结果

分析时，逐项检查模型是否保留了步骤、分支和回路，是否正确表达缺失或冲突信息，以及是否添加了输入中没有的内容。程序负责检查 JSON、字段、ID 唯一性和端点引用；需求含义由你对照每个案例判断。

先使用下面的课程示例熟悉预览工具，再从自己的输出中选择一份有效规格，按同样方法生成预览：

```powershell
.venv\Scripts\python.exe starters/hw01/preview.py materials/cases/preview-example.json .runtime/hw01/example.svg
.venv\Scripts\python.exe starters/hw01/preview.py materials/cases/preview-example.json .runtime/hw01/example.drawio
```

在浏览器打开 SVG 或在 draw.io 打开文件。预览采用简单排布，连接关系同时用文字列出。结构无效时先保留原输出与错误，再决定如何处理。

把自己的一个有效输出保存为 .runtime/hw01/chosen-spec.json，再导出 .runtime/hw01/chosen.drawio。转换命令与上例相同，替换输入和输出路径即可。保留它，供 HW2 的补充实验使用。

SVG 中会列出 `questions`，`.drawio` 预览文件只保存节点和连接，待确认问题仍保留在规格 JSON 和报告中。供 HW2 使用的规格应包含可以明确修改的流程步骤。

## 提交内容

- 已完成的模型调用、解析、图关系检查和批量实验程序。
- 三种方式、八项案例、两次重复的结果表；开发改进前后的结果另列。
- 代表性原始输出、图表预览和环境配置。
- HW1 报告：实验假设、检查定义、主要发现、改进依据，以及需要用户确认的信息。
- 在个人课程 fork 中提交源码与 `course-notes/HW1.md`，向自己的 `practice/main` 分支创建 PR；原始运行目录留在本机。

## 完成标准

- 模型能在本机运行，所有结果可对应到具体配置与提示版本。
- dev/eval 分开，失败调用有记录，三种方式可比较。
- 能解释“结构正确”和“需求表达正确”的差别。
- 至少举出一种格式正确但含义有问题的情形；可用自己构造的反例。
- 比较结论引用实际输入和输出，能发现并解释模型的错误。

## 排查与支持

连接失败时，先重新运行 `smoke_test.py`，核对模型服务地址与标签。解析失败时，保存原始文本和错误；尝试修复输出后，另外记录修复内容及检查结果。调试批量实验时，可以先用固定字符串验证循环和记录格式，再接入本地模型。概念示例见[导读](../docs/primer.md)。
