<!-- META: {"nodeId": "mExel2BLV5NzBpEptPakDgZKJgk9rpMq", "title": "vue3引入tinymce富文本组件使用工具栏时无反应", "docUrl": "https://alidocs.dingtalk.com/i/nodes/mExel2BLV5NzBpEptPakDgZKJgk9rpMq?utm_scene=team_space", "path": "/自研/产品功能问题/vue3引入tinymce富文本组件使用工具栏时无反应", "fetchTime": "2026-08-13 23:57:13"} -->

## 问题现象

vue3引入tinymce富文本组件使用工具栏时无反应

## 问题原因

当富文本在某一个弹窗上使用时，工具栏会出现下拉选择时的层级比弹窗的小，所以，选项会被弹窗遮挡

## 解决方案

需要把工具栏的下拉框的层级提高，找到tinymce这个文件夹下面的skin.css,skin.min.css
把class名为tox-tinymce-aux的第一个的z-index属性变大即可。

---

## 附加信息

**对应版本**: 供应商平台

**问题类型**: 产品功能问题

**解决方案类型**: 代码修改

**技术栈**: JS, JavaScript

**问题关键字**: tinymce 工具栏 失效

**单据编号**: FX-20240511-039

**提交人**: 肖阳  \|  **提交部门**: 研发1部  \|  **提交日期**: 2024-05-11
