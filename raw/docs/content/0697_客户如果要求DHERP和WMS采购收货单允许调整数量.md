<!-- META: {"nodeId": "YQBnd5ExVEGvByzyIgmBpyYX8yeZqMmz", "title": "客户如果要求DHERP和WMS采购收货单允许调整数量", "docUrl": "https://alidocs.dingtalk.com/i/nodes/YQBnd5ExVEGvByzyIgmBpyYX8yeZqMmz?utm_scene=team_space", "path": "/时空/产品功能问题/客户如果要求DHERP和WMS采购收货单允许调整数量", "fetchTime": "2026-08-14 00:03:54"} -->

## 问题现象

客户如果要求DHERP和WMS采购收货单允许调整数量

## 问题原因

DHERP从PC端收货到PDA收货确认操作会有时间差异，一般不建议修改。
如果业务需要一定需要调整，需要清理客户已经生成的收货数据和PC收货数据。

## 解决方案

delete wmsrecemt where billno in (select billno from wmsrecedt where rfbillno =:billno )
delete wmsrecedt were rfbillno =:billno
delete wmsinmt where billno=:billno 
,delete tmp\_pda\_getingoods where rfbillno =:billno
billno参数为收货单billno
采购收货单进行单据调整后保存，保证PC端收货数据和PDA收货数据是一致的。

---

## 附加信息

**对应版本**: 时空智友

**对应模块**: 数据仓库模块

**问题类型**: 产品功能问题

**解决方案类型**: 数据库操作

**技术栈**: MySQL

**技术关键词**: 凭证, 接口

**问题关键字**: 数量调整

**单据编号**: FX-20240102-006

**提交人**: 柳皖智  \|  **提交部门**: 实施2部  \|  **提交日期**: 2024-01-02
