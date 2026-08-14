<!-- META: {"nodeId": "XPwkYGxZV3MZB3l3c9Rj3DyO8AgozOKL", "title": "系统内的检索方案selector，在检索弹出的时候无法复制，且无法通过表单设计工具设置", "docUrl": "https://alidocs.dingtalk.com/i/nodes/XPwkYGxZV3MZB3l3c9Rj3DyO8AgozOKL?utm_scene=team_space", "path": "/时空/软件补丁问题/系统内的检索方案selector，在检索弹出的时候无法复制，且无法通过表单设计工具设置", "fetchTime": "2026-08-14 00:01:46"} -->

## 问题现象

系统内的检索方案selector，在检索弹出的时候无法复制，且无法通过表单设计工具设置

## 问题原因

selector调用的的tomcat里的js文件，所以无法用设计器修改

## 解决方案

ROOT/form/html/js/htmlselectDiv.js
找到这个目录的js文件打开
在new HtmlGrid的方法里面加入"enablecopy" : "true",
然后重启tomcat生效

---

## 附加信息

**对应版本**: 时空智友

**对应模块**: 供应链管理系统

**问题类型**: 软件补丁问题

**解决方案类型**: 代码修改, 重启服务

**技术栈**: Tomcat, JS

**技术关键词**: 权限

**问题关键字**: 检索方案复制

**单据编号**: FX-20231130-107

**提交人**: 汪松  \|  **提交部门**: 服务值班组  \|  **提交日期**: 2023-11-30
