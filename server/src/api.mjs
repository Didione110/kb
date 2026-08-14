#!/usr/bin/env node
/**
 * 知识库 REST API 服务（零外部依赖，Node 原生 http）
 *
 * 端点:
 *   GET /api/health           健康检查
 *   GET /api/stats            统计信息
 *   GET /api/categories       分类体系
 *   GET /api/search?q=&top_k=&product_line=&problem_type=&version=&module=
 *   GET /api/entries/:id      按 ID 获取条目
 *   GET /api/keywords?q=      关键词索引检索
 *   GET /api/entries          列出全部条目（分页 page/size）
 *
 * 启动: node src/api.mjs [--port 8787]
 */
import http from "node:http";
import { fileURLToPath } from "node:url";
import {
  search,
  searchByKeyword,
  loadEntry,
  loadAllEntries,
  getCategories,
  getStats,
  toCitation,
} from "./core.mjs";

const PORT = Number(process.env.KB_API_PORT || 8787);
const HOST = process.env.KB_API_HOST || "0.0.0.0";

function json(res, status, body) {
  const payload = JSON.stringify(body);
  res.writeHead(status, {
    "Content-Type": "application/json; charset=utf-8",
    "Access-Control-Allow-Origin": "*",
    "Content-Length": Buffer.byteLength(payload),
  });
  res.end(payload);
}

function readQuery(url) {
  return Object.fromEntries(new URL(url, "http://localhost").searchParams.entries());
}

const routes = async (req, res) => {
  const url = new URL(req.url, "http://localhost");
  const pathname = url.pathname;

  // CORS preflight
  if (req.method === "OPTIONS") {
    res.writeHead(204, {
      "Access-Control-Allow-Origin": "*",
      "Access-Control-Allow-Methods": "GET, OPTIONS",
      "Access-Control-Allow-Headers": "*",
    });
    return res.end();
  }

  try {
    if (pathname === "/api/health") {
      return json(res, 200, { ok: true, service: "kb-api", ts: new Date().toISOString() });
    }

    if (pathname === "/api/stats") {
      return json(res, 200, { success: true, body: await getStats() });
    }

    if (pathname === "/api/categories") {
      return json(res, 200, { success: true, body: await getCategories() });
    }

    if (pathname === "/api/search") {
      const q = url.searchParams.get("q") || url.searchParams.get("query") || "";
      if (!q) return json(res, 400, { success: false, error: "缺少查询参数 q" });
      const topK = Math.min(Number(url.searchParams.get("top_k") || 5), 50);
      const filters = {
        product_line: url.searchParams.get("product_line") || undefined,
        problem_type: url.searchParams.get("problem_type") || undefined,
        version: url.searchParams.get("version") || undefined,
        module: url.searchParams.get("module") || undefined,
        category: url.searchParams.get("category") || undefined,
      };
      const results = await search(q, topK, filters);
      return json(res, 200, {
        success: true,
        query: q,
        count: results.length,
        results: results.map((e) => ({ ...e, citation: toCitation(e) })),
      });
    }

    if (pathname === "/api/keywords") {
      const q = url.searchParams.get("q") || "";
      if (!q) return json(res, 400, { success: false, error: "缺少查询参数 q" });
      const topK = Math.min(Number(url.searchParams.get("top_k") || 20), 50);
      const results = await searchByKeyword(q, topK);
      return json(res, 200, {
        success: true,
        query: q,
        count: results.length,
        results: results.map((e) => ({ ...e, citation: toCitation(e) })),
      });
    }

    if (pathname === "/api/entries") {
      const page = Math.max(Number(url.searchParams.get("page") || 1), 1);
      const size = Math.min(Math.max(Number(url.searchParams.get("size") || 100), 1), 500);
      const all = await loadAllEntries();
      const start = (page - 1) * size;
      const items = all.slice(start, start + size);
      return json(res, 200, {
        success: true,
        page,
        size,
        total: all.length,
        items: items.map((e) => ({ ...e, citation: toCitation(e) })),
      });
    }

    const entryMatch = pathname.match(/^\/api\/entries\/([^/]+)$/);
    if (entryMatch) {
      const e = await loadEntry(decodeURIComponent(entryMatch[1]));
      if (!e) return json(res, 404, { success: false, error: "条目不存在" });
      return json(res, 200, { success: true, body: { ...e, citation: toCitation(e) } });
    }

    return json(res, 404, { success: false, error: "接口不存在", path: pathname });
  } catch (err) {
    console.error("[kb-api] 错误:", err);
    return json(res, 500, { success: false, error: String(err.message || err) });
  }
};

const server = http.createServer(routes);
server.listen(PORT, HOST, () => {
  console.log(`[kb-api] 知识库 REST API 已启动: http://${HOST}:${PORT}`);
  console.log(`[kb-api] 健康检查: http://${HOST}:${PORT}/api/health`);
  console.log(`[kb-api] 搜索示例: http://${HOST}:${PORT}/api/search?q=U8%20登录失败`);
});
