<!-- META: {"nodeId": "lyQod3RxJKEGBNRNhoX1ZGXpWkb4Mw9r", "title": "oracle 金额数据如何保留两位小数  显示  时空数据集是可以解决，  但如何在数据库格式化显示的问题", "docUrl": "https://alidocs.dingtalk.com/i/nodes/lyQod3RxJKEGBNRNhoX1ZGXpWkb4Mw9r?utm_scene=team_space", "path": "/时空/产品功能问题/oracle 金额数据如何保留两位小数  显示  时空数据集是可以解决，  但如何在数据库格式化显示的问题", "fetchTime": "2026-08-14 00:04:00"} -->

## 问题现象

oracle 金额数据如何保留两位小数 显示 
时空数据集是可以解决，

但如何在数据库格式化显示的问题

## 问题原因

如果金额 为10.10时，在oracle中不会显示最后一个0

## 解决方案

TO\_CHAR(a.taxamount,'FM999999990.00')
进行格式化显示

---

## 附加信息

**对应版本**: 时空智友

**对应模块**: RM模块

**问题类型**: 产品功能问题

**解决方案类型**: SQL脚本

**技术栈**: Oracle

**技术关键词**: 打印

**问题关键字**: Oracle 金额 格式化

**单据编号**: FX-20240522-052

**提交人**: 黄振兴  \|  **提交部门**: 需求&KA部  \|  **提交日期**: 2024-05-22
