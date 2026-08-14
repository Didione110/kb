<!-- META: {"nodeId": "o14dA3GK8g2jxGpGUn3mz3LzJ9ekBD76", "title": "用sqldeveloper工具连接oracle数据库时提示Undefined error", "docUrl": "https://alidocs.dingtalk.com/i/nodes/o14dA3GK8g2jxGpGUn3mz3LzJ9ekBD76?utm_scene=team_space", "path": "/时空/环境问题/用sqldeveloper工具连接oracle数据库时提示Undefined error", "fetchTime": "2026-08-14 00:01:53"} -->

## 问题现象

用sqldeveloper工具连接oracle数据库时提示Undefined error

## 问题原因

一般是由于ojdbc的jar版本和oracel数据库版本不兼容导致

## 解决方案

找到SQLDeveloper目录下的jdbc里的lib用低版本ojdbc.jar替换里面的ojdbc.jar
附件为低版本的ojdbc压缩包

---

## 附加信息

**对应版本**: 时空智友

**对应模块**: 供应链管理系统

**问题类型**: 环境问题

**解决方案类型**: 替换文件

**技术栈**: Oracle

**技术关键词**: 接口, 加密

**问题关键字**: SQL Developer

**单据编号**: FX-20241009-022

**提交人**: 何盛泽  \|  **提交部门**: 实施4部  \|  **提交日期**: 2024-10-09
