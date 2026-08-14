<!-- META: {"nodeId": "QG53mjyd809pBOwOtwNDXgY9W6zbX04v", "title": "三医院IPS平台上传追溯码，追溯码太多，接口接收不了，显示报错 { code  0, message   Request body too large. }", "docUrl": "https://alidocs.dingtalk.com/i/nodes/QG53mjyd809pBOwOtwNDXgY9W6zbX04v?utm_scene=team_space", "path": "/自研/数据接口问题/三医院IPS平台上传追溯码，追溯码太多，接口接收不了，显示报错 { code  0, message   Request body too large. }", "fetchTime": "2026-08-13 23:56:07"} -->

## 问题现象

三医院IPS平台上传追溯码，追溯码太多，接口接收不了，显示报错

## 问题原因

传入内容太多

## 解决方案

在程序中按照单据号分组调用接口传递
不需要实施人员修改存储过程

---

## 附加信息

**对应版本**: 供应商平台

**问题类型**: 数据接口问题

**解决方案类型**: 代码修改

**技术栈**: Tomcat, Nginx, WebLogic

**技术关键词**: 接口

**问题关键字**: 追溯码超限

**单据编号**: FX-20250705-007

**提交人**: 黄芳  \|  **提交部门**: 研发1部  \|  **提交日期**: 2025-07-05
