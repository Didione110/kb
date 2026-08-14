<!-- META: {"nodeId": "KGZLxjv9VGEqBQaQh62l62Zm86EDybno", "title": "用户网络安全软件扫描到tomcat密码安全规则为弱，风险高", "docUrl": "https://alidocs.dingtalk.com/i/nodes/KGZLxjv9VGEqBQaQh62l62Zm86EDybno?utm_scene=team_space", "path": "/时空/安装部署问题/用户网络安全软件扫描到tomcat密码安全规则为弱，风险高", "fetchTime": "2026-08-14 00:03:16"} -->

## 问题现象

用户网络安全软件扫描到tomcat密码安全规则为弱，风险高

## 问题原因

DHERP发版时设置了管理员初始密码

## 解决方案

屏蔽Tomcat\> conf\>tomcat-users.xml文件中这段代码

---

## 附加信息

**对应版本**: 时空智友

**对应模块**: 供应链管理系统

**问题类型**: 安装部署问题

**解决方案类型**: 配置修改

**技术栈**: Tomcat

**技术关键词**: 凭证, 权限

**问题关键字**: 弱密码

**单据编号**: FX-20251230-037

**提交人**: 杨明  \|  **提交部门**: 服务值班组  \|  **提交日期**: 2025-12-30
