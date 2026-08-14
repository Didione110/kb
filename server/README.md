# 知识库 API 服务

提供 **REST API** 与 **MCP Server** 两种调用方式，供外部系统与 AI Agent 集成。

## 快速开始

```bash
# 安装依赖
pnpm install

# 启动 REST API（默认端口 8787）
pnpm run api

# 启动 MCP Server（stdio）
pnpm run mcp
```

## REST API

| 方法 | 路径 | 说明 |
|------|------|------|
| GET | `/api/health` | 健康检查 |
| GET | `/api/stats` | 统计信息 |
| GET | `/api/categories` | 分类体系 |
| GET | `/api/search?q=&top_k=&product_line=&problem_type=&version=` | 全文检索 |
| GET | `/api/keywords?q=` | 关键词检索 |
| GET | `/api/entries/:id` | 按 ID 获取条目 |
| GET | `/api/entries?page=&size=` | 分页列出 |

配置：环境变量 `KB_API_PORT`（默认 8787）、`KB_API_HOST`（默认 0.0.0.0）。

## MCP Server

暴露工具：`kb_search`、`kb_keyword`、`kb_get`、`kb_categories`、`kb_stats`。

客户端配置：
```json
{
  "mcpServers": {
    "kb": {
      "command": "node",
      "args": ["/绝对路径/kb/server/src/mcp.mjs"]
    }
  }
}
```

## 模块结构

- `src/core.mjs` — 检索核心（零依赖，从 `scripts/query.py` 移植）
- `src/api.mjs` — REST API 服务
- `src/mcp.mjs` — MCP Server（依赖 `@modelcontextprotocol/sdk`）
