<!-- META: {"nodeId": "R1zknDm0WREaD2O2h0p1R97Q8BQEx5rG", "title": "在Oracle数据库背景下请货单无法保存，报违反唯一主键，经过排查发现表的主键是billno+billsn+entid,根据插入数据发现并没有重复", "docUrl": "https://alidocs.dingtalk.com/i/nodes/R1zknDm0WREaD2O2h0p1R97Q8BQEx5rG?utm_scene=team_space", "path": "/时空/数据错误问题/在Oracle数据库背景下请货单无法保存，报违反唯一主键，经过排查发现表的主键是billno+billsn+entid,根据插入数据发现并没有重复", "fetchTime": "2026-08-14 00:02:01"} -->

## 问题现象

在Oracle数据库背景下请货单无法保存，报违反唯一主键，经过排查发现表的主键是billno\+billsn\+entid,根据插入数据发现并没有重复

## 问题原因

多方排查发现是针对RequestOrg表建的索引有问题，索引的主键是entid\+orgid\+goodsid,所以导致重复了

## 解决方案

将错误索引删除后正常保存；

---

## 附加信息

**对应版本**: 时空智友

**对应模块**: 供应链管理系统

**问题类型**: 数据错误问题

**解决方案类型**: SQL脚本, 数据库操作

**技术栈**: Oracle

**问题关键字**: 主键冲突

**单据编号**: FX-20251009-001

**提交人**: 徐东  \|  **提交部门**: 需求&KA部  \|  **提交日期**: 2025-10-09
