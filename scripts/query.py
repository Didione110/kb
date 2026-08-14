#!/usr/bin/env python3
"""
知识库查询接口 (CLI)
用法:
  python3 query.py "问题描述"                      # 全文检索，返回 Top-N 条目
  python3 query.py --keyword "WebView2"           # 按关键词检索
  python3 query.py --product-line 用友 --type 应用操作  # 按分类筛选
  python3 query.py --id FX-20221130-059            # 按 ID 精确获取
  python3 query.py --format markdown "问题"        # 输出引用格式 markdown
  python3 query.py --json "问题"                  # 输出 JSON（默认）
  python3 query.py --list-categories              # 列出分类体系
  python3 query.py --stats                        # 统计信息

供客服机器人/AI Agent 调用：返回结构化结果 + 引用来源（doc_url）。
"""
import json, os, sys, argparse, re, glob
from collections import defaultdict

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
ENTRIES_DIR = os.path.join(ROOT, "knowledge", "entries")
INDEX_DIR = os.path.join(ROOT, "knowledge", "index")

def load_index():
    si = json.load(open(os.path.join(INDEX_DIR, "search_index.json")))
    return {item["id"]: item["file"] for item in si["items"]}

def load_entry(eid):
    fmap = load_index()
    f = fmap.get(eid)
    if not f:
        return None
    with open(os.path.join(ENTRIES_DIR, f)) as fp:
        return json.load(fp)

def tokenize(text):
    if not text:
        return set()
    tokens = set()
    for m in re.finditer(r"[a-zA-Z0-9][a-zA-Z0-9._\-]{1,40}", text.lower()):
        tokens.add(m.group(0))
    cn = re.sub(r"[^\u4e00-\u9fff]", "", text)
    for n in (2, 3, 4):
        for i in range(max(0, len(cn) - n + 1)):
            tokens.add(cn[i:i+n])
    return tokens

def score_entry(e, q_tokens):
    """基于字段权重的简单打分"""
    score = 0.0
    # 精确字段匹配（产品线/版本/问题类型）权重最高
    for field, w in [("product_line", 8.0), ("version", 6.0), ("module", 3.0)]:
        v = str(e.get(field, "")).lower()
        for qt in q_tokens:
            if qt in v:
                score += w
    # 标题/问题现象：整段包含查询词权重高
    title = (e.get("title", "") or "").lower()
    problem = (e.get("problem", "") or "").lower()
    for qt in q_tokens:
        if qt in title:
            score += 5.0
        if qt in problem:
            score += 4.0
    hay_fields = [
        (e.get("keywords") or [], 3.0), (e.get("tech_keywords") or [], 2.5),
        (e.get("tech_stack") or [], 2.0), (e.get("cause",""), 1.5),
        (e.get("solution",""), 1.2),
    ]
    for text, w in hay_fields:
        if isinstance(text, list):
            text = " ".join(text)
        t = text.lower()
        for qt in q_tokens:
            if qt in t:
                score += w
    return score

def search(query, top_k=5, filters=None):
    """全文检索 + 过滤"""
    filters = filters or {}
    q_tokens = tokenize(query)
    results = []
    for f in glob.glob(os.path.join(ENTRIES_DIR, "*.json")):
        e = json.load(open(f))
        # 过滤
        if filters.get("product_line") and e.get("product_line") != filters["product_line"]:
            continue
        if filters.get("problem_type") and e.get("problem_type") != filters["problem_type"]:
            continue
        if filters.get("version") and filters["version"] not in (e.get("version") or ""):
            continue
        s = score_entry(e, q_tokens)
        if s > 0:
            results.append((s, e))
    results.sort(key=lambda x: -x[0])
    return [e for _, e in results[:top_k]]

def search_by_keyword(kw, top_k=20):
    """按关键词索引检索"""
    kws = json.load(open(os.path.join(INDEX_DIR, "keywords.json")))["map"]
    ids = set()
    for token in re.findall(r"[\w\u4e00-\u9fff]+", kw.lower()):
        if token in kws:
            ids.update(kws[token])
    out = []
    for eid in list(ids)[:top_k]:
        e = load_entry(eid)
        if e:
            out.append(e)
    return out

def to_citation(e):
    """生成引用格式（客服机器人回答时附上）"""
    src = e.get("source", {})
    cite = {
        "id": e["id"],
        "title": e.get("title",""),
        "problem": e.get("problem",""),
        "solution": e.get("solution",""),
        "source_url": src.get("doc_url",""),
        "source_type": src.get("type",""),
        "product_line": e.get("product_line",""),
        "version": e.get("version",""),
        "module": e.get("module",""),
        "keywords": e.get("keywords") or [],
    }
    return cite

def to_markdown(e):
    src = e.get("source", {})
    lines = []
    lines.append(f"### {e.get('title','')}")
    lines.append(f"- **产品线**: {e.get('product_line','-')} | **版本**: {e.get('version','-')} | **模块**: {e.get('module','-')}")
    lines.append(f"- **问题类型**: {e.get('problem_type','-')}")
    if e.get("problem"):
        lines.append(f"\n**问题现象**:\n{e.get('problem')}")
    if e.get("cause"):
        lines.append(f"\n**问题原因**:\n{e.get('cause')}")
    if e.get("solution"):
        lines.append(f"\n**解决方案**:\n{e.get('solution')}")
    lines.append(f"\n**引用**: [{src.get('doc_url','')}]({src.get('doc_url','')})")
    return "\n".join(lines)

def main():
    ap = argparse.ArgumentParser(description="知识库查询接口")
    ap.add_argument("query", nargs="?", default=None, help="检索关键词/问题描述")
    ap.add_argument("--keyword", help="按关键词索引检索")
    ap.add_argument("--id", help="按条目 ID 获取")
    ap.add_argument("--product-line", help="按产品线过滤")
    ap.add_argument("--type", dest="ptype", help="按问题类型过滤")
    ap.add_argument("--version", help="按版本过滤")
    ap.add_argument("--top", type=int, default=5, help="返回条数")
    ap.add_argument("--format", choices=["json","markdown"], default="json", help="输出格式")
    ap.add_argument("--list-categories", action="store_true")
    ap.add_argument("--stats", action="store_true")
    args = ap.parse_args()

    if args.list_categories:
        cats = json.load(open(os.path.join(INDEX_DIR, "categories.json")))
        print(json.dumps(cats, ensure_ascii=False, indent=1))
        return
    if args.stats:
        print(json.dumps(json.load(open(os.path.join(ROOT, "knowledge", "stats.json"))),
                         ensure_ascii=False, indent=1))
        return
    if args.id:
        e = load_entry(args.id)
        if not e:
            print(json.dumps({"error": "not found", "id": args.id}, ensure_ascii=False))
            sys.exit(1)
        print(json.dumps(to_citation(e) if args.format == "json" else to_markdown(e),
                         ensure_ascii=False, indent=1))
        return
    if args.keyword:
        results = search_by_keyword(args.keyword, args.top)
    elif args.query:
        filters = {}
        if args.product_line: filters["product_line"] = args.product_line
        if args.ptype: filters["problem_type"] = args.ptype
        if args.version: filters["version"] = args.version
        results = search(args.query, args.top, filters)
    else:
        ap.print_help()
        return

    if args.format == "markdown":
        for e in results:
            print(to_markdown(e))
            print("\n---\n")
    else:
        print(json.dumps([to_citation(e) for e in results], ensure_ascii=False, indent=1))

if __name__ == "__main__":
    main()
