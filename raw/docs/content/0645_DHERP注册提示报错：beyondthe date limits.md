<!-- META: {"nodeId": "gvNG4YZ7JnRPAl7ltNdeoXgeJ2LD0oRE", "title": "DHERP注册提示报错：beyondthe date limits", "docUrl": "https://alidocs.dingtalk.com/i/nodes/gvNG4YZ7JnRPAl7ltNdeoXgeJ2LD0oRE?utm_scene=team_space", "path": "/时空/安装部署问题/DHERP注册提示报错：beyondthe date limits", "fetchTime": "2026-08-14 00:03:14"} -->

## 问题现象

DHERP注册提示报错：beyondthe date limits

## 问题原因

DHERP，更换注册服务器操作后

## 解决方案
1. 找北京将对应产品号注册重置
2. 之前使用的tomcat也需要关闭
3. 新服务器tomcat下对应数据库，清除了下面内容，

select \* from ModuleAccrt
select \* from FuncAccredit
select \* from ProductAccrt
select \* from sysstate，
4. 新服务器tomcat文件夹缓存清除
5. 确保ROOT版本是新版本
6. 然后重启tomcat，进行注册

---

## 附加信息

**对应版本**: 时空智友

**对应模块**: RM模块

**问题类型**: 安装部署问题

**解决方案类型**: 环境设置, 重启服务, 替换文件, 数据库操作

**技术栈**: Tomcat, Java

**技术关键词**: 权限

**问题关键字**: 日期超限

**单据编号**: FX-20231116-063

**提交人**: 黄振兴  \|  **提交部门**: 需求&KA部  \|  **提交日期**: 2023-11-16
