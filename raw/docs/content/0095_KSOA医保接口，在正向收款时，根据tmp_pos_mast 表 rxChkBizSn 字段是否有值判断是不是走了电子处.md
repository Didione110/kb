<!-- META: {"nodeId": "QOG9lyrgJPEzvGyGhv51Dqaa8zN67Mw4", "title": "KSOA医保接口，在正向收款时，根据tmp_pos_mast 表 rxChkBizSn 字段是否有值判断是不是走了电子处方流程，有值调用7207药品销售出库明细上传接口 在退货收款时，根据tmp...", "docUrl": "https://alidocs.dingtalk.com/i/nodes/QOG9lyrgJPEzvGyGhv51Dqaa8zN67Mw4?utm_scene=team_space", "path": "/自研/数据接口问题/KSOA医保接口，在正向收款时，根据tmp_pos_mast 表 rxChkBizSn 字段是否有值判断是不是走了电子处方流程，有值调用7207药品销售出库明细上传接口 在退货收款时，根据tmp...", "fetchTime": "2026-08-13 23:56:05"} -->

## 问题现象

KSOA医保接口，在正向收款时，根据tmp\_pos\_mast 表 rxChkBizSn 字段是否有值判断是不是走了电子处方流程，有值调用7207药品销售出库明细上传接口
在退货收款时，根据tmp\_pos\_mast 表 rxno 字段判断是否有处方，调用7208药品销售出库明细撤销接口

## 问题原因

ksoa医保接口增加7207和7208接口

## 解决方案

KSOA医保接口，在正向收款时，根据tmp\_pos\_mast 表 rxChkBizSn 字段是否有值判断是不是走了电子处方流程，有值调用7207药品销售出库明细上传接口
在退货收款时，根据tmp\_pos\_mast 表 rxno 字段判断是否有处方，调用7208药品销售出库明细撤销接口

---

## 附加信息

**对应版本**: 医保接口

**问题类型**: 数据接口问题

**解决方案类型**: 数据库操作

**技术栈**: REST API, OpenAPI

**技术关键词**: 接口

**问题关键字**: 电子处方

**单据编号**: FX-20231104-013

**提交人**: 黄芳  \|  **提交部门**: 产品开发部  \|  **提交日期**: 2023-11-04
