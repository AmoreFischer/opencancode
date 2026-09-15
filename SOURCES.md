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
| `snippets/AGENTS-cot.md` | [NoWait: arXiv:2506.08343](https://arxiv.org/html/2506.08343v1)（EMNLP 2025 Findings）＋ apolo.us 推理 token 分析 ＋ [linshenkx/prompt-optimizer](https://github.com/linshenkx/prompt-optimizer) 评估模板的「禁令-失败模式绑定」措辞范式 | 方法论吸收（不复制 AGPL 模板文本）：每条禁令绑定一个具体失败模式；分推理层（部分有效，减负）与输出层（硬禁令）两档；Non-Goals 显式声明不禁真实回溯。第 0 条输入侧闸门（2026-09-15 增）为 **Original**——「澄清先于揣测」纪律的泛化（歧义短指令列候选请用户选，禁默认揣测），与推理层禁令构成先后两道闸门 |
| `skills/提问智慧/SKILL.md` ESR 六律与追问框架 | [ESR: How To Ask Questions The Smart Way](http://www.catb.org/~esr/faqs/smart-questions.html)（中译 [ryanhanwu/How-To-Ask-Questions-The-Smart-Way](https://github.com/ryanhanwu/How-To-Ask-Questions-The-Smart-Way)） | 六律从「论坛求助」转化为「AI 协作追问」框架；模式体系（诊断/自检/grilling/共享语言/小模型注入）为原创组合；共享语言示例表改用虚构项目 |
| `skills/提问智慧/SKILL.md` 模式 D/E | [mattpocock/skills](https://github.com/mattpocock/skills) | `/grill-me` → Grilling Session（≤6 问结构化对齐）；`CONTEXT.md` → 共享语言注入，泛化为 agent 无关写法 |
| `skills/brainstorming/SKILL.md` | [obra/superpowers](https://github.com/obra/superpowers)（其 brainstorming skill）＋ [github/spec-kit](https://github.com/github/spec-kit) | 设计先行 checklist 与 HARD-GATE 移植；`[NEEDS CLARIFICATION]` 自检来自 spec-kit；跨技能引用改为本仓技能链 |
| `skills/writing-plans/SKILL.md` | [obra/superpowers](https://github.com/obra/superpowers)（其 writing-plans skill）＋ [github/spec-kit](https://github.com/github/spec-kit) | 2-5 分钟任务粒度与 TDD 循环保留；Pre-Implementation Gates 融合 spec-kit 门禁思想；计划模板 frontmatter 泛化 |
| `skills/systematic-debugging/SKILL.md` + `skills/极简沟通/SKILL.md`（模式C）+ `skills/整理/SKILL.md`（L3.2） | [obra/superpowers](https://github.com/obra/superpowers)（其 systematic-debugging skill）＋ [DietrichGebert/ponytail](https://github.com/DietrichGebert/ponytail) | 4 阶段流程（复现→隔离→根因→验证）保留；ponytail「修共享函数不修调用者」并入阶段 4、极简沟通模式 C 与整理 L3.2 三处应用 |
| `skills/study/SKILL.md` 学习前自检 | [multica-ai/andrej-karpathy-skills](https://github.com/multica-ai/andrej-karpathy-skills) | Karpathy 四准则（先想清楚/简单优先/精确修改/目标驱动）转为学习场景自检（与 iron-rules #12-15 同源） |
| `skills/study/SKILL.md` 学习结晶 + 声明核验 | Hermes Agent（开源 agent 项目，名称照录） | 「学习 → 结晶 → 技能 → 自我改进」闭环与 Grounded Citations（声明回溯原文逐条核验）思想吸收 |
| `skills/study/SKILL.md` 学术研究模式 | nature-skills / paper-craft-skills / ljg-skill-xray-paper / ljg-skill-paper（GitHub 技能库，名称照录可检索） | 论文解构五步（结构解构/钥匙概念/认知碰撞/声明核验/科研绘图）为方法论吸收，不装上游本体 |
| `skills/小本本/SKILL.md` 模式 C | memorax（闭源云记忆产品，名称照录） | 「relevant to current task」最小召回思想——只吸收规则，不引入闭源本体 |
| `skills/小本本/SKILL.md` 记忆两契约 | affaan-m/ECC（GitHub，名称照录）＋「记忆投毒=持久化 prompt injection」安全共识 | create-only 写入契约 + 召回内容不可执行契约，防记忆覆写与记忆投毒 |
| `skills/极简沟通/SKILL.md` 模式 A | [mattpocock/skills](https://github.com/mattpocock/skills)（其 /caveman 技能） | 压缩四规则（去冠词/填充/客套/犹豫；保留技术实质；`[THING][VERB][REASON]` 句式；安全例外）；本版增加 A-/B 分档与上下文自动触发 |
| `skills/极简沟通/SKILL.md` 反伪压缩/永不省清单/模式 A-/Auto-Clarity | [JuliusBrussee/caveman](https://github.com/JuliusBrussee/caveman)（**MIT**） | v2.6 规则文本吸收：中文适配（否定词/数字/助词永不省）、禁自造缩写与箭头、受众轴局部恢复；遵循 MIT 许可注明出处，版权归上游作者 |
| `skills/整理/SKILL.md` L3.3 R1-R6 诊断链 | [hyhmrright/brooks-lint](https://github.com/hyhmrright/brooks-lint)（MIT） | 12 本经典书蒸馏的六维诊断（认知过载/变更传播/知识重复/偶发复杂度/依赖失序/领域模型扭曲）方法论吸收；出处编号对齐本仓 iron-rules |

其余文件（模板 / 示例 / 片段）为上述规则的派生内容。引用均遵循上游各自许可证；本仓库整体以 [MIT](LICENSE) 发布。
