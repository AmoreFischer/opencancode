# 会话交接模板

> 会话结束前填写 `journal/_handoff.md`，直接覆盖上一份（每个 agent 写自己的最新状态）。全文 **< 100 行**，电报体。规则见 [rules/journal-handoff.md](../rules/journal-handoff.md)。

```markdown
# Handoff — <YYYY-MM-DD HH:mm>

## 会话目标
<一句话>

## 已完成
- [x] <具体产出 + 关键决策>

## 未完成
- [ ] <任务 + 阻塞原因>

## 上下文快照
- 变更文件：<清单或 git diff --name-only 输出>
- 分支 / 环境状态：<clean / dirty；关键状态变量>
- 基线条目：基于 #<DEVLOG 前条目标识>

## 下次第一步
<具体起始指令>
```
