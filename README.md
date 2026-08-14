# 科情客服智能知识库

基于钉钉 AI 表格「科情OA知识库数据梳理」+ 钉钉知识库双数据源构建的**客服智能知识库**。
面向客服机器人 / AI Agent / 客服人员：**准确定位问题 → 引用权威答案 → 精准回答**。

## 产品形态

| 组件 | 路径 | 说明 |
|------|------|------|
| **数据层** | `knowledge/` | 2485 条结构化知识条目（单一事实源） |
| **采集层** | `scripts/` | 钉钉同步 / 清洗 / 索引脚本 |
| **Web 门户** | `portal/` | VitePress 站点（浏览器访问、搜索、分类树） |
| **API 服务** | `server/` | REST API + MCP Server（供系统与 AI Agent 调用） |
| **CI/CD** | `.github/workflows/` | 自动构建门户并发布 GitHub Pages |

## 快速开始

### 1. 浏览门户

```bash
cd portal
pnpm install
pnpm run dev        # 本地预览 http://localhost:5173
pnpm run build      # 构建静态站点 → .vitepress/dist
```

### 2. 调用 API

```bash
cd server
npm install
npm run api         # REST API → http://localhost:8787

# 检索示例
curl "http://localhost:8787/api/search?q=U8%20登录失败&top_k=5"
curl "http://localhost:8787/api/stats"
```

### 3. 调用 MCP（供 AI Agent）

```bash
cd server
npm run mcp         # stdio MCP Server
```

客户端配置：
```json
{ "mcpServers": { "kb": { "command": "node", "args": ["<仓库路径>/server/src/mcp.mjs"] } } }
```

### 4. 命令行查询

```bash
cd scripts
python3 query.py "客户提问的问题描述"      # 全文检索 Top-5
python3 query.py --keyword "WebView2"    # 关键词检索
python3 query.py --id FX-20221130-059    # 精确获取
```

## 维护流程

```bash
# 1. 从钉钉同步最新数据
bash scripts/sync_from_dingtalk.sh

# 2. 重建索引
python3 scripts/build_index.py

# 3. 重新生成门户页面
cd portal && node scripts/generate.mjs

# 4. 构建并提交
cd portal && pnpm run build
cd .. && git add -A && git commit -m "同步最新知识" && git push
```

## 目录结构

```
kb/
├── raw/                    # 原始采集数据（只读）
├── knowledge/              # 清洗后知识库（entries + index + markdown）
├── scripts/                # 采集/清洗/索引/查询脚本
├── portal/                 # VitePress Web 门户
│   ├── scripts/generate.mjs  # 知识条目 → 门户页面生成器
│   └── docs/                 # 生成的站点页面
├── server/                 # API 服务（REST + MCP）
│   └── src/
│       ├── core.mjs        # 检索核心（共享）
│       ├── api.mjs         # REST API
│       └── mcp.mjs         # MCP Server
├── docs/                   # 使用文档（机器人集成等）
└── .github/workflows/      # CI 部署
```

## 设计原则

1. **单一事实源**：钉钉端数据源是权威，本地知识库是投影
2. **双向同步**：增量拉取 → 清洗/分类/索引；本地修正可回写
3. **自进化**：每次同步自动发现新增/修改/删除，增量更新
4. **机器可读 + 人可读**：JSON 供程序消费，Markdown/门户供人阅读
5. **引用可溯源**：每条知识携带来源（钉钉文档 URL / 表格记录），回答必须引用
6. **多人协作**：Git 版本管理 + PR 审查 + 自动发布

## 详细文档

- [使用文档](docs/USAGE.md)
- [机器人集成指南](docs/robot-integration.md)
- [门户使用指南](portal/docs/guide/)
- [API 文档](portal/docs/api/)
- [维护手册](portal/docs/maintain/)
