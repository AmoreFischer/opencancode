---
name: writing-plans
description: "将已批准的设计文档转化为可执行的实施计划。每个步骤 2-5 分钟粒度，包含 TDD 循环（写测试→验证失败→写实现→验证通过→提交）。Use when: 设计已批准、需要编写实施计划。NOT for: 还没有设计的项目（先用 brainstorming）。"
version: "1.3"
triggers: ["写计划", "实施计划", "开发计划", "做个计划", "写实施方案", "plan", "实施", "开始做", "动手吧"]
source: "adapted — obra/superpowers writing-plans + github/spec-kit（溯源见仓库 SOURCES.md）"
---

# Skill: 写计划 📋

> 版本：1.3 | 安全等级：🟢 无风险（纯文档）
> 灵感来源：obra/superpowers — writing-plans skill
> 前置技能：[brainstorming](../brainstorming/SKILL.md)（设计文档）

---

## 目标

将已批准的设计文档转化为详细的、可逐步执行的实施计划。计划要足够清晰，让一个没有项目上下文、没有判断力的热情初级工程师也能按步执行。

<HARD-GATE>
必须已有经过用户批准的设计文档。如果没有，先走 [brainstorming](../brainstorming/SKILL.md)。
</HARD-GATE>

---

## 核心原则

- **YAGNI**：你不会需要它——只计划当前需求要的东西
- **DRY**：不要重复自己——复用已有组件
- **TDD**：测试驱动开发——每个任务都走 RED-GREEN-REFACTOR
- **小步提交**：每个步骤完成后立即提交
- **门禁执行**：不满足 Pre-Implementation Gates 的计划不能进入执行——原则不是建议，是门禁

---

## 核心流程

### 流程图

```
设计文档 → 范围检查 → 文件结构规划 → 任务分解(2-5min)
    │                                        │
    ↓                                        ↓
 已批准？                          每任务: 写测试→验证FAIL
    │                               →写实现→验证PASS→提交
    ↓                                        │
 拆分子计划                                所有任务完成？
    │                                    ↙       ↘
    ↓                                 继续      集成验证→最终提交
 范围OK                                      →用户审批→开始执行
```

### Checklist

- [ ] **Spec 先行确认**（来自 obra/superpowers 与 github/spec-kit 的 spec-driven 实践）
  - 进入任务分解前，先确认"要构建什么 / 为什么 / 验收标准"已用**分块 spec** 与用户对齐（逐块确认，不一次性 dump 整份）
  - 若 spec 未对齐 → 回退到 [提问智慧](../提问智慧/SKILL.md) / [brainstorming](../brainstorming/SKILL.md)，不进入门禁
- [ ] **0. Pre-Implementation Gates**（门禁，必须全部通过才能继续）
  - [ ] **Simplicity Gate**：核心变更 ≤3 个，无"未来预留""也许需要"的功能
  - [ ] **Anti-Abstraction Gate**：直接使用框架/库，不创建不必要的抽象层。过工程必须以 `[COMPLEXITY JUSTIFICATION: 理由]` 格式显式记录（架构问责制）
  - [ ] **Clarification Gate**：上游设计文档中所有 `[NEEDS CLARIFICATION]` 标记已解决，计划中无残留
- [ ] **1. 范围检查** — 确认设计聚焦到一个可计划的范围内（如涉及多个独立子系统，建议拆分）
- [ ] **2. 文件结构规划** — 列出要创建/修改的所有文件及其职责
- [ ] **3. 任务分解** — 将设计拆成 2-5 分钟粒度的小任务
- [ ] **4. 每个任务写 TDD 步骤** — 测试先行
- [ ] **5. 保存计划** — 保存到 `plans/YYYY-MM-DD_<功能名>/plan.md`
- [ ] **6. 用户审批计划** — 确认后开始执行

---

## 文件结构规划

在定义任务之前，先列出文件结构：

```
将创建/修改的文件：
- 创建：exact/path/to/file.py  ← 职责：xxx
- 修改：exact/path/to/existing.py:123-145  ← 修改内容：xxx
- 测试：tests/exact/path/to/test.py  ← 测试内容：xxx
```

