#!/usr/bin/env node
/**
 * 知识库门户生成脚本
 * 输入: ../knowledge/entries/*.json + ../knowledge/index/categories.json
 * 输出: ../docs/kb/ 下页面 + ../.vitepress/sidebar.gen.json 侧边栏
 *
 * 每次同步/更新知识后运行: node scripts/generate.mjs
 */
import { promises as fs } from "node:fs";
import path from "node:path";
import { fileURLToPath } from "node:url";

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const KB_ROOT = path.resolve(__dirname, "..", ".."); // kb/
const ENTRIES_DIR = path.join(KB_ROOT, "knowledge", "entries");
const INDEX_DIR = path.join(KB_ROOT, "knowledge", "index");
const DOCS_KB_DIR = path.resolve(__dirname, "..", "docs", "kb");

/** 将分类路径安全转换为文件系统路径 */
function safeSegment(s) {
  return String(s || "").replace(/[\\/:*?"<>|\s]+/g, "_").replace(/^_+|_+$/g, "") || "_";
}

/** Markdown 表格转义 */
function esc(s) {
  return String(s ?? "").replace(/\|/g, "\\|").replace(/\n/g, "<br>");
}

/** 正文转义：防止 `<`/`>` 被 Vue/Markdown 解析为 HTML 标签，防止 `{`/`}` 触发 markdown-it-attrs */
function body(s) {
  return String(s ?? "")
    .replace(/</g, "&lt;")
    .replace(/>/g, "&gt;")
    .replace(/\{/g, "&#123;")
    .replace(/\}/g, "&#125;");
}

/** 渲染单个知识条目为 VitePress 页面 */
function renderEntry(e) {
  const src = e.source || {};
  const meta = e.meta || {};
  const cats = e.category || [];
  const l1 = safeSegment(cats[0] || "未分类");
  const l2 = safeSegment(cats[1] || "默认");

  const frontmatter = {
    title: e.title || e.id,
    kbId: e.id,
    productLine: e.product_line || "",
    productSeries: e.product_series || "",
    version: e.version || "",
    module: e.module || "",
    problemType: e.problem_type || "",
    solutionTypes: e.solution_types || [],
    techStack: e.tech_stack || [],
    techKeywords: e.tech_keywords || [],
    keywords: e.keywords || [],
    category: cats,
    submitter: meta.submitter || "",
    department: meta.department || "",
    date: meta.date || "",
    sourceType: src.type || "",
    sourceUrl: src.doc_url || "",
    sourcePath: src.doc_path || e.doc_path || "",
    status: e.status || "active",
    updatedAt: e.updated_at || "",
    outDir: `${l1}/${l2}`,
  };

  const lines = [];
  lines.push("---");
  // frontmatter 中的文本同样转义尖括号，避免 Vue 编译期解析 HTML
  const fm = { ...frontmatter, title: body(frontmatter.title), sourcePath: body(frontmatter.sourcePath) };
  lines.push(JSON.stringify(fm, null, 2));
  lines.push("---");
  lines.push("");
  lines.push(`# ${body(e.title || e.id)}`);
  lines.push("");
  lines.push("> 知识条目 · 可被客服机器人引用");
  lines.push("");

  // 元信息表
  lines.push("## 元信息");
  lines.push("");
  lines.push("| 字段 | 值 |");
  lines.push("|------|----|");
  lines.push(`| 知识ID | \`${esc(e.id)}\` |`);
  lines.push(`| 产品线 | ${esc(e.product_line || "-")} |`);
  lines.push(`| 产品系列 | ${esc(e.product_series || "-")} |`);
  lines.push(`| 版本 | ${esc(e.version || "-")} |`);
  lines.push(`| 模块 | ${esc(e.module || "-")} |`);
  lines.push(`| 问题类型 | ${esc(e.problem_type || "-")} |`);
  lines.push(`| 解决方案类型 | ${esc((e.solution_types || []).join(", "))} |`);
  lines.push(`| 技术栈 | ${esc((e.tech_stack || []).join(", "))} |`);
  lines.push(`| 技术关键词 | ${esc((e.tech_keywords || []).join(", "))} |`);
  lines.push(`| 问题关键字 | ${esc((e.keywords || []).join(", "))} |`);
  lines.push(`| 分类路径 | ${esc(cats.join(" / "))} |`);
  lines.push(`| 提交人 | ${esc(meta.submitter || "-")} |`);
  lines.push(`| 提交部门 | ${esc(meta.department || "-")} |`);
  lines.push(`| 提交日期 | ${esc(meta.date || "-")} |`);
  lines.push(`| 状态 | ${esc(e.status || "active")} |`);
  lines.push("");

  // 问题/原因/解决方案
  if (e.problem) {
    lines.push("## 问题现象");
    lines.push("");
    lines.push(body(e.problem));
    lines.push("");
  }
  if (e.cause) {
    lines.push("## 问题原因");
    lines.push("");
    lines.push(body(e.cause));
    lines.push("");
  }
  if (e.solution) {
    lines.push("## 解决方案");
    lines.push("");
    lines.push(body(e.solution));
    lines.push("");
  }

  // 引用来源
  lines.push("## 引用来源");
  lines.push("");
  lines.push(`- 来源类型: \`${src.type || ""}\``);
  if (src.doc_url) lines.push(`- 来源链接: ${src.doc_url}`);
  if (src.doc_path) lines.push(`- 知识库路径: \`${src.doc_path}\``);
  if (src.record_id) lines.push(`- 表格记录ID: \`${src.record_id}\``);
  lines.push("");

  return {
    relPath: `${l1}/${l2}/${e.id}.md`,
    content: lines.join("\n"),
    l1,
    l2,
  };
}

/** 生成分类索引页 */
function renderCategoryIndex(l1, l2Counts, entries) {
  const lines = [];
  lines.push("---");
  lines.push(`title: ${l1}`);
  lines.push("---");
  lines.push("");
  lines.push(`# ${l1}`);
  lines.push("");
  lines.push(`> 一级分类 · 共 ${entries.length} 条知识`);
  lines.push("");
  lines.push("## 二级分类");
  lines.push("");
  for (const [l2, count] of Object.entries(l2Counts).sort((a, b) => b[1] - a[1])) {
    lines.push(`- **[${l2 || "默认"}](./${safeSegment(l2 || "默认")}/)** — ${count} 条`);
  }
  lines.push("");
  lines.push("## 全部条目");
  lines.push("");
  for (const e of entries.slice().sort((a, b) => (a.title || "").localeCompare(b.title || "", "zh"))) {
    const cats = e.category || [];
    const l2 = safeSegment(cats[1] || "默认");
    lines.push(`- [${e.title || e.id}](./${l2}/${e.id}.md)`);
  }
  lines.push("");
  return `${l1}/index.md`;
}

/** 收集所有条目，按分类组织 */
async function collect() {
  const files = (await fs.readdir(ENTRIES_DIR)).filter((f) => f.endsWith(".json"));
  const entries = [];
  for (const f of files) {
    try {
      entries.push(JSON.parse(await fs.readFile(path.join(ENTRIES_DIR, f), "utf8")));
    } catch {
      // 跳过损坏的条目文件
    }
  }
  return entries;
}

async function main() {
  console.log("[generate] 读取知识条目...");
  const entries = await collect();
  console.log(`[generate] 共 ${entries.length} 条知识`);

  // 清理旧输出
  await fs.rm(DOCS_KB_DIR, { recursive: true, force: true });
  await fs.mkdir(DOCS_KB_DIR, { recursive: true });

  // 按一级/二级分类组织
  const byCat = new Map(); // `${l1}/${l2}` -> {l1, l2, entries: []}
  const l1Counts = new Map();
  const l2CountsByL1 = new Map();

  for (const e of entries) {
    const cats = e.category || [];
    const l1Raw = cats[0] || "未分类";
    const l2Raw = cats[1] || "默认";
    const l1 = safeSegment(l1Raw);
    const l2 = safeSegment(l2Raw);
    const key = `${l1}/${l2}`;
    if (!byCat.has(key)) byCat.set(key, { l1, l1Raw, l2, l2Raw, entries: [] });
    byCat.get(key).entries.push(e);
    l1Counts.set(l1Raw, (l1Counts.get(l1Raw) || 0) + 1);
    if (!l2CountsByL1.has(l1Raw)) l2CountsByL1.set(l1Raw, new Map());
    const m = l2CountsByL1.get(l1Raw);
    m.set(l2Raw, (m.get(l2Raw) || 0) + 1);
  }

  // 渲染每个条目
  let written = 0;
  for (const [key, group] of byCat) {
    const dir = path.join(DOCS_KB_DIR, group.l1, group.l2);
    await fs.mkdir(dir, { recursive: true });
    for (const e of group.entries) {
      const { relPath, content } = renderEntry(e);
      const out = path.join(DOCS_KB_DIR, relPath);
      await fs.writeFile(out, content, "utf8");
      written++;
    }
  }
  console.log(`[generate] 已生成 ${written} 个条目页面`);

  // 渲染分类索引页
  const idxPages = [];
  for (const [l1Raw, m] of l2CountsByL1) {
    const l1 = safeSegment(l1Raw);
    const groupEntries = [];
    for (const [key, g] of byCat) {
      if (g.l1 === l1) groupEntries.push(...g.entries);
    }
    const rel = renderCategoryIndex(l1, Object.fromEntries(m), groupEntries);
    await fs.writeFile(path.join(DOCS_KB_DIR, rel), groupEntries.length ? "" : "", "utf8");
    idxPages.push(rel);
  }

  // 重新生成分类索引页（需要内容）
  for (const [l1Raw, m] of l2CountsByL1) {
    const l1 = safeSegment(l1Raw);
    const groupEntries = [];
    for (const [key, g] of byCat) {
      if (g.l1 === l1) groupEntries.push(...g.entries);
    }
    const content = renderCategoryIndex(l1, Object.fromEntries(m), groupEntries);
    await fs.writeFile(path.join(DOCS_KB_DIR, `${l1}/index.md`), content, "utf8");
  }
  console.log(`[generate] 已生成 ${l2CountsByL1.size} 个分类索引页`);

  // 生成侧边栏配置
  const sidebar = [];
  const l1Order = [...l2CountsByL1.keys()].sort();
  for (const l1Raw of l1Order) {
    const l1 = safeSegment(l1Raw);
    const children = [];
    const m = l2CountsByL1.get(l1Raw);
    for (const [l2Raw, count] of [...m.entries()].sort((a, b) => b[1] - a[1])) {
      const l2 = safeSegment(l2Raw);
      children.push({
        text: `${l2Raw} (${count})`,
        link: `/kb/${l1}/${l2}/`,
        items: byCat.get(`${l1}/${l2}`)?.entries
          .slice()
          .sort((a, b) => (a.title || "").localeCompare(b.title || "", "zh"))
          .map((e) => ({ text: body(e.title || e.id), link: `/kb/${l1}/${l2}/${e.id}` })) || [],
      });
    }
    sidebar.push({
      text: `${l1Raw} (${l1Counts.get(l1Raw)})`,
      collapsed: true,
      items: children,
    });
  }

  const sidebarOut = path.resolve(__dirname, "..", ".vitepress", "sidebar.gen.json");
  await fs.writeFile(sidebarOut, JSON.stringify(sidebar, null, 2), "utf8");
  console.log(`[generate] 侧边栏已写入 ${sidebarOut}`);

  // 统计信息
  console.log(`[generate] 完成: ${written} 页, ${l2CountsByL1.size} 个一级分类`);
}

main().catch((err) => {
  console.error("[generate] 失败:", err);
  process.exit(1);
});
