<!-- META: {"nodeId": "7NkDwLng8ZEL2OAOhN4D37j2JKMEvZBY", "title": "客户在ERP修改批号，效期，生产日期需要同步给WMS", "docUrl": "https://alidocs.dingtalk.com/i/nodes/7NkDwLng8ZEL2OAOhN4D37j2JKMEvZBY?utm_scene=team_space", "path": "/其他/应用操作/客户在ERP修改批号，效期，生产日期需要同步给WMS", "fetchTime": "2026-08-13 23:58:18"} -->

## 问题现象

客户在ERP修改批号，效期，生产日期需要同步给WMS

## 问题原因

因WMS管理货位，对于一个品种，一个批号部分数量进行处理时，不是很好处理（需要新的货位）

## 解决方案

让客户在ERP发起批号，效期，生产日期调整，传到WMS，WMS在盘点界面提取两条数据（一条旧，一条新），然后通过修改实盘数量和手动选择架位号来解决该问题。

---

## 附加信息

**对应版本**: 郑州时空WMS

**问题类型**: 应用操作

**解决方案类型**: 其他

**技术栈**: REST API, WebService, DEE

**技术关键词**: 库存, 追溯码, 接口

**问题关键字**: ERP-WMS同步

**单据编号**: FX-20230630-021

**提交人**: 曾德军  \|  **提交部门**: 实施3部  \|  **提交日期**: 2023-06-30
