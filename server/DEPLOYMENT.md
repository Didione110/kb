# 知识库服务部署指南

本文档说明如何在本机（或公司服务器）部署知识库的 **REST API** 与 **MCP Server** 服务，以及数据自动同步机制。

## 架构总览

```
GitHub (Didione110/keqing-kb)           ← 知识数据源头（Git 仓库）
        │ git pull（每小时，systemd timer）
        ▼
DSH-workspace/kb-runtime/keqing-kb      ← 本地运行副本
        │
        ├── server/src/api.mjs          → REST API（systemd: kb-api，端口 8787）
        ├── server/src/mcp.mjs          → MCP Server（由 AI Agent 按需拉起）
        └── knowledge/                  → 知识数据（2485 条 JSON + 索引）
```

## 一、服务清单

| 服务 | systemd 单元 | 状态 | 说明 |
|------|-------------|------|------|
| REST API | `kb-api.service` | ✅ enabled + running | 监听 `0.0.0.0:8787`，开机自启，崩溃自动重启 |
| 数据同步 | `kb-sync.timer` | ✅ enabled | 每小时 git pull + 重启 API，开机 5 分钟后首次执行 |
| MCP Server | `kb-mcp.service` | ⏸ disabled | MCP 为 stdio 协议，由 AI Agent 客户端按需拉起，无需常驻 |

## 二、部署位置

| 项目 | 路径 |
|------|------|
| 运行副本 | `/home/admin/deepseek-harness/DSH-workspace/kb-runtime/keqing-kb` |
| 同步脚本 | `/home/admin/deepseek-harness/DSH-workspace/kb-runtime/sync-data.sh` |
| 同步日志 | `/home/admin/deepseek-harness/DSH-workspace/kb-runtime/sync.log` |
| systemd 单元 | `~/.config/systemd/user/kb-*.service` |

## 三、日常操作

### 查看服务状态

```bash
systemctl --user status kb-api.service      # API 状态
systemctl --user status kb-sync.timer       # 定时器状态
journalctl --user -u kb-api.service -f      # 实时日志
tail -f ~/deepseek-harness/DSH-workspace/kb-runtime/sync.log   # 同步日志
```

### 手动同步数据

```bash
bash ~/deepseek-harness/DSH-workspace/kb-runtime/sync-data.sh
```

### 重启 / 停止 API

```bash
systemctl --user restart kb-api.service
systemctl --user stop kb-api.service
```

## 四、REST API 使用

### 端点

| 方法 | 路径 | 说明 |
|------|------|------|
| GET | `http://<host>:8787/api/health` | 健康检查 |
| GET | `http://<host>:8787/api/stats` | 统计 |
| GET | `http://<host>:8787/api/categories` | 分类体系 |
| GET | `http://<host>:8787/api/search?q=xxx&top_k=5` | 全文检索 |
| GET | `http://<host>:8787/api/keywords?q=xxx` | 关键词检索 |
| GET | `http://<host>:8787/api/entries/:id` | 单条获取 |
| GET | `http://<host>:8787/api/entries?page=1&size=100` | 分页列表 |

### 示例

```bash
# 检索
curl "http://127.0.0.1:8787/api/search?q=U8%20登录失败&top_k=3"

# 带过滤
curl "http://127.0.0.1:8787/api/search?q=接口报错&product_line=用友"
```

## 五、MCP Server 接入（AI Agent）

MCP Server 通过 **stdio** 协议工作，由 AI Agent 客户端配置后按需拉起：

```json
{
  "mcpServers": {
    "kb": {
      "command": "node",
      "args": ["/home/admin/deepseek-harness/DSH-workspace/kb-runtime/keqing-kb/server/src/mcp.mjs"]
    }
  }
}
```

暴露工具：`kb_search`（全文检索）、`kb_keyword`（关键词检索）、`kb_get`（获取条目）、`kb_categories`（分类）、`kb_stats`（统计）。

### 手动测试 MCP

```bash
cd /home/admin/deepseek-harness/DSH-workspace/kb-runtime/keqing-kb/server
node src/mcp.mjs
# 通过标准输入发送 JSON-RPC 请求
```

## 六、数据更新流程

当钉钉数据源更新后（人工在钉钉端录入），需要：

```bash
# 1. 在原始仓库 kb/ 执行（有钉钉凭证的机器）
bash scripts/sync_from_dingtalk.sh      # 从钉钉拉取
python3 scripts/build_index.py           # 重建索引
cd portal && node scripts/generate.mjs   # 重新生成门户页面
git add -A && git commit -m "同步最新知识" && git push

# 2. 服务器自动生效（无需操作）
# 每小时 kb-sync.timer 自动 git pull + 重启 API
# 门户 CI 自动重新构建发布
```

## 七、迁移到公司服务器

本方案使用**用户级 systemd**（无需 root），迁移到公司 Linux 服务器步骤：

```bash
# 1. 安装依赖
sudo apt install -y nodejs npm git
corepack enable

# 2. 克隆仓库
mkdir -p /opt/kb && cd /opt/kb
git clone https://github.com/Didione110/keqing-kb.git

# 3. 安装依赖
cd keqing-kb && pnpm install

# 4. 创建 systemd 服务（内容见下方模板）
# 5. 启动
systemctl --user daemon-reload
systemctl --user enable --now kb-api.service kb-sync.timer
loginctl enable-linger $(whoami)   # 关键：登出后服务继续运行
```

### systemd 单元模板（迁移用）

将 `~/.config/systemd/user/kb-api.service` 中的 `WorkingDirectory` 改为 `/opt/kb/keqing-kb/server` 即可。

> ⚠️ 注意：`loginctl enable-linger` 必须执行，否则用户登出后 systemd 用户服务会停止。
> 若服务器有多用户或需系统级管理，可改用系统级 systemd（`/etc/systemd/system/`，需 root）。

## 八、故障排查

| 症状 | 排查 |
|------|------|
| API 无法访问 | `systemctl --user status kb-api.service` 看是否 running；`journalctl --user -u kb-api.service` 看日志 |
| 搜索返回空 | 检查 `knowledge/entries/` 是否有数据；运行 `bash sync-data.sh` 强制同步 |
| 同步失败 | 查看 `sync.log`；确认网络可达 GitHub |
| 端口冲突 | 修改 `~/.config/systemd/user/kb-api.service` 中 `KB_API_PORT`，然后 `daemon-reload && restart` |
