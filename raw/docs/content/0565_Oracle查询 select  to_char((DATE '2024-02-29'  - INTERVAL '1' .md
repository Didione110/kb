<!-- META: {"nodeId": "R1zknDm0WREaD2O2h0p109dO8BQEx5rG", "title": "Oracle查询 select  to_char((DATE '2024-02-29'  - INTERVAL '1' YEAR( ( from dual 提示日期无效（ora-01839）", "docUrl": "https://alidocs.dingtalk.com/i/nodes/R1zknDm0WREaD2O2h0p109dO8BQEx5rG?utm_scene=team_space", "path": "/时空/效率问题/Oracle查询 select  to_char((DATE '2024-02-29'  - INTERVAL '1' YEAR( ( from dual 提示日期无效（ora-01839）", "fetchTime": "2026-08-14 00:02:14"} -->

## 问题现象

Oracle查询 select to\_char((DATE '2024-02-29' - INTERVAL '1' YEAR) ) from dual 提示日期无效（ora-01839）

## 问题原因

闰年查询2月29日日期有效，平年查询2月29年日期无效

## 解决方案

使用月度计算，月份会取2月28日 select TO\_CHAR(ADD\_MONTHS(date'2024-02-29', -12),'YYYY-MM-DD') from dual

---

## 附加信息

**对应版本**: 时空智友

**对应模块**: 供应链管理系统

**问题类型**: 效率问题

**解决方案类型**: SQL脚本, 数据库操作

**技术栈**: Oracle

**技术关键词**: 凭证, 审批流, 追溯码, 工作流

**问题关键字**: 日期无效

**单据编号**: FX-20240301-001

**提交人**: 陈波  \|  **提交部门**: 需求&KA部  \|  **提交日期**: 2024-03-01
