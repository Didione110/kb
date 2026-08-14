<!-- META: {"nodeId": "2Amq4vjg8920o545UmAbPLXoW3kdP0wQ", "title": "DHERP器械专版的系统自带采购收货提取采购订单拆分明细后新增明细为空", "docUrl": "https://alidocs.dingtalk.com/i/nodes/2Amq4vjg8920o545UmAbPLXoW3kdP0wQ?utm_scene=team_space", "path": "/时空/产品功能问题/DHERP器械专版的系统自带采购收货提取采购订单拆分明细后新增明细为空", "fetchTime": "2026-08-14 00:03:40"} -->

## 问题现象

DHERP器械专版的系统自带采购收货提取采购订单拆分明细后新增明细为空

## 问题原因

拆分明细调用方法问题

## 解决方案

async function uf\_splitLine()\{
		if(ds\_ddmx.field("num").value \> 0)\{
		var row = ds\_ddmx.recno \+ 1;
		await ds\_ddmx.insert();
		await pf\_copyRow(ds\_ddmx, ds\_ddmx, row, "billsn,billSort,billno,bofAdjNum");
	\}
\}
调用方法下加个异步

---

## 附加信息

**对应版本**: 时空智友

**对应模块**: 供应链管理系统

**问题类型**: 产品功能问题

**解决方案类型**: 代码修改

**技术栈**: 前端配置, JavaScript

**技术关键词**: 凭证, 接口, 工作流

**问题关键字**: 采购明细为空

**单据编号**: FX-20240813-037

**提交人**: 吴中涛  \|  **提交部门**: 实施3部  \|  **提交日期**: 2024-08-13
