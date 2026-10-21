# 环境准备

环境按课程阶段准备。W1、W2 的 Python 实验在课程仓库中运行；W3 起需要另行克隆教学项目，安装 Node 依赖并启动应用。

建议将 `cs146s-public` 和 `drawio-course-work` 放在同一个工作目录下，分别保存课程材料及前两周实验、后续产品代码。本文命令使用 Windows PowerShell。运行前执行 `Get-Location`，确认当前目录与说明一致。

## 首次获取课程仓库

打开 GitHub 上的[课程仓库](https://github.com/NewPhrexian/cs146s_5w)，点击 Fork，在自己的账号下创建副本。然后进入选定的本地工作目录，将下面的用户名替换为自己的账号，再执行命令：

```powershell
$student = '你的GitHub用户名'
git clone "https://github.com/$student/cs146s_5w.git" cs146s-public
Set-Location cs146s-public
git switch -c practice/main
git push -u origin practice/main
```

如果已经有本地课程仓库，先执行 `git remote -v`，确认 `origin` 指向自己的 fork，再创建 `practice/main`。W1、W2 的代码通过 PR 合并到这条分支，操作方法见[开发与提交](collaboration.md)。

## W1：本地模型实验

安装 Python 3.11+、Git 与 [Ollama](https://ollama.com/download)。以下命令在本课程仓库根目录执行：

```powershell
python --version
python -m venv .venv
.venv\Scripts\python.exe -m pip install -r starters/hw01/requirements.txt
if (-not (Test-Path starters/hw01/.env)) { Copy-Item starters/hw01/.env.example starters/hw01/.env }
```

本文代码块使用 PowerShell。macOS/Linux 可使用 PowerShell 7 沿用流程，并将 Python 路径换成 .venv/bin/python；使用 Bash 时，按所用 shell 转换变量、目录切换和复制命令。命令直接调用虚拟环境中的 Python。

### 选择模型与记录配置

实验默认使用完整模型标签 `qwen3:4b-q4_K_M`。量化方式决定模型权重采用怎样的数值精度存储，会影响内存占用；上下文长度决定一次请求能够处理多少内容。先运行下面的命令，确认设备可以加载模型，再观察运行速度和内存占用：

```powershell
ollama --version
ollama pull qwen3:4b-q4_K_M
ollama show qwen3:4b-q4_K_M
ollama run qwen3:4b-q4_K_M
```

收到回答后输入 /bye。在 starters/hw01/.env 中填写完整标签与本机服务地址，默认地址为 http://127.0.0.1:11434。W2 准备环境时沿用这些值。

```powershell
.venv\Scripts\python.exe starters/hw01/smoke_test.py
ollama ps
```

连通性检查应显示模型标签、非空回答和请求耗时。在实验报告中记录操作系统、Python 与 Ollama 版本、量化方式、`ollama ps` 中的 PROCESSOR 和 CONTEXT，以及实际内存或显存占用。4 GB 显存可先尝试 Q4 并接受 CPU 分担；有更多可用资源时可试 Q8。以实际加载结果确定配置，整个比较实验保持同一配置。模型标签见 [Ollama Qwen3](https://ollama.com/library/qwen3)。

## W2：准备可修改的练习文件

从课程根目录安装 MCP 相关依赖，再准备实验配置与练习文件：

```powershell
.venv\Scripts\python.exe -m pip install -r starters/hw02/requirements.txt
if (-not (Test-Path starters/hw02/.env)) { Copy-Item starters/hw02/.env.example starters/hw02/.env }
.venv\Scripts\python.exe starters/hw02/prepare.py
```

编辑 `starters/hw02/.env`，沿用 HW1 已验证的模型标签和服务地址。`prepare.py` 会将练习文件写入 `.runtime/hw02/workspace/practice.drawio`。该文件已存在时，脚本会停止；请先给本轮结果改名保存，再重新准备练习文件。

`starters/shared/diagram_io.py` 提供未压缩 mxfile 的解析与受控写入。HW2 使用这类小文件；真实项目的压缩页面、多页语义从 HW3 的源码导读继续学习。

## W3：个人 fork 与产品环境

在 GitHub 打开[教学项目](https://github.com/NewPhrexian/next-ai-draw-io_cs146s)，点击 Fork，创建自己的副本。安装 Node.js 24 LTS；用 `node --version` 确认当前终端使用 v24。

以下从课程仓库的上一级工作目录执行，将用户名改为自己的账号：

```powershell
$student = '你的GitHub用户名'
git clone "https://github.com/$student/next-ai-draw-io_cs146s.git" drawio-course-work
Set-Location drawio-course-work
git remote add upstream https://github.com/NewPhrexian/next-ai-draw-io_cs146s.git
git fetch upstream
git switch -c course/main 6cc5cd7925777a141e4b278d0017dfbcc8cdfef2
git push -u origin course/main
node --version
npm ci
```

首次推送按 Git 提示完成 GitHub 身份验证。确认 origin 是自己的产品 fork。依赖安装完成后，在产品根目录依次检查：

```powershell
npx tsc --noEmit
npm run check
npm run test -- --run
npm run build
```

从此处开始，产品命令都在 `drawio-course-work` 根目录执行。固定版本见[教学源码说明](baseline.md)。保存首次检查的命令和结果；如果失败，先检查第一条错误。这份修改前的记录用于判断后续问题是否由自己的代码引起。

类型检查成功时可能没有额外输出；测试会打印用例汇总；构建成功后生成 .next。每条命令执行后查看结果，再执行下一条。启动失败时先解决环境问题，保留未改代码时的记录供后续比较。

### 启动和首次操作

```powershell
npm run dev
```

开发地址为 [localhost:6002](http://localhost:6002)。服务所在终端保持运行；编辑文件和执行其他检查时另开终端。首次启动和构建会下载版本固定的 draw.io 资源，网络失败时按终端的 fetch-drawio 错误检查下载地址与连接。

先在应用中导入课程的 `materials/fixtures/normal.drawio`，修改一个名称，导出后重新打开，确认编辑结果得到保留。这些操作及后续固定规则检查可以在未配置模型密钥时完成。

应用通过模型提供对话画图和修改功能。需要使用这些功能时，复制 `env.example` 为 `.env.local`，按教学项目 [模型配置](https://github.com/NewPhrexian/next-ai-draw-io_cs146s/blob/6cc5cd7925777a141e4b278d0017dfbcc8cdfef2/docs/cn/ai-providers.md) 填写所用 provider、model 和凭据，重启服务。学生自己的 Coding Agent 在其开发工具内配置，两处配置用途不同。

### 生产构建

停止自己启动的开发服务，再执行：

```powershell
npm run build
npm run start
```

生产地址为 [localhost:6001](http://localhost:6001)。浏览器开发预览用于修改和调试，生产构建用于 W9/W10 的运行与交付检查。

## 常见现象

| 现象 | 检查与下一步 |
|---|---|
| 模型连接失败 | 确认 Ollama 运行、HOST 地址和完整标签；重跑 smoke_test |
| 返回格式错误 | 保留原始内容，检查提示、schema 和解析结果 |
| Node 版本不符 | Windows 用 Get-Command node,npm 检查路径，并比较 node --version 与 npm version --json 中的 node；使用同一套 Node 24/npm |
| 测试缺少 native binding | 先确认 npm 实际使用 Node 24，再运行 npm ci --include=optional；保留原 package-lock |
| 画布空白 | 查看 fetch-drawio 输出、浏览器资源请求及 iframe 是否就绪 |
| 端口占用 | 停止自己先前的实例；需要改端口时同步测试配置并记录 |
| 初始测试失败 | 保存命令、版本和首个错误，先在固定提交确认是否可复现 |
| 原有功能回归 | 比较本周 diff，运行与受影响流程相关的测试 |
