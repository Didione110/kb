#!/usr/bin/env python3
# 采集 AI 表格「科情OA知识库数据梳理」全部记录（分页），保存 JSON
import json, os, subprocess, sys, time

BASE_ID = "o14dA3GK8g2jxGpGUK3X2o95J9ekBD76"
OUT_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "raw", "aitable")
os.makedirs(OUT_DIR, exist_ok=True)

ENV = dict(os.environ)
ENV["HOME"] = "/home/admin/deepseek-harness/DSH-workspace/.dws-home"
ENV["DWS_CONFIG_DIR"] = "/home/admin/deepseek-harness/DSH-workspace/.dws-config"

TABLES = [
    ("hERWDMS", "数据表"),
    ("0mSTARa", "技术问题知识分享"),
    ("PRYSzWY", "知识分享副本"),
]

def dws(*args, timeout=60):
    r = subprocess.run(["dws", *args, "--format", "json"], capture_output=True,
                       text=True, env=ENV, timeout=timeout)
    try:
        return json.loads(r.stdout)
    except Exception:
        raise RuntimeError(f"dws {' '.join(args)} non-json: {r.stdout[:300]} err={r.stderr[:300]}")

def collect(table_id, table_name):
    all_records = []
    cursor = ""
    page = 0
    while True:
        page += 1
        if cursor:
            d = dws("aitable", "record", "query", "--base-id", BASE_ID,
                    "--table-id", table_id, "--limit", "100", "--cursor", cursor)
        else:
            d = dws("aitable", "record", "query", "--base-id", BASE_ID,
                    "--table-id", table_id, "--limit", "100")
        data = d.get("data", {})
        recs = data.get("records", []) if isinstance(data, dict) else d.get("records", [])
        nc = data.get("nextCursor") if isinstance(data, dict) else d.get("nextCursor")
        print(f"[{table_name}] page {page}: {len(recs)} records, nextCursor={nc}")
        all_records.extend(recs)
        if not nc or not recs:
            break
        cursor = nc
        time.sleep(0.3)
    return all_records

for table_id, table_name in TABLES:
    recs = collect(table_id, table_name)
    out = os.path.join(OUT_DIR, f"{table_id}_{table_name}_records.json")
    with open(out, "w") as f:
        json.dump(recs, f, ensure_ascii=False, indent=1)
    print(f"[{table_name}] SAVED {len(recs)} records -> {out}")
print("=== DONE ===")
