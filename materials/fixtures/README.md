# 图表输入与使用方法

本目录的图表由 [make_cases.py](../../tools/make_cases.py)生成，均为人工构造的教学案例。`normal` 等有效图表可以直接导入应用。测试无效 XML、DTD 或断开引用时，应将文件内容直接传入数据适配器；应用导入器可能提前拒绝或修复这些输入，影响对检查核心的验证。

| 文件 | 用途 |
|---|---|
| [normal](normal.drawio) | 三个命名步骤与两条连接 |
| [labels](labels.drawio) | page-a/n2 为空白名称；HW2 修改副本 |
| [html-label](html-label.drawio) | 只有 HTML 格式和实体空格 |
| [multi-page](multi-page.drawio) | 两页复用图元 ID，仅 page-b 的 n2 缺名 |
| [grouped](grouped.drawio) | 分组、标题、装饰和包装图元；不把它们当流程步骤 |
| [free-endpoint](free-endpoint.drawio) | flowchart 与 sketch 配置差异 |
| [dangling](dangling.drawio) | 引用不存在的端点 |
| [empty](empty.drawio) | 有效空白页面与根节点 |
| [compressed](compressed.drawio) | 压缩页面应与 normal 语义一致 |
| [text-safety](text-safety.drawio) | 标签含 HTML/脚本片段，测试安全文本呈现 |
| [invalid](invalid.drawio) | 格式错误 |
| [external-entity](external-entity.drawio) | 禁止声明；测试拒绝和无外部访问 |

`batch` 目录包含 `a-normal`、`b-warning`、`c-error`、`d-invalid` 四项，按文件名排序处理，用于验证遇到无效文件后仍保留其他结果。`normal` 与 `compressed` 表示相同图表，因此问题与统计应相同；文件的字节表示不同，输入摘要可以不同。

性能实验和输入上限测试所需的大型图表，使用生成器保存到本地 `.runtime/` 目录。生成方法和使用要求见 [W9](../../weeks/week09.md)和 [HW6](../../assignments/HW6.md)。
