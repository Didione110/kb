<!-- META: {"nodeId": "G1DKw2zgV2gP63q3cqbMNM70JB5r9YAn", "title": "通用看板使用vue-json-excel组件导出表格打开报文件和扩展名不匹配问题", "docUrl": "https://alidocs.dingtalk.com/i/nodes/G1DKw2zgV2gP63q3cqbMNM70JB5r9YAn?utm_scene=team_space", "path": "/自研/产品功能问题/通用看板使用vue-json-excel组件导出表格打开报文件和扩展名不匹配问题", "fetchTime": "2026-08-13 23:57:19"} -->

## 问题现象

通用看板使用vue-json-excel组件导出表格打开报文件和扩展名不匹配问题

## 问题原因

vue-json-excel使用html表格绘制.xls文件，Microsoft Excel不再将HTML作为原生内容，因此打开报错

## 解决方案

使用file-saver xlsx组件实现导出excel

---

## 附加信息

**对应版本**: 供应商平台

**问题类型**: 产品功能问题

**解决方案类型**: 代码修改

**技术栈**: JavaScript

**问题关键字**: vue-json-excel

**单据编号**: FX-20230228-051

**提交人**: 肖阳  \|  **提交部门**: 研发1部  \|  **提交日期**: 2023-02-28
