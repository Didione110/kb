<!-- META: {"nodeId": "XPwkYGxZV3MZB3l3c9Rj1eO28AgozOKL", "title": "人福微信小程序删除商品使用splice方法删除对象数组，点击一次会删除多条数据", "docUrl": "https://alidocs.dingtalk.com/i/nodes/XPwkYGxZV3MZB3l3c9Rj1eO28AgozOKL?utm_scene=team_space", "path": "/自研/产品功能问题/人福微信小程序删除商品使用splice方法删除对象数组，点击一次会删除多条数据", "fetchTime": "2026-08-13 23:57:05"} -->

## 问题现象

人福微信小程序删除商品使用splice方法删除对象数组，点击一次会删除多条数据

## 问题原因

splice方法会改变原数组的值，在foreach中使用，会导致index改变删除多条数据

## 解决方案

使用filter过滤删除数组

---

## 附加信息

**对应版本**: 供应商平台

**问题类型**: 产品功能问题

**解决方案类型**: 代码修改

**技术栈**: JS, JavaScript

**问题关键字**: splice误删

**单据编号**: FX-20250304-006

**提交人**: 肖阳  \|  **提交部门**: 研发1部  \|  **提交日期**: 2025-03-04
