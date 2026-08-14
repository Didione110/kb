<!-- META: {"nodeId": "gvNG4YZ7JnRPAl7ltNdeqDPLJ2LD0oRE", "title": "DHERP使用谷歌环境后，在GRID表格控件内，存在一个BUG， 即当输入数字类型字段时，控件默认允许输入小数， 会造成操作员误操作问题", "docUrl": "https://alidocs.dingtalk.com/i/nodes/gvNG4YZ7JnRPAl7ltNdeqDPLJ2LD0oRE?utm_scene=team_space", "path": "/时空/产品功能问题/DHERP使用谷歌环境后，在GRID表格控件内，存在一个BUG， 即当输入数字类型字段时，控件默认允许输入小数， 会造成操作员误操作问题", "fetchTime": "2026-08-14 00:03:41"} -->

## 问题现象

DHERP使用谷歌环境后，在GRID表格控件内，存在一个BUG，
即当输入数字类型字段时，控件默认允许输入小数， 会造成操作员误操作问题

## 问题原因

DHERP使用谷歌环境，对这块支持不是很好

## 解决方案

在输入数量后，执行函数判断，判断当前输入的数量是否为整数，使用Number.isInteger函数来判断

案例：
	if(!Number.isInteger(ds\_ddmx.field("Num").value))

---

## 附加信息

**对应版本**: 时空智友

**对应模块**: 供应链管理系统

**问题类型**: 产品功能问题

**解决方案类型**: 代码修改

**技术栈**: JavaScript, Chrome

**技术关键词**: 审批流, 工作流

**问题关键字**: GRID数字输入

**单据编号**: FX-20251009-004

**提交人**: 汪松  \|  **提交部门**: 经理办  \|  **提交日期**: 2025-10-09
