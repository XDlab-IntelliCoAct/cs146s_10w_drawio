# W2：工具调用、控制循环与 MCP

上周的模型生成了图表规格。本周让模型读取文件、修改指定步骤，再检查实际结果。程序需要判断哪些工具请求可以执行，以及什么时候应结束。

## 推荐讲座视频

本周共 1 场，总时长 **1:44:11**（原速）。本周用一场完整工作坊串起工具、客户端、服务器与 Agent 循环，再将这些关系对应到自己的 Python 程序。

**[Building Agents with Model Context Protocol - Full Workshop with Mahesh Murag of Anthropic](https://www.youtube.com/watch?v=kQmXtrmQ5Zg)**（1:44:11）

讲者与来源：Mahesh Murag（Anthropic）；AI Engineer Summit 2025。

讲者先解释 MCP 要解决的集成问题，再演示工具连接和 Agent 组织方式。适合在 HW2 中区分模型提出调用、程序控制执行，以及 MCP 负责传递哪些信息。

观看时重点思考：

- 从 00:00 的协议动机和 09:39 的构建示例入手，区分 tools、resources、prompts 的用途。
- 重点看 26:25 后的 Agent 部分，画出模型请求、工具结果回传和下一轮决策之间的关系。
- 将示例中的客户端与服务器对应到自己的 MCP 骨架，说明参数校验、版本冲突和结束判断仍由哪些代码负责。

工作坊中的远程连接和后续协议规划用于理解扩展方向。HW2 按课程提供的 stdio 骨架和共同约定实现。

[查看十周视频安排](../materials/videos.md#w2)。

## 先了解程序怎样修改文件

按[环境准备的 W2 部分](../docs/setup.md)安装依赖，准备 practice.drawio。在课程根目录运行：

```powershell
.venv\Scripts\python.exe starters/hw02/adapter_demo.py
```

示例会在临时副本中修改节点名称，显示修改前后的版本是否相同，然后尝试使用旧版本再次写入。你应看到“版本是否变化: True”和 `version_conflict`，原练习文件保持原样。这里使用文件字节的 SHA-256 摘要表示版本，因此文件内容变化后，摘要也会随之改变。

## 阅读工具与循环

阅读[构建 Coding Agent](../materials/slides/week02-0929-building-a-coding-agent.pptx)、[自定义 MCP Server](../materials/slides/week02-1003-custom-mcp-server.pptx)，查阅[工具调用文档](https://docs.ollama.com/capabilities/tool-calling)与 [MCP 入门](https://modelcontextprotocol.io/docs/getting-started/intro)。

阅读后，画出一轮工具交互：模型提出调用，程序检查参数并执行工具，再将实际结果返回模型。随后了解 MCP 如何通过客户端与服务器通信完成工具发现和调用，比较它与直接调用 Python 函数的区别。

## 先验证程序，再观察模型

按 [HW2](../assignments/HW2.md)完成工具、循环、响应注入与真实模型案例。响应注入让测试返回指定模型消息，用来稳定检查异常和上限。

完成后提交工具接口说明、Agent 程序、测试、运行记录和 MCP 调用结果。W3 将切换到真实产品开发，继续采用先明确输入输出、再实现和验证的方法。届时从固定教学版本创建产品分支，使用 TypeScript 编写功能。

[返回十周安排](../syllabus.md)
