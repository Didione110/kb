#!/usr/bin/env python3
# 构建检索索引：分类体系 + 关键词映射 + 按分类组织 + 统计
# 输入: knowledge/entries/*.json
# 输出: knowledge/index/{categories,keywords,by_category,search_index}.json
import json, os, glob, re, hashlib
from collections import defaultdict, Counter

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
ENTRIES_DIR = os.path.join(ROOT, "knowledge", "entries")
INDEX_DIR = os.path.join(ROOT, "knowledge", "index")
os.makedirs(INDEX_DIR, exist_ok=True)

entries = []
for f in sorted(glob.glob(os.path.join(ENTRIES_DIR, "*.json"))):
    entries.append(json.load(open(f)))

# ---------- 1. 分类体系 ----------
cat_tree = defaultdict(lambda: defaultdict(int))  # 一级 -> 二级 -> 计数
for e in entries:
    cats = e.get("category", [])
    l1 = cats[0] if len(cats) > 0 else "未分类"
    l2 = cats[1] if len(cats) > 1 else ""
    cat_tree[l1][l2] += 1

categories = {
    "version": "1.0",
    "type": "taxonomy",
    "description": "知识条目分类体系：一级=产品线/来源，二级=问题类型",
    "tree": {k: dict(v) for k, v in sorted(cat_tree.items())},
}
with open(os.path.join(INDEX_DIR, "categories.json"), "w") as f:
    json.dump(categories, f, ensure_ascii=False, indent=1)

# ---------- 2. 关键词映射 ----------
# 关键词来源: keywords + tech_keywords + tech_stack + title + problem 分词
kw_map = defaultdict(list)  # 关键词 -> [entry_id...]

def tokenize(text):
    if not text:
        return []
    # 中文分词简化：按 2-4 字滑窗 + 整词
    tokens = set()
    s = re.sub(r"[^\w\u4e00-\u9fff]+", "", text)
    # 英文/数字词（不含中文）
    for m in re.finditer(r"[a-zA-Z0-9][a-zA-Z0-9._\-]{1,40}", text):
        tokens.add(m.group(0).lower())
    # 中文 2-gram 到 4-gram
    cn = re.sub(r"[^\u4e00-\u9fff]", "", s)
    for n in (2, 3, 4):
        for i in range(0, max(0, len(cn) - n + 1)):
            tokens.add(cn[i:i+n])
    return list(tokens)

for e in entries:
    eid = e["id"]
    # 显式关键词
    for k in (e.get("keywords") or []) + (e.get("tech_keywords") or []) + (e.get("tech_stack") or []):
        if k:
            kw_map[k].append(eid)
    # 从标题/问题现象抽取
    for t in tokenize((e.get("title") or "") + " " + (e.get("problem") or "")):
        kw_map[t].append(eid)

# 去重并限制词条数量（太长的、频率太低的丢弃）
kw_clean = {}
for k, v in kw_map.items():
    if not k or len(k) > 30:
        continue
    kk = k.strip().lower()
    if len(v) < 2 and len(kk) <= 1:
        continue
    kw_clean[kk] = list(dict.fromkeys(v))

# 词频排序
kw_sorted = dict(sorted(kw_clean.items(), key=lambda x: -len(x[1])))
with open(os.path.join(INDEX_DIR, "keywords.json"), "w") as f:
    json.dump({"count": len(kw_sorted), "map": kw_sorted}, f, ensure_ascii=False, indent=1)

# ---------- 3. 按分类组织 ----------
by_cat = defaultdict(list)
for e in entries:
    key = "/".join(e.get("category", [])[:2]) or "未分类"
    by_cat[key].append({"id": e["id"], "title": e.get("title","")})

with open(os.path.join(INDEX_DIR, "by_category.json"), "w") as f:
    json.dump({k: v for k, v in sorted(by_cat.items())}, f, ensure_ascii=False, indent=1)

# ---------- 4. 全文检索索引 ----------
# 先建 id -> file 映射，避免 O(n²) glob
id_to_file = {}
for f in sorted(glob.glob(os.path.join(ENTRIES_DIR, "*.json"))):
    try:
        e = json.load(open(f))
        id_to_file[e["id"]] = os.path.basename(f)
    except Exception:
        continue

search_index = []
for e in entries:
    hay = " ".join([
        e.get("title",""), e.get("problem",""), e.get("cause",""),
        e.get("solution",""), " ".join(e.get("keywords") or []),
        " ".join(e.get("tech_keywords") or []), " ".join(e.get("tech_stack") or []),
        e.get("product_line",""), e.get("version",""), e.get("module",""),
        e.get("problem_type",""),
    ])
    search_index.append({
        "id": e["id"],
        "file": id_to_file.get(e["id"], ""),
        "text": hay,
    })
with open(os.path.join(INDEX_DIR, "search_index.json"), "w") as f:
    json.dump({"count": len(search_index), "items": search_index}, f, ensure_ascii=False, indent=1)

# ---------- 5. 统计 ----------
stats = {
    "total_entries": len(entries),
    "categories_l1": len(cat_tree),
    "categories_l2": sum(len(v) for v in cat_tree.values()),
    "keywords": len(kw_sorted),
    "by_product_line": dict(Counter(e.get("product_line") or "未分类" for e in entries).most_common()),
    "by_problem_type": dict(Counter(e.get("problem_type") or "未分类" for e in entries).most_common()),
}
with open(os.path.join(ROOT, "knowledge", "stats.json"), "w") as f:
    json.dump(stats, f, ensure_ascii=False, indent=1)

print("=== 索引构建完成 ===")
print(json.dumps(stats, ensure_ascii=False, indent=1))
