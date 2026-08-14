<!-- META: {"nodeId": "gwva2dxOW4jYe3B3FkwNkYYNJbkz3BRL", "title": "工单系统复制输入框内容到粘贴板报错TypeError Cannot read properties of undefined", "docUrl": "https://alidocs.dingtalk.com/i/nodes/gwva2dxOW4jYe3B3FkwNkYYNJbkz3BRL?utm_scene=team_space", "path": "/自研/产品功能问题/工单系统复制输入框内容到粘贴板报错TypeError Cannot read properties of undefined", "fetchTime": "2026-08-13 23:57:11"} -->

## 问题现象

工单系统复制输入框内容到粘贴板报错TypeError: Cannot read properties of undefined (reading 'writeText')

## 问题原因

vue3\+vite项目复制内容使用writeText方法导致报错

## 解决方案

临时构建一个input元素，将需要复制的内容赋值给input元素并选中，选择实例内容并复制， 删除临时input元素

---

## 附加信息

**对应版本**: 供应商平台

**问题类型**: 产品功能问题

**解决方案类型**: 代码修改

**技术栈**: JavaScript

**技术关键词**: 接口, 权限

**问题关键字**: 粘贴板报错

**单据编号**: FX-20241008-006

**提交人**: 肖阳  \|  **提交部门**: 研发1部  \|  **提交日期**: 2024-10-08
