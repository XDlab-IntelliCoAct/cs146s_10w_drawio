# 开发与提交

## W1/W2：本地实验

在课程仓库完成 starters 中的学生任务。本地实验输出分别保存到 `.runtime/hw01/` 与 `.runtime/hw02/`。为每次运行设置一个独立的 `run_id`，例如日期加序号，以便根据报告找到相应原始输出。

在自己的课程 fork 中，把 HW1/HW2 的源码与 course-notes/HW1.md、course-notes/HW2.md 分别通过 PR 合并到 practice/main。模型权重、.env 和临时运行目录保存在本机；报告引用有代表性的输出和本地记录索引。

首次分支按[环境准备](setup.md)建立。以 HW1 为例，在课程根目录执行：

```powershell
git switch practice/main
git switch -c hw01/prompt-evaluation
```

完成后先看 git status --short 和 git diff，再明确选择源码与报告文件提交：

```powershell
git add starters/hw01/prompt_lab.py course-notes/HW1.md
git commit -m "Complete HW1 prompt evaluation"
git push -u origin hw01/prompt-evaluation
```

额外编写的测试和配置也按实际路径加入提交。打开 GitHub PR，base repository 选择自己的课程 fork，base 选择 practice/main。合并后更新本地 practice/main，再建立 hw02/diagram-agent。下一项作业始终从上一项已合并成果继续。

## W3 起：个人 fork 与每周 PR

产品功能、测试、CI 和报告保存在个人产品 fork 中。`course/main` 是个人课程开发主分支，每次作业从它创建独立分支，再通过 PR 将修改合并回来。

此处切换到产品仓库。课程仓库的 practice/main 保存前两周实验，产品仓库的 course/main 保存 W3–W10 的连续功能，两条分支位于不同仓库。

以 HW3 为例，从产品仓库根目录执行：

```powershell
git switch course/main
git switch -c hw03/first-check
```

完成修改与验证后，检查 diff，再按自己的实际文件提交并推送。GitHub 创建 PR 时选择**自己的 fork**作为 base repository，base 为 course/main，compare 为本周分支。

提交前确认新增的 .runtime 已在产品 .gitignore 中。把报告中提到的代码、测试与固定案例一起提交；使用 git diff --cached 查看将要提交的实际内容，再 commit 和 push。

PR 合并后，下一周从已合并成果继续：

```powershell
git fetch origin
git switch course/main
git merge --ff-only origin/course/main
git switch -c hw04/rules-and-report
```

后续分支依次为 hw05/cli-ci、hw06/quality、hw07/review、hw08/workflow、week09/operations、week10/delivery。ff-only 失败先检查本地提交和差异，保存自己的工作后处理。

## 每周报告的内容与保存位置

在产品仓库新增 course-notes/HW3.md 至 course-notes/HW8.md，最后两周用 course-notes/W9.md、course-notes/W10.md。每份报告应说明以下内容：

1. 用户问题与本周新增行为。
2. 需求、设计选择和关联源码。
3. Agent 获得的上下文、任务交接及关键调整。
4. 实际改动与人工决定。
5. 验证命令、输入、观察和结果。
6. 本次 PR 与依赖的前次成果。

临时运行输出放入产品仓库自己的 `.runtime/`，并加入该仓库 .gitignore；需要随代码交付的固定人工案例和配置放到明确的课程资源目录。

## PR 描述

先说明触发情境和行为变化，再写验证。例如：“导入含空白步骤名的流程图并运行检查后，结果列表显示问题所在的页面和图元。补充名称并重新检查后，该问题消失。”

附上实际测试、构建和浏览器结果。审查发现问题时，链接对应意见、复现和修复提交。使用报告索引链接详细材料，避免把全部终端日志贴在 PR 首页。

## 向 Agent 提供任务并检查修改

向 Agent 分配任务时，说明用户目标、输入、修改范围、相关接口和完成条件。完成后阅读实际 diff，并运行对应验证。需要换会话继续开发时，提供已完成内容、可运行命令、待处理事项和相关变更；请新会话先复述理解，再继续实现。

API key 在开发工具或环境中配置，课程案例使用人工数据。向 Agent 提供代码前，了解所用工具如何处理上传内容，并确认自己有权使用这些材料。
