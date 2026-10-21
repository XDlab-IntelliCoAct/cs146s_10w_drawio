# W7：多轮审查与交付判断

本周选取此前的一项实际代码变更，从用户行为、模块设计和可靠性三个角度审查。你需要核实每条意见，修复确认的问题，并判断当前版本能否继续进行完整界面集成。

## 推荐讲座视频

本周共 2 场，总时长 **1:32:56**（原速）。先学习怎样提出和处理审查意见，再讨论 AI 生成大量代码后如何分配审查精力。观看后，为 HW7 的三轮审查确定各自的问题和核验方式。

**[Better Code Reviews FTW! - Tess Ferrandez-Norlander - NDC London 2024](https://www.youtube.com/watch?v=VuG4QhA89es)**（1:00:41）

讲者与来源：Tess Ferrandez-Norlander；NDC London 2024。

讲座从反馈的目的出发，讨论提出和接收审查意见的方法。它帮助你将行为缺陷、设计问题和表达偏好分别说明，使审查能够指导实际修改。

观看时重点思考：

- 检查一条意见是否说明了问题位置、原因和预期影响，区分需要修复的问题与可讨论的建议。
- 为确认、误报、重复和证据不足的意见分别设计处理方式，并记录结论所依据的代码或复现结果。

**[Why Teams Only Pretend to Review AI Code | Dr. Michaela Greiler](https://www.youtube.com/watch?v=oUszgdHwhtE)**（32:15）

讲者与来源：Michaela Greiler；Ankit Jain 主持，Aviator HangarDX。

访谈讨论面对大量 AI 代码时的审查困难，并提出按风险、理解程度和团队共识安排核验的方法。它直接关联 HW7 中对跨模块变更的优先级判断。

观看时重点思考：

- 重点看 17:00 关于审查流于形式的讨论、20:16 的 SCOPE 方法，以及 23:33 后对指导 Agent 与接受输出的区分。
- 选择一条高影响调用过程，说明哪些判断依靠代码阅读、哪些需要复现，哪些可以交给自动测试。

[查看十周视频安排](../materials/videos.md#w7)。

## 先核验一句意见

在 PowerShell 运行：

```powershell
node -e "const items=[]; console.log(items.length)"
node -e "const items=[]; console.log(items[0].name)"
```

第一条输出 0，第二条访问不存在的第一项而报错。面对“空数组会崩溃”这条意见，先确认访问方式与调用者输入，再判断是否成立。

阅读 [AI Code Review](../materials/slides/week07-1103-ai-code-review.pptx)与 [Tomas Reimers 演讲](../materials/slides/week07-1107-tomas-reimers-slides.pdf)，熟悉[审查记录](../materials/templates/review.md)和[短变更案例](../materials/labs/review-lab.md)。

## 审查历史变更，交付本周改进

按 [HW7](../assignments/HW7.md)选择涉及至少两个模块的历史代码变更，记录修改前后的提交，并在三个新会话中分别审查。本周 PR 提交对这些意见的核验记录、确认问题的修复，以及新增回归测试。

如果审查后没有确认产品缺陷，仍需记录核验依据，并用独立短案例完成复现、修复和复审练习。根据实际审查与测试结果，确定产品候选版本。

完成后提交审查材料、逐项判断和回归结果，并记录候选提交 SHA。下一周从该版本继续开发界面，已有 CLI 和报告功能仍需正常工作。

[返回十周安排](../syllabus.md)
