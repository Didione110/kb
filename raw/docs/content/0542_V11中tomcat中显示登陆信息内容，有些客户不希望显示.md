<!-- META: {"nodeId": "6LeBq413JA0w1YkYC3O0pXLbVDOnGvpb", "title": "V11中tomcat中显示登陆信息内容，有些客户不希望显示", "docUrl": "https://alidocs.dingtalk.com/i/nodes/6LeBq413JA0w1YkYC3O0pXLbVDOnGvpb?utm_scene=team_space", "path": "/时空/环境问题/V11中tomcat中显示登陆信息内容，有些客户不希望显示", "fetchTime": "2026-08-14 00:01:56"} -->

## 问题现象

V11中tomcat中显示登陆信息内容，有些客户不希望显示

## 问题原因

V11中tomcat中显示登陆信息内容，有些客户不希望显示

## 解决方案

修改webapps\\ROOT\\WEB-INF的web.xml的内容
 屏蔽有关AccessLogFilter的内容
之后不会显示登录信息

---

## 附加信息

**对应版本**: 时空智友

**对应模块**: RM模块

**问题类型**: 环境问题

**解决方案类型**: 配置修改

**技术栈**: Tomcat, Java

**技术关键词**: 权限

**问题关键字**: 登录信息

**单据编号**: FX-20231122-078

**提交人**: 黄振兴  \|  **提交部门**: 需求&KA部  \|  **提交日期**: 2023-11-22
