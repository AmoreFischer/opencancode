# 技能清单示例 — 虚构工作区全链演示

> 展示「frontmatter → 机器清单 → 触发词表」的生成链，以及一次变更后的重建。规则见 [rules/skills.md](../rules/skills.md)。

## 1. 两个技能的 frontmatter

`<skills-dir>/code-review/SKILL.md`：

```yaml
---
name: code-review
description: 按检查清单审查代码质量与安全问题
version: 1.2
triggers: [review, 代码审查, 检查质量]
source: original
---
```

`<skills-dir>/deploy-check/SKILL.md`：

```yaml
---
name: deploy-check
description: 发布前环境与配置核对
version: 1.0
triggers: [deploy, 发布检查]
source: original
---
```

## 2. 重建出的 `SKILLS.json`

```json
{
  "updated": "2026-09-12",
  "skills": [
    { "id": "code-review", "version": "1.2", "description": "按检查清单审查代码质量与安全问题" },
    { "id": "deploy-check", "version": "1.0", "description": "发布前环境与配置核对" }
  ]
}
```

## 3. 生成的入口触发词表（AGENTS.md 片段）

| 触发词 | 技能 | 版本 |
|---|---|---|
| review / 代码审查 / 检查质量 | code-review | 1.2 |
| deploy / 发布检查 | deploy-check | 1.0 |

## 4. 一次变更后的重建

给 code-review 增加了安全检查步骤 → `version: 1.2` → `1.3` → 重读全部 frontmatter 重建 `SKILLS.json` 与上表 → 与 SKILL.md 改动**同一个 commit** 提交。其他平台 pull 后，启动对账发现 1.3 > 已加载 1.2，提示刷新。
