# 教学源码与环境

课程使用 [NewPhrexian/next-ai-draw-io_cs146s](https://github.com/NewPhrexian/next-ai-draw-io_cs146s) 的提交：

```text
6cc5cd7925777a141e4b278d0017dfbcc8cdfef2
```

对应的维护信息保存在 [baseline.json](baseline.json)。使用 Node 24，并通过 `npm ci` 按项目的 `package-lock` 安装依赖，以便各次实验使用相同的依赖版本。

## 这个版本中可阅读和复用的能力

- 对话生成与编辑图表、图表导入导出。
- 多页读取、当前页面状态、画布桥接。
- 版本比较、恢复和撤销。
- XML 规范化、视觉模型校验。
- Vitest、Playwright 与现有 GitHub Actions。

课程作业在上述功能基础上增加用户主动发起的图表检查、统一报告、CLI 和检查面板。阅读已有实现后，再确定新增功能的接入位置。解压和规范化时应保留待检查的问题，例如指向不存在节点的引用，供后续规则识别。

## 确认初始提交和仓库地址

克隆并创建 course/main 后，在产品仓库执行：

```powershell
git rev-parse HEAD
git remote -v
git status --short
```

初次创建 `course/main` 时，`HEAD` 应为上述提交。之后各周都从自己已经合并的代码继续，通过每周 PR 保存修改。固定教学提交只用于建立最初版本。

源码链接固定到这个版本；教师更新版本时，先试做课程检查场景，再一起更新基线与导航。
