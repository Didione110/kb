<!-- META: {"nodeId": "MNDoBb60VLEQBk0khmE1ydGzJlemrZQ3", "title": "图片附件上传保存时提示违反了 PRIMARY KEY 约束，不能在对象'dbo.KMATTACHMENT'中插入重复键。", "docUrl": "https://alidocs.dingtalk.com/i/nodes/MNDoBb60VLEQBk0khmE1ydGzJlemrZQ3?utm_scene=team_space", "path": "/时空/数据错误问题/图片附件上传保存时提示违反了 PRIMARY KEY 约束，不能在对象'dbo.KMATTACHMENT'中插入重复键。", "fetchTime": "2026-08-14 00:02:00"} -->

## 问题现象

图片附件上传保存时提示违反了 PRIMARY KEY 约束，不能在对象'dbo.KMATTACHMENT'中插入重复键。

## 问题原因

原因为上传的billno与KMATTACHMENT表中的billno重复

## 解决方案

调整billno生成的最大值，再上传就不会提示重复。调整syscode表中prefix列为A的recnum值

---

## 附加信息

**对应版本**: 时空智友

**对应模块**: 供应链管理系统

**问题类型**: 数据错误问题

**解决方案类型**: 数据库操作

**技术栈**: SQL Server

**技术关键词**: 凭证

**问题关键字**: 主键冲突

**单据编号**: FX-20240201-012

**提交人**: 杨明  \|  **提交部门**: 服务值班组  \|  **提交日期**: 2024-02-01
