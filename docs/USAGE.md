# 知识库使用文档

## 一、这是什么

基于钉钉两个数据源构建的**客服智能知识库**，供 AI Agent / 客服机器人准确定位问题、引用权威答案：

| 数据源 | 说明 | 采集量 |
|--------|------|--------|
| AI 表格「科情OA知识库数据梳理」 | 结构化问题记录（产品线/版本/模块/现象/原因/方案） | 2431 条 |
| 钉钉知识库（QqWXwjyd1796xz31） | 详细问题文档（含 803 个与表格对应的详细版） | 868 篇 |
| **融合后知识条目** | 表格为主 + 文档补充 + 纯文档 | **2485 条** |

## 二、目录结构

```
kb/
├── raw/                          # 原始采集数据（只读）
│   ├── aitable/                  # AI 表格原始 JSON
│   └── docs/                     # 知识库文档（markdown + tree.json + done_ids.txt）
├── knowledge/                    # 处理后的知识库
│   ├── entries/                  # 2485 条知识条目（JSON，每条一文件）
│   ├── index/                    # 检索索引
│   │   ├── categories.json       # 分类体系（产品线 → 问题类型）
│   │   ├── keywords.json         # 关键词 → 条目映射（13.9万词）
│   │   ├── by_category.json      # 按分类组织的条目清单
│   │   └── search_index.json     # 全文检索索引
│   ├── markdown/                 # 面向客服的 Markdown 版（按产品线分目录）
│   ├── stats.json                # 统计信息
│   └── sync.log                  # 同步日志
├── docs/
│   ├── robot-integration.md      # 客服机器人集成指南 ★
│   └── data-dictionary.md        # 字段字典
├── scripts/                      # 全部脚本
└── README.md                     # 架构说明
```

## 三、日常使用

### 查询（最重要）
```bash
cd kb/scripts
python3 query.py "客户提问的问题描述"          # 全文检索 Top-5
python3 query.py --keyword "WebView2"        # 关键词检索
python3 query.py --product-line 用友 --type 应用操作 --top 10  # 分类浏览
python3 query.py --id FX-20221130-059        # 精确取一条
python3 query.py --list-categories           # 查看分类体系
python3 query.py --stats                     # 查看统计
```

### 同步更新（自进化）
```bash
bash scripts/sync_from_dingtalk.sh           # 一键增量同步（推荐每日执行）
```
流程：刷新文档树 → 采集表格 → 增量采集文档（断点续传）→ 清洗融合 → 重建索引。
幂等：重复执行不会产生重复数据。

## 四、字段字典（知识条目）

| 字段 | 类型 | 说明 |
|------|------|------|
| id | string | 知识 ID（单据编号 FX-xxx / doc-xxx） |
| title | string | 标题 |
| problem / cause / solution | string | 问题现象 / 原因 / 解决方案 |
| problem_type | string | 问题类型（应用操作/产品功能/安装部署/环境/接口/数据错误/实施/无法使用/效率/补丁/安全） |
| product_line | string | 产品线（用友/时空/致远OA/自研/其他/蓝凌OA/钉钉） |
| product_series / version / module | string | 产品系列 / 版本 / 模块 |
| solution_types | list | 解决方案类型（配置修改/代码修改/SQL脚本/数据库操作等） |
| tech_stack / tech_keywords / keywords | list | 技术栈 / 技术关键词 / 问题关键字 |
| category | list | 分类路径 [产品线, 问题类型] |
| source | object | 来源（type: doc/aitable, doc_url, node_id, doc_path, record_id） |
| meta | object | 提交人 / 提交部门 / 提交日期 |
| status | string | active |

## 五、自进化机制

1. **新增**：钉钉端新增记录/文档 → 下次 `sync_from_dingtalk.sh` 自动采集入库。
2. **修改**：文档重采集覆盖（done_ids.txt 按 nodeId 去重，内容更新自动生效）；表格全量覆盖。
3. **删除**：文档树刷新后，本地孤儿文件标记 `stale`（可人工清理）。
4. **索引**：清洗后自动重建，无需手工维护。

## 六、常见问题

- **Q: 采集文档时报网络错误？** A: 脚本有断点续传，重跑会跳过已完成部分。
- **Q: 如何在钉钉端验证数据？** A: 表格访问 https://alidocs.dingtalk.com/i/nodes/o14dA3GK8g2jxGpGUK3X2o95J9ekBD76
- **Q: 凭证在哪？** A: `kb/.dws-home` 和 `kb/.dws-config`（勿删除、勿提交到仓库）。
