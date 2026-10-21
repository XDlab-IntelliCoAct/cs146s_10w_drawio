# 讲座视频维护记录：2026-10-21

学生从[材料目录](../materials/README.md)或各周学习页查看推荐视频，详细说明集中在[每周视频指南](../materials/videos.md)。本页记录选择依据和核实方法，供教师维护时使用。

## 选择依据与观看安排

本次选择 17 场视频，其中 6 场来自原有推荐，11 场为新增。每周安排一场长讲座或两场中等长度视频，采用完整视频时长计算，包含其中的问答。单场最短为 29 分 58 秒，各周合计为 1 小时 23 分 38 秒至 1 小时 53 分 52 秒。

选择时先核对视频能否通过经验、案例或论证帮助学生形成工程判断，再比较它与本周任务的关系、讲解深度和每周时长。平台术语、配置语法和操作步骤放在按需查阅的官方文档中。工具演示的观看说明着重解释可以迁移到课程的方法，涉及的账号、平台和功能不增加为作业要求。

| 周次 | 选择内容 | 与本周作业的关系 | 原速总时长 |
|---|---|---|---|
| W1 | 模型导论、基于运行记录的评估 | 理解输出行为，建立结构、关系与含义的判断标准 | 1:52:18 |
| W2 | MCP 与 Agent 完整工作坊 | 区分协议通信、工具执行和控制循环 | 1:44:11 |
| W3 | 代码阅读、已有项目中的 AI 编辑 | 追踪数据，提供上下文，核对实际修改 | 1:49:40 |
| W4 | 长时间开发任务演示 | 分析任务依赖、交接信息和验证反馈 | 1:23:38 |
| W5 | CLI 设计、持续交付的反馈与取舍 | 设计命令行为，安排检查阶段并分析反馈质量 | 1:53:52 |
| W6 | 性质测试、安全代码生成评估 | 扩展输入覆盖，复现并验证风险 | 1:50:45 |
| W7 | 审查反馈、AI 代码的风险核验 | 核实意见，安排人工判断和回归验证 | 1:32:56 |
| W8 | 状态图结对编程、React 副作用 | 描述状态转换，处理异步结果和画布操作 | 1:29:04 |
| W9 | 开发阶段的可观测性、AI 故障诊断 | 记录事件，检验故障假设，确认恢复 | 1:49:35 |
| W10 | 用户测试完整演示 | 观察独立操作，选择反馈并复测修改 | 1:29:27 |

## 原有十场推荐的取舍

| 原视频 | 本次安排 | 依据 |
|---|---|---|
| Intro to Large Language Models | 保留于 W1 | 模型原理可以支持本地实验与输出分析，展望部分注明录制背景 |
| Building a coding agent from scratch | 以 W2 的 MCP 工作坊替代 | 原视频仍可用于学习工具与流程编排；本轮采用一场工作坊统一说明工具、协议和 Agent 的关系，使 W2 能完整覆盖 MCP 学习任务 |
| Cursor Crash Course & AI Coding For Beginners | 保留于 W3 | 包含已有项目、上下文、局部修改和 Next.js 示例，观看重点对应项目阅读与首次开发 |
| The Build System: Mission Impossible | 保留于 W4 | 较长的实际开发演示可用于分析计划、任务协调和验证，课堂讨论将这些做法用于自己的模块交接 |
| Warp 2.0: the Agentic Development Environment | 以 W5 的 CLI 设计和持续交付讲座替代 | 原视频较多讨论工具界面、产品演进和商业问题；新增视频分别讨论命令设计和自动检查中的工程取舍 |
| Prompt Hardening | 保留于 W6 | 结构化安全评估与复现方法适合安全验证任务 |
| Reading Code | 保留并安排于 W3 | 陌生项目阅读是首次接入功能前的准备，也用于之后检查 Agent 修改 |
| Full Lovable Tutorial | 以 W8 的状态图与 React 副作用视频替代 | 原教程主要涉及另建应用、认证、支付和部署；新增视频对应现有画布中的状态、异步任务和定位交互 |
| AI SRE for root cause in minutes | 保留于 W9 | 可以分析多种运行信息如何支持假设检验；与可观测性讲座配合使用 |
| The Modern Software Engineer | 以 W10 的用户测试演示替代 | 原访谈偏向职业角色与课程整体讨论；本周需要具体的试用主持、观察和问题改进方法 |

## 内容、链接与时长的核实

视频链接均使用发布者或主办方频道中的原视频。核实读取了 YouTube 页面的标题、频道、简介和播放器元数据，17 场所选视频均返回 `playabilityStatus.status=OK`，表示核实时页面提供了可播放状态。

内容核对依据发布者简介和已有章节，并对照能够访问的主办方说明或访谈文字。例如：

- [AI Engineer 的 MCP 工作坊页面](https://ai.engineer/talks/kQmXtrmQ5Zg-building-agents-with-mcp)提供讲者信息、章节和文字记录。
- [OpenUK 的 CLI 讲座页面](https://openuk.uk/event-calendar/command-line-interface-design-philosophy-and-practice/)说明讲者经历、设计主题和原视频。
- [PIPELINE 的持续交付讲座页面](https://learn.pipelineconf.info/2018/03/21/dave-farley-optimising-continuous-delivery-pipeline-conference-2018/)链接原视频；[同题讲义](https://speakerdeck.com/devopslx/2018-dot-04-meetup-talk-dave-farley-optimising-continuous-delivery)讨论反馈周期、慢测试、并行执行和不稳定测试。
- [Aviator 的 Michaela Greiler 访谈页面](https://www.aviator.co/podcast/code-review-michaela-greiler)提供讨论主题和访谈文字。
- [React Brussels 的副作用讲座页面](https://www.react.brussels/talks/goodbye-use-effect-david-khourshid)说明状态建模和副作用的关系。
- [Digital.gov 的用户测试活动页面](https://digital.gov/event/2018/06/14/usability-testing-with-steve-krug)说明现场演示与问题改进的安排。

时长采用播放器 `videoDetails.lengthSeconds`，按秒计算每周合计。搜索卡片、活动时段和部分第三方摘要可能有取整或不同剪辑版本，材料中的数值统一按实际链接对应的视频元数据填写。未依据未读取的字幕编写时间点；观看说明中的时间点来自视频发布者提供的章节。

核实日期、原始标题、频道、秒数和课程说明保存在[视频清单](../materials/videos.json)。本地页面元数据及搜索记录保存在 `.local/evidence/video-reading-20261021`。本次核实包括内容范围与链接信息，没有逐场完整观看视频。

## 后续维护

开课前重新确认原视频页面与播放状态，并核对平台操作示例是否仍适用于当前环境。若更换视频，先核对本周任务和观看重点，再更新视频清单、材料目录、视频指南及对应周学习页，重新计算总时长。

课程涉及具体实现时，以共同接口、固定教学源码和当前官方文档为准。历史视频中的工具版本、价格或技术展望按录制背景理解。

## W5 推荐修订

移除 GitHub Actions 平台入门视频，改选 Dave Farley 的持续交付讲座，时长 58:34。观看说明围绕反馈速度、测试成本、阶段安排、隔离和不稳定测试展开。W5 两场合计 1:53:52。原视频侧重可以按需查询的平台操作，没有为讲座时间提供足够的经验分析。
