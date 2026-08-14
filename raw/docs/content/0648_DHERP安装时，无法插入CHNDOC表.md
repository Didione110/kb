<!-- META: {"nodeId": "mExel2BLV5NzBpEptPakmdBeJgk9rpMq", "title": "DHERP安装时，无法插入CHNDOC表", "docUrl": "https://alidocs.dingtalk.com/i/nodes/mExel2BLV5NzBpEptPakmdBeJgk9rpMq?utm_scene=team_space", "path": "/时空/安装部署问题/DHERP安装时，无法插入CHNDOC表", "fetchTime": "2026-08-14 00:03:17"} -->

## 问题现象

DHERP安装时，无法插入CHNDOC表

## 问题原因

oracle字符集不对，需要更换oracle字符集

## 解决方案

修改方法（以改成UTF8为例）

以高级管理员的权限登录进去

\$ sqlplus / as sysdba;

首先查看一下你DB的编码 select userenv('language') from dual;

SQL\> shutdown immediate;
SQL\> startup mount;
SQL\> alter system enable restricted session;
SQL\> alter system set job\_queue\_processes=0;
SQL\> alter database open;
SQL\> alter database character set internal\_use AL32UTF8(或者是UTF8);
SQL\> shutdown immediate;
SQL\> startup
SQL\>alter system disable restricted session;

注意： 执行完别忘记了执行最后一句，否则可能后续很多事情都做不了
以上如果都执行成功后，可再次查询DB编码 select userenv('language') from dual;
我的查询结果为：AL32UTF8
证明DB的编码已改为UTF-8了;

---

## 附加信息

**对应版本**: 时空智友

**对应模块**: RM模块

**问题类型**: 安装部署问题

**解决方案类型**: SQL脚本, 数据库操作

**技术栈**: Oracle

**技术关键词**: 权限

**问题关键字**: CHNDOC插入失败

**单据编号**: FX-20241210-014

**提交人**: 黄振兴  \|  **提交部门**: 需求&KA部  \|  **提交日期**: 2024-12-10
