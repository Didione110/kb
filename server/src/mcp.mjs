#!/usr/bin/env node
/**
 * 知识库 MCP Server
 * 暴露工具:
 *   kb_search      全文检索知识库（支持过滤）
 *   kb_keyword     关键词索引检索
 *   kb_get         按 ID 获取单条知识
 *   kb_categories  获取分类体系
 *   kb_stats       获取统计信息
 *
 * 启动: node src/mcp.mjs
 * 客户端配置示例 (claude_desktop_config.json / dsh):
 *   { "mcpServers": { "kb": { "command": "node", "args": ["/path/to/kb/server/src/mcp.mjs"] } } }
 */
import { McpServer } from "@modelcontextprotocol/sdk/server/mcp.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";
import { z } from "zod";
import {
  search,
  searchByKeyword,
  loadEntry,
  getCategories,
  getStats,
  toCitation,
} from "./core.mjs";

const server = new McpServer({
  name: "keqing-kb",
  version: "1.0.0",
});

server.registerTool(
  "kb_search",
  {
    title: "搜索知识库",
    description:
      "在客服知识库中全文检索。输入客户问题描述或关键词，返回最相关的知识条目（含问题现象、原因、解决方案、来源引用）。支持按产品线/问题类型/版本过滤。",
    inputSchema: {
      query: z.string().describe("问题描述或检索词，如 'U8 登录失败'、'打印模板页码'"),
      top_k: z.number().optional().describe("返回条数，默认 5，最大 20"),
      product_line: z.string().optional().describe("按产品线过滤，如 用友/致远OA/时空/自研/蓝凌OA/其他/钉钉"),
      problem_type: z.string().optional().describe("按问题类型过滤，如 应用操作/环境问题/数据接口问题"),
      version: z.string().optional().describe("按版本过滤，如 U8"),
    },
  },
  async (args) => {
    const topK = Math.min(Number(args.top_k || 5), 20);
    const results = await search(args.query, topK, {
      product_line: args.product_line,
      problem_type: args.problem_type,
      version: args.version,
    });
    const text = results.length
      ? results.map((e, i) => {
          const src = e.source || {};
          return [
            `### [${i + 1}] ${e.title || e.id}`,
            `- 知识ID: ${e.id} | 产品线: ${e.product_line || "-"} | 版本: ${e.version || "-"} | 问题类型: ${e.problem_type || "-"}`,
            `- 问题现象: ${(e.problem || "").slice(0, 200)}`,
            `- 解决方案: ${(e.solution || "").slice(0, 300)}`,
            `- 来源: ${src.doc_url || src.type || "manual"}`,
            "",
          ].join("\n");
        }).join("\n")
      : "未找到匹配的知识条目，请尝试更换关键词。";
    return {
      content: [{ type: "text", text: text }],
      structuredContent: { query: args.query, count: results.length, results: results.map(toCitation) },
    };
  },
);

server.registerTool(
  "kb_keyword",
  {
    title: "关键词检索",
    description: "按关键词索引检索知识库（适合明确的技术词，如 WebView2、SQL Server）。",
    inputSchema: {
      keyword: z.string().describe("技术关键词，如 WebView2"),
      top_k: z.number().optional().describe("返回条数，默认 10"),
    },
  },
  async (args) => {
    const topK = Math.min(Number(args.top_k || 10), 20);
    const results = await searchByKeyword(args.keyword, topK);
    const text = results.length
      ? results.map((e, i) => `### [${i + 1}] ${e.title || e.id}\n- 知识ID: ${e.id} | 产品线: ${e.product_line || "-"}\n- 问题现象: ${(e.problem || "").slice(0, 150)}\n- 解决方案: ${(e.solution || "").slice(0, 200)}\n`).join("\n")
      : "未找到匹配的关键词条目。";
    return {
      content: [{ type: "text", text: text }],
      structuredContent: { keyword: args.keyword, count: results.length, results: results.map(toCitation) },
    };
  },
);

server.registerTool(
  "kb_get",
  {
    title: "获取知识条目",
    description: "按知识 ID（如 FX-20221130-059）获取单条知识的完整内容。",
    inputSchema: {
      id: z.string().describe("知识条目 ID，格式如 FX-20221130-059"),
    },
  },
  async (args) => {
    const e = await loadEntry(args.id);
    if (!e) {
      return { content: [{ type: "text", text: `未找到知识条目: ${args.id}` }] };
    }
    const src = e.source || {};
    const text = [
      `# ${e.title || e.id}`,
      `- 知识ID: ${e.id} | 产品线: ${e.product_line || "-"} | 版本: ${e.version || "-"} | 问题类型: ${e.problem_type || "-"}`,
      "",
      `## 问题现象\n${e.problem || "-"}`,
      "",
      `## 问题原因\n${e.cause || "-"}`,
      "",
      `## 解决方案\n${e.solution || "-"}`,
      "",
      `## 引用来源\n- 类型: ${src.type || ""}\n- 链接: ${src.doc_url || "无"}\n- 路径: ${src.doc_path || ""}`,
    ].join("\n");
    return {
      content: [{ type: "text", text }],
      structuredContent: { ...e, citation: toCitation(e) },
    };
  },
);

server.registerTool(
  "kb_categories",
  {
    title: "获取分类体系",
    description: "获取知识库分类体系（产品线 → 问题类型 → 条目数）。",
    inputSchema: {},
  },
  async () => {
    const cats = await getCategories();
    const lines = ["知识库分类体系:", ""];
    for (const [l1, subs] of Object.entries(cats.tree)) {
      lines.push(`## ${l1}`);
      for (const [l2, count] of Object.entries(subs)) {
        lines.push(`- ${l2}: ${count} 条`);
      }
      lines.push("");
    }
    return {
      content: [{ type: "text", text: lines.join("\n") }],
      structuredContent: cats,
    };
  },
);

server.registerTool(
  "kb_stats",
  {
    title: "知识库统计",
    description: "获取知识库统计信息（总条目数、分类概况）。",
    inputSchema: {},
  },
  async () => {
    const stats = await getStats();
    const text = [
      `知识库统计:`,
      `- 总条目数: ${stats.total || "未知"}`,
      `- 一级分类: ${(stats.categories || []).length} 个`,
    ].join("\n");
    return {
      content: [{ type: "text", text }],
      structuredContent: stats,
    };
  },
);

const transport = new StdioServerTransport();
await server.connect(transport);
console.error("[kb-mcp] 知识库 MCP Server 已启动 (stdio)");
