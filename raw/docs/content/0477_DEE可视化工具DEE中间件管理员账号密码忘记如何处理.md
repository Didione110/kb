<!-- META: {"nodeId": "7NkDwLng8ZEL2OAOhN4DXR92JKMEvZBY", "title": "DEE可视化工具DEE中间件管理员账号密码忘记如何处理", "docUrl": "https://alidocs.dingtalk.com/i/nodes/7NkDwLng8ZEL2OAOhN4DXR92JKMEvZBY?utm_scene=team_space", "path": "/致远OA/安装部署问题/DEE可视化工具DEE中间件管理员账号密码忘记如何处理", "fetchTime": "2026-08-14 00:01:05"} -->

## 问题现象

DEE可视化工具、DEE中间件，管理员账号密码忘记，页面上没有重置密码、忘记密码的功能，如何处理？

## 问题原因

DEE可视化工具、DEE中间件没有设计忘记密码、重置密码的功能，但是可以通过修改配置达到重置密码的效果。

## 解决方案

1、打开安装目录，修改配置文件：\\DEETool\\DEE\_Configurator\\webapps\\ROOT\\WEB-INF\\classes\\login.properties
2、password的值改成如下：password=wDGIHXQsRDzV7SrdRXPFMw==
3、不用重启，直接登录，密码和登录名一样都是dee\_admin
4、登录进去以后，请立刻修改密码，以保证安全。

---

## 附加信息

**对应版本**: A8企业版

**对应模块**: dee数据引擎

**问题类型**: 安装部署问题

**解决方案类型**: 配置修改

**技术栈**: DEE

**技术关键词**: 加密, 权限

**问题关键字**: 密码重置

**单据编号**: FX-20240930-047

**提交人**: 陈娜娜  \|  **提交部门**: 经理办  \|  **提交日期**: 2024-09-30
