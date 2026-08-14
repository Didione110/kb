#!/usr/bin/env python3
# 清洗与融合：AI 表格记录 + 知识库文档 → 统一知识条目
# 1) 表格记录为主数据（去重：0mSTARa 与 PRYSzWY 内容相同，只保留一份）
# 2) 有对应文档的记录，用文档详细 markdown 补充问题现象/原因/解决方案
# 3) 无单据编号的文档（纯技巧类）单独纳入
# 输出: knowledge/entries/*.json + knowledge/index/*.json
import json, os, re, glob, hashlib

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
RAW_AITABLE = os.path.join(ROOT, "raw", "aitable")
RAW_DOCS = os.path.join(ROOT, "raw", "docs", "content")
OUT_ENTRIES = os.path.join(ROOT, "knowledge", "entries")
OUT_INDEX = os.path.join(ROOT, "knowledge", "index")
os.makedirs(OUT_ENTRIES, exist_ok=True)
os.makedirs(OUT_INDEX, exist_ok=True)

# ---- 字段映射（fieldId -> 字段名） ----
FIELD_MAP = {
    "mqbn9ed13bv3vkvqlxxvb": "单据编号",
    "m2b70sy36k1ecxpt2jrt4": "提交人",
    "olnc4a7e9su3jk63clybo": "提交部门",
    "g92ajoa7xgc617ps6vpgp": "提交日期",
    "ll6xs2lyhyrmkzx5zfmm7": "对应产品线",
    "2403n5ic7pya9krzoi3jb": "产品线系列",
    "mf4h6pwyinr9l2a4cpjt7": "对应版本",
    "h7tlyp6kbvbh488tusblk": "对应模块",
    "u3w7fc0qr1i7x2u30t81g": "问题类型",
    "o687i7pynjdlc7dp6o3ok": "问题现象",
    "8fbjpkho6bcnrislxuqum": "问题原因",
    "xilcj2rfnje836pe4wlrb": "解决方案",
    "ngAM08z": "解决方案类型",
    "qBnlp3p": "技术栈",
    "gk8pxBX": "技术关键词",
    "G9f8YXm": "问题关键字",
}

def cell_value(v):
    """把单元格值归一化为可读文本"""
    if v is None:
        return ""
    if isinstance(v, dict):
        return v.get("name", "")
    if isinstance(v, list):
        return [x.get("name", "") if isinstance(x, dict) else str(x) for x in v]
    return str(v)

def cell_text(v):
    """单元格值 → 单行文本"""
    val = cell_value(v)
    if isinstance(val, list):
        return ", ".join(x for x in val if x)
    return val

def parse_date(v):
    s = cell_text(v)
    if not s:
        return ""
    return s[:10]

def normalize_ws(s):
    """清洗：去首尾空白、折叠空白"""
    if not s:
        return ""
    return re.sub(r"[ \t]+", " ", s).strip()

def norm_list(v):
    """统一为 list[str]，过滤空值"""
    if v is None:
        return []
    if isinstance(v, str):
        return [x.strip() for x in v.split(",") if x.strip()]
    if isinstance(v, list):
        out = []
        for x in v:
            if isinstance(x, dict):
                x = x.get("name","")
            if isinstance(x, str) and x.strip():
                out.append(x.strip())
            elif not isinstance(x, str):
                out.append(str(x))
        return out
    return []

def clean_solution(s):
    """清理解决方案中的 markdown 残留"""
    if not s:
        return ""
    s = s.replace("---", "").strip()
    return re.sub(r"\n{3,}", "\n\n", s).strip()

# ---- 1. 读取 AI 表格记录（0mSTARa 为主，若为空则用 PRYSzWY） ----
def load_records(path):
    if not os.path.exists(path):
        return []
    return json.load(open(path))

records = load_records(os.path.join(RAW_AITABLE, "0mSTARa_技术问题知识分享_records.json"))
if not records:
    records = load_records(os.path.join(RAW_AITABLE, "PRYSzWY_知识分享副本_records.json"))

print("AI 表格记录数:", len(records))

# ---- 2. 读取文档 markdown，按单据编号索引 ----
doc_by_no = {}   # 单据编号 -> {markdown, path, docUrl, title}
doc_no_number = {}  # 文档路径 -> 单据编号
all_docs = []
for f in glob.glob(os.path.join(RAW_DOCS, "*.md")):
    c = open(f).read()
    meta_m = re.search(r"<!-- META: (\{.*?\}) -->", c, re.S)
    meta = json.loads(meta_m.group(1)) if meta_m else {}
    body = c[meta_m.end():].strip() if meta_m else c
    all_docs.append({"meta": meta, "body": body})
    n = re.search(r"\*\*单据编号\*\*: (FX-[\w-]+)", c)
    if n:
        no = n.group(1)
        doc_by_no[no] = {"meta": meta, "body": body}
        doc_no_number[meta.get("path","")] = no
