<!-- META: {"nodeId": "20eMKjyp81D3BY5YFe0ggXQDJxAZB1Gv", "title": "数据平铺视图 tileview中，添加附件后，不显示到最新的那一项", "docUrl": "https://alidocs.dingtalk.com/i/nodes/20eMKjyp81D3BY5YFe0ggXQDJxAZB1Gv?utm_scene=team_space", "path": "/自研/应用操作/数据平铺视图 tileview中，添加附件后，不显示到最新的那一项", "fetchTime": "2026-08-13 23:56:31"} -->

## 问题现象

数据平铺视图 tileview中，添加附件后，不显示到最新的那一项

## 问题原因

增加代码 滚动到新添加的项

## 解决方案

// 滚动到新添加的项
int newRowHandle = tileView.DataRowCount - 1;
if (newRowHandle \>= 0) 

---

## 附加信息

**对应版本**: 药监接口

**问题类型**: 应用操作

**解决方案类型**: 代码修改

**技术栈**: C# (.NET)

**技术关键词**: 打印, 工作流

**问题关键字**: 附件不显示

**单据编号**: FX-20250603-010

**提交人**: 黄芳  \|  **提交部门**: 研发1部  \|  **提交日期**: 2025-06-03
