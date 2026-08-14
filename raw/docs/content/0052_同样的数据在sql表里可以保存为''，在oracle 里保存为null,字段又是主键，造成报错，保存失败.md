<!-- META: {"nodeId": "P7QG4Yx2JpbLAn0nHQN7zQN9W9dEq3XD", "title": "同样的数据在sql表里可以保存为''，在oracle 里保存为null,字段又是主键，造成报错，保存失败", "docUrl": "https://alidocs.dingtalk.com/i/nodes/P7QG4Yx2JpbLAn0nHQN7zQN9W9dEq3XD?utm_scene=team_space", "path": "/自研/数据错误问题/同样的数据在sql表里可以保存为''，在oracle 里保存为null,字段又是主键，造成报错，保存失败", "fetchTime": "2026-08-13 23:55:32"} -->

## 问题现象

同样的数据在sql表里可以保存为‘’，在oracle 里保存为null,字段又是主键，造成报错，保存失败

## 问题原因

同样的数据在sql表里可以保存为‘’，在oracle 里保存为null,字段又是主键，造成报错，保存失败

## 解决方案

不启用可能为''的值作为主键

---

## 附加信息

**对应版本**: 税控发票

**问题类型**: 数据错误问题

**解决方案类型**: 数据库操作

**技术栈**: Oracle

**问题关键字**: 主键空值

**单据编号**: FX-20221104-009

**提交人**: 黄芳  \|  **提交部门**: 产品开发部  \|  **提交日期**: 2022-11-04
