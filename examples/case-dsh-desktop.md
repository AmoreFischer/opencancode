# 案例研究：把 agent harness 从 CLI 迁到官方桌面版（DeepSeek Harness Desktop 0.2.0-rc.2）

> 一个真实迁移的完整复盘：如何在不丢配置的前提下，把跑在 `npx` 固定版本上的 [DeepSeek Harness](https://github.com/deepseek-ai/deepseek-harness)（`dsh`）迁移到官方桌面应用，并把「自动更新」驯服成可控流程。
> 适用读者：任何在用 dsh（或同类带本地数据目录、会自动更新的 agent 运行时）的人。
> 写法说明：路径已泛化（`~` = 用户主目录，`<DSH_HOME>` = 数据目录，默认 `~/.dsh`）；时间 2026-10，版本以当时为准。
>
> 🤖 **给 agent**：替用户执行本案例类部署前，先遵守 [`snippets/AGENTS-deploy.md`](../snippets/AGENTS-deploy.md)（环境检测含模型层 → 汇报 → 等用户指令 → 再动手）。

## TL;DR — 迁移清单

1. 风险核清：扫版本间提交关键词 + 查官方升级指南门禁 + 读版本间行为通知
2. 备份：数据目录**全量快照放到目录之外** + 关键配置文件 SHA256 基线
3. 安装：安装包哈希对照官方更新清单 → 静默安装 → 注册表确认版本
4. 首启验证：进程/端口/关键文件 hash 对照（认语义不认字节）
5. **最大坑**：桌面版首启会自建 profile 并实例化**官方干净模板**——旧配置不会自动带过来，要手工并入
6. 更新门禁：接受任何自动更新前先快照，更新后跑对照脚本
7. 回滚通道：备份 + 旧启动方式归档留档，随时可退

## 背景

dsh 有两种等价形态：npm CLI（`npx @deepseek-ai/dsh web`，端口 3080）和官方桌面应用（Electron 壳包完整 Web 应用，端口 19387）。两者**共享同一个数据目录**（`DSH_HOME`，默认 `~/.dsh`）——profiles、会话、技能、插件配置同源。

桌面版的优势：开箱即用（自带 Node/pnpm）、托盘常驻、自动更新、插件管理页。代价：**版本时点控制权让渡给自动更新**（含强制更新流）。从「固定版本的 CLI」迁过去，本质是把「升级是显式动作」改成「更新是门禁动作」——更新你拦不住，但可以每次都留下快照和验证。

## 第一步：风险核清（升级前必做）

三个公开信息源，十分钟：

1. **提交关键词扫描**：用 GitHub compare API 拉两个版本之间的全部提交信息，`grep -iE "breaking|migrat|deprecat"`。本次 0.1.7-rc.2→0.2.0-rc.2 扫了 1400+ 行，零命中。
2. **官方升级指南门禁**：这个项目在 `docs/upgrade-guide/` 下维护逐版本升级指南（有 CI 校验的「变更/迁移」章节）。某版本**没有**指南条目 = 官方自认无可感知破坏性变更。注意查的是你**跳过的那些版本**——从 rc.1 直接跳 0.2.0 的人，从没看过 rc.2 的两份行为通知。
3. **行为通知本身**：逐份评估对自己的影响。本次两份：schedule 插件可选包化（未用到，无影响）、transcript 默认展示从「标准」变「详细」（纯外观，设置可改回）。

社区反馈渠道（issue 区）如果没开放，就诚实记下「社区情报不可得」，靠后面的备份+验证兜底。

## 第二步：备份（两个要点）

```bash
# 1) 全量快照 —— 关键：放到数据目录【之外】，新内核永远碰不到它
#    Windows 上 robocopy 很快（254MB 约 1 秒）；排除历史遗留的大目录
robocopy "$HOME/.dsh" "$HOME/.dsh-backup-pre-migration-$(date +%Y%m%d-%H%M%S)" /E /NFL /NDL /NP

# 2) 关键文件 SHA256 基线 —— 升级后每个阶段 diff 这份清单
cd ~/.dsh && sha256sum \
  AGENTS.md settings.yaml.imported \
  profiles/*/cordis.patch.yml > MANIFEST-SHA256.txt
```

要点：sessions 历史也一起备（它很大但它是你的历史）；旧备份目录不用套娃备份。

## 第三步：安装（三道校验）

```bash
# 1) 下载后先验哈希 —— 官方更新清单（electron-builder feed）自带 sha512：
curl -s "https://download.deepseek.com/dsh-desk/feeds/win-x64/nightly.yml"   # 看 version + sha512
openssl dgst -sha512 -binary <installer.exe> | openssl base64 -A              # 对照，一致才装

# 2) 静默安装（NSIS 标准 /S），装完从注册表确认版本
cmd //c "installer.exe /S"
powershell "Get-ItemProperty 'HKCU:\...\Uninstall\*' | ? DisplayName -like '*DeepSeek*'"

# 3) 启动后验证：进程在、Host 端口监听（19387）、旧端口（3080）无冲突
```

## 第四步：首启验证

对照基线逐项核实：关键配置文件 hash 是否与备份基线一致（一致 = 没有发生意外的迁移动作）；技能/插件目录是否有非预期改动；Host 端口正常。**hash 一致是「没被动过」的证据，hash 变了要逐项核对语义**——GUI 的读-改-写回属正常机制，配置格式丢失才是事故。

## 第五步（最大的坑）：桌面版自建 profile，旧配置不会自动带过来

**症状**：桌面版一切正常，但模型列表只剩官方款，自建的 provider/模型目录/桥接插件全部「消失」。

**取证**：旧 profile 的配置文件 hash 与备份基线完全一致——数据没丢。真凶：桌面版首次启动会创建**自己的 profile**（`profiles/desktop/`），并按官方干净模板实例化——和 `--profile headless` 首次使用的行为是同一个机制。GUI 显示的是这个新 profile 的空目录。

**修法**：把旧 profile patch 里的用户层条目（自定义 provider 模型目录、桥接插件 insert、默认模型等）手工并入桌面 profile 的 `cordis.patch.yml`，同时保留桌面版自己写入的引导状态条目。两个操作纪律：

1. **改 patch 前先退出应用**（GUI 会读-改-写回，手改会被覆盖）；
2. 改前 `cp` 一份 `.bak`，改完重启应用验证条目齐全。

**语义变化**：自此桌面 profile 的 patch 成为事实权威源，旧 profile 的 patch 降级为回滚快照——在笔记里写明，别让两份「权威」并存。

## 第六步：更新门禁（驯服自动更新）

自动更新拦不住，但每次更新可以留下证据链。一个 40 行的 bash 门禁脚本，两个子命令：

```bash
./update-gate.sh pre   # 接受更新【前】：快照数据目录 + 写基线 hash
./update-gate.sh post  # 更新完成【后】：当前关键文件 hash 对照快照 + 端口检查 + 打印 GUI 手工清单
```

`post` 的判读口径：全部 SAME = PASS；个别 DIFF = 正常（GUI 写回），**按语义核对**（模型目录还在不在、条目格式有没有被降级）；格式性丢失 = 回滚。手工清单四项：模型目录全量 / 自定义插件或桥接可用 / 会话历史完整 / 注册过 CLI 的话跑 `--version`。

**踩坑记录（shell 脚本）**：先写了个 `.cmd` 批处理版，栽在嵌套 `for /f` 里调 PowerShell（manifest 静默写空 + 比对循环挂死）。批处理的嵌套转义/括号陷阱是重灾区（同一项目里 launcher 脚本也栽过 `chcp`/`findstr` 的坑）——**能用 bash 的场景别用 batch**，`sha256sum` 一行顶十行。

## 第七步：注册终端 CLI（可选但推荐）

桌面版应用菜单 **Manage dsh Command → Install** 会把它自带的 CLI 注册进用户 PATH。两个特性让它值得装：**版本永远跟随桌面版**（单一版本源，永不分叉），且**桌面应用关闭时也能用**（headless/脚本/canary 通道保住了）。注意：注册前开着的终端继承旧 PATH，**新开终端**才能用。

## 小坑集

- **两头鲸鱼撞脸**：Docker Desktop 的托盘图标（Moby 鲸）和 dsh 的托盘图标都是鲸鱼。分辨法：悬停看 tooltip（"Docker Desktop" vs "DeepSeek Harness"），或右键看菜单项。
- **Win11 溢出区**：新应用的托盘图标默认藏在 `^` 弹层里；设置 → 个性化 → 任务栏 → 其他系统托盘图标里按应用名开常驻。
- **关窗 ≠ 退出**：点 × 只是隐藏到托盘，任务继续跑；只有托盘右键 Quit 才是真停止（它会先检查有没有运行中的任务）。
- **双形态别同时开**：CLI web 和桌面版共享数据目录，同一 profile 双进程并发读-改-写配置的行为未知——用完一个关一个。

## 回滚通道（全程保留）

迁移后不要立刻删旧入口：旧启动脚本改名归档（`.archived-<日期>` 后缀）而非删除；全量备份留在数据目录外。回滚 = 停应用 → 恢复备份 → 解档旧脚本，三步回到迁移前。等观察期（几天）过了再考虑清理。

## 提炼：这次迁移用到的通用原则

| 原则 | 在本案例中的形态 |
|------|----------------|
| 备份前置，放到改动面之外 | 快照目录在 `DSH_HOME` 外，新内核碰不到 |
| 证据分级 | 「hash 一致」≠「配置没丢」≠「功能可用」——文件、语义、行为三级分开验证 |
| 认语义不认字节 | GUI 读-改-写回导致的 hash 变化是正常的，格式/条目丢失才回滚 |
| 更新门禁 | 拦不住自动更新，但让每次更新都留下「前快照 + 后对照」的证据链 |
| 单一版本源 | CLI 注册跟随桌面版，消灭「两个版本读写同一份配置」的分叉 |
| 回滚通道留档 | 旧入口归档不删除，观察期后再清理 |
| 计划先行 | 风险核清 → 设计两个方案（双入口/仅桌面）→ 拍板后一次跑通 |

## 相关

- 部署纪律的可粘贴形态：[`snippets/AGENTS-deploy.md`](../snippets/AGENTS-deploy.md)（检测 → 汇报 → 等指令 → 证据链 → 三态汇报）
- 上游产品：[deepseek-ai/deepseek-harness](https://github.com/deepseek-ai/deepseek-harness)（桌面版源码在 `apps/desktop`，其 README 对端口、共享 profile、CLI 注册、托盘行为有权威描述）
- 本仓 `rules/registry.md`：迁移前后的环境登记（模型从哪个 provider 走、CLI 在哪、端口谁占）正是 registry 表要记的内容
