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
│   ├── journal-handoff.md   # daily journal + <100-line session handoff
│   └── registry.md          # environment registry: look up before asking, register on change
├── templates/
│   ├── DEVLOG-entry.md      # fill-in entry template
│   ├── HANDOFF.md           # fill-in handoff template
│   ├── REGISTRY-models.md   # fill-in model registry template
│   └── REGISTRY-proxy.md    # fill-in proxy & port registry template
├── examples/
│   ├── devlog-example.md    # fictional project, 3 entries incl. cross-model & cross-runtime relay
│   └── registry-example.md  # fictional workspace with models & proxy tables filled in
└── snippets/
    ├── AGENTS-log.md        # paste-ready rule block: development logging
    └── AGENTS-registry.md   # paste-ready rule block: environment registry lookup
```

## Adopt in 3 steps

1. Paste `snippets/AGENTS-log.md` and `snippets/AGENTS-registry.md` into your agent's instruction file (`AGENTS.md`, `CLAUDE.md`, system prompt — whatever your agent reads).
2. Copy `templates/` into your workspace as starting points for `DEVLOG.md`, `journal/_handoff.md`, and your `registry/` tables.
3. Follow `rules/`: every entry records what was done, decisions, pitfalls, artifacts — plus **who / where / which model / which baseline** via the execution metadata block.

## Core ideas in one minute

- **Execution metadata block** — every log entry opens with platform, session id, model (with thinking/reasoning level), mode, cost, and relay point. Future-you can audit any entry.
- **Relay reconciliation** — when a different model or runtime continues the work, the entry must reference what it continues ("based on #12"), and reconcile before writing if the baseline moved. Think optimistic locking for logs.
- **Handoff under 100 lines** — end every session with a compact structured handoff: goal / done / undone / context snapshot / next first step.
- **Registry: register once, look up everywhere** — which models you have (and how each agent calls them), which proxy ports serve what, live in `registry/` tables. Agents look them up before asking you, and register changes as they happen — no more re-stating your setup in every conversation.

## 中文简介

面向 AI 编程 agent 的开放式开发日志协议：**DEVLOG 执行元信息** + **journal / 会话交接** + **环境注册表**。任何 agent（CLI / IDE / 自治 harness，或混用）都可采用：把 `snippets/` 里的规则片段粘进你的 agent 指令文件，用 `templates/` 起步，规则细节见 `rules/`。核心主张：每条日志都能回答「谁、在哪个平台、用哪个模型、基于哪条基线写的」；模型、代理端口等环境资产一次登记，agent 先查后问，跨对话免重复强调。

## Sources & attribution

See [SOURCES.md](SOURCES.md). The metadata protocol is original; the handoff structure is adapted from [mattpocock/skills](https://github.com/mattpocock/skills); the relay-reconciliation rule is inspired by [code-yeongyu/oh-my-openagent](https://github.com/code-yeongyu/oh-my-openagent).

## License

[MIT](LICENSE)
