<!-- META: {"nodeId": "Y1OQX0akWm7xqXnXIbxm0oEPJGlDd3mE", "title": "mssql如果无法连接数据库，需要调整视图 存储", "docUrl": "https://alidocs.dingtalk.com/i/nodes/Y1OQX0akWm7xqXnXIbxm0oEPJGlDd3mE?utm_scene=team_space", "path": "/时空/环境问题/mssql如果无法连接数据库，需要调整视图 存储", "fetchTime": "2026-08-14 00:01:59"} -->

## 问题现象

mssql如果无法连接数据库，需要调整视图/存储

## 问题原因

mssql如果无法连接数据库，需要调整视图/存储

## 解决方案

可以在开发工具查询出视图/存储过程创建语句
EXEC sp\_helptext 'k\_nn\_writeback'; -- 请替换为你的存储过程
SELECT OBJECT\_DEFINITION(OBJECT\_ID('v\_nn\_billdt')) AS ViewDefinition; -- 请替换为你的视图

---

## 附加信息

**对应版本**: 时空智友

**对应模块**: 供应链管理系统

**问题类型**: 环境问题

**解决方案类型**: SQL脚本, 数据库操作

**技术栈**: SQL Server

**问题关键字**: 数据库连接

**单据编号**: FX-20251119-023

**提交人**: 柳皖智  \|  **提交部门**: 实施2部  \|  **提交日期**: 2025-11-19