**原则**：
- 每个文件一个明确职责
- 小而聚焦的文件优于大而全的文件
- 一起变化的文件放在一起
- 遵循已有项目模式

---

## 任务粒度

**每个步骤是一个动作（2-5 分钟）**：

```
✅ 好的步骤：
- "写失败测试"     ← 2分钟
- "运行确认失败"   ← 1分钟
- "写最小实现"     ← 3分钟
- "运行确认通过"   ← 1分钟
- "提交"           ← 1分钟

❌ 坏的步骤：
- "实现整个功能"   ← 太大
- "写代码"         ← 太模糊
- "处理所有边界情况" ← 太笼统
```

---

## 计划文档模板

```markdown
---
title: "<功能名> 实施计划"
project: <项目名>
tags: [计划, <功能标签>]
created: YYYY-MM-DD
updated: YYYY-MM-DD
source: "brainstorming 产出 design.md"
---

# <功能名> 实施计划

> 创建：YYYY-MM-DD | 关联设计：design.md

**目标：** 一句话描述要构建什么

**架构：** 2-3 句话描述方法

**技术栈：** 关键技术/库

---

## Pre-Implementation Gates

| 门禁 | 检查内容 | 状态 |
|------|---------|------|
| Simplicity Gate | 核心变更 ≤3 个，无未来预留 | ✅ / ❌ |
| Anti-Abstraction Gate | 直接用框架，无不必要抽象层 | ✅ / ❌ |
| Clarification Gate | 所有 `[NEEDS CLARIFICATION]` 已解决 | ✅ / ❌ |

> ❌ 任一门禁不通过 → 回退到 brainstorming/提问智慧阶段解决，不进入执行

### 复杂性追踪（如 Simplicity/Anti-Abstraction Gate 未通过）

> 过工程必须有显式记录。格式：`[COMPLEXITY JUSTIFICATION: 理由简述]`

- （无 / 或逐项记录）

## 待澄清项（如有）

> 从上游设计文档继承的 `[NEEDS CLARIFICATION]` 标记，必须在此全部解决

（无待澄清项 / 或逐项列出解决方案）

---

## 反借口表（Anti-Rationalization）

| 你正在想… | 实际情况 |
|-----------|---------|
| "直接开干就行了，写计划浪费时间" | **15 分钟的计划省下数小时的重做。** 没有计划 = 没有验收标准。 |
| "需求会变的，写了也白写" | 计划是活的文档。更新它，不是放弃它。 |
| "我知道要做什么，不需要写下来" | 如果写不下来，说明你没想清楚。**模糊是 bug 的温床。** |
| "边做边想更高效" | 那是碰运气，不是工程。没有计划 = Agent 的输出就是验收标准。 |
| "这个功能很小，计划可以跳过" | 小功能也值得写 3 行计划。**习惯 > 规模。** |

## 文件结构
- 创建：`path/to/file.py` — 职责说明
- 修改：`path/to/existing.py` — 修改说明
- 测试：`tests/path/to/test.py` — 测试说明

---

### Task 1: <组件名>

**文件：**
- 创建：`exact/path/to/file.py`
- 测试：`tests/exact/path/to/test.py`

- [ ] **Step 1: 写失败测试**

```python
def test_specific_behavior():
    result = function(input)
    assert result == expected
```

- [ ] **Step 2: 运行测试确认失败**

运行：`pytest tests/path/test.py::test_name -v`
预期：FAIL

- [ ] **Step 3: 写最小实现**

```python
def function(input):
    return expected
```

- [ ] **Step 4: 运行测试确认通过**

运行：`pytest tests/path/test.py::test_name -v`
预期：PASS

- [ ] **Step 5: 提交**

```bash
git add -A && git commit -m "feat: <简述>"
```

---

### Task 2: <组件名>
...（同上格式）

---

### Task N: 集成验证

- [ ] **运行全部测试**
- [ ] **手动冒烟测试**
- [ ] **最终提交**
```

