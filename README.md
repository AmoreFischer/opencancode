# OpenCanCode

> **One ordinary person's agent usage habits. Better suggestions welcome!**
> 一名普通人的 agent 使用习惯。欢迎提供更好的建议！

Open, agent-agnostic protocols for **development logging** — a DEVLOG execution-metadata convention plus a daily journal & session-handoff chain that any AI coding agent can adopt: CLI agents, IDE agents, autonomous harnesses, or a mix of them.

## Why

AI agents work across sessions, models, and runtimes. A log entry without context decays fast: three months later nobody can tell which model wrote it, on what platform, or which baseline it continued from. This repo distills one battle-tested logging chain into small, copy-paste pieces.

## What's inside

```
opencancode/
├── rules/
│   ├── devlog.md            # DEVLOG protocol: entry structure + execution metadata + relay reconciliation
│   ├── iron-rules.md        # 28 engineering iron rules for AI coding agents (5 groups)
│   ├── journal-handoff.md   # daily journal + <100-line session handoff
│   ├── registry.md          # environment registry: models/proxy/APIs/services/tools — look up before asking, register on change
│   ├── search-chain.md      # free search chain: self-hosted backend -> free fallback -> STOP
│   ├── skills.md            # skill registry: frontmatter is the source, indexes are generated
│   └── onboarding.md        # agent onboarding protocol: discover workspace root, save stable rules, never hardcode paths
├── skills/
│   ├── 提问智慧/SKILL.md              # requirement refinement: ESR six rules -> precise clarification list, grilling session, shared language
│   ├── brainstorming/SKILL.md         # design first: refine an idea into an approved design doc before any code
│   ├── writing-plans/SKILL.md         # turn an approved design into a 2-5-min-step TDD implementation plan
│   ├── systematic-debugging/SKILL.md  # 4-stage debugging: reproduce -> isolate -> root cause -> fix & verify
│   ├── study/SKILL.md                 # four research modes: quick learn / deep research / ecosystem scan / dual-axis analysis + crystallization
│   ├── 小本本/SKILL.md                # pitfall memory: five-element notes, create-only write contract, minimal task-scoped recall
│   ├── 极简沟通/SKILL.md              # caveman-style compressed output (A-/A/B tiers) + ponytail pre-code ladder
│   ├── 整理/SKILL.md                  # session hygiene: stage wrap / end-of-day / code cleanup (ponytail) / doc review / consistency (+ references/ toolkit)
│   ├── ext-manager/SKILL.md           # extension governance: register -> evaluate (4 questions) -> install -> enable -> review; never install unregistered
│   ├── 内肃/SKILL.md                  # heavy system purge (3 tiers): full-code / whole-system / monthly audit; explicit user trigger only, backup first
│   ├── deep-dive/SKILL.md             # six-dimension muckraking research on a company/industry/product; narrative output, not data tables
│   └── kb-evolve/SKILL.md             # feedback-driven KB/QA evolution loop: 4-type diagnosis + attribution matrix + evolution-task ledger
├── templates/
│   ├── DEVLOG-entry.md      # fill-in entry template
│   ├── HANDOFF.md           # fill-in handoff template
│   ├── REGISTRY-apis.md     # fill-in external API registry template
│   ├── REGISTRY-models.md   # fill-in model registry template
│   ├── REGISTRY-proxy.md    # fill-in proxy & port registry template
│   ├── REGISTRY-services.md # fill-in local service registry template
│   ├── REGISTRY-tools.md    # fill-in tool registry template
│   ├── SKILL.md             # skill file template (frontmatter: name/description/version/triggers)
│   ├── SKILLS.json          # machine-readable skill manifest template (generated, never hand-edited)
│   └── REPORT.html          # single-file report template: 3-pane (meta/content/toc) + draggable splitters + dark-first + theme toggle + back-to-top
├── examples/
│   ├── devlog-example.md    # fictional project, 3 entries incl. cross-model & cross-runtime relay
│   ├── registry-example.md  # fictional workspace with all five registry tables filled in
│   └── skills-manifest-example.md  # frontmatter → manifest → trigger table, plus a rebuild after change
├── tools/
│   └── q/q.py               # universal free-search CLI: searxng -> sogou-news fallback -> STOP
├── deploy/
│   ├── searxng-compose.yml  # self-hosted search backend, loopback-bound, one command
│   └── settings.example.yml # minimal backend settings (json on, limiter off)
└── snippets/
    ├── AGENTS-log.md        # paste-ready rule block: development logging
    ├── AGENTS-registry.md   # paste-ready rule block: environment registry lookup
    ├── AGENTS-rules.md      # paste-ready rule block: Top 10 iron rules
    ├── AGENTS-search.md     # paste-ready rule block: free search chain + STOP discipline
    ├── AGENTS-skills.md     # paste-ready rule block: skill manifest reconciliation
    ├── AGENTS-onboarding.md # paste-ready rule block: first-time agent onboarding into a long-term workspace
    └── AGENTS-cot.md        # paste-ready rule block: chain-of-thought quality bans (reasoning + final output)
```

## Adopt in 3 steps

