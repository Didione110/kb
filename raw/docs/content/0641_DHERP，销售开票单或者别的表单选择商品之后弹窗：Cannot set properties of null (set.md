<!-- META: {"nodeId": "gvNG4YZ7JnRPAl7ltNdeOdG2J2LD0oRE", "title": "DHERP，销售开票单或者别的表单选择商品之后弹窗：Cannot set properties of null (setting 'value'(", "docUrl": "https://alidocs.dingtalk.com/i/nodes/gvNG4YZ7JnRPAl7ltNdeOdG2J2LD0oRE?utm_scene=team_space", "path": "/时空/实施问题/DHERP，销售开票单或者别的表单选择商品之后弹窗：Cannot set properties of null (setting 'value'(", "fetchTime": "2026-08-14 00:03:12"} -->

## 问题现象

DHERP，销售开票单或者别的表单选择商品之后弹窗：Cannot set properties of null (setting 'value')

## 问题原因

商品选择“selector控件”后事件异步代码问题

## 解决方案

注释掉“await sys\_afterGoods();”代码中的“await”就行。

---

## 附加信息

**对应版本**: 时空智友

**对应模块**: 供应链管理系统

**问题类型**: 实施问题

**解决方案类型**: 代码修改

**技术栈**: JS, JavaScript

**问题关键字**: 商品选择 null值

**单据编号**: FX-20231130-116

**提交人**: 刘盾  \|  **提交部门**: 实施2部  \|  **提交日期**: 2023-11-30
