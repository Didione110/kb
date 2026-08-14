<!-- META: {"nodeId": "MNDoBb60VLEQBk0khmE1NEKrJlemrZQ3", "title": "sql 链接 oracle 数据库的快捷语句", "docUrl": "https://alidocs.dingtalk.com/i/nodes/MNDoBb60VLEQBk0khmE1NEKrJlemrZQ3?utm_scene=team_space", "path": "/时空/安装部署问题/sql 链接 oracle 数据库的快捷语句", "fetchTime": "2026-08-14 00:03:24"} -->

## 问题现象

sql 链接 oracle 数据库的快捷语句

## 问题原因

sql 链接 oracle 数据库的快捷语句

## 解决方案

--1.安装oracle 的客户端工具

--2.创建Oracle链接服务器（无需配置监听）
EXEC sp\_addlinkedserver
 @server = 'ORACLE\_LINK1',
 @srvproduct = 'Oracle',
 @provider = 'OraOLEDB.Oracle',
 @datasrc = '111.62.175.1:1521/orcl'; --oracle 地址

--3.账号密码绑定
EXEC sp\_addlinkedsrvlogin
 @rmtsrvname = 'ORACLE\_LINK1',
 @useself = 'FALSE',
 @rmtuser = 'race',
 @rmtpassword = '123456';

--4.开启远程查询权限
EXEC sp\_serveroption 'ORACLE\_LINK1','RPC OUT','TRUE';
GO

--5.测试链接查询是否成功
SELECT \* FROM OPENQUERY(ORACLE\_LINK1,'SELECT \* FROM entdoc');

---

## 附加信息

**对应版本**: 时空智友

**对应模块**: 供应链管理系统

**问题类型**: 安装部署问题

**解决方案类型**: 配置修改, SQL脚本, 环境设置, 数据库操作

**技术栈**: Oracle, SQL Server

**技术关键词**: 凭证, 接口

**问题关键字**: Oracle连接

**单据编号**: FX-20260430-025

**提交人**: 何盛泽  \|  **提交部门**: 实施4部  \|  **提交日期**: 2026-04-30