---

## 任务分解策略

### 分解顺序

1. **基础层** — 数据模型、配置、工具函数
2. **核心层** — 主要业务逻辑
3. **接口层** — API/UI 对外暴露
4. **集成层** — 连接各组件
5. **验证层** — 端到端测试

### 任务间依赖

- 标注任务间依赖关系：`依赖 Task 1, 2`
- 无依赖的任务可以并行（不支持并行的 agent，标记依赖即可）
- 每个任务应该能独立验证

---

## 架构建议（非强制）

> 来源：github/spec-kit Article II — CLI Interface Mandate，适配 agent 工作模式

- **CLI 可调用**：每个工具/脚本应设计为可通过 CLI 调用（`python script.py --arg`），确保可测试、可组合、可自动化
- 不要求所有功能都暴露 CLI，但关键逻辑应独立于交互界面（Bot/API/Web），可通过命令行验证

## 约束

### 必须做
- 每个任务必须包含测试步骤
- 计划中必须指定具体的文件路径
- 每个步骤必须包含验证命令
- 保存到 `plans/YYYY-MM-DD_<功能名>/plan.md`
- 计划完成后 git commit
- 获得用户批准后才能开始执行
- **Pre-Implementation Gates 必须全部通过**才能进入任务分解。任一 Gate 不通过 → 回退上游解决

### 不要做
- ❌ 跳过测试步骤
- ❌ 定义模糊的大任务（"实现功能"）
- ❌ 不指定文件路径
- ❌ 计划中包含未设计的内容
- ❌ 一次性计划多个独立子系统
- ❌ 跳过 Pre-Implementation Gates 直接进入任务分解
- ❌ 在门禁未通过时开始写代码

---

## 与其他技能的关系

```
[brainstorming](../brainstorming/SKILL.md) → writing-plans（本技能） → 实际编码执行
              （设计文档）                      （实施计划）           （逐步实现）
```

- **前置**：brainstorming — 产出设计文档
- **本技能**：将设计转化为可执行计划
- **后续**：按计划逐步执行，每个任务走 TDD

---

## Red Flags

| 你在想… | 实际情况 |
|---------|---------|
| "这个任务可以合并" | 大任务是上下文失控的根源 |
| "测试后面再补" | 没有测试的计划不是计划 |
| "先实现再看" | 计划的意义在于先想清楚 |
| "这个步骤太细了" | 2-5 分钟粒度正好 |
| "不需要指定文件路径" | 没有路径的计划无法执行 |
| "门禁可以后面再过" | 门禁是前置条件，不是事后补充 |
| "这个抽象层以后会用到" | YAGNI——以后用到时再加 |

---

## 版本历史

| 版本 | 日期 | 变更 |
|------|------|------|
| 1.3 | 2026-09-15 | 公开切片：模板 frontmatter 泛化、去内部引用（语义不变） |
| 1.2 | 2026-07-09 | **spec 先行步骤**：Checklist 增加「Spec 先行确认」（分块 spec 与用户对齐）。来源：obra/superpowers 与 github/spec-kit |
| 1.1 | 2026-05-17 | **spec-kit 约束融合**：+Pre-Implementation Gates（Simplicity/Anti-Abstraction/Clarification）+ `[NEEDS CLARIFICATION]` 检查门 + CLI 架构建议。来源：github/spec-kit |
| 1.0 | 2026-05-16 | 初始版本（obra/superpowers writing-plans skill 移植） |

---

## 验证

> 全部通过才算完成（可检验的结果，不是"原则性符合"）。

- [ ] Pre-Implementation Gates 三项全过，`[NEEDS CLARIFICATION]` 零残留
- [ ] 每个任务有具体文件路径 + 测试步骤 + 验证命令；步骤粒度 2-5 分钟
- [ ] 用户已批准计划；批准前未开始写代码（HARD-GATE 未破）

**On failure:** 回退上游（brainstorming / 提问智慧）解决阻塞项，不降格发布半成品计划。
