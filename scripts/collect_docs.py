#!/usr/bin/env python3
# 批量读取知识库全部文档内容，保存 markdown 原始数据（支持断点续传）
# 用法: python3 collect_docs.py
import json, os, subprocess, hashlib, time, sys

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
TREE = os.path.join(ROOT, "raw", "docs", "tree.json")
OUT_DIR = os.path.join(ROOT, "raw", "docs", "content")
DONE_FILE = os.path.join(ROOT, "raw", "docs", "done_ids.txt")
os.makedirs(OUT_DIR, exist_ok=True)

ENV = dict(os.environ)
ENV["HOME"] = "/home/admin/deepseek-harness/DSH-workspace/.dws-home"
ENV["DWS_CONFIG_DIR"] = "/home/admin/deepseek-harness/DSH-workspace/.dws-config"

def safe_name(path):
    parts = path.strip("/").split("/")
    title = parts[-1]
    title = "".join(c for c in title if c not in '/\\:*?"<>|\n\r\t')
    return title[:60]

def main():
    tree = json.load(open(TREE))
    files = [t for t in tree if t["nodeType"] == "file"]
    done = set()
    if os.path.exists(DONE_FILE):
        done = set(l.strip() for l in open(DONE_FILE) if l.strip())

    ok, fail = 0, 0
    with open(DONE_FILE, "a") as df:
        for i, f in enumerate(files):
            nid = f["nodeId"]
            if nid in done:
                ok += 1
                continue
            idx = f"{i:04d}"
            title = safe_name(f["path"])
            out_path = os.path.join(OUT_DIR, f"{idx}_{title}.md")
            try:
                r = subprocess.run(["dws", "doc", "read", "--node", nid, "--format", "json"],
                                   capture_output=True, text=True, env=ENV, timeout=60)
                try:
                    d = json.loads(r.stdout)
                except Exception:
                    raise RuntimeError("non-json: " + r.stdout[:200])
                if not d.get("success"):
                    raise RuntimeError("api fail: " + json.dumps(d.get("error", {}), ensure_ascii=False)[:300])
                md = d.get("markdown", "") or ""
                meta = {
                    "nodeId": nid,
                    "title": d.get("title", "") or title,
                    "docUrl": d.get("docUrl", ""),
                    "path": f["path"],
                    "fetchTime": time.strftime("%Y-%m-%d %H:%M:%S"),
                }
                with open(out_path, "w") as of:
                    of.write("<!-- META: " + json.dumps(meta, ensure_ascii=False) + " -->\n\n")
                    of.write(md)
                df.write(nid + "\n")
                df.flush()
                ok += 1
            except Exception as e:
                fail += 1
                print(f"FAIL {i} {nid} {f['path']}: {e}", flush=True)
                time.sleep(1)
            if (i + 1) % 50 == 0:
                print(f"progress {i+1}/{len(files)} ok={ok} fail={fail}", flush=True)
    print(f"DONE ok={ok} fail={fail} total={len(files)}")

if __name__ == "__main__":
    main()
