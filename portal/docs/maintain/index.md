---
title: 维护流程
---

# 知识维护

本知识库设计为**可维护、可更新、可新增**的活系统，维护链路如下：

```
钉钉数据源（权威） ──同步脚本──▶ kb/knowledge（单一事实源） ──生成脚本──▶ 门户页面
      ▲                                 │                              │
      │                                 ▼                              ▼
  新增/修改知识                     Git 版本管理                     自动发布
  （多人协作）                    （PR 审查 + 历史回溯）            （CI → Pages）
```

## 三个维护层次

| 层次 | 工具 | 适用场景 |
|------|------|----------|
| **数据源层** | 钉钉 AI 表格 / 钉钉知识库 | 客服人员在钉钉端直接录入新问题 |
| **数据层** | 同步 + 清洗 + 索引脚本 | 定时增量拉取钉钉数据到本地 |
| **展示层** | 门户生成 + Git + CI | 页面自动更新、多人协作审查 |

## 维护命令速查

```bash
# 1. 从钉钉同步最新数据
bash scripts/sync_from_dingtalk.sh

# 2. 重建索引
python3 scripts/build_index.py

# 3. 重新生成门户页面
cd portal && node scripts/generate.mjs

# 4. 本地预览
cd portal && pnpm run dev

# 5. 提交变更（Git 工作流）
git add -A && git commit -m "同步最新知识" && git push
```
