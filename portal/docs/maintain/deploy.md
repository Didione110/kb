---
title: 部署发布
---

# 部署发布

门户是**静态站点**，构建后可部署到任意静态托管（GitHub Pages / Gitee Pages / Nginx）。

## 本地构建

```bash
cd portal
pnpm install
pnpm run build          # 输出到 portal/.vitepress/dist
pnpm run preview        # 本地预览 http://localhost:4173
```

## 发布到 GitHub Pages

仓库已配置 CI（`.github/workflows/deploy.yml`），推送 `main` 分支后自动构建并发布：

```bash
git add -A && git commit -m "更新知识库" && git push origin main
```

## 手动部署到服务器

```bash
# 构建产物复制到 Nginx 目录
rsync -av portal/.vitepress/dist/ /var/www/kb/
```

## REST API / MCP 部署

API 与 MCP 是常驻服务，部署在公司服务器（Node ≥ 20）：

```bash
cd server
npm install
npm run api      # REST API，默认端口 8787
npm run mcp      # MCP Server（stdio）
```
