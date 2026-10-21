# 每周讲座视频

课程每周安排一场长讲座或两场中等长度视频，完整观看约需 83–114 分钟。时长按原速计算，包含视频中的演示与问答，暂停练习另计。下表列出观看顺序和总时长；每周学习页也列有对应视频。

先观看，再带着问题阅读课件和完成作业。观看重点用于联系课程中的实现任务，可以写入自己的学习笔记。视频中的工具演示与本课程的实现约定在各周说明中分别交代。

| 周次 | 主题与视频 | 合计 |
|---|---|---|
| [W1](#w1) | 模型输出与评估：[大语言模型导论](https://www.youtube.com/watch?v=zjkBMFhNj_g)（59:48）、[用实际案例建立 AI 评估](https://www.youtube.com/watch?v=uiza7wp1KrE)（52:30） | 1:52:18 |
| [W2](#w2) | 工具调用、Agent 循环与 MCP：[使用 MCP 构建 Agent](https://www.youtube.com/watch?v=kQmXtrmQ5Zg)（1:44:11） | 1:44:11 |
| [W3](#w3) | 阅读项目并使用 Coding Agent 开发：[阅读陌生代码的方法](https://www.youtube.com/watch?v=8xKQ2cX-h5E)（56:59）、[在已有项目中使用 AI 编辑器](https://www.youtube.com/watch?v=5zR1ZE5aqho)（52:41） | 1:49:40 |
| [W4](#w4) | 组织 Agent 任务与验证交接结果：[长时间开发任务中的计划与验证](https://www.youtube.com/watch?v=pHGGlrKSnJ8)（1:23:38） | 1:23:38 |
| [W5](#w5) | CLI 设计与持续集成：[命令行工具的设计原则与实践](https://www.youtube.com/watch?v=ChJjaPuT_KA)（55:18）、[持续交付中的反馈速度与设计取舍](https://www.youtube.com/watch?v=gDgAVqkFYWs)（58:34） | 1:53:52 |
| [W6](#w6) | 性质测试与 AI 生成代码的安全验证：[通过性质测试发现遗漏案例](https://www.youtube.com/watch?v=IYzDFHx6QPY)（52:50）、[评估 AI 生成代码的安全性](https://www.youtube.com/watch?v=bKphnQByVZI)（57:55） | 1:50:45 |
| [W7](#w7) | 代码审查与 AI 修改的人工核验：[让代码审查产生有用的反馈](https://www.youtube.com/watch?v=VuG4QhA89es)（1:00:41）、[怎样审查 AI 生成的代码](https://www.youtube.com/watch?v=oUszgdHwhtE)（32:15） | 1:32:56 |
| [W8](#w8) | 界面状态与异步交互：[用状态机描述界面行为](https://www.youtube.com/watch?v=uRfQJJArZEg)（59:06）、[理解 React 中的副作用](https://www.youtube.com/watch?v=bGzanfKVFeU)（29:58） | 1:29:04 |
| [W9](#w9) | 运行信息、故障诊断与恢复：[开发者怎样为程序提供可观测性](https://www.youtube.com/watch?v=ACHr-qwHS8Y)（51:34）、[用 AI 辅助定位运行故障](https://www.youtube.com/watch?v=YrdtOwMzJCU)（58:01） | 1:49:35 |
| [W10](#w10) | 用户试用、反馈与产品迭代：[可用性测试演示与问题改进](https://www.youtube.com/watch?v=6fjn1Zz3lMU)（1:29:27） | 1:29:27 |

## W1

**模型输出与评估；总时长 1:52:18。**

先理解模型怎样生成回答，再学习如何从实际输出中建立评估标准。两场视频分别帮助你解释模型行为和设计 HW1 的逐案例检查。

### 大语言模型导论

[[1hr Talk] Intro to Large Language Models](https://www.youtube.com/watch?v=zjkBMFhNj_g)

Andrej Karpathy；发布频道：Andrej Karpathy；时长 **59:48**。

讲座从模型参数、推理和训练讲起，适合建立本地模型实验所需的基本认识。用它解释 HW1 中重复运行的差异，以及为什么格式正确的回答仍可能遗漏或编造流程信息。

观看重点：

- 区分训练、推理和作为助手回答问题的过程，说明 Ollama 实验发生在哪个阶段。
- 留意模型生成内容与外部工具提供信息的区别；对照自己的案例，找出需要另外核查的节点和关系。

后半部分的能力展望以 2023 年的技术背景为出发点；本周重点使用模型原理和输出核查方法。

### 用实际案例建立 AI 评估

[AI Evaluations Clearly Explained in 50 Minutes (Real Example) | Hamel Husain](https://www.youtube.com/watch?v=uiza7wp1KrE)

Hamel Husain；Peter Yang 主持；发布频道：Peter Yang；时长 **52:30**。

通过实际运行记录和表格演示如何归纳错误、定义判断标准，再逐步组织评估。它能帮助你将“看起来不错”转化为 HW1 中可以逐项填写的结构、关系和含义判断。

观看重点：

- 重点看 01:25 的运行记录分析、09:50 的评估标准整理和 24:44 的通过／不通过判断。
- 为一个开发案例写出明确的失败条件，再检查这些条件能否解释自己的提示修改。

## W2

**工具调用、Agent 循环与 MCP；总时长 1:44:11。**

本周用一场完整工作坊串起工具、客户端、服务器与 Agent 循环，再将这些关系对应到自己的 Python 程序。

### 使用 MCP 构建 Agent

[Building Agents with Model Context Protocol - Full Workshop with Mahesh Murag of Anthropic](https://www.youtube.com/watch?v=kQmXtrmQ5Zg)

Mahesh Murag（Anthropic）；AI Engineer Summit 2025；发布频道：AI Engineer；时长 **1:44:11**。

讲者先解释 MCP 要解决的集成问题，再演示工具连接和 Agent 组织方式。适合在 HW2 中区分模型提出调用、程序控制执行，以及 MCP 负责传递哪些信息。

观看重点：

- 从 00:00 的协议动机和 09:39 的构建示例入手，区分 tools、resources、prompts 的用途。
- 重点看 26:25 后的 Agent 部分，画出模型请求、工具结果回传和下一轮决策之间的关系。
- 将示例中的客户端与服务器对应到自己的 MCP 骨架，说明参数校验、版本冲突和结束判断仍由哪些代码负责。

工作坊中的远程连接和后续协议规划用于理解扩展方向。HW2 按课程提供的 stdio 骨架和共同约定实现。

## W3

**阅读项目并使用 Coding Agent 开发；总时长 1:49:40。**

先学习怎样理解陌生代码，再观察开发者怎样向 Coding Agent 提供项目上下文。观看后回到教学项目，追踪图表导入、状态更新和结果显示。

### 阅读陌生代码的方法

[Reading Code - Marit van Dijk - NDC London 2025](https://www.youtube.com/watch?v=8xKQ2cX-h5E)

Marit van Dijk；NDC London 2025；发布频道：NDC Conferences；时长 **56:59**。

讲座讨论刻意练习代码阅读、借助 IDE 熟悉项目，以及怎样判断 AI 辅助生成的代码。它为 HW3 的源码阅读和实际 diff 核对提供方法。

观看重点：

- 观察讲者怎样从局部代码和导航工具建立对项目的理解，区分已经读到的事实与尚待验证的猜测。
- 为图表导入选择一条调用过程，列出关键函数、状态和需要继续查看的调用者。

### 在已有项目中使用 AI 编辑器

[Cursor Crash Course & AI Coding For Beginners](https://www.youtube.com/watch?v=5zR1ZE5aqho)

Brad Traversy；Traversy Media；发布频道：Traversy Media；时长 **52:41**。

教程展示上下文、项目规则、局部编辑和对话修改，也包含 Next.js 示例。观看重点是怎样组织现有项目的开发任务，并核对修改结果。

观看重点：

- 重点看 06:58 的上下文、14:17 的已有项目、19:02 的局部编辑和 37:05 的项目上下文文件。
- 结合 HW3 写一份任务说明，包含相关文件、行为样例和验证命令，再阅读 Agent 生成的实际 diff。

可以在自己使用的 Coding Agent 中采用相同方法。产品价格和按钮位置以所用工具为准。

## W4

**组织 Agent 任务与验证交接结果；总时长 1:23:38。**

本周通过一场较长的开发演示，观察复杂任务怎样拆分、执行和验证，再为自己的适配、规则与报告模块编写交接材料。

### 长时间开发任务中的计划与验证

[The Build System: Mission Impossible with Eno Reyes, CTO Factory AI](https://www.youtube.com/watch?v=pHGGlrKSnJ8)

Eno Reyes（Factory）；The Modern Software Developer；发布频道：The Modern Software Developer；时长 **1:23:38**。

视频以实际开发过程展示 Missions 怎样组织计划、代码修改和验证，适合分析多项任务之间的依赖，以及 Agent 运行较长时间后怎样确认结果。

观看重点：

- 记录计划、任务分配、代码修改和验证分别使用了什么信息，找出结果需要人工核查的环节。
- 将本周数据适配、规则执行、报告生成三项任务的输入输出写清，说明其中一项交给新会话时还需要提供什么。
- 观察验证结果怎样影响后续操作，设计一个能发现模块接口不一致的集成测试。

演示使用 Factory。课程中使用自己的 Coding Agent 完成交接，重点比较任务组织和验证方法。

## W5

**CLI 设计与持续集成；总时长 1:53:52。**

先从使用者角度设计命令，再思考自动检查应当怎样提供及时、可信的反馈。两场视频分别对应 HW5 的 CLI 行为和检查流程设计。

### 命令行工具的设计原则与实践

[Future Leaders Aanand Prasad on Command-Line Interface Design: Philosophy and Practice](https://www.youtube.com/watch?v=ChJjaPuT_KA)

Aanand Prasad；OpenUK；发布频道：OpenUK；时长 **55:18**。

讲者结合 Docker Compose 等命令行工具的经验，解释 CLI 的使用习惯和设计原则。适合思考批量检查的帮助文字、输出、失败反馈和脚本调用方式。

观看重点：

- 比较面向交互使用与面向脚本执行的需求，检查自己的摘要、JSON 输出和退出码是否各司其职。
- 为目录检查、输出已存在和 dry-run 各写一条调用示例，判断使用者能否从反馈中知道接下来怎样处理。

### 持续交付中的反馈速度与设计取舍

[Dave Farley - Optimising Continuous Delivery - PIPELINE conference 2018](https://www.youtube.com/watch?v=gDgAVqkFYWs)

Dave Farley；PIPELINE Conference 2018；发布频道：Pipeline Conference；时长 **58:34**。

流水线能够运行之后，仍可能因测试增多、阶段安排不当或测试之间相互依赖而难以提供及时反馈。讲座讨论这些问题的成因和优化方法，帮助你判断每项自动检查的价值、成本与执行位置。

观看重点：

- 为什么检查更多、等待更久，未必意味着交付更可靠？分析快速反馈怎样影响开发者发现和修复问题。
- 为类型检查、规则测试、CLI 批处理和浏览器测试安排执行阶段，说明各项检查的成本，以及它们分别能发现什么问题。
- 比较优化慢测试、并行执行和将检查后置的适用条件；分析测试隔离与不稳定测试怎样影响流水线的可信度。

## W6

**性质测试与 AI 生成代码的安全验证；总时长 1:50:45。**

一场讲座帮助你从固定案例走向性质测试，另一场讨论怎样系统评价 AI 生成代码的安全性。两者共同服务于 HW6 的测试矩阵和问题复现。

### 通过性质测试发现遗漏案例

[The lazy programmer's guide to writing thousands of tests - Scott Wlaschin](https://www.youtube.com/watch?v=IYzDFHx6QPY)

Scott Wlaschin；NDC Conferences；发布频道：NDC Conferences；时长 **52:50**。

讲座从手工编写示例测试出发，介绍如何用通用性质和生成输入发现特殊情况。它直接对应图元顺序、坐标变化和跨页独立性等测试要求。

观看重点：

- 区分某个示例的正确答案与一类输入应满足的性质，说明性质成立的前提。
- 为“图元重新排列不改变问题集合”设计输入变换和断言，再考虑怎样保留失败输入以便复现。

示例语言和库用于理解测试方法；本周在项目现有 TypeScript 测试环境中应用这些方法。

### 评估 AI 生成代码的安全性

[Prompt Hardening - Secure Code Generation Using AI - Sean Sinclair - NDC Manchester 2025](https://www.youtube.com/watch?v=bKphnQByVZI)

Sean Sinclair；NDC Manchester 2025；发布频道：NDC Conferences；时长 **57:55**。

讲者使用结构化评估比较安全代码生成提示，并讨论如何把安全要求加入开发过程。它帮助你把安全提示、生成结果和实际验证分开分析。

观看重点：

- 观察安全要求怎样写成可检查的条件，以及评估怎样发现生成代码中的问题。
- 将方法用于 XML、报告文本和输出路径：为每项风险准备触发输入，核对程序实际行为，并验证修复。

## W7

**代码审查与 AI 修改的人工核验；总时长 1:32:56。**

先学习怎样提出和处理审查意见，再讨论 AI 生成大量代码后如何分配审查精力。观看后，为 HW7 的三轮审查确定各自的问题和核验方式。

### 让代码审查产生有用的反馈

[Better Code Reviews FTW! - Tess Ferrandez-Norlander - NDC London 2024](https://www.youtube.com/watch?v=VuG4QhA89es)

Tess Ferrandez-Norlander；NDC London 2024；发布频道：NDC Conferences；时长 **1:00:41**。

讲座从反馈的目的出发，讨论提出和接收审查意见的方法。它帮助你将行为缺陷、设计问题和表达偏好分别说明，使审查能够指导实际修改。

观看重点：

- 检查一条意见是否说明了问题位置、原因和预期影响，区分需要修复的问题与可讨论的建议。
- 为确认、误报、重复和证据不足的意见分别设计处理方式，并记录结论所依据的代码或复现结果。

### 怎样审查 AI 生成的代码

[Why Teams Only Pretend to Review AI Code | Dr. Michaela Greiler](https://www.youtube.com/watch?v=oUszgdHwhtE)

Michaela Greiler；Ankit Jain 主持，Aviator HangarDX；发布频道：Aviator；时长 **32:15**。

访谈讨论面对大量 AI 代码时的审查困难，并提出按风险、理解程度和团队共识安排核验的方法。它直接关联 HW7 中对跨模块变更的优先级判断。

观看重点：

- 重点看 17:00 关于审查流于形式的讨论、20:16 的 SCOPE 方法，以及 23:33 后对指导 Agent 与接受输出的区分。
- 选择一条高影响调用过程，说明哪些判断依靠代码阅读、哪些需要复现，哪些可以交给自动测试。

## W8

**界面状态与异步交互；总时长 1:29:04。**

先通过结对编程理解状态和事件，再学习如何组织副作用。将这些方法用于检查面板的运行、失败、过期和重复请求处理。

### 用状态机描述界面行为

[XState: Let's pair program state machines and state charts with David Khourshid](https://www.youtube.com/watch?v=uRfQJJArZEg)

David Khourshid、Mattias Petter Johansson；Fun Fun Function；发布频道：Fun Fun Function；时长 **59:06**。

XState 作者通过结对编程演示状态机与状态图，适合学习如何把界面状态、事件和转换条件明确写出来，再检查遗漏的操作顺序。

观看重点：

- 观察示例怎样定义状态和转换，将检查中、完成、失败及过期整理为自己的状态表。
- 列出编辑图表、恢复版本、切换文档和取消检查会触发哪些转换，并据此设计测试。

本周学习状态建模方法，沿用项目现有状态管理方式即可；使用 XState 时另查当前 API。

### 理解 React 中的副作用

[Goodbye, useEffect - David Khourshid](https://www.youtube.com/watch?v=bGzanfKVFeU)

David Khourshid；React Brussels 2022 / BeJS；发布频道：BeJS；时长 **29:58**。

讲座讨论数据请求和命令式接口等副作用，说明如何借助状态与事件理解它们。它有助于分析检查面板、画布桥接和异步返回之间的关系。

观看重点：

- 区分界面渲染、用户事件和需要与外部系统同步的操作，说明检查和画布定位各在何时触发。
- 结合本周延迟测试，核对旧任务返回、图表变化和离开会话后，哪些操作仍有资格更新界面。

## W9

**运行信息、故障诊断与恢复；总时长 1:49:35。**

先学习怎样记录有助于排查的信息，再观察 Agent 如何利用多种信息提出并检验故障假设。将两场视频的方法用于本地生产构建中的三类演练。

### 开发者怎样为程序提供可观测性

[Observability: it's not just an ops thing - Charity Majors](https://www.youtube.com/watch?v=ACHr-qwHS8Y)

Charity Majors；NDC Conferences；发布频道：NDC Conferences；时长 **51:34**。

讲座解释为什么开发者需要在实现时考虑事件、指标和跟踪信息，以及怎样选择有用的记录。它能帮助你为检查阶段耗时、错误类别和任务关联设计记录方式。

观看重点：

- 区分收集大量日志与回答具体运行问题，说明 taskId 和输入摘要分别帮助判断什么。
- 选择一个故障假设，列出支持或排除它所需的信息，同时检查记录是否包含不必要的图表正文或配置。

### 用 AI 辅助定位运行故障

[AWS re:Invent 2025 - Ditch your old SRE playbook: AI SRE for root cause in minutes (AIM260)](https://www.youtube.com/watch?v=YrdtOwMzJCU)

Spiros Xanthos；AWS re:Invent 2025，Resolve AI 合作伙伴场次；发布频道：AWS Events；时长 **58:01**。

讲座讨论如何结合日志、指标、跟踪、配置和代码进行故障诊断，并展示 Agent 使用工具检验假设的过程。适合与自己的故障记录和恢复步骤对照。

观看重点：

- 将症状、假设、检查动作和根因依据分别记下，观察何种信息会改变诊断方向。
- 对本周三类故障分别说明：怎样确定来源，怎样恢复，以及重新执行哪个用户任务才能确认恢复。

视频展示 Resolve AI 场景。本周在自己的产品中记录事件和验证恢复，无需部署该平台。

## W10

**用户试用、反馈与产品迭代；总时长 1:29:27。**

观看完整的用户测试演示，学习怎样提出任务、观察操作和选择值得修复的问题，再开展同学交叉试用。

### 可用性测试演示与问题改进

[Usability Testing with Steve Krug](https://www.youtube.com/watch?v=6fjn1Zz3lMU)

Steve Krug；Digital.gov；发布频道：Digitalgov；时长 **1:29:27**。

视频从实际可用性测试演示开始，讨论怎样用少量参与者发现重要问题并改进产品。它与 W10 的独立操作、观察记录、反馈分类和修改后复测直接对应。

观看重点：

- 观察主持人怎样介绍任务、等待用户操作和询问原因，区分提供任务目标与逐步教操作。
- 分别记录用户做了什么、你认为原因是什么，以及还需要追问什么。
- 选出一项影响用户完成检查、定位或导出的困难，写成验收场景；修改后请原试用者重复相关任务。

视频名称、发布频道和时长于 2026-10-21 核对。完整条目见[视频清单](videos.json)，课程作业仍按[共同接口与行为约定](../docs/contracts.md)实现。
