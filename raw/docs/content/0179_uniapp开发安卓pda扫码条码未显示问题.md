<!-- META: {"nodeId": "7NkDwLng8ZEL2OAOhN4DNYx0JKMEvZBY", "title": "uniapp开发安卓pda扫码条码未显示问题", "docUrl": "https://alidocs.dingtalk.com/i/nodes/7NkDwLng8ZEL2OAOhN4DNYx0JKMEvZBY?utm_scene=team_space", "path": "/自研/产品功能问题/uniapp开发安卓pda扫码条码未显示问题", "fetchTime": "2026-08-13 23:57:10"} -->

## 问题现象

uniapp开发安卓pda扫码条码未显示问题

## 问题原因

pda扫码分键盘输入、广播输入，程序内未配置键盘输入、广播输入需配置pda的自带的广播动作、广播标签

## 解决方案

程序内同时配置键盘输入、广播输入两种扫码模式；键盘输入：需要配置输入框并且监听@confirm事件、获取到条码值；广播输入：使用addAction添加pda自带的广播动作、getStringExtra添加pda自带的广播标签，使用时监听onshow方法获取条码值

---

## 附加信息

**对应版本**: 供应商平台

**问题类型**: 产品功能问题

**解决方案类型**: 代码修改

**技术栈**: 前端配置, JavaScript

**技术关键词**: 接口

**问题关键字**: 扫码不显示

**单据编号**: FX-20240306-024

**提交人**: 肖阳  \|  **提交部门**: 研发1部  \|  **提交日期**: 2024-03-06
