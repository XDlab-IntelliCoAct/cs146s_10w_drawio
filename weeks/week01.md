# W1：模型输出、规格与评估

用户描述了一段流程，模型能否准确整理其中的步骤和关系？本周先运行本地模型，再用一组案例比较三种生成方式。比较时既检查输出格式，也对照用户描述判断步骤和连接是否准确。

## 推荐讲座视频

本周共 2 场，总时长 **1:52:18**（原速）。先理解模型怎样生成回答，再学习如何从实际输出中建立评估标准。两场视频分别帮助你解释模型行为和设计 HW1 的逐案例检查。

**[[1hr Talk] Intro to Large Language Models](https://www.youtube.com/watch?v=zjkBMFhNj_g)**（59:48）

讲者与来源：Andrej Karpathy。

讲座从模型参数、推理和训练讲起，适合建立本地模型实验所需的基本认识。用它解释 HW1 中重复运行的差异，以及为什么格式正确的回答仍可能遗漏或编造流程信息。

观看时重点思考：

- 区分训练、推理和作为助手回答问题的过程，说明 Ollama 实验发生在哪个阶段。
- 留意模型生成内容与外部工具提供信息的区别；对照自己的案例，找出需要另外核查的节点和关系。

后半部分的能力展望以 2023 年的技术背景为出发点；本周重点使用模型原理和输出核查方法。

**[AI Evaluations Clearly Explained in 50 Minutes (Real Example) | Hamel Husain](https://www.youtube.com/watch?v=uiza7wp1KrE)**（52:30）

讲者与来源：Hamel Husain；Peter Yang 主持。

通过实际运行记录和表格演示如何归纳错误、定义判断标准，再逐步组织评估。它能帮助你将“看起来不错”转化为 HW1 中可以逐项填写的结构、关系和含义判断。

观看时重点思考：

- 重点看 01:25 的运行记录分析、09:50 的评估标准整理和 24:44 的通过／不通过判断。
- 为一个开发案例写出明确的失败条件，再检查这些条件能否解释自己的提示修改。

[查看十周视频安排](../materials/videos.md#w1)。

## 从一个可以打开的图表开始

先完成[环境准备的 W1 部分](../docs/setup.md)，确认 smoke_test 返回了模型回答。在课程根目录运行现成的预览示例：

```powershell
.venv\Scripts\python.exe starters/hw01/preview.py materials/cases/preview-example.json .runtime/hw01/intro.svg
```

在浏览器中打开生成的 SVG，再与示例 JSON 对照。`nodes` 中的节点对应流程步骤，`edges` 中的连接表示步骤之间的关系，`questions` 保存需要向用户确认的信息。如果输出文件已经存在，请换一个文件名后运行。

## 带着问题阅读

阅读 [LLM 导论](../materials/slides/week01-0922-intro-to-llms.pptx)和[有效提示](../materials/slides/week01-0926-effective-prompting.pptx)，配合[概念导读](../docs/primer.md)，回答：任务提示应包含什么？JSON 可以解析，是否就表示流程正确？输入冲突时应如何表达？

[Ollama 结构化输出](https://docs.ollama.com/capabilities/structured-outputs)用于实现第三种生成方式。

## 完成本周实验

进入 [HW1](../assignments/HW1.md)：先用一个开发案例完成模型调用、结果解析和记录，确认程序各部分能配合工作，再运行开发集。根据结果修改方案后，固定提示和配置，再运行评估集。案例中的 `dev` 标记表示可用于调整方案，`eval` 标记表示用于评估定稿后的方案。

完成后提交实验程序、逐案例结果与报告，并将一份有效规格导出为 `.drawio` 文件。下一周先用课程提供的统一图表观察工具调用，再用自己的图表进行补充实验。提交位置见[开发与提交](../docs/collaboration.md)。

[返回十周安排](../syllabus.md)
