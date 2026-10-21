# 共同接口与行为约定

本页集中规定各次作业使用的数据格式和功能行为。开始作业时，按下表阅读相关章节；实现过程中需要确认字段、错误或特殊情况的处理时，再回到对应部分查阅。

| 阶段 | 本周阅读与实现 |
|---|---|
| HW1 | 第 1 节：图表规格 |
| HW2 | 第 2 节：工具、快照与事件 |
| HW3 | 第 3 节的页面、图元和名称；第 4 节的 missing-label；按约定返回最小结果 |
| HW4 | 第 3–5 节：完整适配、多规则、配置和报告；在 Node/浏览器两端核对 |
| HW5 | 第 5–6 节：报告比较、命令与批次 |
| HW6 | 第 3、6 节：系统验证输入上限、文件与安全行为 |
| HW8 | 第 7 节：界面任务、快照和报告有效性 |

HW3 的检查结果先包含 `status`、`issues` 和 `error`，每项问题包含 `ruleId`、`severity`、`pageId`、`cellId`、`message`。HW4 在此基础上扩展为 v1 报告，并更新、保留已有测试。输入大小等限制在数据适配层实现，HW6 再集中验证上限附近的行为。

## 1. HW1 图表规格

[spec.schema.json](../starters/hw01/spec.schema.json) 给出字段类型。节点为 `{id, label}`；连接为 `{source, target, label}`；questions 为待确认问题数组。

节点 ID 使用字符串，在同一规格内唯一，连接的端点引用已有节点。预览工具保留 `0`、`1` 作为结构根节点 ID，因此生成规格应使用其他 ID。分支条件写入连接的 `label`，缺失或冲突的信息通过 `questions` 表达，已知内容仍然保留。Schema 检查字段类型，节点引用和需求含义另外核对。

## 2. HW2 工具与事件

工具输入为 JSON 对象；只接受注册的名称和参数。统一返回：

```json
{"ok":true,"data":{},"error":null}
```

执行失败时，`ok=false`、`data=null`，`error` 包含 `code` 与 `message`。分别记录参数错误、版本冲突、文件错误和程序异常。某个工具执行成功，只能说明这次调用完成；Agent 还需要依据读取、修改和复查结果判断用户任务是否完成。

向模型提供四种工具：`read_diagram(name)`、`inspect_diagram(name)`、`apply_changes(name, expected_version, operations)`、`compare_changes(before, after)`。

其中 `before` 和 `after` 是程序保存的快照标识。程序根据标识取出实际快照，再调用 Python 函数 `compare_tool(before_snapshot, after_snapshot)`；找不到标识时返回参数错误。每次 Agent 运行使用独立的快照表。

操作字段：

| op | 共同字段 | 其他字段 |
|---|---|---|
| rename_node | page_id、cell_id | label |
| add_edge | page_id、cell_id | source、target |
| set_endpoints | page_id、cell_id | source、target |

每批修改包含 1–20 项操作，通过 `shared` 中的文件适配器执行。工作区为 `.runtime/hw02/workspace`，工具只接受其中的 `.drawio` 文件名。文件版本使用原文件字节的 SHA-256 表示；版本冲突时先重新读取。本实验由单个执行器顺序写入文件。

Agent 最多 8 轮模型请求、12 次工具调用尝试；未知工具和无效参数也计入尝试次数。同轮调用按顺序处理，超过上限的请求记录拒绝结果并结束。events 每项包含序号、类型、工具名、参数、执行结果和相关版本；模型失败、工具错误和结束也有事件。结束原因至少区分 answered、clarification、limit、model_error、tool_error。状态未知时，最终回答说明需要继续检查。

## 3. 产品检查输入与图元角色

数据适配器接收 `mxfile` 或单个 `mxGraphModel`，并利用项目已有方法处理压缩页面。规范化时只转换表示形式，保留重复 ID 和错误引用等原始信息，供后续校验和规则判断。单独的 `mxGraphModel` 使用逻辑页面 ID `page-1`。