1. Paste the `snippets/` rule blocks you need into your agent's instruction file (`AGENTS.md`, `CLAUDE.md`, system prompt — whatever your agent reads): development logging (`AGENTS-log.md`), environment registry (`AGENTS-registry.md`), iron rules (`AGENTS-rules.md`), skill reconciliation (`AGENTS-skills.md`), free search chain (`AGENTS-search.md`), first-time onboarding (`AGENTS-onboarding.md`), chain-of-thought quality bans (`AGENTS-cot.md`).
2. Copy `templates/` into your workspace as starting points for `DEVLOG.md`, `journal/_handoff.md`, and your `registry/` tables. Copy any `skills/<id>/` directory you want into your agent's skills folder — one directory per skill, frontmatter (`name/description/version/triggers`) is the single source of truth (see `rules/skills.md`).
3. Follow `rules/`: every entry records what was done, decisions, pitfalls, artifacts — plus **who / where / which model / which baseline** via the execution metadata block.

## Core ideas in one minute

- **Execution metadata block** — every log entry opens with platform, session id, model (with thinking/reasoning level), mode, cost, and relay point. Future-you can audit any entry.
- **Relay reconciliation** — when a different model or runtime continues the work, the entry must reference what it continues ("based on #12"), and reconcile before writing if the baseline moved. Think optimistic locking for logs.
- **Handoff under 100 lines** — end every session with a compact structured handoff: goal / done / undone / context snapshot / next first step.
- **Registry: register once, look up everywhere** — which models you have (and how each agent calls them), which proxy ports serve what, which external APIs you depend on, which services run locally, and where your tools live — all in `registry/` tables (`models` / `proxy` / `apis` / `services` / `tools`). Agents look them up before asking you, and register changes as they happen — no more re-stating your setup in every conversation.
- **Iron rules** — 28 engineering disciplines in five groups (process & principles, environment isolation, Git & credentials, service ops, debugging methodology) that override agent defaults; a Top-10 paste-ready snippet gets you started.
- **Skill registry** — each skill's frontmatter is the single source of truth; manifests and trigger tables are **generated, never hand-copied**; sessions reconcile against the manifest at start, so stale skill lists surface themselves instead of silently misleading.
- **Twelve ready-to-adopt skills** — three clusters covering the full working arc. Process: clarify before guessing (提问智慧), design before code (brainstorming), plan before implementation (writing-plans), root cause before patch (systematic-debugging). Knowledge & communication: four-mode research with a crystallization step (study), pitfall memory with create-only and recall-is-not-execute contracts (小本本), tiered token-economy output (极简沟通), session hygiene (整理). Governance & deep research: extension lifecycle gated on register-first (ext-manager), heavy three-tier system purge that only ever fires on explicit user request with backup-first (内肃), six-dimension muckraking narrative research (deep-dive), and a feedback-driven evolution loop for knowledge/QA services (kb-evolve). Each is a self-contained `skills/<id>/SKILL.md` with explicit trigger words; they cross-reference into a chain: 提问智慧 → brainstorming → writing-plans → execution, systematic-debugging when things break, 整理 to wrap up, 内肃 when it's purge season.
- **Search kit** — a self-hosted free search chain: the `q` CLI queries your own SearXNG backend (`deploy/` brings it up in one command), falls back to free news scraping, and **stops** when both fail — agents never silently degrade to paid or platform-native search; every result carries a cost stamp.

## 中文简介

面向 AI 编程 agent 的开放式开发日志协议：**DEVLOG 执行元信息** + **journal / 会话交接** + **环境注册表** + **工程铁律** + **技能管理** + **技能库十二件**（流程：需求澄清 提问智慧 / 设计先行 brainstorming / 实施计划 writing-plans / 系统调试 systematic-debugging；知识与沟通：研究 study / 踩坑记忆 小本本 / 极简沟通 / 会话卫生 整理；治理与深挖：扩展管理 ext-manager / 重型清理 内肃 / 深挖 deep-dive / 知识库进化 kb-evolve） + **免费搜索链** + **Agent 入职协议**。任何 agent（CLI / IDE / 自治 harness，或混用）都可采用：把 `snippets/` 里的规则片段粘进你的 agent 指令文件，用 `templates/` 起步，`skills/` 目录整拷进你的技能目录，`deploy/` 一把起自托管搜索后端、`tools/q/` 一行命令全平台调用，规则细节见 `rules/`、技能见 `skills/`。核心主张：每条日志都能回答「谁、在哪个平台、用哪个模型、基于哪条基线写的」；环境资产一次登记先查后问；铁律为 agent 提供行为约束层；技能索引生成不手抄；联网获取走免费链、全程盖章可审计，绝不静默降级付费/原生。

## Sources & attribution

See [SOURCES.md](SOURCES.md). The metadata protocol is original; the handoff structure is adapted from [mattpocock/skills](https://github.com/mattpocock/skills); the relay-reconciliation rule is inspired by [code-yeongyu/oh-my-openagent](https://github.com/code-yeongyu/oh-my-openagent).

## License

[MIT](LICENSE)
