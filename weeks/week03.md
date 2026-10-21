# W3：真实项目阅读与首次交付

本周开始在真实产品中开发。你需要找到图表数据从哪里进入、在哪里保存，再让用户通过检查按钮找到缺少名称的步骤。

## 推荐讲座视频

本周共 2 场，总时长 **1:49:40**（原速）。先学习怎样理解陌生代码，再观察开发者怎样向 Coding Agent 提供项目上下文。观看后回到教学项目，追踪图表导入、状态更新和结果显示。

**[Reading Code - Marit van Dijk - NDC London 2025](https://www.youtube.com/watch?v=8xKQ2cX-h5E)**（56:59）

讲者与来源：Marit van Dijk；NDC London 2025。

讲座讨论刻意练习代码阅读、借助 IDE 熟悉项目，以及怎样判断 AI 辅助生成的代码。它为 HW3 的源码阅读和实际 diff 核对提供方法。

观看时重点思考：

- 观察讲者怎样从局部代码和导航工具建立对项目的理解，区分已经读到的事实与尚待验证的猜测。
- 为图表导入选择一条调用过程，列出关键函数、状态和需要继续查看的调用者。

**[Cursor Crash Course & AI Coding For Beginners](https://www.youtube.com/watch?v=5zR1ZE5aqho)**（52:41）

讲者与来源：Brad Traversy；Traversy Media。

教程展示上下文、项目规则、局部编辑和对话修改，也包含 Next.js 示例。观看重点是怎样组织现有项目的开发任务，并核对修改结果。

观看时重点思考：

- 重点看 06:58 的上下文、14:17 的已有项目、19:02 的局部编辑和 37:05 的项目上下文文件。
- 结合 HW3 写一份任务说明，包含相关文件、行为样例和验证命令，再阅读 Agent 生成的实际 diff。

可以在自己使用的 Coding Agent 中采用相同方法。产品价格和按钮位置以所用工具为准。

[查看十周视频安排](../materials/videos.md#w3)。

## 准备产品仓库并运行应用

按[环境准备的 W3 部分](../docs/setup.md)创建个人 fork 和 drawio-course-work 目录。先完成导入、编辑、导出和重新打开，保存修改前的测试与构建结果。

前两周的练习帮助你理解了规格、工具接口和验证方法。本周使用 TypeScript 和 React 实现产品功能，需要先了解对象类型、组件和状态的基本用法。先读[语言与组件导读](../docs/primer.md)，再按[源码导航](../docs/source-map.md)的 HW3 行阅读。

## 理解需求怎样落到代码

先阅读导读中的字符计数 PR 示例，找出需求、组件输入和测试条件之间的对应关系。然后回到项目，追踪 `openDiagramFile`、`chartXML` 与用户编辑之间的调用，画出图表数据从导入到更新的过程。

阅读 [AI IDE](../materials/slides/week03-1006-ai-ide-setup.pptx)与 [Silas Alberti 演讲](../materials/slides/week03-1010-silas-alberti.pptx)。需要理解组件状态时，查阅 [React 状态](https://react.dev/learn/state-a-components-memory)和 [TypeScript 入门](https://www.typescriptlang.org/docs/handbook/typescript-in-5-minutes.html)。

## 实现并验证名称检查

按 [HW3](../assignments/HW3.md)分析需求和阅读源码，比较接入方案，再实现检查函数、开发环境中的按钮和结果列表。本周检查整个文件，在列表中显示问题所属的页面和图元。下一周继续增加规则、配置和正式报告。

提交 PR 前，确认图表数据能够正确读入，名称检查函数可以单独测试，按钮和结果列表能够在应用中使用。再用同一份图表完成检查、补充名称和重新检查，解释结果为何变化，并记录浏览器操作结果。

[返回十周安排](../syllabus.md)
