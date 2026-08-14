<!-- META: {"nodeId": "Y1OQX0akWm7xqXnXIbxmjrAGJGlDd3mE", "title": "客户linux服务器环境变化，导致配置的守护进程不能启动接口服务。报错找不到 dotnet 命令。(1)", "docUrl": "https://alidocs.dingtalk.com/i/nodes/Y1OQX0akWm7xqXnXIbxmjrAGJGlDd3mE?utm_scene=team_space", "path": "/自研/环境问题/客户linux服务器环境变化，导致配置的守护进程不能启动接口服务。报错找不到 dotnet 命令。(1)", "fetchTime": "2026-08-13 23:55:09"} -->

## 问题现象

客户linux服务器环境变化，导致配置的守护进程不能启动接口服务。报错找不到 dotnet 命令。

## 问题原因

配置的原dotnet 命令地址在 /usr/local/bin/dotnet
通过whereis dotne 命令查看现在的dotnet命令在目录 /usr/bin/dotnet
需要修改配置的命令地址

## 解决方案

通过ln 命令做软连接，不用重新配置命令地址
例：ln -s /usr/bin/dotnet /usr/local/bin/dotnet

---

## 附加信息

**对应版本**: 电商接口

**问题类型**: 环境问题

**解决方案类型**: 环境设置

**技术栈**: Linux, C# (.NET)

**问题关键字**: dotnet缺失

**单据编号**: FX-20240104-010

**提交人**: 黄芳  \|  **提交部门**: 产品开发部  \|  **提交日期**: 2024-01-04