文件大小上限为 2 MiB，页数上限为 20 页，`mxCell` 数量上限为 10,000 个，包含结构根节点。超过任一限制返回 `invalid`。拒绝 DTD 和实体声明，解析过程不请求外部资源。图元数量按解压后的内容统计；解压内容按 8 MiB 上限约束，达到限制时停止展开。

适配层将文件转换为 `pages`、`nodes` 和 `edges`，保留所属页面 ID、原图元 ID 和原始文本。ID 为 `0`、`1` 的 `mxCell` 是结构根节点，不参与流程规则检查。图元由 `object` 或 `UserObject` 包装时，从包装元素读取 ID 和标签。

图元角色按下表优先判断，style 按分号拆成键值或标志：

| 条件 | 角色 |
|---|---|
| edge=1 或具有 source/target | 连接 |
| 其余图元 style 显式 courseRole=process/annotation/container/decoration | 对应角色 |
| group 标志或 swimlane 标志 | 容器 |
| text 标志、text=1 或 edgeLabel 标志 | 注释 |
| image 标志或 shape=image | 装饰 |
| 其他 vertex=1 | 流程步骤 |

courseRole 是课程用的图元角色标记；它设置在 style 中，帮助区分步骤、注释、容器和装饰。未知显式值返回无效输入，并指出具体图元。容器中的流程步骤继续参与检查。孤立检查统计 source 或 target 引用该步骤的连接，自连接也算连接。

名称按图元的 html 设置读取：html=1 时提取可读文本并解码实体，其余按普通文本处理；最后去除首尾空白。只有格式标记或空格的 HTML 名称视为空。界面将取得的文本转义后显示。

同一页面中出现重复图元 ID 时，输入无效；不同页面可以使用相同图元 ID。`mxfile` 的每个页面必须具有唯一页面 ID，只有一页时也要满足该要求。问题所属页面被删除后，应提示重新检查，不能将问题定位到另一页。

## 4. 规则与配置

| 规则 ID | 行为 | flowchart | sketch |
|---|---|---|---|
| missing-label | 流程步骤可读名称为空 | warning | warning |
| isolated-step | 流程步骤没有连接 | warning | warning |
| missing-endpoint | 连接缺少 source 或 target | warning | 关闭 |
| dangling-endpoint | 非空端点引用不存在的节点或容器 | error | error |

`missing-endpoint` 检查连接未指定一端或两端的情况；`sketch` 允许这种自由连接，因此关闭该规则。`dangling-endpoint` 则检查已经填写端点、但相应节点或容器不存在的情况。每个图元在同一条规则下最多生成一项问题，需要时在说明中合并两端的情况；不同规则可以分别报告问题。

配置结构为 {id, rules}，rules 按规则 ID 映射到 off/warning/error。两种内置配置列出全部四个规则。自定义配置也必须列全这四项，缺项、未知键和无效值均返回具体错误。

## 5. 检查报告 v1

| 字段 | 定义 |
|---|---|
| schemaVersion | 固定 1 |
| input | name（展示名）、fingerprint（输入 XML UTF-8 字节的 SHA-256）；未能读取字节时 fingerprint 为 null |
| scope | kind 为 all/current；current 时有 pageId |
| profile | id、完整 rules 和配置摘要 configDigest；配置无法解析时为 null |
| status | completed / invalid / failed |
| issues | ruleId、severity、pageId、cellId、message |
| summary | pages、cells、errors、warnings |
| error | 正常为 null；失败为 code、message |
| generatedAt | ISO 时间；不参与问题身份或比较 |

completed 表示已经完成检查，可以包含严重程度为 error 的问题。invalid 表示格式、限制或配置无效，failed 表示读取或执行异常。后两者的 issues=[]，summary 各值为 null。

有效空白页也是 completed：pages=1，cells=2（两个结构根节点），errors=0，warnings=0。文件完全没有内容则是 invalid。

字段样例见[完成报告](../materials/examples/report-completed.json)和[无效输入报告](../materials/examples/report-invalid.json)。其中 a/b/c 重复组成的摘要用于示意字段长度，实际程序计算真实 SHA-256。configDigest 根据按规则 ID 排序的 rules 对象的紧凑 JSON 计算，不包含显示名称 id。

