# Journal 与会话交接协议

> 面向任何 AI coding agent 的日常工作记录与交接约定。与 [devlog 协议](devlog.md)配合使用：DEVLOG 记「项目账」，journal 记「日常账」，handoff 记「交给下一个会话的账」。版本 v1.0。

## 1. 每日 Journal

- 工作区级目录：`journal/YYYY-MM-DD.md`，一天一文件。
- 每次操作 / 会话追加一条：时间 + 一两句话（做了什么、结论）。
- 多个 agent 共用同一 journal 时，每条记录加 `[<agent-名>]` 前缀，避免混淆。
- 任何密钥 / token 写入 journal 前必须脱敏。

## 2. 会话交接（Handoff）

会话结束前更新 `journal/_handoff.md`，让下一个会话（哪怕换了模型 / 平台）能无缝续接。

**结构**（全文 **< 100 行**，电报体、删客套）：

```markdown
# Handoff — <YYYY-MM-DD HH:mm>

## 会话目标
<一句话>

## 已完成
- [x] <具体产出 + 关键决策>

## 未完成
- [ ] <任务 + 阻塞原因>

## 上下文快照
- 变更文件：<清单>
- 分支 / 环境状态：<clean 或 dirty + 关键状态变量>
- 基线条目：基于 #<DEVLOG 前条目标识>

## 下次第一步
<具体起始指令>
```

**约束**：

- `< 100 行`；安全相关的状态必须完整记录，不受篇幅约束。
- 最后一个写入者直接覆盖 `_handoff.md`——每个 agent 写自己的最新状态，属设计内行为（更早状态由当日 journal 与 DEVLOG 兜底）。

> 交接文档结构参考 [mattpocock/skills](https://github.com/mattpocock/skills) 的 `/handoff` 技能，改动说明见 [SOURCES.md](../SOURCES.md)。
