# 技能对账规则片段（OpenCanCode）

> **用法**：整段粘贴进任意 agent 的指令文件（`AGENTS.md` / `CLAUDE.md` / system prompt），`<skills-dir>` 换成你的技能目录。规则详情见 [rules/skills.md](../rules/skills.md)。

## 技能管理（Skills）

1. 技能放 `<skills-dir>/<id>/SKILL.md`；frontmatter（name / description / version / triggers）是**唯一权威**。
2. 会话启动时对比 `SKILLS.json` 与本地 / 已加载技能：缺失或版本不一致 → 提示刷新，**不静默用旧清单干活**。
3. 技能变更后：递增 version → 重建 `SKILLS.json` 与各入口触发词表 → 与技能改动**同一个 commit**；未提交 = 其他平台不可见。
4. 禁止在入口文件手抄技能条目——一切索引从 frontmatter 重建，手抄一处就是漂移的开始。
