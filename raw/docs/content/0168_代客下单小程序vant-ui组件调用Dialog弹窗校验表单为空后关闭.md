<!-- META: {"nodeId": "m9bN7RYPWdkMYeNeuKOlpRYz8Zd1wyK0", "title": "代客下单小程序vant-ui组件调用Dialog弹窗校验表单为空后关闭", "docUrl": "https://alidocs.dingtalk.com/i/nodes/m9bN7RYPWdkMYeNeuKOlpRYz8Zd1wyK0?utm_scene=team_space", "path": "/自研/产品功能问题/代客下单小程序vant-ui组件调用Dialog弹窗校验表单为空后关闭", "fetchTime": "2026-08-13 23:57:01"} -->

## 问题现象

代客下单小程序vant-ui组件调用Dialog弹窗校验表单为空后关闭

## 问题原因

直接使用this.setdata修改显示弹窗字段不可行

## 解决方案

使用before-close异步操作判断当前确认操作，返回是否弹窗显示结果

---

## 附加信息

**对应版本**: 供应商平台

**问题类型**: 产品功能问题

**解决方案类型**: 代码修改

**技术栈**: JS, JavaScript

**技术关键词**: 凭证, 审批流, 接口, 工作流, 权限

**问题关键字**: Dialog校验

**单据编号**: FX-20240201-006

**提交人**: 肖阳  \|  **提交部门**: 研发1部  \|  **提交日期**: 2024-02-01
