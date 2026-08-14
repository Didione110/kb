/**
 * 知识库检索核心（零外部依赖）
 * 从 query.py 移植：加载条目、分词、打分、检索、过滤
 */
import { promises as fs } from "node:fs";
import path from "node:path";
import { fileURLToPath } from "node:url";

const __dirname = path.dirname(fileURLToPath(import.meta.url));
export const KB_ROOT = path.resolve(__dirname, "..", ".."); // kb/
export const ENTRIES_DIR = path.join(KB_ROOT, "knowledge", "entries");
export const INDEX_DIR = path.join(KB_ROOT, "knowledge", "index");

let _entriesCache = null; // {id -> entry}
let _indexCache = null; // {id -> filename}

async function loadIndex() {
  if (_indexCache) return _indexCache;
  const raw = await fs.readFile(path.join(INDEX_DIR, "search_index.json"), "utf8");
  const si = JSON.parse(raw);
  _indexCache = Object.fromEntries(si.items.map((i) => [i.id, i.file]));
  return _indexCache;
}

export async function loadEntry(eid) {
  const fmap = await loadIndex();
  const f = fmap[eid];
  if (!f) return null;
  try {
    return JSON.parse(await fs.readFile(path.join(ENTRIES_DIR, f), "utf8"));
  } catch {
    return null;
  }
}

export async function loadAllEntries() {
  if (_entriesCache) return Object.values(_entriesCache);
  const files = (await fs.readdir(ENTRIES_DIR)).filter((f) => f.endsWith(".json"));
  const map = {};
  for (const f of files) {
    try {
      const e = JSON.parse(await fs.readFile(path.join(ENTRIES_DIR, f), "utf8"));
      map[e.id || f] = e;
    } catch {
      // 跳过损坏条目
    }
  }
  _entriesCache = map;
  return Object.values(map);
}

/** 分词：英文/数字词 + 中文 2-4 gram */
export function tokenize(text) {
  if (!text) return new Set();
  const tokens = new Set();
  const s = String(text);
  for (const m of s.matchAll(/[a-zA-Z0-9][a-zA-Z0-9._\-]{1,40}/g)) {
    tokens.add(m[0].toLowerCase());
  }
  const cn = s.replace(/[^\u4e00-\u9fff]/g, "");
  for (let n = 2; n <= 4; n++) {
    for (let i = 0; i <= cn.length - n; i++) {
      tokens.add(cn.slice(i, i + n));
    }
  }
  return tokens;
}

/** 打分：字段权重 */
export function scoreEntry(e, qTokens) {
  let score = 0;
  for (const [field, w] of [
    ["product_line", 8.0],
    ["version", 6.0],
    ["module", 3.0],
  ]) {
    const v = String(e[field] || "").toLowerCase();
    for (const qt of qTokens) if (v.includes(qt)) score += w;
  }
  const title = (e.title || "").toLowerCase();
  const problem = (e.problem || "").toLowerCase();
  for (const qt of qTokens) {
    if (title.includes(qt)) score += 5.0;
    if (problem.includes(qt)) score += 4.0;
  }
  const hayFields = [
    [e.keywords || [], 3.0],
    [e.tech_keywords || [], 2.5],
    [e.tech_stack || [], 2.0],
    [e.cause || "", 1.5],
    [e.solution || "", 1.2],
  ];
  for (const [text, w] of hayFields) {
    const t = (Array.isArray(text) ? text.join(" ") : text).toLowerCase();
    for (const qt of qTokens) if (t.includes(qt)) score += w;
  }
  return score;
}

/** 全文检索 + 过滤 */
export async function search(query, topK = 5, filters = {}) {
  const qTokens = tokenize(query);
  const results = [];
  const entries = await loadAllEntries();
  for (const e of entries) {
    if (filters.product_line && e.product_line !== filters.product_line) continue;
    if (filters.problem_type && e.problem_type !== filters.problem_type) continue;
    if (filters.version && !(e.version || "").includes(filters.version)) continue;
    if (filters.module && !(e.module || "").includes(filters.module)) continue;
    if (filters.category && !(e.category || []).includes(filters.category)) continue;
    const s = scoreEntry(e, qTokens);
    if (s > 0) results.push({ score: s, entry: e });
  }
  results.sort((a, b) => b.score - a.score);
  return results.slice(0, topK).map((r) => r.entry);
}

/** 关键词索引检索 */
export async function searchByKeyword(kw, topK = 20) {
  const raw = await fs.readFile(path.join(INDEX_DIR, "keywords.json"), "utf8");
  const kws = JSON.parse(raw).map;
  const ids = new Set();
  for (const token of String(kw).toLowerCase().match(/[\w\u4e00-\u9fff]+/g) || []) {
    if (kws[token]) for (const id of kws[token]) ids.add(id);
  }
  const out = [];
  for (const id of [...ids].slice(0, topK)) {
    const e = await loadEntry(id);
    if (e) out.push(e);
  }
  return out;
}

/** 分类体系 */
export async function getCategories() {
  const raw = await fs.readFile(path.join(INDEX_DIR, "categories.json"), "utf8");
  return JSON.parse(raw);
}

/** 统计 */
export async function getStats() {
  try {
    const raw = await fs.readFile(path.join(KB_ROOT, "knowledge", "stats.json"), "utf8");
    return JSON.parse(raw);
  } catch {
    const entries = await loadAllEntries();
    return { total: entries.length, categories: Object.keys((await getCategories()).tree) };
  }
}

/** 引用格式（机器人回答时附带） */
export function toCitation(e) {
  const src = e.source || {};
  return {
    id: e.id,
    title: e.title || "",
    problem: e.problem || "",
    solution: e.solution || "",
    source_url: src.doc_url || "",
    source_type: src.type || "",
    product_line: e.product_line || "",
    version: e.version || "",
    module: e.module || "",
    keywords: e.keywords || [],
  };
}
