---
{
  "title": "蓝凌没有像致远一样的分管领导角色直接选择",
  "kbId": "doc-f54d8d1fbd",
  "productLine": "蓝凌OA",
  "productSeries": "",
  "version": "",
  "module": "",
  "problemType": "",
  "solutionTypes": [],
  "techStack": [],
  "techKeywords": [],
  "keywords": [],
  "category": [
    "蓝凌OA",
    "实施问题"
  ],
  "submitter": "",
  "department": "",
  "date": "",
  "sourceType": "doc",
  "sourceUrl": "https://alidocs.dingtalk.com/i/nodes/r1R7q3QmWeXe3YkYCNy0a3yX8xkXOEP2?utm_scene=team_space",
  "sourcePath": "/蓝凌OA/实施问题/蓝凌没有像致远一样的分管领导角色直接选择",
  "status": "active",
  "updatedAt": "",
  "outDir": "蓝凌OA/实施问题"
}
---

# 蓝凌没有像致远一样的分管领导角色直接选择

> 知识条目 · 可被客服机器人引用

## 元信息

| 字段 | 值 |
|------|----|
| 知识ID | `doc-f54d8d1fbd` |
| 产品线 | 蓝凌OA |
| 产品系列 | - |
| 版本 | - |
| 模块 | - |
| 问题类型 | - |
| 解决方案类型 |  |
| 技术栈 |  |
| 技术关键词 |  |
| 问题关键字 |  |
| 分类路径 | 蓝凌OA / 实施问题 |
| 提交人 | - |
| 提交部门 | - |
| 提交日期 | - |
| 状态 | active |

## 问题现象

蓝凌没有像致远一样的分管领导角色直接选择

## 问题原因

实际场景可能需要根据控件匹配分管领导，蓝凌预制只能通过提交人来获取，或需要购买单独的单位管理模块来实现，而单位管理是配合公文管理来实现的所以在实施中极为不方便

## 解决方案

在没有单位管理模块的情况下，只能通过公式定义器来写函数，如：$组织架构.获取n级直线领导$
($提交部门$
,2,"管理员")，获取选择的地址本/组织架构对象的n级直线领导（从对象开始由下往上算的领导），排除掉特定用户后，返回领导列表，且领导不重复出现。第一个参数为组织架构对象，可为地址本；第二个为第n级领导，数字；第三个为不参与审批的人员列表。

## 引用来源

- 来源类型: `doc`
- 来源链接: https://alidocs.dingtalk.com/i/nodes/r1R7q3QmWeXe3YkYCNy0a3yX8xkXOEP2?utm_scene=team_space
- 知识库路径: `/蓝凌OA/实施问题/蓝凌没有像致远一样的分管领导角色直接选择`
