---
title: 数据同步
---

# 数据同步

知识库与钉钉数据源保持**单向同步**（钉钉 → 本地），本地是投影。

## 同步流程

```bash
# 一键同步（采集 → 清洗 → 索引）
bash scripts/sync_from_dingtalk.sh

# 或分步执行
python3 scripts/collect_aitable.py   # 拉取 AI 表格
python3 scripts/collect_docs.py      # 拉取知识库文档
python3 scripts/clean_fusion.py      # 清洗融合
python3 scripts/build_index.py       # 构建索引
```

## 同步产物

| 产物 | 路径 | 说明 |
|------|------|------|
| 原始数据 | `raw/` | 只读采集产物 |
| 知识条目 | `knowledge/entries/` | 2485 条 JSON |
| 检索索引 | `knowledge/index/` | 分类/关键词/全文 |
| 统计 | `knowledge/stats.json` | 数量统计 |

## 自动化建议

在服务器配置 cron 定时同步：

```cron
# 每天凌晨 2 点同步
0 2 * * * cd /path/to/kb && bash scripts/sync_from_dingtalk.sh >> knowledge/sync.log 2>&1
```
