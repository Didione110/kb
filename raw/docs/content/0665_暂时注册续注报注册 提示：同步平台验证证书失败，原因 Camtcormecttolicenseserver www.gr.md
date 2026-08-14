<!-- META: {"nodeId": "ZX6GRezwJlnAq2m2IgY11qa3WdqbropQ", "title": "暂时注册续注报注册 提示：同步平台验证证书失败，原因 Camtcormecttolicenseserver www.gr960.com.Socket can t connect the serv...", "docUrl": "https://alidocs.dingtalk.com/i/nodes/ZX6GRezwJlnAq2m2IgY11qa3WdqbropQ?utm_scene=team_space", "path": "/时空/安装部署问题/暂时注册续注报注册 提示：同步平台验证证书失败，原因 Camtcormecttolicenseserver www.gr960.com.Socket can t connect the serv...", "fetchTime": "2026-08-14 00:03:30"} -->

## 问题现象

暂时注册续注报注册
提示：同步平台验证证书失败，原因:Camtcormecttolicenseserver www.gr960.com.Socket can t connect the serverWwW.gr960.com

## 问题原因

老版本指向注册服务器不对
license.server,name=www. qy960.com
license.server.port=2009

## 解决方案

指向以下位置

license.server.name=license.qy960.com
license.server.port=2009

---

## 附加信息

**对应版本**: 时空智友

**对应模块**: RM模块

**问题类型**: 安装部署问题

**解决方案类型**: 配置修改

**技术栈**: Java, DEE, EAI

**技术关键词**: 接口, 加密

**问题关键字**: 证书连接失败

**单据编号**: FX-20240330-065

**提交人**: 黄振兴  \|  **提交部门**: 需求&KA部  \|  **提交日期**: 2024-03-30