print("文档总数:", len(all_docs), "| 含单据编号:", len(doc_by_no))

# ---- 3. 解析文档正文中的结构化附加信息 ----
def parse_doc_body(body):
    """从文档 markdown 提取 问题现象/原因/解决方案/附加信息字段"""
    fields = {"问题现象":"", "问题原因":"", "解决方案":""}
    extras = {}
    # 提取 ## 小节
    parts = re.split(r"\n## ", body)
    for p in parts[1:]:
        title = p.split("\n",1)[0].strip()
        content = p.split("\n",1)[1].strip() if "\n" in p else ""
        if title in fields:
            fields[title] = content
        elif title == "附加信息":
            for line in content.split("\n"):
                m = re.match(r"\*\*([^*]+)\*\*: (.*)", line.strip())
                if m:
                    extras[m.group(1).strip()] = m.group(2).strip()
    return fields, extras

# ---- 4. 融合构建知识条目 ----
entries = []
for r in records:
    cells = r.get("cells", {})
    no = cell_text(cells.get("mqbn9ed13bv3vkvqlxxvb"))
    eid = no or ("rec-" + r.get("recordId",""))
    rec = {
        "id": eid,
        "record_id": r.get("recordId",""),
        "title": cell_text(cells.get("o687i7pynjdlc7dp6o3ok")) or cell_text(cells.get("G9f8YXm")),
        "problem": normalize_ws(cell_text(cells.get("o687i7pynjdlc7dp6o3ok"))),
        "cause": normalize_ws(cell_text(cells.get("8fbjpkho6bcnrislxuqum"))),
        "solution": clean_solution(normalize_ws(cell_text(cells.get("xilcj2rfnje836pe4wlrb")))),
        "solution_types": norm_list(cell_value(cells.get("ngAM08z"))),
        "tech_stack": norm_list(cell_value(cells.get("qBnlp3p"))),
        "tech_keywords": norm_list(cell_value(cells.get("gk8pxBX"))),
        "keywords": [k.strip() for k in cell_text(cells.get("G9f8YXm")).split(",") if k.strip()],
        "problem_type": cell_text(cells.get("u3w7fc0qr1i7x2u30t81g")),
        "product_line": cell_text(cells.get("ll6xs2lyhyrmkzx5zfmm7")),
        "product_series": cell_text(cells.get("2403n5ic7pya9krzoi3jb")),
        "version": cell_text(cells.get("mf4h6pwyinr9l2a4cpjt7")),
        "module": cell_text(cells.get("h7tlyp6kbvbh488tusblk")),
        "meta": {
            "submitter": cell_text(cells.get("m2b70sy36k1ecxpt2jrt4")),
            "department": cell_text(cells.get("olnc4a7e9su3jk63clybo")),
            "date": parse_date(cells.get("g92ajoa7xgc617ps6vpgp")),
        },
        "source": {
            "type": "aitable",
            "doc_url": "https://alidocs.dingtalk.com/i/nodes/o14dA3GK8g2jxGpGUK3X2o95J9ekBD76",
            "record_id": r.get("recordId",""),
        },
        "status": "active",
    }
    # 若有对应文档，用文档详细内容覆盖/补充
    if no and no in doc_by_no:
        d = doc_by_no[no]
        df, extras = parse_doc_body(d["body"])
        if df["问题现象"]:
            rec["problem"] = normalize_ws(df["问题现象"])
        if df["问题原因"]:
            rec["cause"] = normalize_ws(df["问题原因"])
        if df["解决方案"]:
            rec["solution"] = clean_solution(normalize_ws(df["解决方案"]))
        # 附加信息补充
        for k, v in extras.items():
            key_map = {"对应版本":"version","对应模块":"module","问题类型":"problem_type",
                       "解决方案类型":"solution_types","技术栈":"tech_stack",
                       "技术关键词":"tech_keywords","问题关键字":"keywords"}
            if k in key_map and not (isinstance(rec.get(key_map[k]), str) and rec[key_map[k]]):
                if k == "keywords":
                    rec["keywords"] = [x.strip() for x in v.split(",") if x.strip()]
                elif k in ("solution_types","tech_stack","tech_keywords"):
                    rec[key_map[k]] = norm_list(v)
                else:
                    rec[key_map[k]] = v.strip()
        rec["source"] = {
            "type": "doc",
            "doc_url": d["meta"].get("docUrl",""),
            "node_id": d["meta"].get("nodeId",""),
            "doc_path": d["meta"].get("path",""),
            "record_id": r.get("recordId",""),
        }
        rec["doc_path"] = d["meta"].get("path","")
    # 从 doc_path / 产品线推导分类层级
    cat_parts = []
    if rec.get("doc_path"):
        parts = rec["doc_path"].strip("/").split("/")
        if parts:
            cat_parts.append(parts[0])           # 一级：产品线
        if len(parts) > 1:
            cat_parts.append(parts[1])           # 二级：问题类型
    elif rec["product_line"]:
        cat_parts.append(rec["product_line"])
    if rec["problem_type"] and rec["problem_type"] not in cat_parts:
        cat_parts.append(rec["problem_type"])
    rec["category"] = cat_parts
    entries.append(rec)

