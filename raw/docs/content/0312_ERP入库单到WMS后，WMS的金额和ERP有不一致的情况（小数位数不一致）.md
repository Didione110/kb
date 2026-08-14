<!-- META: {"nodeId": "R1zknDm0WREaD2O2h0p1B9OY8BQEx5rG", "title": "ERP入库单到WMS后，WMS的金额和ERP有不一致的情况（小数位数不一致）", "docUrl": "https://alidocs.dingtalk.com/i/nodes/R1zknDm0WREaD2O2h0p1B9OY8BQEx5rG?utm_scene=team_space", "path": "/其他/实施问题/ERP入库单到WMS后，WMS的金额和ERP有不一致的情况（小数位数不一致）", "fetchTime": "2026-08-13 23:58:51"} -->

## 问题现象

ERP入库单到WMS后，WMS的金额和ERP有不一致的情况（小数位数不一致）

## 问题原因

除了检查收货，验收明细表的金额小数位，还要检查WMS收货和验收2个临时表

## 解决方案

调整收货和验收明细小数位(含历史表)，临时表temp\_WMS\_Receiving，Temp\_WMS\_ReceivingChect这2个表的小数位

---

## 附加信息

**对应版本**: 郑州时空WMS

**问题类型**: 实施问题

**解决方案类型**: 数据库操作

**技术栈**: Oracle, SQL Server, PolarDB

**技术关键词**: 审批流, 工作流

**问题关键字**: 金额不一致

**单据编号**: FX-20250121-041

**提交人**: 张彬  \|  **提交部门**: 实施3部  \|  **提交日期**: 2025-01-21
