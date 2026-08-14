---
title: 搜索知识
---

# 搜索知识

门户内置**本地全文搜索**（`Ctrl+K` 或点击右上角 🔍），支持中文分词检索。

## 搜索技巧

- **输入问题描述**：如 `U8 登录失败`、`打印模板页码不显示`
- **输入技术关键词**：如 `WebView2`、`SQL Server`、`EAI`
- **输入产品/版本**：如 `用友 U8`、`郑州时空WMS`

## 分类浏览

左侧侧边栏按「产品线 → 问题类型」组织，每个二级分类下按条目标题排序：

```
用友 (636)
├── 应用操作 (636)
│   ├── U8 库存查询慢
│   ├── ...
```

点击分类名称（如「应用操作 (636)」）可查看该分类下全部条目。

## 过滤检索（程序调用）

程序化调用支持精确过滤，见 [API 文档](/api/index.html)。

### 通过 REST API

```bash
curl "http://localhost:8787/api/search?q=U8+登录失败&top_k=5"
```

### 通过命令行

```bash
# 全文检索
python3 scripts/query.py "U8 登录失败" --top 3 --format json

# 分类过滤
python3 scripts/query.py "接口报错" --product-line 用友 --type 数据接口问题
```
