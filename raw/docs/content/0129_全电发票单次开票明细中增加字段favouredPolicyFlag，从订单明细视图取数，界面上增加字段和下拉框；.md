<!-- META: {"nodeId": "mExel2BLV5NzBpEptPakg4pqJgk9rpMq", "title": "全电发票单次开票明细中增加字段favouredPolicyFlag，从订单明细视图取数，界面上增加字段和下拉框；", "docUrl": "https://alidocs.dingtalk.com/i/nodes/mExel2BLV5NzBpEptPakg4pqJgk9rpMq?utm_scene=team_space", "path": "/自研/应用操作/全电发票单次开票明细中增加字段favouredPolicyFlag，从订单明细视图取数，界面上增加字段和下拉框；", "fetchTime": "2026-08-13 23:56:30"} -->

## 问题现象

全电发票单次开票明细中增加字段favouredPolicyFlag，从订单明细视图取数，界面上增加字段和下拉框；

## 问题原因

全电发票的favouredPolicyFlag 字段不是之前发票应用中传默认值0，需要根据实际情况获取数据

## 解决方案

更新诺诺开票程序，开票取值中取到应传入的值。

---

## 附加信息

**对应版本**: 税控发票

**问题类型**: 应用操作

**解决方案类型**: 补丁更新

**技术栈**: REST API, WebService

**技术关键词**: 接口

**问题关键字**: 全电发票、开票明细、favouredPolicyFlag

**单据编号**: FX-20231106-021

**提交人**: 黄芳  \|  **提交部门**: 产品开发部  \|  **提交日期**: 2023-11-06
