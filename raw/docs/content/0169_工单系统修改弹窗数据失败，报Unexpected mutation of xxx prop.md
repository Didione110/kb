<!-- META: {"nodeId": "2Amq4vjg8920o545UmAbK0NvW3kdP0wQ", "title": "工单系统修改弹窗数据失败，报Unexpected mutation of xxx prop", "docUrl": "https://alidocs.dingtalk.com/i/nodes/2Amq4vjg8920o545UmAbK0NvW3kdP0wQ?utm_scene=team_space", "path": "/自研/产品功能问题/工单系统修改弹窗数据失败，报Unexpected mutation of xxx prop", "fetchTime": "2026-08-13 23:57:02"} -->

## 问题现象

工单系统修改弹窗数据失败，报Unexpected mutation of “xxx“ prop

## 问题原因

vue3中直接修改父组件传递数据失败

## 解决方案

子组件中新声明变量，将父组件数据复制给新变量后再次修改

---

## 附加信息

**对应版本**: 供应商平台

**问题类型**: 产品功能问题

**解决方案类型**: 代码修改

**技术栈**: JavaScript

**问题关键字**: props mutation

**单据编号**: FX-20250121-030

**提交人**: 肖阳  \|  **提交部门**: 研发1部  \|  **提交日期**: 2025-01-21
