<!-- META: {"nodeId": "6LeBq413JA0w1YkYC3O0qGApVDOnGvpb", "title": "Formtalk推送V5失败，通过FT采集的外部数据部分推送OA失败", "docUrl": "https://alidocs.dingtalk.com/i/nodes/6LeBq413JA0w1YkYC3O0qGApVDOnGvpb?utm_scene=team_space", "path": "/致远OA/数据接口问题/Formtalk推送V5失败，通过FT采集的外部数据部分推送OA失败", "fetchTime": "2026-08-14 00:00:14"} -->

## 问题现象

Formtalk推送V5失败，通过FT采集的外部数据部分推送OA失败

## 问题原因

查看应用日志，因FT填写的数据长度超过了OA表单设置长度，导致数据推送失败；

## 解决方案

找到Formtalk推送V5的集成字段，修改OA表单的字段长度，因FT文本未设置字段长度，尽量调大OA表单字段长度，以满足大文本字段集成要求。

---

## 附加信息

**对应版本**: A8企业版

**对应模块**: formtalk

**问题类型**: 数据接口问题

**解决方案类型**: 配置修改

**技术栈**: DEE

**技术关键词**: 接口

**问题关键字**: 推送失败

**单据编号**: FX-20240202-028

**提交人**: 陈娜娜  \|  **提交部门**: 经理办  \|  **提交日期**: 2024-02-02
