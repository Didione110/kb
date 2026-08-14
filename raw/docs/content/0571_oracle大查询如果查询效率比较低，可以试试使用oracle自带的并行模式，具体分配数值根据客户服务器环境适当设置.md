<!-- META: {"nodeId": "R1zknDm0WREaD2O2h0p1kkEd8BQEx5rG", "title": "oracle大查询如果查询效率比较低，可以试试使用oracle自带的并行模式，具体分配数值根据客户服务器环境适当设置", "docUrl": "https://alidocs.dingtalk.com/i/nodes/R1zknDm0WREaD2O2h0p1kkEd8BQEx5rG?utm_scene=team_space", "path": "/时空/效率问题/oracle大查询如果查询效率比较低，可以试试使用oracle自带的并行模式，具体分配数值根据客户服务器环境适当设置", "fetchTime": "2026-08-14 00:02:19"} -->

## 问题现象

oracle大查询如果查询效率比较低，可以试试使用oracle自带的并行模式，具体分配数值根据客户服务器环境适当设置

## 问题原因

oracle大查询如果查询效率比较低，可以试试使用oracle自带的并行模式，具体分配数值根据客户服务器环境适当设置

## 解决方案

select /\*\+ parallel(4) \*/ \* from trbillmt

---

## 附加信息

**对应版本**: 时空智友

**对应模块**: 供应链管理系统

**问题类型**: 效率问题

**解决方案类型**: SQL脚本, 数据库操作

**技术栈**: Oracle

**技术关键词**: 凭证

**问题关键字**: 并行查询

**单据编号**: FX-20221203-021

**提交人**: 童光  \|  **提交部门**: 实施2部  \|  **提交日期**: 2022-12-03
