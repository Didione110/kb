#!/usr/bin/env bash
# 一键增量同步：从钉钉数据源拉取最新数据 → 清洗 → 重建索引 → 生成报告
# 用法: bash sync_from_dingtalk.sh [--full]
#   --full  全量重新采集（默认增量：跳过已采集的文档，表格全量覆盖）
set -u
export HOME=/home/admin/deepseek-harness/DSH-workspace/.dws-home
export DWS_CONFIG_DIR=/home/admin/deepseek-harness/DSH-workspace/.dws-config

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
LOG="$ROOT/knowledge/sync.log"
TS=$(date '+%Y-%m-%d %H:%M:%S')
echo "=== [$TS] 开始同步 ===" | tee -a "$LOG"

# 1. 刷新文档树（发现新增/删除）
echo "[1/5] 刷新知识库文档树..." | tee -a "$LOG"
python3 "$ROOT/scripts/collect_tree.py" >> "$LOG" 2>&1 || { echo "文档树刷新失败" | tee -a "$LOG"; exit 1; }

# 2. 采集 AI 表格（全量覆盖，幂等）
echo "[2/5] 采集 AI 表格..." | tee -a "$LOG"
python3 "$ROOT/scripts/collect_aitable.py" >> "$LOG" 2>&1 || { echo "AI 表格采集失败" | tee -a "$LOG"; exit 1; }

# 3. 采集知识库文档（断点续传，增量）
echo "[3/5] 采集知识库文档..." | tee -a "$LOG"
python3 "$ROOT/scripts/collect_docs.py" >> "$LOG" 2>&1 || { echo "文档采集失败" | tee -a "$LOG"; exit 1; }

# 4. 清洗融合
echo "[4/5] 清洗融合..." | tee -a "$LOG"
python3 "$ROOT/scripts/clean_fusion.py" >> "$LOG" 2>&1 || { echo "清洗失败" | tee -a "$LOG"; exit 1; }

# 5. 重建索引
echo "[5/5] 重建索引..." | tee -a "$LOG"
python3 "$ROOT/scripts/build_index.py" >> "$LOG" 2>&1 || { echo "索引构建失败" | tee -a "$LOG"; exit 1; }

echo "=== [$TS] 同步完成 ===" | tee -a "$LOG"
python3 -c "import json; s=json.load(open('$ROOT/knowledge/stats.json')); print(json.dumps(s, ensure_ascii=False, indent=1))"
