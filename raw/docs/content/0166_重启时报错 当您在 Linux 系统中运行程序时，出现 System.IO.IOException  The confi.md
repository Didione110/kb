<!-- META: {"nodeId": "Y1OQX0akWm7xqXnXIbxm2vbrJGlDd3mE", "title": "重启时报错 当您在 Linux 系统中运行程序时，出现 System.IO.IOException  The configured user limit (128( on the number ...", "docUrl": "https://alidocs.dingtalk.com/i/nodes/Y1OQX0akWm7xqXnXIbxm2vbrJGlDd3mE?utm_scene=team_space", "path": "/自研/安装部署问题/重启时报错 当您在 Linux 系统中运行程序时，出现 System.IO.IOException  The configured user limit (128( on the number ...", "fetchTime": "2026-08-13 23:57:00"} -->

## 问题现象

重启时报错
当您在 Linux 系统中运行程序时，出现 System.IO.IOException: The configured user limit (128) on the number of inotify instances has been reached 错误

## 问题原因

通常是由于系统对 inotify 实例数量的限制导致的。inotify 是 Linux 文件系统事件监控机制，默认限制可能不足以满足某些应用程序的需求。

## 解决方案

解决方法
1. 检查当前限制

使用以下命令查看当前系统对 inotify 实例的限制：

cat /proc/sys/fs/inotify/max\_user\_instances
复制
2\. 临时修改限制

通过以下命令临时增加限制，例如将限制设置为 1024：

echo 1024 \> /proc/sys/fs/inotify/max\_user\_instances
复制
此更改将在系统重启后失效。
2. 永久修改限制

为了使更改永久生效，可以编辑 /etc/sysctl.conf 文件并添加以下内容：

fs.inotify.max\_user\_instances = 1024
复制
然后运行以下命令应用更改：

sudo sysctl -p

---

## 附加信息

**对应版本**: 医保接口

**问题类型**: 安装部署问题

**解决方案类型**: 配置修改

**技术栈**: Linux, Shell

**技术关键词**: 接口, 工作流, 权限

**问题关键字**: inotify 限制

**单据编号**: FX-20260105-001

**提交人**: 黄振兴  \|  **提交部门**: 需求&KA部  \|  **提交日期**: 2026-01-05
