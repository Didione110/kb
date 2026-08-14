---
title: 引用与溯源
---

# 引用与溯源

**每条知识必须可溯源**：客服机器人 / AI Agent 在回答中引用本知识库内容时，必须附带来源。

## 引用格式

每条知识条目末尾的「引用来源」包含：

- **来源类型**：`doc`（钉钉知识库文档）或 `aitable`（AI 表格记录）
- **来源链接**：钉钉文档 URL
- **知识库路径**：如 `/自研/实施问题/xxx`
- **表格记录ID**：如 `YNZcO4rwPu`

## 机器人引用示例

```markdown
**解决方案**：在存储过程 k_prn_bill 中添加...

> 来源：[钉钉知识库文档](https://alidocs.dingtalk.com/i/nodes/xxx) · 知识ID: FX-20221204-027
```

## 查询接口返回的引用字段

```json
{
  "id": "FX-20221204-027",
  "title": "客户在使用一键打印的时候...",
  "source_url": "https://alidocs.dingtalk.com/i/nodes/xxx",
  "source_type": "doc"
}
```
