<!-- META: {"nodeId": "QG53mjyd809pBOwOtwNDANvGW6zbX04v", "title": "Oracle数据库生成AWR报告方法", "docUrl": "https://alidocs.dingtalk.com/i/nodes/QG53mjyd809pBOwOtwNDANvGW6zbX04v?utm_scene=team_space", "path": "/时空/环境问题/Oracle数据库生成AWR报告方法", "fetchTime": "2026-08-14 00:01:48"} -->

## 问题现象

Oracle数据库生成AWR报告方法

## 问题原因

Oracle数据库生成AWR报告方法

## 解决方案

Oracle数据库生成AWR报告方法

切换用户
使用oralce用户登陆操作系统，如果不知道oracle用户密码，可从root用户
su -oracle

sqlplus连接数据库
在oracle用户下执行 sqlplus /as sysdba命令，连接到oracle数据库:

在sqlplus中执行 @?/rdbms/admin/awrrpt.sql

输入导出报告的格式
在执行@?rdbms/admin/awrrpt.sql命令后，会提示输入导出报告的格式，默认格式为html，如果想导出html格式，直接Enter即可:

输入导出天数
根据需要，输入导出的报告的具体天数，即当前时间N天之内的所有信息:

输入要导出的snap的开始ID
在输入要导出的天数之后，oracle会列出所有满足预期天数的snap的信息，根据需要，输入snap的开始ID:

输入要导出的snap的截止ID
输入开始ID之后，会提示输入截止ID，根据需要输入截止ID:

设置导出的报告名称
导出报告时，如果需要设置导出的报告名称，可根据提示进行修改:

查看报告
输入报告名称之后并敲击回车之后，oracle会自动生成AWR报告，可退出sqlplus进行查看

---

## 附加信息

**对应版本**: 时空智友

**对应模块**: RM模块

**问题类型**: 环境问题

**解决方案类型**: SQL脚本, 数据库操作

**技术栈**: Oracle

**技术关键词**: 权限

**问题关键字**: AWR报告

**单据编号**: FX-20241021-027

**提交人**: 黄振兴  \|  **提交部门**: 需求&KA部  \|  **提交日期**: 2024-10-21
