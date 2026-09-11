# 注册表示例 — demo-app 工作区（虚构）

> 展示 `registry/` 两张表填好后的样子。所有名称、端口均为虚构。规则见 [rules/registry.md](../rules/registry.md)。

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

**本示例展示的要点**

- 停用模型 `gamma` 保留行、注明替代者——决策可追溯。
- 「调用入口」只有凭据位置，没有凭据本身。
- 端口表写到「启停方式可直接执行」的程度；换代理只改这张表，全工作区生效。
