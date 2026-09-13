# SOURCES — 来源与改动说明

> 本仓库遵循「原创吸收、改动可溯源」：凡借鉴外部内容，标明来源仓库与改动点；原创内容标 Original。

| 本仓内容 | 来源 | 改动说明 |
|---|---|---|
| `rules/devlog.md` 条目结构与执行元信息块 | **Original**（作者日常 agent 使用习惯的沉淀） | — |
| `rules/devlog.md` §接力对账（Relay Reconciliation） | [code-yeongyu/oh-my-openagent](https://github.com/code-yeongyu/oh-my-openagent) | 将其 `edit_assistant_message` 的 leaf-token 乐观锁思想，抽象为日志领域的「接力注明基线 + 写前对账不覆写」规则 |
| `rules/journal-handoff.md` 交接文档结构 | [mattpocock/skills](https://github.com/mattpocock/skills)（其 `/handoff` 技能） | 压缩至 100 行内；增加「上下文快照」段；改写为平台中立的通用写法 |
| `rules/iron-rules.md` #12-15、#18 部分原则 | [multica-ai/andrej-karpathy-skills](https://github.com/multica-ai/andrej-karpathy-skills)（Karpathy CLAUDE.md 规则集） | 编号化为铁律并合并改写；补强「暴露权衡」维度；去除个人化表述 |
| `rules/iron-rules.md` #17-18 标记法与测试门禁 | [github/spec-kit](https://github.com/github/spec-kit) | Test-First 门禁与 `[NEEDS CLARIFICATION]` 标记法，适配 agent 工作模式 |
| `rules/iron-rules.md` #19 环境隔离 | Python 官方 venv 指南 + claude-code best practices | 泛化为跨语言的环境隔离要求 |
| `deploy/` + `tools/q/q.py` 的搜索后端 | [searxng/searxng](https://github.com/searxng/searxng)（AGPL-3.0） | 作为**独立后端服务引用**（未改其源码）；本仓仅提供部署样例（compose/settings）与调用协议 |
| `rules/search-chain.md` 搜狗选择器与节流参数 | **Original**（批量实证沉淀：`div.vrwrap` 无验证码最优、≤4 批/75-120s 间隔、跨任务 ≥90s、双故障形态判别表） | — |
| `rules/onboarding.md` + `snippets/AGENTS-onboarding.md` | 社区分享「我给所有 AI Agent 写了一份入职手册」（2026-09-13，未署名原帖） | 14 节提示词改写为协议体；去除 WorkBuddy 专属路径泛化为 `.<agent>/memory/`；修正全角句号笔误；与 registry / skills 协议交叉引用 |
| `snippets/AGENTS-cot.md` | [NoWait: arXiv:2506.08343](https://arxiv.org/html/2506.08343v1)（EMNLP 2025 Findings）＋ apolo.us 推理 token 分析 ＋ [linshenkx/prompt-optimizer](https://github.com/linshenkx/prompt-optimizer) 评估模板的「禁令-失败模式绑定」措辞范式 | 方法论吸收（不复制 AGPL 模板文本）：每条禁令绑定一个具体失败模式；分推理层（部分有效，减负）与输出层（硬禁令）两档；Non-Goals 显式声明不禁真实回溯 |

其余文件（模板 / 示例 / 片段）为上述规则的派生内容。引用均遵循上游各自许可证；本仓库整体以 [MIT](LICENSE) 发布。
