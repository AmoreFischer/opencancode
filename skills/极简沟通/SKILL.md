---
name: 极简沟通
description: "超压缩沟通模式，砍掉 ~75% token，只保留技术实质。Use when: 用户说'极简沟通''caveman''省token''简洁模式''cut the crap'，或上下文使用率 >70% 时自动触发。NOT for: 安全警告、不可逆操作确认、新手用户首次交互。"
version: "1.5"
triggers: ["极简沟通", "caveman", "省token", "简洁模式", "cut the crap", "压缩输出", "ponytail", "懒人模式", "yagni", "少写代码", "最简方案"]
source: "adapted — mattpocock/skills /caveman + JuliusBrussee/caveman (MIT) + DietrichGebert/ponytail（溯源见仓库 SOURCES.md）"
---

# Skill: 极简沟通 🔇

> 版本：1.5 | 安全等级：🟢 无风险（纯输出风格）
> 灵感来源：mattpocock/skills `/caveman` + DietrichGebert/ponytail
> 核心理念：Agent 默认太啰嗦。砍掉 ~75% token，只保留技术实质。

---

## 目标

<HARD-GATE>
安全相关操作（删除、force push、凭据操作、生产环境变更）**不受** caveman 模式影响，必须保持完整沟通。
</HARD-GATE>

减少 Agent 输出的 token 消耗，在上下文紧张或用户偏好简洁时激活。

### 💰 为什么值得（token 经济）

- 输出 token 直接构成 API 成本与响应延迟——压缩输出 = 省钱 + 更快
- 上下文窗口是稀缺资源——每轮啰嗦输出都会挤占后续工作的空间
- 按量计费、或高峰时段加倍计费的 API 下，压缩的收益直接放大
- 信噪比是给用户的真正交付——技术实质不变，废话归零

---

<what-to-do>

## 启动协议（每次会话自动加载）

此技能在以下条件**自动激活**（由 agent 指令文件的触发表调度，如 AGENTS.md / CLAUDE.md）：

```
□ 上下文使用率 50-70% → 模式 A-（专业档）
□ 上下文使用率 >70%  → 模式 A
□ 上下文使用率 >85%  → 模式 B
□ 即将调用 Edit/Write → 模式 C（Ponytail 阶梯）
□ 用户说了 ponytail/懒人模式/yagni → 模式 C
```

退出条件：用户说"正常模式" / "恢复完整" / 上下文使用率回落到 <50%。

## 模式 A：Caveman（默认）

**规则**：

| 动作 | 说明 |
|------|------|
| **去掉** | 冠词（一个/这个/那个）、填充词（实际上/基本上/一般来说）、客套（很高兴/当然/没问题）、犹豫（也许/可能/大概） |
| **永不省** | 否定词（不/没/非/not/never/except）、数字与单位、中文语法助词（的/了/在——只压客套，不压语言）[溯源: JuliusBrussee/caveman 中文适配] |
| **保留** | 技术术语、代码块、错误信息、文件路径、命令 |
| **格式** | `[事物] [动作] [原因]. [下一步].` |

**反伪压缩**（[溯源: JuliusBrussee/caveman v2.6]）：

- 禁自造缩写——tokenizer 里并不省
- 禁 → 箭头——箭头自身占 token，零收益
- 禁装腔破语法——破语法换不来节省
- 压缩措辞不比平话短，就用平话

**示例**：

```
❌ 完整版：
"我已经仔细检查了代码，发现了一个问题。在 src/main.py 的第 42 行，
有一个潜在的类型错误，可能会导致程序崩溃。我建议我们使用类型注解来修复这个问题。"

✅ Caveman：
"src/main.py:42 有类型错误，可能崩溃。加类型注解修复。"
```

## 模式 A-：专业档（lite，日常默认）

**触发**：日常默认表达；上下文 50-70% 区间。

**规则**：去填充词与客套，保留完整句子与语法——专业但紧凑，不破句、不电报体。

```
❌ 完整版：（同上例）
✅ A-：  "src/main.py 第 42 行有类型错误，可能导致崩溃，建议加类型注解修复。"
```

## 模式 B：Ultra-Caveman

**触发**：上下文使用率 >85% 或用户显式要求极度简洁

**格式**：仅 `[事物] [动作] [结果]`，无标点修饰。

```
❌ Caveman:  "src/main.py:42 有类型错误，可能崩溃。加类型注解修复。"
✅ Ultra:    "main.py:42 类型错误 加注解"
```

## 模式 C：Ponytail 阶梯检查（写代码前）

> 灵感来源：DietrichGebert/ponytail — "The best code is the code never written."
> 阶梯在理解问题之后执行：先完整读代码、追踪流程，再爬阶梯。

写代码前，停在第一个成立台阶：

```
1. 这需要存在吗？          → 不需要就跳过（YAGNI）
2. 代码库里已有？          → 复用，不重写
3. 标准库有？              → 用它
4. 平台/浏览器自带？        → 用它（<input type="date"> > 任何选择器库）
5. 已安装的依赖能解决？      → 用它，不加新依赖
6. 能一行写完？             → 一行
7. 以上都不行 → 最少代码
```

