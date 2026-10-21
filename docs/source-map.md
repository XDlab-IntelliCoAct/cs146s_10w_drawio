# 带问题阅读源码

以下链接指向固定教学提交中的源码。每周先根据表中的任务打开本地文件，搜索函数或状态名称，再查看哪些代码调用或更新它。将阅读得到的调用关系写入本周报告，用来解释新增功能应放在哪里。

| 阶段 | 阅读入口 | 要回答的问题 |
|---|---|---|
| HW3 数据 | [DiagramProvider / useDiagram](https://github.com/NewPhrexian/next-ai-draw-io_cs146s/blob/6cc5cd7925777a141e4b278d0017dfbcc8cdfef2/contexts/diagram-context.tsx) | chartXML 与 chartXMLRef 怎样更新？loadDiagram、requestExport 各在什么时候使用？ |
| HW3 导入 | [ChatEngine](https://github.com/NewPhrexian/next-ai-draw-io_cs146s/blob/6cc5cd7925777a141e4b278d0017dfbcc8cdfef2/components/chat/chat-engine.tsx) | openDiagramFile 怎样将图表写入应用状态？恢复旧会话和旧版本时分别调用哪些函数？ |
| HW3 页面 | [canvas store](https://github.com/NewPhrexian/next-ai-draw-io_cs146s/blob/6cc5cd7925777a141e4b278d0017dfbcc8cdfef2/stores/canvas-store.ts) | currentPageId、selection 与文件 XML 怎样配合？ |
| HW3 入口 | [ChatPanel](https://github.com/NewPhrexian/next-ai-draw-io_cs146s/blob/6cc5cd7925777a141e4b278d0017dfbcc8cdfef2/components/chat/chat-panel.tsx) | 按钮、导出和版本操作在什么位置定义？怎样增加只在开发环境显示的检查按钮？ |
| HW4 多页 | [diagram-pages](https://github.com/NewPhrexian/next-ai-draw-io_cs146s/blob/6cc5cd7925777a141e4b278d0017dfbcc8cdfef2/lib/diagram-pages.ts) | modelOfPage 怎样处理压缩页面？pageModelXml 的默认页面行为适合检查吗？ |
| HW4 规范化 | [load-diagram](https://github.com/NewPhrexian/next-ai-draw-io_cs146s/blob/6cc5cd7925777a141e4b278d0017dfbcc8cdfef2/packages/mcp-server/src/load-diagram.ts) | decompressPageContent 的失败怎样表达？检查适配器如何保留原始问题？ |
| HW5 工具链 | [package.json](https://github.com/NewPhrexian/next-ai-draw-io_cs146s/blob/6cc5cd7925777a141e4b278d0017dfbcc8cdfef2/package.json) | esbuild、saxes、Vitest 各可用于哪里？CLI 如何共享核心而不引入 React？ |
| HW6 浏览器测试 | [E2E fixtures](https://github.com/NewPhrexian/next-ai-draw-io_cs146s/blob/6cc5cd7925777a141e4b278d0017dfbcc8cdfef2/tests/e2e/lib/fixtures.ts) | openApp、openDrawioFile、chunkedReplies 如何构造稳定测试？ |
| HW7 比较 | [diagram-diff](https://github.com/NewPhrexian/next-ai-draw-io_cs146s/blob/6cc5cd7925777a141e4b278d0017dfbcc8cdfef2/lib/diagram-diff.ts) | plainLabel 与原标签的区别？图表变化和问题变化为何不同？ |
| HW8 定位 | [editor-bridge](https://github.com/NewPhrexian/next-ai-draw-io_cs146s/blob/6cc5cd7925777a141e4b278d0017dfbcc8cdfef2/lib/drawio/editor-bridge.ts) | selectPage、highlightCells 的能力与返回值是什么？如何补充可见区域定位？ |
| HW8 输入 | [ChatEngine](https://github.com/NewPhrexian/next-ai-draw-io_cs146s/blob/6cc5cd7925777a141e4b278d0017dfbcc8cdfef2/components/chat/chat-engine.tsx) | 怎样通过 setInput 填写待发送内容，由用户调用 submit 确认，并通过 restoreVersion 恢复旧版本？ |

## 怎样整理源码阅读结果

选择一次实际用户操作，说明它调用了哪些函数、读取或修改了什么状态，以及结果怎样显示。可以画数据流图，也可以用文字串起调用关系。然后标出计划新增的模块，解释选择该位置的原因，并引用实际文件路径和符号；必要时附一小段代码。

## 阅读时需要核对的实现细节

多页工具有“找不到 pageId 时使用第一页”的默认逻辑。检查报告的定位必须确认 pageId 存在，不能误定位到另一页。

应用通过画布桥接代码操作 iframe 中的编辑器，这需要相应的同源访问能力。`highlightCells` 可以高亮图元，但是否同时完成选择和滚动定位，需要实际验证。根据结果为定位操作增加小型适配器；访问不可用时，界面显示页面和图元标识，并保留检查、导出功能。

`lib/diagram-pages.ts` 使用浏览器的 `DOMParser` 和 `XMLSerializer`。阅读其中的页面选择与解压逻辑后，需要另行考虑 Node 怎样解析文件：可以选择两端适用的库，也可以分别解析后转换成同一种数据结构。规则核心只处理转换后的数据。

`lib/diagram-diff.ts` 中的 `plainLabel` 带有用于显示的长度参数。名称检查需要完整的可读文本，复用时要核对是否会发生截断。
