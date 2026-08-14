<!-- META: {"nodeId": "vy20BglGWOA24X3Xcg41w9jzJA7depqY", "title": "win10升级到win11后sql服务无法启动：请求失败或服务未及时响应", "docUrl": "https://alidocs.dingtalk.com/i/nodes/vy20BglGWOA24X3Xcg41w9jzJA7depqY?utm_scene=team_space", "path": "/用友/环境问题/win10升级到win11后sql服务无法启动：请求失败或服务未及时响应", "fetchTime": "2026-08-14 00:04:24"} -->

## 问题现象

win10升级到win11后sql服务无法启动：请求失败或服务未及时响应

## 问题原因

在运行 Win11系统上，某些新的存储设备和设备驱动程序将公开支持大于4 KB 扇区大小的磁盘扇区大小。
发生这种情况时，由于文件系统不受支持，SQL Server将无法启动，因为SQL Server当前支持512字节和 4KB 的扇区存储大小。

## 解决方案

在SQL Server实列的启动参数中添加“-T1800”跟踪标志，然后再启动SQL Server
默认情况下不启用此跟踪标志。 跟踪标志1800强制SQL Server使用4 KB 作为所有读取和写入操作的扇区大小。 在物理扇区大小大于4 KB 的磁盘上运行SQL Server时，使用跟踪标志1800将模拟本机4 KB 驱动器，这是SQL Server支持的扇区大小。

---

## 附加信息

**对应版本**: U8

**对应模块**: 财务会计

**问题类型**: 环境问题

**解决方案类型**: 配置修改, 重启服务

**技术栈**: SQL Server

**问题关键字**: SQL服务启动

**单据编号**: FX-20230220-036

**提交人**: 汪心文  \|  **提交部门**: 成功部创新组-停用  \|  **提交日期**: 2023-02-20
