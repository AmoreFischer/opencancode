# 注册表示例 — demo-app 工作区（虚构）

> 展示 `registry/` 五张表填好后的样子。所有名称、端口均为虚构。规则见 [rules/registry.md](../rules/registry.md)。

## registry/models.md

| 别名 | 正式名 | 提供商 | 接入类型 | 思考档 | 各 agent 调用入口 | 用途定位 | 状态 | 更新日期 |
|---|---|---|---|---|---|---|---|---|
| alpha | model-alpha-2 | AlphaCloud | openai 兼容 | 支持 high | CLI agent：`ALPHA_API_KEY`（`.env`）+ `configs/alpha.yaml`；IDE agent：插件设置选 alpha | 编程主力 | 活跃 | 2026-09-10 |
| beta | model-beta-mini | BetaAI | anthropic 兼容 | 不支持 | CLI agent：`BETA_API_KEY`（`.env`） | 日常快问 | 活跃 | 2026-09-08 |
| gamma | model-gamma | GammaLabs | openai 兼容 | 支持 medium | —（入口已下线） | 旧编程主力 | 停用（由 alpha 替代） | 2026-09-05 |

## registry/proxy.md

| 端口 | 协议 | 用途 | 所属应用 | 启停方式 | 状态 | 更新日期 |
|---|---|---|---|---|---|---|
| 9001 | http | 外网 API 访问 | ProxyApp | 系统托盘开关 | 活跃 | 2026-09-10 |
| 9002 | socks5 | 浏览器抓取 | ProxyApp | 随主应用启停 | 活跃 | 2026-09-10 |

## registry/apis.md

| 别名 | 提供商 | 端点 | 凭据位置 | 用途 | 计费 | 状态 | 更新日期 |
|---|---|---|---|---|---|---|---|
| ocr | AlphaCloud | `https://api.alphademo.example/v1/ocr` | `ALPHA_OCR_KEY`（`.env`） | 截图文字提取 | 按量 | 活跃 | 2026-09-10 |
| imggen | GrsaiDemo | `https://api.grsaidemo.example/v1` | `GRSAI_DEMO_KEY`（`.env`） | 插画生成 | 积分制 | 活跃 | 2026-09-08 |
| weather | OpenSkyDemo | `https://api.openskydemo.example/v2` | —（无需 key） | 日报天气数据 | 免费 | 活跃 | 2026-09-01 |
| mailer | BetaMail | `https://api.betamail.example` | `BETAMAIL_TOKEN`（`configs/betamail.yaml`） | 状态页通知 | 订阅 | 停用（由 push-demo 接管） | 2026-09-05 |

## registry/services.md

| 名称 | 端点 | 用途 | 启停方式 | 健康检查 | 所属路径 | 状态 | 更新日期 |
|---|---|---|---|---|---|---|---|
| search-bridge | 127.0.0.1:18123 | agent 聚合搜索 | `docker start search-bridge`（~8s 就绪） | `GET /healthz` | `infra/search-bridge/` | 活跃（按需启动） | 2026-09-10 |
| mcp-hub | 127.0.0.1:19456 | MCP server 桥 | `pnpm mcp:start` | 端口探测 | `tools/mcp-hub/` | 活跃 | 2026-09-09 |
| status-ui | 127.0.0.1:15901 | 内部状态页 | `docker compose up -d status-ui` | `GET /` | `infra/status-ui/` | 停用（并入 admin-ui） | 2026-09-05 |

## registry/tools.md

| 角色 | 工具/脚本 | 路径或命令 | 适用场景 | 状态 | 更新日期 |
|---|---|---|---|---|---|
| fmt | ruff | `ruff format <路径>` | Python 格式化 | 活跃 | 2026-09-10 |
| snap | shot.py | `scripts/shot.py --selector <css>` | 确定性页面截图 | 活跃 | 2026-09-06 |
| xlsx | tabular.py | `scripts/tabular.py <md> -o <xlsx>` | 给非技术读者的报告表格 | 活跃 | 2026-09-02 |
| legacy-build | build.sh | `scripts/build.sh` | 旧版打包 | 停用（由 `pnpm build` 替代） | 2026-09-01 |

**本示例展示的要点**

- 停用模型 `gamma` 保留行、注明替代者——决策可追溯。
- 「调用入口」只有凭据位置，没有凭据本身。
- 端口表写到「启停方式可直接执行」的程度；换代理只改这张表，全工作区生效。
- API 表带计费形态（免费/按量/订阅/积分）——只看表即可做成本审计；`weather` 无需 key 也登记（一行说清「为什么不用配凭据」）。
- `search-bridge` 标注「按需启动 + 就绪耗时」——agent 先 `docker start` 再探测，不误判故障。
- tools 表以**角色**为句柄（`fmt`/`snap`/`xlsx`），文档与技能引用角色而非工具名——换工具只改一行。
