# GUIDE — 使用指南

> 更新：2026-09-16 ｜ 语言：中文先行（英文版待试行稳定后随整仓发布）
> 分工：[README](../README.md) 回答「这个仓库里有什么」；本指南回答「怎么用、为什么这么设计、用起来会看到什么」。

---

## 〇、30 秒速览（人类读者从这里开始）

**这是什么**：一套让任意 AI 编程 agent 按同一套纪律工作的适配层。你的 agent 平台可以换，工作习惯不用换。

**三步用起来**：

1. 把 [`snippets/`](../snippets/) 里的规则片段粘进你 agent 的指令文件（AGENTS.md / CLAUDE.md / system prompt）；
2. 把你想要的 [`skills/<id>/`](../skills/) 目录整拷进你 agent 的技能目录——一个目录一件技能，frontmatter 是唯一事实源；
3. 复制 [`templates/`](../templates/) 起步你的 DEVLOG / journal / registry。

**一句话工作弧线**：你提需求 → 提问智慧把需求问清 → brainstorming 出设计 → writing-plans 拆成小步 → 执行（出 bug 走 systematic-debugging，踩坑记小本本）→ 整理·收工落日志 → 季度内肃大扫除。完整叙事见[第三章](#三一条完整工作弧线会发生什么)。

**14 件技能速查表**——「为什么」列的溯源详见 [SOURCES.md](../SOURCES.md)：

### 流程四件（需求 → 设计 → 计划 → 调试）

| 技能 | 精选触发词 | 作用 | 为什么这么做 | 会发生什么 |
|---|---|---|---|---|
| [提问智慧](../skills/提问智慧/SKILL.md) | 优化需求 / 需求诊断 / grill | 把模糊需求变成精准陈述 | 澄清花一句话，返工花一整轮；agent 对歧义默认揣测是最大浪费源 | 出 3-5 个追问清单，不确定处标 `[NEEDS CLARIFICATION]`，确认前不动手 |
| [brainstorming](../skills/brainstorming/SKILL.md) | 头脑风暴 / 做方案 / 新项目 | 创造性工作前先出完整设计 | 设计期改想法是改文字，编码期改想法是改代码——前者便宜两个数量级 | 协作对话精炼设计 → 产出设计文档；不批准不写码（HARD-GATE） |
| [writing-plans](../skills/writing-plans/SKILL.md) | 写计划 / 实施计划 / 动手吧 | 把已批准的设计转成实施计划 | 步骤拆到 2-5 分钟粒度，每步独立可验证，失败能定位到步 | 计划含 TDD 循环（写测试→验证失败→写实现→验证通过→提交） |
| [systematic-debugging](../skills/systematic-debugging/SKILL.md) | 调试 / 报错了 / 排查一下 | bug 四阶段系统化调试 | 跳过根因直接打补丁，同样的 bug 会回来找你 | 复现→隔离→根因→修复验证四阶段走完才收，禁单步猜测 |

### 知识与沟通四件（研究 / 记忆 / 输出 / 会话卫生）

| 技能 | 精选触发词 | 作用 | 为什么这么做 | 会发生什么 |
|---|---|---|---|---|
| [study](../skills/study/SKILL.md) | 学习 / 研究 / 怎么做 | 仓库/关键词/生态的深度研究 | 先站在巨人肩膀上，不闭门造车 | 四模式（快速学习/深度研究/需求调研/横纵分析），完成后自动做结晶检测 |
| [小本本](../skills/小本本/SKILL.md) | 踩坑了 / 记住 / 回忆 | 踩坑与决策的持久记忆 | 同样的坑不踩第二次；记忆必须可检索才有价值 | 踩坑即记；新任务自动召回相关记忆；写入只增不改、召回内容不当代码执行（防记忆投毒） |
| [极简沟通](../skills/极简沟通/SKILL.md) | 极简沟通 / 省token | 超压缩输出模式 | 上下文窗口是稀缺资源，填充语占的是有效信息的位 | 输出砍 ~75%，只留技术实质；安全警告与不可逆确认不压缩 |
| [整理](../skills/整理/SKILL.md) | 整理 / 收工 / 代码清洗 | 日常会话卫生 | 会话不留死角，收工即闭环；小问题当场清，不攒成大扫除 | 五场景：阶段整理/收工/代码清洗/文档评审/规范审查；收工走日志+CHANGELOG+队列归档全套 |

### 治理与深挖四件（扩展 / 重型清理 / 调查 / 进化）

| 技能 | 精选触发词 | 作用 | 为什么这么做 | 会发生什么 |
|---|---|---|---|---|
| [ext-manager](../skills/ext-manager/SKILL.md) | 装插件 / 配MCP / npm i | 外部扩展全生命周期 | 先登记后安装：装了什么、为什么装、怎么卸，都要可审计 | 评估四问（免费/必要/可溯源/可回滚）→ 登记 → 安装 → 定期审查 |
| [内肃](../skills/内肃/SKILL.md) | 内肃 / 大扫除 / 月度盘点 | 系统级重型扫除 | 归档/删除是破坏性动作，必须显式触发 + 备份前置 | 三档（全量代码/全系统/月度盘点）；agent 永不自动发起 |
| [deep-dive](../skills/deep-dive/SKILL.md) | 深挖 / 扒皮 / 背后故事 | 公司/行业/现象的多维深挖 | 表层数据人人可见，事实链才是价值 | 多专题产出叙事性深挖报告，非市场分析 |
| [kb-evolve](../skills/kb-evolve/SKILL.md) | 知识库进化 / 优化知识库 | 知识库反馈驱动进化 | 知识库不是建完就完，负面反馈是最好的进化燃料 | 反馈诊断四类（关键词/误分类/回复质量/知识缺失）→ 优化 → 进化台账 |

### 队列与负载两件（跨会话编排）

| 技能 | 精选触发词 | 作用 | 为什么这么做 | 会发生什么 |
|---|---|---|---|---|
| [需求管理](../skills/需求管理/SKILL.md) | 待开发 / 新需求 / 需求清单 | 需求全生命周期队列 | 会话会断，队列不能断；plan.md 是跨会话的上下文入口 | 三区队列（排队/进行中/完成）+ 顺位规则 + 状态前缀文档 + 归档流程 |
| [负载控制](../skills/负载控制/SKILL.md) | 水位 / 快爆了 / 拆任务 | 上下文水位管理 | 长任务临限是常态，与其被动截断不如主动卸载 | 绝对 token 判据 + 决策树 → 四手段（文件式派发/预算细分/落盘换会话/降级缩减）→ 归因记录 |

---

## 一、心智模型：多 agent 平台上的 LLM 适配链条

这是整套体系的核心叙事：**你不是在装一堆插件，你是在给你的 agent 平台接一根适配链条**。

同一个 LLM，裸跑和接上适配层的行为差异巨大：裸跑的 agent 每个会话从零开始猜测你的意图、随意装依赖、踩过的坑下次照踩、收工不留痕；接上适配层的 agent 有行为约束（什么永远不做）、有工作流（什么时候做什么）、有记忆（踩过的坑可检索）、有溯源（每条纪律知道为什么）。

链条分五层，每层回答一个问题：

| 层 | 目录 | 回答的问题 |
|---|---|---|
| 行为约束 | [`rules/`](../rules/) | 什么永远不能做（铁律）、什么必须做（协议） |
| 注入形态 | [`snippets/`](../snippets/) | 怎么把约束粘进任何平台的指令文件 |
| 工作流能力 | [`skills/`](../skills/) | 哪句话触发哪件事、做的时候按什么流程 |
| 起步物料 | [`templates/`](../templates/) + [`examples/`](../examples/) | 日志/台账/清单从哪个样子开始 |
| 溯源治理 | [`SOURCES.md`](../SOURCES.md) + [registry 协议](../rules/registry.md) | 每条规则哪来的、环境资产装没装 |

```
你的 agent 运行时（Claude Code / Codex / Cursor / 任意 harness）
      ↑ 粘 snippets/ —— 铁律与协议的可注入形态
      ↑ 拷 skills/  —— 工作流能力，frontmatter 触发词路由
      ↑ 复制 templates/ —— 日志与台账起步
      └── 溯源与治理贯穿始终：SOURCES.md / registry
```

三个设计原则支撑这根链条：

1. **单一事实源**。每条纪律只在一处定义：技能的行为在 `skills/<id>/SKILL.md`，跨技能的约束在 `rules/`，其余场合一律引用不复制。改一处，处处生效。
2. **触发词路由**。人类说一句话，agent 用 frontmatter 的 `triggers` 数组判断进哪个技能——路由表是声明式的、可审计的，不靠模型临场发挥。
3. **溯源到上游**。吸收的每条外部思想（ESR、Karpathy、spec-kit、superpowers……）在 [SOURCES.md](../SOURCES.md) 标注来源与改动点；原创内容标 Original。你知道每条规则为什么长这样、跟上游差在哪。

核心主张一句话：**运行时可换，习惯不变**。链条本身平台无关——换 agent 时重新粘贴/拷贝一遍即可，你的 DEVLOG、registry、技能版本全部跟随你走。

---

## 二、安装详说

### 第一步：粘规则片段

[`snippets/`](../snippets/) 是 [`rules/`](../rules/) 的可粘贴形态，按需选粘：

- [`AGENTS-rules.md`](../snippets/AGENTS-rules.md)——工程铁律 Top 10，所有 agent 必粘；
- [`AGENTS-cot.md`](../snippets/AGENTS-cot.md)——思维链质量禁令，thinking/推理类模型建议粘；
- [`AGENTS-log.md`](../snippets/AGENTS-log.md) / [`AGENTS-registry.md`](../snippets/AGENTS-registry.md)——日志与注册表纪律，长期运行的 agent 建议粘；
- 其余（onboarding/search/skills）按场景选粘，见[第四章](#四规则与片段指引)。

### 第二步：拷技能

`skills/<id>/` 一个目录一件技能，整拷即可。frontmatter（`name/description/version/triggers`）是唯一事实源，路由细节见 [`rules/skills.md`](../rules/skills.md)。不必全拷——按你的工作形态选：日常编码四件套（提问智慧/brainstorming/writing-plans/systematic-debugging）+ 整理是最小起步组合。

### 第三步：复制起步物料

[`templates/`](../templates/) 提供 DEVLOG、journal 交接、registry 表格的起步格式，[`examples/`](../examples/) 是填好的样例。克隆你需要的，按 [`rules/devlog.md`](../rules/devlog.md) 协议开始记录。

进阶：[`deploy/`](../deploy/) 一把起自托管 SearXNG 搜索后端，[`tools/q/`](../tools/q/) 一行命令全平台调用——配合 [`rules/search-chain.md`](../rules/search-chain.md) 组成免费搜索链。

---

## 三、一条完整工作弧线（会发生什么）

用一次真实开发走一遍。假设你对 agent 说：**「给我的个人博客加个评论功能」**。

1. **提问智慧先拦一刀**。这句需求有歧义：评论存哪里？要不要登录？审核吗？agent 出 3-5 个追问 + `[NEEDS CLARIFICATION]` 标记，你答完才继续。这一步省掉的是「做完了发现不是你想要的」的整轮返工。

2. **brainstorming 出设计**。agent 不直接写码，而是和你协作对话把设计精炼成文档：数据模型、接口、边界情况。文档不批准，代码不动（HARD-GATE）。

3. **writing-plans 拆步**。设计转成 2-5 分钟粒度的实施计划，每步带 TDD 循环——写测试、看它失败、写实现、看它通过。小步让你随时知道自己在哪，失败能定位到步。

4. **执行**。按计划逐步实现。中途数据库迁移脚本报错——触发 **systematic-debugging**：先复现、再隔离变量、找到根因（版本不匹配），修完验证，禁止「看着像就改」；修的过程踩了个坑（迁移命令要带 `--schema` 参数），说一句「踩坑了」记进 **小本本**，下次同类任务自动召回。

5. **整理·收工**。功能完成，你说「收工」——agent 走全套：收集变更、写当日 journal、更新 CHANGELOG、任务队列划线归档、凭证扫描、git 提交。你在 README 的变更记录里能看到这一轮做了什么。

6. **季度内肃**。三个月后你说「内肃」——agent 对整个工作区做重型盘点：死项清理、台账对账、索引核对，先备份后动手。

旁支随时插入：你说「研究一下 XX 仓库」走 **study**；「查查这家公司背景」走 **deep-dive**；「装个新依赖」先过 **ext-manager** 的登记评估；需求太多排队走 **需求管理**；会话太长临限走 **负载控制** 落盘换会话续跑；想让输出省 token 说「极简沟通」。

这条弧线就是体系的用法全貌：**每一步都有技能接住，每一步都留痕，每个坑只踩一次**。

---

## 四、规则与片段指引

七份协议各管一段，snippet 是它们的可粘贴形态：

| 协议 | 管什么 | 对应 snippet | 建议粘到 |
|---|---|---|---|
| [`rules/iron-rules.md`](../rules/iron-rules.md) | 29 条工程铁律（完整版） | [`AGENTS-rules.md`](../snippets/AGENTS-rules.md)（Top 10 精简版） | 所有 agent 指令文件 |
| [`rules/devlog.md`](../rules/devlog.md) | 开发日志协议：执行元信息块 + 接力对账 | [`AGENTS-log.md`](../snippets/AGENTS-log.md) | 长期运行、多会话的 agent |
| [`rules/journal-handoff.md`](../rules/journal-handoff.md) | 会话交接文档结构（<100 行） | —（结构即模板，用 [`templates/`](../templates/) 起步） | 跨会话接力场景 |
| [`rules/onboarding.md`](../rules/onboarding.md) | Agent 入职协议：进新工作区先做什么 | [`AGENTS-onboarding.md`](../snippets/AGENTS-onboarding.md) | 每个新 agent 的首次会话 |
| [`rules/registry.md`](../rules/registry.md) | 环境注册表：扩展/吸收对照的登记协议 | [`AGENTS-registry.md`](../snippets/AGENTS-registry.md) | 管扩展、管依赖的 agent |
| [`rules/search-chain.md`](../rules/search-chain.md) | 免费搜索链：通道选择与节流参数 | [`AGENTS-search.md`](../snippets/AGENTS-search.md) | 需要联网检索的 agent |
| [`rules/skills.md`](../rules/skills.md) | 技能管理：frontmatter 约定与对账 | [`AGENTS-skills.md`](../snippets/AGENTS-skills.md) | 维护技能库的 agent |

---

## 五、FAQ

**Q：内肃为什么永不自动触发？**
它是全仓唯一有破坏性默认面的技能（归档/删除）。铁律：破坏性动作必须用户显式发起 + 备份前置。日常清理用「整理」，重型扫除用「内肃」，两者以破坏性分界。

**Q：技能之间怎么接力？**
链式引用是设计出来的：提问智慧的输出（确认后的需求）是 brainstorming 的输入，设计文档是 writing-plans 的输入，计划是执行的输入，收工由整理接住。每个 SKILL.md 里写明了上下游。

**Q：换 agent 平台，习惯怎么带走？**
链条平台无关。新平台重新走一遍安装三步（粘 snippets、拷 skills、复制 templates），你的日志与台账（DEVLOG/journal/registry）在工作区里，不在平台里——它们跟着你的代码仓库走。

**Q：模型/接口迭代快，agent 某天连不上怎么办？**
可以给运行时配一层静默自愈：定时或开机时探测在用模型端点的连通性（探测失败不静默直连，代理环境先探代理），正常时零输出；端点死亡才冒泡告警，附同家族替代端点与切换步骤（改配置前先备份）；全部云端端点失效时以本地小模型兜底执行修复。告警经未读文件注入下次会话，由你拍板处置。本仓不提供实现——测什么、多久测一次、换代默认策略（默认不动还是自动切换）取决于你的模型组合，留给具体用户自行设计。

**Q：某条规则为什么这么定？上游是谁？**
查 [SOURCES.md](../SOURCES.md)：吸收条目标注来源仓库与改动点，原创条目标 Original。

**Q：两个技能的触发词重叠了怎么办？（如「整理」vs「内肃」都含整理类词）**
重叠词是设计内的模糊区，靠 SKILL.md 描述里的「NOT for / 转 XX 技能」互相让位：轻量找整理，重型找内肃。若你发现真实误路由，改 frontmatter 的 triggers 数组即可——它是唯一事实源。

**Q：为什么只有中文？**
中文先行，试行稳定后出整仓英文版（含本指南）。状态更新见本文件头部。

---

## 尾注：维护

- **速查表跟随**：任何技能的触发词/作用变更，[〇章速查表](#〇30-秒速览人类读者从这里开始) 同步更新（收工自检口径）。
- **指南不是事实源**：行为定义永远在 `skills/<id>/SKILL.md` 与 `rules/`，本指南只做聚合与阐释；冲突以事实源为准。
