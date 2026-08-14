<!-- META: {"nodeId": "Qnp9zOoBVBbYBmXmHPYAnDzOV1DK0g6l", "title": "按批次和入库数量自定义唯一码（数量为10，唯一码为angleid1,angleid2....angleid10）", "docUrl": "https://alidocs.dingtalk.com/i/nodes/Qnp9zOoBVBbYBmXmHPYAnDzOV1DK0g6l?utm_scene=team_space", "path": "/时空/应用操作/按批次和入库数量自定义唯一码（数量为10，唯一码为angleid1,angleid2....angleid10）", "fetchTime": "2026-08-14 00:02:36"} -->

## 问题现象

按批次和入库数量自定义唯一码（数量为10，唯一码为angleid1,angleid2....angleid10）

## 问题原因

按批次和入库数量自定义唯一码（数量为10，唯一码为angleid1,angleid2....angleid10）

## 解决方案

WITH numbers AS (
 SELECT top 500 ROW\_NUMBER() OVER (ORDER BY (SELECT NULL)) AS n
 FROM sys.all\_columns c1
 CROSS JOIN sys.all\_columns c2 
)
SELECT 
 b.angleid\+ CAST(aa.n AS VARCHAR(10)) AS result
FROM purindt a
JOIN batchcode b 
 ON a.angleid = b.angleid 
 AND a.entid = b.entid
JOIN numbers aa
 ON aa.n \<= a.num 
WHERE a.num \> 0 
ORDER BY a.angleid, a.entid, aa.n;

---

## 附加信息

**对应版本**: 时空智友

**对应模块**: 供应链管理系统

**问题类型**: 应用操作

**解决方案类型**: SQL脚本, 数据库操作

**技术栈**: SQL Server

**技术关键词**: 追溯码

**问题关键字**: 唯一码批次

**单据编号**: FX-20250806-009

**提交人**: 向阳  \|  **提交部门**: 实施2部  \|  **提交日期**: 2025-08-06
