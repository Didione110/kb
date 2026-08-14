<!-- META: {"nodeId": "QG53mjyd809pBOwOtwNDr3jRW6zbX04v", "title": "el-table表格组件自定义表格内容显示全是同一内容", "docUrl": "https://alidocs.dingtalk.com/i/nodes/QG53mjyd809pBOwOtwNDr3jRW6zbX04v?utm_scene=team_space", "path": "/自研/产品功能问题/el-table表格组件自定义表格内容显示全是同一内容", "fetchTime": "2026-08-13 23:57:28"} -->

## 问题现象

el-table表格组件自定义表格内容显示全是同一内容

## 问题原因

使用v-if判断是直接讲表格列赋值成了同一类型

## 解决方案

修改判断类型，使用v-if和v-else-if搭配判断

---

## 附加信息

**对应版本**: 供应商平台

**问题类型**: 产品功能问题

**解决方案类型**: 代码修改

**技术栈**: UI模板, JavaScript

**技术关键词**: 工作流

**问题关键字**: 数据绑定

**单据编号**: FX-20240425-073

**提交人**: 肖阳  \|  **提交部门**: 研发1部  \|  **提交日期**: 2024-04-25
