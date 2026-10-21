# W6：测试设计、性质与输入安全

前几周已经有规则、配置、CLI 和最小界面。本周检查它们组合后是否仍满足需求，尤其是复杂结构、错误输入与文件操作。

## 推荐讲座视频

本周共 2 场，总时长 **1:50:45**（原速）。一场讲座帮助你从固定案例走向性质测试，另一场讨论怎样系统评价 AI 生成代码的安全性。两者共同服务于 HW6 的测试矩阵和问题复现。

**[The lazy programmer's guide to writing thousands of tests - Scott Wlaschin](https://www.youtube.com/watch?v=IYzDFHx6QPY)**（52:50）

讲者与来源：Scott Wlaschin；NDC Conferences。

讲座从手工编写示例测试出发，介绍如何用通用性质和生成输入发现特殊情况。它直接对应图元顺序、坐标变化和跨页独立性等测试要求。

观看时重点思考：

- 区分某个示例的正确答案与一类输入应满足的性质，说明性质成立的前提。
- 为“图元重新排列不改变问题集合”设计输入变换和断言，再考虑怎样保留失败输入以便复现。

示例语言和库用于理解测试方法；本周在项目现有 TypeScript 测试环境中应用这些方法。

**[Prompt Hardening - Secure Code Generation Using AI - Sean Sinclair - NDC Manchester 2025](https://www.youtube.com/watch?v=bKphnQByVZI)**（57:55）

讲者与来源：Sean Sinclair；NDC Manchester 2025。

讲者使用结构化评估比较安全代码生成提示，并讨论如何把安全要求加入开发过程。它帮助你把安全提示、生成结果和实际验证分开分析。

观看时重点思考：

- 观察安全要求怎样写成可检查的条件，以及评估怎样发现生成代码中的问题。
- 将方法用于 XML、报告文本和输出路径：为每项风险准备触发输入，核对程序实际行为，并验证修复。

[查看十周视频安排](../materials/videos.md#w6)。

## 从输入变化预测结果

打开 normal.drawio，查看 x/y 坐标。假设所有坐标各增加 10：布局会移动，名称、角色和连接关系保持原样，结构检查的问题集合也应相同。先写出预期结果，再在作业中生成平移后的图表，并用测试断言比较问题集合。

这种“输入变化后，某些结论应保持或按规律变化”的关系称为变形关系，可用于检查没有逐项标准答案的输入。

## 选择适合各项需求的测试层次

阅读 [AI QA、SAST 与 DAST](../materials/slides/week06-1027-ai-qa-sast-dast.pptx)，查阅 [Vitest](https://vitest.dev/guide/)和 [OWASP 输入验证](https://cheatsheetseries.owasp.org/cheatsheets/Input_Validation_Cheat_Sheet.html)。

在需求—风险—测试矩阵中说明：规则适合单元测试，退出码需要子进程测试，文本是否安全显示需要浏览器观察。

## 根据证据完成验证与修复

按 [HW6](../assignments/HW6.md)为复杂图表、五种性质、输入上限、安全文本和输出保护编写测试。再在隔离副本中引入指定缺陷，观察哪些测试能够发现；补足遗漏的测试后，恢复正确实现并完成回归。

完成后提交测试矩阵、可复现输入、安全验证和修复记录。下一周的代码审查将使用这些材料，因此每项结论都应能找到对应输入或测试。

[返回十周安排](../syllabus.md)