**规则：**
- 无未经请求的抽象（一个实现不需要接口，一个产品不需要工厂）
- 无模板/脚手架"为以后准备的"。
- 删除 > 增加。无聊 > 聪明。最少文件数。
- 最短可工作 diff 胜出——但前提是你理解了问题。改对地方的小 diff 才是懒，改错地方的小 diff 是第二个 bug。
- 简化标记：`// ponytail: 简化原因`。有已知天花板的（全局锁/O(n²)/启发式）注释写明天花板和升级路径。
- 非平凡逻辑留一个可运行检查（assert demo/self-check 或一个测试文件，无框架无 fixture）。

**Bug 修复 = 根因，非症状：** bug 报告命名一个症状。修改前 grep 要修改的函数的所有调用者。懒的修复就是根因修复：在共享函数里加一个守卫，diff 比在每个调用者加守卫小——只修报告指明的路径，兄弟调用者仍然坏着。一次修好，所有调用者流过同一处。（与 [systematic-debugging](../systematic-debugging/SKILL.md) 阶段 4 修复原则同源）

## 例外与边界

以下场景**必须恢复完整沟通**，不受 caveman 模式影响：

1. **安全警告** — 涉及数据丢失、权限问题、凭据泄露
2. **不可逆操作确认** — 删除文件、force push、数据库迁移
3. **多步序列** — 超过 3 步的操作流程，需要逐步确认
4. **错误诊断** — 排查问题时需要完整上下文
5. **HARD-GATE 检查点** — 任何技能的 HARD-GATE 触发时

**Auto-Clarity 局部恢复**（[溯源: JuliusBrussee/caveman v2.6]）：触发例外时只恢复**当前这句/这段**为完整沟通，说完补一句「继续极简」即回原档位——不必整段退出。

**受众轴**：压缩只作用于 **agent 施工管道**——agent 自消费的产物（journal、中间状态、踩坑记录条目、任务队列行内备注）可压；**人类阅读的交付物**（报告、给用户的说明、docs、commit message）保持完整丰富，不适用此技能。

## 自动触发条件

| 条件 | 模式 |
|------|------|
| 上下文使用率 50-70% | 模式 A-（专业档） |
| 上下文使用率 >70% | 模式 A |
| 上下文使用率 >85% | 模式 B |
| 用户说"极简"/"caveman"/"省token" | 模式 A |
| 用户说"恢复完整"/"正常模式" | 退出极简 |

## 与其他技能的交互

- **[提问智慧](../提问智慧/SKILL.md)**：诊断输出用 caveman 格式，但 Grilling Session 的问题保持完整（用户需要理解每个问题）
- **[整理](../整理/SKILL.md)**：状态输出（✅/⚠️/🔴）天然适合 caveman
- **[systematic-debugging](../systematic-debugging/SKILL.md)**：错误信息和诊断结论用 caveman，但反馈循环构建步骤保持完整
- **[小本本](../小本本/SKILL.md)**：写入条目用 caveman 格式（受众轴：踩坑记录归 agent 管道侧，可压——见「例外与边界」）

</what-to-do>

---

<supporting-info id="mattpocock-reference">

## mattpocock caveman 原始规则

来源：https://github.com/mattpocock/skills

Matt 的 caveman 规则（40 行）：
1. Strip articles, filler words, pleasantries, hedging
2. Keep: technical terms, code blocks, error messages
3. Pattern: `[THING] [VERB] [REASON]. [NEXT STEP].`
4. Safety exceptions: security warnings, irreversible actions, multi-step sequences

本版的差异：
- 增加了 Ultra-Caveman 模式（上下文 >85%）
- 增加了自动触发条件（基于上下文使用率）
- 增加了与其他技能的交互指引
- 回流了 JuliusBrussee/caveman v2.6 的中文适配与反伪压缩规则（MIT，见 SOURCES）

</supporting-info>

---

## 版本历史

| 版本 | 日期 | 变更 |
|------|------|------|
| 1.5 | 2026-09-15 | 模式 A- 接入两处调度表（50-70% 档正式生效）；模式 B 示例去箭头（贯彻反伪压缩）；公开切片去内部化（语义不变） |
| 1.4 | 2026-09-14 | 回流 caveman v2.6 四条：反伪压缩四则 + 否定词/数字/助词永不省 + 模式A- 专业档 + 例外与边界（Auto-Clarity 局部恢复 + 受众轴）[溯源: JuliusBrussee/caveman] |
| 1.3 | 2026-09-04 | 跨平台副本同步适配（内容同 1.2，补 frontmatter 元数据） |
| 1.2 | 2026-08 | 触发词与自动触发条件微调 |
| 1.1 | 2026-06-25 | +模式C Ponytail 阶梯检查（YAGNI 决策树+根因修复规则）融合自 DietrichGebert/ponytail |
| 1.0 | 2026-05-17 | 初始版本：Caveman + Ultra-Caveman + 安全例外 + 自动触发 |

---

## 验证

> 全部通过才算完成（可检验的结果，不是"原则性符合"）。

- [ ] 压缩后技术实质零丢失（技术术语/代码/错误信息/路径/命令/否定词/数字全保留）
- [ ] 例外场景（安全/不可逆/多步/诊断/HARD-GATE）沟通完整，未因极简牺牲确认质量
- [ ] 受众轴正确：agent 管道产物可压，人类交付物未压
- [ ] 无反伪压缩违例（自造缩写/箭头链/破语法）

**On failure:** 该段重写为完整沟通；安全相关内容漏确认 → 立即补完整确认。