print("表格融合条目:", len(entries))

# ---- 5. 补充：无单据编号的纯文档 ----
extra_docs = 0
for d in all_docs:
    path = d["meta"].get("path","")
    if path in doc_no_number:
        continue
    if not d["body"].strip():
        continue
    df, extras = parse_doc_body(d["body"])
    title = d["meta"].get("title","") or os.path.basename(path)
    rec = {
        "id": "doc-" + hashlib.md5(path.encode()).hexdigest()[:10],
        "record_id": "",
        "title": title,
        "problem": normalize_ws(df["问题现象"]) or title,
        "cause": normalize_ws(df["问题原因"]),
        "solution": normalize_ws(df["解决方案"]),
        "solution_types": [],
        "tech_stack": [],
        "tech_keywords": [],
        "keywords": [],
        "problem_type": extras.get("问题类型",""),
        "product_line": "",
        "product_series": "",
        "version": extras.get("对应版本",""),
        "module": extras.get("对应模块",""),
        "meta": {},
        "source": {
            "type": "doc",
            "doc_url": d["meta"].get("docUrl",""),
            "node_id": d["meta"].get("nodeId",""),
            "doc_path": path,
        },
        "doc_path": path,
        "status": "active",
    }
    cat_parts = []
    parts = path.strip("/").split("/")
    if parts:
        cat_parts.append(parts[0])
    if len(parts) > 1:
        cat_parts.append(parts[1])
    rec["category"] = cat_parts
    entries.append(rec)
    extra_docs += 1
print("纯文档补充:", extra_docs)
print("知识条目总数:", len(entries))

# ---- 6. 写出 ----
# 每条一个 JSON 文件（用索引编号命名 + id）
os.makedirs(OUT_ENTRIES, exist_ok=True)
for f in glob.glob(os.path.join(OUT_ENTRIES, "*.json")):
    os.remove(f)

# 最终清洗：统一列表字段类型、清理残留、确保必填字段
LIST_FIELDS = ["solution_types", "tech_stack", "tech_keywords", "keywords", "category"]
for e in entries:
    for f in LIST_FIELDS:
        e[f] = norm_list(e.get(f))
    e["solution"] = clean_solution(e.get("solution", ""))
    e["cause"] = normalize_ws(e.get("cause", ""))
    e["problem"] = normalize_ws(e.get("problem", ""))
    if not e.get("title"):
        e["title"] = e.get("problem") or e.get("id")
    if not e.get("product_line"):
        e["product_line"] = e.get("category", [""])[0] if e.get("category") else ""

manifest = []
for i, e in enumerate(entries):
    fname = f"{i:05d}_{e['id'].replace('/','_')}.json"
    fpath = os.path.join(OUT_ENTRIES, fname)
    with open(fpath, "w") as f:
        json.dump(e, f, ensure_ascii=False, indent=1)
    manifest.append({"file": fname, "id": e["id"]})

with open(os.path.join(OUT_INDEX, "manifest.json"), "w") as f:
    json.dump(manifest, f, ensure_ascii=False, indent=1)

# 统计
stats = {
    "total_entries": len(entries),
    "from_aitable": len(records),
    "with_doc_detail": len(set(e["id"] for e in entries if e["source"]["type"]=="doc" and e.get("record_id"))),
    "doc_only": extra_docs,
}
with open(os.path.join(ROOT, "knowledge", "stats.json"), "w") as f:
    json.dump(stats, f, ensure_ascii=False, indent=1)
print(json.dumps(stats, ensure_ascii=False, indent=1))
print("=== 清洗完成 ===")
