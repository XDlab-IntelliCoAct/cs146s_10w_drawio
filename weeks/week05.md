# W5：终端、批处理与持续集成

开发者希望一次检查整个目录，并在 PR 中自动运行。你将为 HW4 核心编写 CLI（命令行工具），再配置 CI（持续集成），使 PR 能够自动执行这些检查。

## 推荐讲座视频

本周共 2 场，总时长 **1:53:52**（原速）。先从使用者角度设计命令，再思考自动检查应当怎样提供及时、可信的反馈。两场视频分别对应 HW5 的 CLI 行为和检查流程设计。

**[Future Leaders Aanand Prasad on Command-Line Interface Design: Philosophy and Practice](https://www.youtube.com/watch?v=ChJjaPuT_KA)**（55:18）

讲者与来源：Aanand Prasad；OpenUK。

讲者结合 Docker Compose 等命令行工具的经验，解释 CLI 的使用习惯和设计原则。适合思考批量检查的帮助文字、输出、失败反馈和脚本调用方式。

观看时重点思考：

- 比较面向交互使用与面向脚本执行的需求，检查自己的摘要、JSON 输出和退出码是否各司其职。
- 为目录检查、输出已存在和 dry-run 各写一条调用示例，判断使用者能否从反馈中知道接下来怎样处理。

**[Dave Farley - Optimising Continuous Delivery - PIPELINE conference 2018](https://www.youtube.com/watch?v=gDgAVqkFYWs)**（58:34）

讲者与来源：Dave Farley；PIPELINE Conference 2018。

流水线能够运行之后，仍可能因测试增多、阶段安排不当或测试之间相互依赖而难以提供及时反馈。讲座讨论这些问题的成因和优化方法，帮助你判断每项自动检查的价值、成本与执行位置。

观看时重点思考：

- 为什么检查更多、等待更久，未必意味着交付更可靠？分析快速反馈怎样影响开发者发现和修复问题。
- 为类型检查、规则测试、CLI 批处理和浏览器测试安排执行阶段，说明各项检查的成本，以及它们分别能发现什么问题。
- 比较优化慢测试、并行执行和将检查后置的适用条件；分析测试隔离与不稳定测试怎样影响流水线的可信度。

[查看十周视频安排](../materials/videos.md#w5)。

## 理解命令的两种输出

在 PowerShell 运行：

```powershell
node -e "console.log('发现一个检查问题'); process.exitCode = 1"
$LASTEXITCODE
```

这条命令显示一行文字，并以退出码 1 结束；`$LASTEXITCODE` 可以查看这个值。文字帮助人理解结果，退出码让后续脚本决定是否继续。图表检查也需要区分“无法读取文件”和“检查完成但发现问题”，为它们返回不同的退出码。

阅读[AI 开发者产品](../materials/slides/week05-1020-ai-developer-product.pptx)与 [GitHub Actions 官方文档](https://docs.github.com/en/actions/get-started/understand-github-actions)，再看[命令约定](../docs/contracts.md)。

## 进入开发工作流

1. 按 [HW5](../assignments/HW5.md)实现单文件与批处理，验证参数、输出保护与 dry-run。
2. 生成修改前后报告，比较新增、已解决和持续问题。
3. 在个人 fork 运行正常 PR 和独立的预期失败 PR。

CLI 中的 Node 代码负责处理参数和文件，再调用 HW4 核心进行检查。用相同输入分别运行 CLI 和开发界面，比较问题列表及统计，确认两者使用相同规则。

完成后提交命令行工具、子进程测试、CI 运行链接和可下载报告。下一周将针对这些调用方式增加系统测试，检查输入安全，并通过缺陷实验检验测试的有效性。

[返回十周安排](../syllabus.md)
