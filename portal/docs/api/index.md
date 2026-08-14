---
title: API 文档
---

# API 文档

知识库提供 **REST API** 与 **MCP Server** 两种调用方式，供外部系统与 AI Agent 集成。

## REST API

服务地址：`http://<host>:8787`（可通过环境变量 `KB_API_PORT` 修改端口）

### 认证

API 面向公司内网，默认无需认证。如需接入公网，建议在反向代理层添加访问控制（IP 白名单 / Token）。

### 端点一览

| 方法 | 路径 | 说明 |
|------|------|------|
| GET | `/api/health` | 健康检查 |
| GET | `/api/stats` | 统计信息（总数/分类/关键词量） |
| GET | `/api/categories` | 分类体系（产品线 → 问题类型 → 条目数） |
| GET | `/api/search` | 全文检索（推荐） |
| GET | `/api/keywords` | 关键词索引检索 |
| GET | `/api/entries/:id` | 按知识 ID 获取单条 |
| GET | `/api/entries` | 分页列出全部条目 |

### 搜索示例

```bash
# 全文检索
curl "http://localhost:8787/api/search?q=U8%20登录失败&top_k=5"

# 带过滤
curl "http://localhost:8787/api/search?q=接口报错&product_line=用友&problem_type=数据接口问题"

# 按 ID 获取
curl "http://localhost:8787/api/entries/FX-20221130-059"

# 统计
curl "http://localhost:8787/api/stats"
```

### 返回格式

```json
{
  "success": true,
  "query": "U8 登录失败",
  "count": 2,
  "results": [
    {
      "id": "FX-20240301-003",
      "title": "报表无法登录，提示单点登录失败；",
      "problem": "...",
      "cause": "...",
      "solution": "...",
      "citation": {
        "id": "FX-20240301-003",
        "title": "报表无法登录，提示单点登录失败；",
        "source_url": "https://alidocs.dingtalk.com/i/nodes/xxx",
        "source_type": "doc"
      }
    }
  ]
}
```

> 每条结果都附带 `citation` 字段（来源 URL + 知识 ID），供客服系统引用溯源。

## MCP Server

供 AI Agent（DSH / Claude Desktop / 自研 Agent）直接调用。

### 启动

```bash
cd kb/server
npm run mcp
```

### 客户端配置

```json
{
  "mcpServers": {
    "kb": {
      "command": "node",
      "args": ["/path/to/kb/server/src/mcp.mjs"]
    }
  }
}
```

### 工具清单

| 工具 | 说明 |
|------|------|
| `kb_search` | 全文检索（支持产品线/问题类型/版本过滤） |
| `kb_keyword` | 关键词索引检索 |
| `kb_get` | 按知识 ID 获取完整条目 |
| `kb_categories` | 获取分类体系 |
| `kb_stats` | 获取统计信息 |

### MCP 工具调用示例

```
kb_search(query="U8 登录失败", top_k=3)
→ 返回最相关的知识条目，含问题现象、原因、解决方案、来源引用
```

## 命令行（备选）

```bash
cd kb/scripts
python3 query.py "U8 登录失败" --top 3 --format json
```
