#!/usr/bin/env python3
# 递归遍历知识库文档树，刷新 tree.json（发现新增/删除的文档）
# 用法: python3 collect_tree.py
import json, os, subprocess

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
OUT = os.path.join(ROOT, "raw", "docs", "tree.json")
WORKSPACE_ID = "QqWXwjyd1796xz31"

ENV = dict(os.environ)
ENV["HOME"] = "/home/admin/deepseek-harness/DSH-workspace/.dws-home"
ENV["DWS_CONFIG_DIR"] = "/home/admin/deepseek-harness/DSH-workspace/.dws-config"

def dws(*args, timeout=60):
    r = subprocess.run(["dws", *args, "--format", "json"], capture_output=True,
                       text=True, env=ENV, timeout=timeout)
    try:
        return json.loads(r.stdout)
    except Exception:
        raise RuntimeError(f"dws {' '.join(args)} non-json: {r.stdout[:300]}")

def walk(node_id, depth, path):
    d = dws("doc", "list", "--folder", node_id)
    nodes = d.get("nodes", [])
    out = []
    for n in nodes:
        out.append({
            "name": n.get("name"),
            "nodeId": n.get("nodeId"),
            "nodeType": n.get("nodeType"),
            "contentType": n.get("contentType"),
            "hasChildren": n.get("hasChildren"),
            "docUrl": n.get("docUrl"),
            "path": path + "/" + n.get("name", ""),
        })
        if n.get("hasChildren"):
            out.extend(walk(n["nodeId"], depth + 1, path + "/" + n.get("name", "")))
    return out

def main():
    d = dws("doc", "list", "--workspace", WORKSPACE_ID)
    roots = d.get("nodes", [])
    tree = []
    for n in roots:
        tree.append({
            "name": n.get("name"),
            "nodeId": n.get("nodeId"),
            "nodeType": n.get("nodeType"),
            "contentType": n.get("contentType"),
            "hasChildren": n.get("hasChildren"),
            "docUrl": n.get("docUrl"),
            "path": "/" + n.get("name", ""),
        })
        if n.get("hasChildren"):
            tree.extend(walk(n["nodeId"], 1, "/" + n.get("name", "")))
    with open(OUT, "w") as f:
        json.dump(tree, f, ensure_ascii=False, indent=1)
    files = sum(1 for t in tree if t["nodeType"] == "file")
    print(f"树刷新完成: {len(tree)} 节点, {files} 个文档 -> {OUT}")

if __name__ == "__main__":
    main()
