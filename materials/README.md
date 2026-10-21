# 课件、阅读与练习材料

本目录收录 Fall 2025 的 15 份课件，文件中保留原作者和来源标记。每周先阅读学习页，了解本周要解决的问题，再查阅下表中的课件，并将相关方法用于作业。

| 周 | 课件 | 阅读时关注 |
|---|---|---|
| W1 | [LLM 导论](slides/week01-0922-intro-to-llms.pptx)、[有效提示](slides/week01-0926-effective-prompting.pptx) | 模型输出、规格与评估 |
| W2 | [构建 Coding Agent](slides/week02-0929-building-a-coding-agent.pptx)、[自定义 MCP Server](slides/week02-1003-custom-mcp-server.pptx) | 工具调用、控制循环与 MCP |
| W3 | [AI IDE](slides/week03-1006-ai-ide-setup.pptx)、[Silas Alberti 演讲](slides/week03-1010-silas-alberti.pptx) | 真实项目阅读与首次交付 |
| W4 | [管理 Agent 开发任务](slides/week04-1013-agent-manager.pptx)、[Boris Cherny 演讲](slides/week04-1017-boris-cherny.pptx) | 模块接口与 Agent 任务交接 |
| W5 | [AI 开发者产品](slides/week05-1020-ai-developer-product.pptx) | 终端、批处理与持续集成 |
| W6 | [AI QA、SAST 与 DAST](slides/week06-1027-ai-qa-sast-dast.pptx) | 测试设计、性质与输入安全 |
| W7 | [AI 代码审查](slides/week07-1103-ai-code-review.pptx)、[Tomas Reimers 演讲](slides/week07-1107-tomas-reimers-slides.pdf) | 多轮审查与交付判断 |
| W8 | [端到端应用](slides/week08-1110-end-to-end-app.pptx) | 产品界面、画布与异步工作流 |
| W9 | [Incident Response & DevOps](slides/week09-1117-incident-response-devops.pptx)、[Resolve](slides/week09-1121-resolve-guest-lecture-slides.pdf) | 观察、定位、恢复和验证 |
| W10 | 重读 W4/W7/W9 中与自己迭代相关的部分 | 将需求、开发、审查与运行连接起来 |

每周学习页还列有实现时可查阅的官方文档。课件文件的校验值保存在[课件清单](slides.sha256.json)中，供维护时核对。

材料中既有可以直接运行的示例，也有需要完成的作业代码，使用顺序见[课程学习路线](../docs/learning-route.md)。可以直接运行的示例包括 [W2 文件修改示例](../starters/hw02/adapter_demo.py)和 [W8 搜索结果顺序示例](examples/task-order.mjs)，具体命令见对应学习页。


## 推荐讲座视频

每周安排一场长讲座或两场中等长度视频，原速总时长约为 83–114 分钟。下表按观看顺序列出链接与时长，推荐理由和观看重点见[每周视频指南](videos.md)，也可直接在对应周学习页阅读。

| 周次 | 视频与时长 | 合计 |
|---|---|---|
| [W1](videos.md#w1) | [大语言模型导论](https://www.youtube.com/watch?v=zjkBMFhNj_g)（59:48）、[用实际案例建立 AI 评估](https://www.youtube.com/watch?v=uiza7wp1KrE)（52:30） | 1:52:18 |
| [W2](videos.md#w2) | [使用 MCP 构建 Agent](https://www.youtube.com/watch?v=kQmXtrmQ5Zg)（1:44:11） | 1:44:11 |
| [W3](videos.md#w3) | [阅读陌生代码的方法](https://www.youtube.com/watch?v=8xKQ2cX-h5E)（56:59）、[在已有项目中使用 AI 编辑器](https://www.youtube.com/watch?v=5zR1ZE5aqho)（52:41） | 1:49:40 |
| [W4](videos.md#w4) | [长时间开发任务中的计划与验证](https://www.youtube.com/watch?v=pHGGlrKSnJ8)（1:23:38） | 1:23:38 |
| [W5](videos.md#w5) | [命令行工具的设计原则与实践](https://www.youtube.com/watch?v=ChJjaPuT_KA)（55:18）、[持续交付中的反馈速度与设计取舍](https://www.youtube.com/watch?v=gDgAVqkFYWs)（58:34） | 1:53:52 |
| [W6](videos.md#w6) | [通过性质测试发现遗漏案例](https://www.youtube.com/watch?v=IYzDFHx6QPY)（52:50）、[评估 AI 生成代码的安全性](https://www.youtube.com/watch?v=bKphnQByVZI)（57:55） | 1:50:45 |
| [W7](videos.md#w7) | [让代码审查产生有用的反馈](https://www.youtube.com/watch?v=VuG4QhA89es)（1:00:41）、[怎样审查 AI 生成的代码](https://www.youtube.com/watch?v=oUszgdHwhtE)（32:15） | 1:32:56 |
| [W8](videos.md#w8) | [用状态机描述界面行为](https://www.youtube.com/watch?v=uRfQJJArZEg)（59:06）、[理解 React 中的副作用](https://www.youtube.com/watch?v=bGzanfKVFeU)（29:58） | 1:29:04 |
| [W9](videos.md#w9) | [开发者怎样为程序提供可观测性](https://www.youtube.com/watch?v=ACHr-qwHS8Y)（51:34）、[用 AI 辅助定位运行故障](https://www.youtube.com/watch?v=YrdtOwMzJCU)（58:01） | 1:49:35 |
| [W10](videos.md#w10) | [可用性测试演示与问题改进](https://www.youtube.com/watch?v=6fjn1Zz3lMU)（1:29:27） | 1:29:27 |

## 实践资源

- [提示案例](cases/prompt-cases.json)：包含四个开发案例和四个独立评估案例。
- [规格预览示例](cases/preview-example.json)：用于熟悉 JSON 规格与图表预览的关系。
- [完成报告](examples/report-completed.json)、[无效输入报告](examples/report-invalid.json)：用于核对报告字段，以及失败时未知统计的表示方法。
- [Agent 任务](cases/agent-cases.json)与[注入案例说明](labs/replay.md)。
- [图表案例目录](fixtures/README.md)：多页、角色、端点与安全文本。
- [CI 失败](labs/ci-failure.md)、[缺陷实验](labs/mutation-lab.md)、[审查练习](labs/review-lab.md)。
- [异步与运行故障](labs/fault-injection.md)、[性能输入](../tools/make_cases.py)。
- [Agent 上下文](templates/agent-context.md)、[审查](templates/review.md)、[反馈](templates/feedback.md)模板。
