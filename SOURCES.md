# SOURCES — 来源与改动说明

> 本仓库遵循「原创吸收、改动可溯源」：凡借鉴外部内容，标明来源仓库与改动点；原创内容标 Original。

| 本仓内容 | 来源 | 改动说明 |
|---|---|---|
| `rules/devlog.md` 条目结构与执行元信息块 | **Original**（作者日常 agent 使用习惯的沉淀） | — |
| `rules/devlog.md` §接力对账（Relay Reconciliation） | [code-yeongyu/oh-my-openagent](https://github.com/code-yeongyu/oh-my-openagent) | 将其 `edit_assistant_message` 的 leaf-token 乐观锁思想，抽象为日志领域的「接力注明基线 + 写前对账不覆写」规则 |
| `rules/journal-handoff.md` 交接文档结构 | [mattpocock/skills](https://github.com/mattpocock/skills)（其 `/handoff` 技能） | 压缩至 100 行内；增加「上下文快照」段；改写为平台中立的通用写法 |

其余文件（模板 / 示例 / 片段）为上述规则的派生内容。引用均遵循上游各自许可证；本仓库整体以 [MIT](LICENSE) 发布。
