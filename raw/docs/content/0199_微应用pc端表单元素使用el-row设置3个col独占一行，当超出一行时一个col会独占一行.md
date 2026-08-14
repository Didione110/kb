<!-- META: {"nodeId": "XPwkYGxZV3MZB3l3c9Rjjrp68AgozOKL", "title": "微应用pc端表单元素使用el-row设置3个col独占一行，当超出一行时一个col会独占一行", "docUrl": "https://alidocs.dingtalk.com/i/nodes/XPwkYGxZV3MZB3l3c9Rjjrp68AgozOKL?utm_scene=team_space", "path": "/自研/产品功能问题/微应用pc端表单元素使用el-row设置3个col独占一行，当超出一行时一个col会独占一行", "fetchTime": "2026-08-13 23:57:26"} -->

## 问题现象

微应用pc端表单元素使用el-row设置3个col独占一行，当超出一行时一个col会独占一行

## 问题原因

使用el-row中col个数之和超过24，不使用flex布局，col会自动换行

## 解决方案

el-row设置类型为flex设置为弹性布局,justify设置为end

---

## 附加信息

**对应版本**: 供应商平台

**问题类型**: 产品功能问题

**解决方案类型**: 代码修改

**技术栈**: UI模板, 前端配置, JavaScript

**问题关键字**: 布局错位

**单据编号**: FX-20230206-021

**提交人**: 肖阳  \|  **提交部门**: 研发1部  \|  **提交日期**: 2023-02-06
