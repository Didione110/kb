<!-- META: {"nodeId": "a9E05BDRVQr29yxytDz1NLZZJ63zgkYA", "title": "WMS电子监管码导出的销售退回的XML文件上传马上放心平台解析不出退货单位", "docUrl": "https://alidocs.dingtalk.com/i/nodes/a9E05BDRVQr29yxytDz1NLZZJ63zgkYA?utm_scene=team_space", "path": "/其他/应用操作/WMS电子监管码导出的销售退回的XML文件上传马上放心平台解析不出退货单位", "fetchTime": "2026-08-13 23:58:40"} -->

## 问题现象

WMS电子监管码导出的销售退回的XML文件上传马上放心平台解析不出退货单位

## 问题原因

电子监管码导出字段取错，客户是连锁药店，总部是仓库，误以为总部就是上游

## 解决方案

修改存储过程LJT\_WMS\_ExportEMC中对应导出取值字段

---

## 附加信息

**对应版本**: 郑州时空WMS

**问题类型**: 应用操作

**解决方案类型**: SQL脚本, 数据库操作

**技术栈**: Oracle, SQL Server

**技术关键词**: 凭证, 接口, 打印

**问题关键字**: 退货单位

**单据编号**: FX-20240326-051

**提交人**: 吴中涛  \|  **提交部门**: 实施3部  \|  **提交日期**: 2024-03-26
