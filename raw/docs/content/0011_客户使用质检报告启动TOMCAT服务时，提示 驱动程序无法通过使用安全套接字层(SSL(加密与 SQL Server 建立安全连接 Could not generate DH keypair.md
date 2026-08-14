<!-- META: {"nodeId": "EpGBa2Lm8aMGRNgNcw7polLx8gN7R35y", "title": "客户使用质检报告启动TOMCAT服务时，提示 驱动程序无法通过使用安全套接字层(SSL(加密与 SQL Server 建立安全连接 Could not generate DH keypair", "docUrl": "https://alidocs.dingtalk.com/i/nodes/EpGBa2Lm8aMGRNgNcw7polLx8gN7R35y?utm_scene=team_space", "path": "/自研/软件无法使用/客户使用质检报告启动TOMCAT服务时，提示 驱动程序无法通过使用安全套接字层(SSL(加密与 SQL Server 建立安全连接 Could not generate DH keypair", "fetchTime": "2026-08-13 23:54:56"} -->

## 问题现象

客户使用质检报告启动TOMCAT服务时，提示
驱动程序无法通过使用安全套接字层(SSL)加密与 SQL Server 建立安全连接
Could not generate DH keypair

## 问题原因

系统JDK版本不对，版本过低

## 解决方案

重新安装高版本JDK

---

## 附加信息

**对应版本**: 供应商平台

**问题类型**: 软件无法使用

**解决方案类型**: 环境设置

**技术栈**: SQL Server, Tomcat, JDK

**问题关键字**: SSL加密

**单据编号**: FX-20231203-009

**提交人**: 张柳青  \|  **提交部门**: 研发2部  \|  **提交日期**: 2023-12-03
