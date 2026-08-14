<!-- META: {"nodeId": "dpYLaezmVNEeKkYkhPn1PPj1WrMqPxX6", "title": "对接的接口，由http升级为https", "docUrl": "https://alidocs.dingtalk.com/i/nodes/dpYLaezmVNEeKkYkhPn1PPj1WrMqPxX6?utm_scene=team_space", "path": "/自研/安全问题/对接的接口，由http升级为https", "fetchTime": "2026-08-13 23:57:00"} -->

## 问题现象

对接的接口，由http升级为https

## 问题原因

使用c#开发对接rest接口或者soap接口，由http升级为https，接口程序报错不能使用

## 解决方案

添加安全协议，不同版本的framework 的安全协议不同，都加上
ServicePointManager.SecurityProtocol = SecurityProtocolType.Ssl3
 \| SecurityProtocolType.Tls
 \| SecurityProtocolType.Tls11
 \| SecurityProtocolType.Tls12;
.net 5里面支持了Tls1.3版本，目前还没用到。

---

## 附加信息

**对应版本**: 一键打印

**问题类型**: 安全问题

**解决方案类型**: 代码修改

**技术栈**: C# (.NET), REST API, WebService

**技术关键词**: 加密

**问题关键字**: HTTPS升级

**单据编号**: FX-20240603-003

**提交人**: 黄芳  \|  **提交部门**: 研发1部  \|  **提交日期**: 2024-06-03
