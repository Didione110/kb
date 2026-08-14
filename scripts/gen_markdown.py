#!/usr/bin/env python3
# 生成面向客服机器人的 Markdown 知识库（按分类组织，含引用）
# 输出: knowledge/markdown/{product_line}/...md 每篇=一个知识条目（含来源引用）
import json, os, glob, re

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
ENTRIES_DIR = os.path.join(ROOT, "knowledge", "entries")
MD_ROOT = os.path.join(ROOT, "knowledge", "markdown")
if os.path.exists(MD_ROOT):
    import shutil
    shutil.rmtree(MD_ROOT)
os.makedirs(MD_ROOT, exist_ok=True)

def esc(s):
    return (s or "").replace("|", "\\|").replace("\n", "<br>")

def render(e):
    src = e.get("source", {})
    lines = []
    lines.append(f"# {e.get('title','')}")
    lines.append("")
    lines.append("> 知识条目 | 可被客服机器人引用")
    lines.append("")
    lines.append("## 元信息")
    lines.append("")
    lines.append("| 字段 | 值 |")
    lines.append("|------|----|")
    lines.append(f"| 知识ID | {esc(e['id'])} |")
    lines.append(f"| 产品线 | {esc(e.get('product_line','-'))} |")
    lines.append(f"| 产品系列 | {esc(e.get('product_series','-'))} |")
    lines.append(f"| 版本 | {esc(e.get('version','-'))} |")
    lines.append(f"| 模块 | {esc(e.get('module','-'))} |")
    lines.append(f"| 问题类型 | {esc(e.get('problem_type','-'))} |")
    lines.append(f"| 解决方案类型 | {esc(', '.join(e.get('solution_types') or []))} |")
    lines.append(f"| 技术栈 | {esc(', '.join(e.get('tech_stack') or []))} |")
    lines.append(f"| 技术关键词 | {esc(', '.join(e.get('tech_keywords') or []))} |")
    lines.append(f"| 问题关键字 | {esc(', '.join(e.get('keywords') or []))} |")
    lines.append(f"| 分类路径 | {esc(' / '.join(e.get('category') or []))} |")
    if e.get("meta"):
        m = e["meta"]
        lines.append(f"| 提交人 | {esc(m.get('submitter','-'))} |")
        lines.append(f"| 提交部门 | {esc(m.get('department','-'))} |")
        lines.append(f"| 提交日期 | {esc(m.get('date','-'))} |")
    lines.append("")
    lines.append("## 问题现象")
    lines.append("")
    lines.append(e.get("problem","") or "-")
    lines.append("")
    lines.append("## 问题原因")
    lines.append("")
    lines.append(e.get("cause","") or "-")
    lines.append("")
    lines.append("## 解决方案")
    lines.append("")
    lines.append(e.get("solution","") or "-")
    lines.append("")
    lines.append("## 引用来源")
    lines.append("")
    lines.append(f"- 来源类型: `{src.get('type','')}`")
    if src.get("doc_url"):
        lines.append(f"- 来源链接: {src.get('doc_url')}")
    if src.get("doc_path"):
        lines.append(f"- 知识库路径: `{src.get('doc_path')}`")
    if src.get("record_id"):
        lines.append(f"- 表格记录ID: `{src.get('record_id')}`")
    lines.append("")
    return "\n".join(lines)

count = 0
by_cat = {}
for f in sorted(glob.glob(os.path.join(ENTRIES_DIR, "*.json"))):
    e = json.load(open(f))
    cats = e.get("category") or []
    l1 = cats[0] if cats else "未分类"
    # 二级：取问题类型
    l2 = e.get("problem_type") or (cats[1] if len(cats) > 1 else "")
    l2 = l2 or "其他"
    l1_dir = os.path.join(MD_ROOT, re.sub(r'[\\/:*?"<>|]', "_", l1))
    os.makedirs(l1_dir, exist_ok=True)
    fname = f"{e['id']}.md"
    with open(os.path.join(l1_dir, fname), "w") as of:
        of.write(render(e))
    count += 1

# 生成 README 索引
idx_lines = ["# 客服机器人知识库（Markdown 版）", "",
             f"共 {count} 篇知识条目，按产品线/问题类型组织。", "",
             "## 目录", ""]
for l1 in sorted(os.listdir(MD_ROOT)):
    if not os.path.isdir(os.path.join(MD_ROOT, l1)):
        continue
    n = len(glob.glob(os.path.join(MD_ROOT, l1, "*.md")))
    idx_lines.append(f"- **{l1}** ({n} 篇)")
with open(os.path.join(MD_ROOT, "README.md"), "w") as f:
    f.write("\n".join(idx_lines) + "\n")

print(f"=== Markdown 知识库生成完成: {count} 篇 -> {MD_ROOT} ===")
