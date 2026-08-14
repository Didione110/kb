<!-- META: {"nodeId": "NZQYprEoWo0nBOROCBYeMma7V1waOeDk", "title": "number类型字段作为公式条件时无法区分0和null，number=null作为公式条件执行的结果当number=0时也会执行", "docUrl": "https://alidocs.dingtalk.com/i/nodes/NZQYprEoWo0nBOROCBYeMma7V1waOeDk?utm_scene=team_space", "path": "/致远OA/产品功能问题/number类型字段作为公式条件时无法区分0和null，number=null作为公式条件执行的结果当number=0时也会执行", "fetchTime": "2026-08-14 00:01:27"} -->

## 问题现象

'number'类型字段作为公式条件时无法区分0和null，number=null作为公式条件执行的结果当number=0时也会执行。

## 问题原因

和总部确认底层逻辑就是这样。

## 解决方案

建议增加一个'nvarchar'类型的字段等于这个'number'字段值，用'nvarchar'作为判断null的条件。

---

## 附加信息

**对应版本**: A8企业版

**对应模块**: 表单制作

**问题类型**: 产品功能问题

**解决方案类型**: 数据库操作

**技术栈**: Oracle

**问题关键字**: null判断

**单据编号**: FX-20231130-110

**提交人**: 代虎  \|  **提交部门**: 实施5部  \|  **提交日期**: 2023-11-30
