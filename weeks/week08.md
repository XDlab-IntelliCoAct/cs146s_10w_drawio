# W8：产品界面、画布与异步工作流

已有检查核心能够生成问题报告。本周将它做成应用中的完整面板，让用户完成检查、定位、修改、重查、比较和导出。界面还需要说明报告属于哪个文档版本，以免用户将旧结果用于已经修改的图表。

## 推荐讲座视频

本周共 2 场，总时长 **1:29:04**（原速）。先通过结对编程理解状态和事件，再学习如何组织副作用。将这些方法用于检查面板的运行、失败、过期和重复请求处理。

**[XState: Let's pair program state machines and state charts with David Khourshid](https://www.youtube.com/watch?v=uRfQJJArZEg)**（59:06）

讲者与来源：David Khourshid、Mattias Petter Johansson；Fun Fun Function。

XState 作者通过结对编程演示状态机与状态图，适合学习如何把界面状态、事件和转换条件明确写出来，再检查遗漏的操作顺序。

观看时重点思考：

- 观察示例怎样定义状态和转换，将检查中、完成、失败及过期整理为自己的状态表。
- 列出编辑图表、恢复版本、切换文档和取消检查会触发哪些转换，并据此设计测试。

本周学习状态建模方法，沿用项目现有状态管理方式即可；使用 XState 时另查当前 API。

**[Goodbye, useEffect - David Khourshid](https://www.youtube.com/watch?v=bGzanfKVFeU)**（29:58）

讲者与来源：David Khourshid；React Brussels 2022 / BeJS。

讲座讨论数据请求和命令式接口等副作用，说明如何借助状态与事件理解它们。它有助于分析检查面板、画布桥接和异步返回之间的关系。

观看时重点思考：

- 区分界面渲染、用户事件和需要与外部系统同步的操作，说明检查和画布定位各在何时触发。
- 结合本周延迟测试，核对旧任务返回、图表变化和离开会话后，哪些操作仍有资格更新界面。

[查看十周视频安排](../materials/videos.md#w8)。

## 观察一次迟到结果

在课程根目录运行现成的搜索示例：

```powershell
node materials/examples/task-order.mjs
```

脚本先发出旧查询，再发出新查询，但让旧查询的结果最后返回。如果不检查任务标识，列表最终显示“旧结果”；检查任务标识后，则保留“新结果”。画出两次请求的时间线，再思考图表检查怎样用 `taskId` 和输入快照处理相同问题。

阅读[端到端应用](../materials/slides/week08-1110-end-to-end-app.pptx)、[React Effect](https://react.dev/learn/synchronizing-with-effects)和 [Playwright](https://playwright.dev/docs/intro)。

## 完成用户工作流

按 [HW8](../assignments/HW8.md)先画草图与状态表，再扩展工作区入口、定位、异步任务和报告操作。沿用 HW4/HW5 的核心、配置与比较能力。

接入“交给 AI 处理”时，先在产品设置中完成画图模型连通性检查。它与编写代码的 Coding Agent 分别配置。用户确认发送后，沿用产品的修改与版本机制。

最后使用固定模型响应进行端到端测试，再实际完成一次模型辅助修改。提交时演示连续检查、编辑后结果过期、多页定位、重查和完整报告导出。下一周将在生产构建中记录运行信息、分析性能，并演练故障恢复。

[返回十周安排](../syllabus.md)
