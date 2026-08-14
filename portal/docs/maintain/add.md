---
title: 新增知识
---

# 新增知识

## 方式一：钉钉端录入（推荐）

在钉钉 AI 表格「科情OA知识库数据梳理」中新增一行记录，或在钉钉知识库中新建文档，然后运行同步脚本即可自动进入知识库：

```bash
bash scripts/sync_from_dingtalk.sh   # 增量拉取
python3 scripts/build_index.py        # 重建索引
cd portal && node scripts/generate.mjs  # 重新生成门户
```

## 方式二：直接编辑本地条目

高级用户可直接在 `kb/knowledge/entries/` 下新增 JSON 文件：

```json
{
  "id": "FX-20260814-001",
  "title": "问题标题",
  "problem": "问题现象描述",
  "cause": "问题原因",
  "solution": "解决方案",
  "problem_type": "应用操作",
  "product_line": "用友",
  "version": "U8",
  "module": "",
  "keywords": ["关键词"],
  "category": ["用友", "应用操作"],
  "source": { "type": "manual", "doc_url": "" }
}
```

然后重建索引与门户。

## 方式三：门户提交（多人协作）

通过 Git 提交 + PR 审查：

```bash
git checkout -b feat/add-knowledge
# 编辑或新增条目 JSON
git add -A
git commit -m "新增知识：xxx"
git push origin feat/add-knowledge
# 在托管平台发起 PR，审查通过后合并
```

## 注意事项

- **单一事实源**：钉钉端是权威源，本地修改可能被下次同步覆盖；如需长期保留请优先在钉钉端修改
- **ID 规范**：`FX-YYYYMMDD-NNN`（日期 + 序号）
- **必填字段**：`title` / `problem` / `solution` / `category`（一级/二级分类）
