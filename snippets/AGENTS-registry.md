# 环境注册表规则片段（OpenCanCode）

> **用法**：整段粘贴进任意 agent 的指令文件（`AGENTS.md` / `CLAUDE.md` / system prompt）。建议与 [AGENTS-log.md](AGENTS-log.md)（开发日志片段）配合使用。规则详情见 [rules/registry.md](../rules/registry.md)。

## 环境注册表（Registry）

1. 工作区维护 `registry/` 目录——一资产类一表：`models.md`（模型清单与各 agent 调用入口）、`proxy.md`（出网代理与端口）、`apis.md`（外部 API 依赖）、`services.md`（本地服务端点）、`tools.md`（本地工具与脚本）。Markdown 表格。
2. **先查后问**：遇到「用哪个模型 / 走哪个代理 / 调哪个 API / 服务怎么启 / 工具在哪」类问题，先查 `registry/` 对应表；查不到才允许问用户。

3. **变更即登记**：配置变更（新增 / 更换 / 停用）完成后，主动更新对应表并刷新该行「更新日期」；停用资产不删行，状态改「停用」并注明替代者。
4. **单一权威源**：其他文档与指令只引用注册表，不复制内容——换配置只改表，全工作区生效。
5. **密钥不登记**：只记凭据位置（如 `.env` 变量名、配置文件路径），绝不写密钥本身。