使用 `pageId`、`cellId` 和 `ruleId` 的组合标识一项问题，并依次按这三个字段排序。相同输入和配置应生成相同的问题与统计，生成时间可以不同。统计只计算 `scope` 选中的页面。

只有 `status=completed` 且 `schemaVersion`、`scope` 一致的报告可以比较，其他情况返回具体原因。配置摘要不同的报告仍列出新增、已解决和持续存在的问题，同时标记 `configurationChanged=true`。修改 `message` 不改变问题标识。比较针对同一图表的前后版本，因此输入 `fingerprint` 可以不同。

## 6. CLI 与批处理

产品脚本统一提供以下用法（由学生在 HW5 实现），从产品根目录运行：

```powershell
npm run course:check -- --input course-fixtures/normal.drawio --profile flowchart --output .runtime/report.json
npm run course:check -- --input course-fixtures/batch --profile sketch --fail-on warning --output .runtime/batch.json
npm run course:check -- --input course-fixtures/batch --dry-run
npm run course:compare -- --before .runtime/before.json --after .runtime/after.json --output .runtime/diff.json
```

命令支持 `--help`。检查命令必须提供 `--input`；`--profile` 默认为 `flowchart`，也可以指定 JSON 配置文件；`--fail-on` 接受 `error` 或 `warning`，默认为 `error`。省略 `--output` 时，只在终端显示摘要。比较命令必须提供 `before` 和 `after`。

目录只处理当前层 .drawio 文件（扩展名忽略大小写），稳定排序，不递归、不跟随符号链接；显式传入链接也拒绝。无匹配文件返回参数/输入错误。输入目录中单项失败后继续，批次报告为 `{schemaVersion:1,reports:[...],summary:{completed,failed}}`，failed 统计 invalid 和 failed。

检查命令使用以下退出码：

- `0`：检查完成，没有达到失败阈值的问题。
- `1`：检查完成，存在达到失败阈值的问题。
- `2`：参数、输入、配置、解析或输出操作发生错误。

批量检查中只要出现执行错误，最终返回 `2`。比较命令成功完成时返回 `0`，参数无效或报告不可比较时返回 `2`。

输出文件已存在时，默认拒绝覆盖。`--force` 允许覆盖已有输出，但输出路径始终不能与任一输入路径相同。需要时可以创建父目录；先写入临时文件，再替换目标，写入失败时保留原报告。

用户可以显式指定产品目录外的输出路径。预览显示最终绝对路径，输入文件始终只读。使用课程案例核对外部输出路径按指定位置处理，没有被误当作输入，也没有因路径变化而跳过权限检查。

`dry-run` 检查参数、配置、路径和覆盖条件，打印将处理的文件及输出位置，不运行规则、不创建目录、不写文件。如果输出父目录尚不存在，列出计划创建的位置，并根据最近的已有父目录检查路径是否可访问。实际写入时仍需处理权限变化导致的错误。预览成功返回 `0`。

## 7. 界面状态、定位与导出

每次检查保存 `taskId`、文档会话 ID、输入 `fingerprint`、`scope` 和配置，使界面能够判断返回结果属于哪次任务、哪个文档版本。任务状态为 `waiting`、`running`、`completed`、`failed` 或 `stale`；画布未就绪和有效空图也需要分别显示。

开始新任务后，旧任务返回的结果不能覆盖新任务；离开文档会话后，原任务也不能继续更新旧界面。检查期间用户编辑图表时，可以保留该次结果，但要标记为 `stale`。导出旧报告时，明确提示它对应的是旧快照。AI 流式修改结束、恢复版本、切换文档都会重新核对 fingerprint。当前页 scope 下切页也使结果过期。

定位同时使用 `pageId` 和 `cellId`。确认当前文档仍与报告快照一致后，切换到目标页面并定位图元。画布桥接不可用时，显示这两个标识，并保留报告导出。对于 `all` 范围的检查，在同一文档中切页定位不会使报告过期。

筛选只影响列表。JSON 导出包含完整报告与生成时的配置，不根据筛选删项。“交给 AI 处理”先填入现有输入框，用户确认后发送；选中问题作为数据描述，不拼成可执行指令。
