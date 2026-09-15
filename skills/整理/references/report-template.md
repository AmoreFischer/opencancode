# 质量快照报告模板

> 复制此模板，填充实际数据后存入 `plans/` 对应目录的 `reports/`（或你习惯的报告位置）

```markdown
# 质量快照 — {日期}

> 项目: {project_name}
> 上次报告: {prev_report_date or "基线（首次）"}

## 指标对比

| 指标 | 上次 | 本次 | 变化 |
|------|------|------|------|
| lint errors | {prev} | {curr} | {delta} |
| tests passed | {prev} | {curr} | {delta} |
| tests failed | {prev} | {curr} | {delta} |
| dependencies | {prev} | {curr} | {delta} |
| source files | {prev} | {curr} | {delta} |
| total lines | {prev} | {curr} | {delta} |

## 变动明细

### ✅ 提升
- {具体改进}

### ⚠️ 退步
- {具体退步}

### 📋 待处理
- {遗留问题}

## 质量评分

| 维度 | 上次 | 本次 | 变化 |
|------|------|------|------|
| 单一职责 | x/10 | x/10 | |
| 生命周期 | x/10 | x/10 | |
| 防御式编程 | x/10 | x/10 | |
| DRY | x/10 | x/10 | |
| KISS | x/10 | x/10 | |
| 可观测性 | x/10 | x/10 | |
| 代码即文档 | x/10 | x/10 | |
| 安全性 | x/10 | x/10 | |
| 测试覆盖 | x/10 | x/10 | |
| 项目结构 | x/10 | x/10 | |

## 自我回顾

### 新发现的模式
- {模式描述}

### 假设
- 假设：增加 {X} 检查项，预期减少 {Y} 类错误
- 验证方式：下次清洗时检查该类错误是否减少

### 检查清单更新
- [ ] 是否需要追加新的检查项到 checklist.md？
```
