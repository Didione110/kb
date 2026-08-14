<!-- META: {"nodeId": "jb9Y4gmKWrAPqaYac4yA5zGy8GXn6lpz", "title": "工单系统h5端使用uniapp开发，上传图片转化成formdata类型传输失败", "docUrl": "https://alidocs.dingtalk.com/i/nodes/jb9Y4gmKWrAPqaYac4yA5zGy8GXn6lpz?utm_scene=team_space", "path": "/自研/产品功能问题/工单系统h5端使用uniapp开发，上传图片转化成formdata类型传输失败", "fetchTime": "2026-08-13 23:57:22"} -->

## 问题现象

工单系统h5端使用uniapp开发，上传图片转化成formdata类型传输失败

## 问题原因

uniapp不能使用uni.request发送formdata类型请求，导致图片上传失败

## 解决方案

使用uni.uploadFile上传图片

---

## 附加信息

**对应版本**: 供应商平台

**问题类型**: 产品功能问题

**解决方案类型**: 代码修改

**技术栈**: JavaScript

**技术关键词**: 接口

**问题关键字**: uniapp 上传失败

**单据编号**: FX-20241130-094

**提交人**: 肖阳  \|  **提交部门**: 研发1部  \|  **提交日期**: 2024-11-30
