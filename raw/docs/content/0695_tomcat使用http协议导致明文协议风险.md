<!-- META: {"nodeId": "m9bN7RYPWdkMYeNeuKOlvlE48Zd1wyK0", "title": "tomcat使用http协议导致明文协议风险", "docUrl": "https://alidocs.dingtalk.com/i/nodes/m9bN7RYPWdkMYeNeuKOlvlE48Zd1wyK0?utm_scene=team_space", "path": "/时空/产品功能问题/tomcat使用http协议导致明文协议风险", "fetchTime": "2026-08-14 00:03:52"} -->

## 问题现象

tomcat使用http协议导致明文协议风险

## 问题原因

http协议在访问时存在账号、密码等数据明文传输问题

## 解决方案

要求客户购买SSL证书，将SSL证书配置到Tomcat中，将http协议更换为https协议（具体修改方法可到知识库中下载查看）

---

## 附加信息

**对应版本**: 时空智友

**对应模块**: RM模块

**问题类型**: 产品功能问题

**解决方案类型**: 配置修改

**技术栈**: Tomcat, SSL

**技术关键词**: 凭证, 加密

**问题关键字**: HTTP明文

**单据编号**: FX-20241104-011

**提交人**: 童光  \|  **提交部门**: 实施4部  \|  **提交日期**: 2024-11-04
