<!-- META: {"nodeId": "QG53mjyd809pBOwOtwNDEwg5W6zbX04v", "title": "工单系统使用el-image引用图片加载失败", "docUrl": "https://alidocs.dingtalk.com/i/nodes/QG53mjyd809pBOwOtwNDEwg5W6zbX04v?utm_scene=team_space", "path": "/自研/产品功能问题/工单系统使用el-image引用图片加载失败", "fetchTime": "2026-08-13 23:57:21"} -->

## 问题现象

工单系统使用el-image引用图片加载失败

## 问题原因

使用require字段引用图片报错，vue3\+vite构建的项目不能使用require，只能用import

## 解决方案

使用import引入图片路径：资源可使用import.meta.globEager(“…/\*.png”) ;
动态引入，需要给 css 路径加括号，vite官网静态资源处理 new URL(url, import.meta.url)

---

## 附加信息

**对应版本**: 供应商平台

**问题类型**: 产品功能问题

**解决方案类型**: 代码修改

**技术栈**: JavaScript

**问题关键字**: el-image加载失败

**单据编号**: FX-20240829-059

**提交人**: 肖阳  \|  **提交部门**: 研发1部  \|  **提交日期**: 2024-08-29
