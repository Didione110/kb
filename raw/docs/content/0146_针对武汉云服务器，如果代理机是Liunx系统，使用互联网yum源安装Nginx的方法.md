<!-- META: {"nodeId": "N7dx2rn0JbjY0oMoFZp1D00XJMGjLRb3", "title": "针对武汉云服务器，如果代理机是Liunx系统，使用互联网yum源安装Nginx的方法", "docUrl": "https://alidocs.dingtalk.com/i/nodes/N7dx2rn0JbjY0oMoFZp1D00XJMGjLRb3?utm_scene=team_space", "path": "/自研/安装部署问题/针对武汉云服务器，如果代理机是Liunx系统，使用互联网yum源安装Nginx的方法", "fetchTime": "2026-08-13 23:56:43"} -->

## 问题现象

针对武汉云服务器，如果代理机是Liunx系统，使用互联网yum源安装Nginx的方法

## 问题原因

针对武汉云服务器，如果代理机是Liunx系统，使用互联网yum源安装Nginx的方法

## 解决方案

如果没有安装epel先用下面命令安装，已经安装了的直接运行安装nginx命令：
1. 安装epel库：sudo yum install epel-release
2. 清除yum缓存：sudo yum clean all
3. 生成新得缓存：sudo yum makecache
4. 安装nginx：sudo yum install nginx
5. 启动nginx：sudo systemctl start nginx
6. 查看nginx运行状态：sudo systemctl status nginx

---

## 附加信息

**对应版本**: 医保接口

**问题类型**: 安装部署问题

**解决方案类型**: 环境设置, 重启服务

**技术栈**: Linux, Nginx

**问题关键字**: 武汉云、Linux、yum、Nginx

**单据编号**: FX-20240407-042

**提交人**: 童光  \|  **提交部门**: 实施4部  \|  **提交日期**: 2024-04-07
