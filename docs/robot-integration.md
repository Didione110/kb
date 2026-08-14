# 客服机器人集成指南

本文档说明如何让客服机器人（或 AI Agent）引用本知识库，实现"准确定位问题、回答精准、回答可溯源"。

## 1. 两种消费方式

### 方式 A：查询接口（推荐，结构化）
机器人后端调用 `scripts/query.py`，拿到结构化 JSON：

```bash
# 全文检索（模拟客户提问）
python3 scripts/query.py "U8 登录失败" --top 3 --format json

# 关键词检索（明确技术词）
python3 scripts/query.py --keyword "WebView2" --top 5

# 分类过滤（限定产品线 + 问题类型）
python3 scripts/query.py "接口报错" --product-line 用友 --type 数据接口问题

# 精确获取
python3 scripts/query.py --id FX-20221130-059
```

返回示例：
```json
[{
  "id": "FX-20260526-025",
  "title": "用户安装悟空报错，提示安装WebView2时失败...",
  "problem": "用户安装悟空报错...",
  "solution": "1、到微软官方下载页...",
  "source_url": "https://alidocs.dingtalk.com/i/nodes/amweZ92...",
  "source_type": "doc",
  "product_line": "钉钉",
  "version": "免费版",
  "module": "悟空",
  "keywords": ["WebView2安装失败"]
}]
```

### 方式 B：Markdown 文件（人读/直接喂给 LLM 上下文）
`knowledge/markdown/{产品线}/{知识ID}.md`，每篇含元信息表 + 问题现象/原因/解决方案 + 引用来源。
适合 RAG（检索增强生成）场景：向量化后按相似度召回，再把整篇作为上下文注入提示词。

## 2. 机器人回答规范（引用协议）

为保证"回答精准 + 可溯源"，机器人回答必须遵守：

1. **命中判定**：用查询接口检索，仅当结果得分 > 0 时视为命中；无命中时明确说"未在知识库中找到对应方案"，不要编造。
2. **答案来源**：答案正文使用 `problem/cause/solution` 字段内容，**不得**脱离原文改写关键操作步骤。
3. **必须引用**：回答末尾附引用块：
   ```
   参考来源：[知识ID: FX-20260526-025](source_url)
   产品线: 钉钉 | 版本: 免费版 | 模块: 悟空
   ```
4. **多候选**：Top-N 结果都给客户时，标注每条对应的问题现象，让客户确认哪个匹配。

## 3. 机器人提示词建议（System Prompt 片段）

```
你是客服智能助手。回答前必须调用知识库查询接口：
1) 将客户问题转为检索关键词，执行 query.py 全文检索；
2) 如有命中，基于命中条目的"问题现象/问题原因/解决方案"组织回答；
3) 回答必须附引用来源链接；
4) 无命中时如实说明，并建议转人工。
禁止编造解决方案；所有操作步骤必须来自知识库原文。
```

## 4. 性能与部署建议

- **检索耗时**：本地 JSON 检索 < 100ms（2485 条），适合高频调用。
- **嵌入向量化**：如接入 LLM RAG，可对 `knowledge/markdown/**/*.md` 做 embedding（建议 chunk=500 字，overlap=50），存向量库（如 Milvus/FAISS/Chroma）。
- **增量更新**：每日定时执行 `bash scripts/sync_from_dingtalk.sh`，自动发现新增知识并重建索引；向量库侧对比 `manifest.json` 差异做增量 embedding。
- **权限**：知识库文件位于 `kb/knowledge/`，机器人服务只需读权限。

## 5. 质量保障

- **溯源闭环**：每条知识的 `source_url` 指向钉钉原文，客服可一键打开核对。
- **更新频率**：钉钉端每周/每月新增知识，同步脚本幂等可重跑，重复执行不会产生重复条目。
- **监控**：`knowledge/stats.json` 提供条目数/分类分布，可接入监控看板。
