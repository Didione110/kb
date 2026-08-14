<!-- META: {"nodeId": "XPwkYGxZV3MZB3l3c9RjLP368AgozOKL", "title": "ERP和OMS无法实现多对一的关系。", "docUrl": "https://alidocs.dingtalk.com/i/nodes/XPwkYGxZV3MZB3l3c9RjLP368AgozOKL?utm_scene=team_space", "path": "/其他/数据接口问题/ERP和OMS无法实现多对一的关系。", "fetchTime": "2026-08-13 23:58:05"} -->

## 问题现象

ERP和OMS无法实现多对一的关系。

## 问题原因

ERP商品编码需要唯一性。

## 解决方案

ERP内新增C端编码，多条同个商品的资料C端编码填一样，OMS统计库存将同个C端编码的库存汇总。
所有C端店铺上架这个商品的时候平台商家编码全部和C端编号字段保持一致。

---

## 附加信息

**对应版本**: 点三OMS

**问题类型**: 数据接口问题

**解决方案类型**: 配置修改, 数据库操作

**技术栈**: DEE

**技术关键词**: 库存, 追溯码, 接口

**问题关键字**: 多对一

**单据编号**: FX-20231130-115

**提交人**: 丁恺  \|  **提交部门**: 实施3部  \|  **提交日期**: 2023-11-30
