# 流程结束但要删除附件

> 知识条目 | 可被客服机器人引用

## 元信息

| 字段 | 值 |
|------|----|
| 知识ID | doc-cb3e89b4c7 |
| 产品线 | 蓝凌OA |
| 产品系列 |  |
| 版本 |  |
| 模块 |  |
| 问题类型 |  |
| 解决方案类型 |  |
| 技术栈 |  |
| 技术关键词 |  |
| 问题关键字 |  |
| 分类路径 | 蓝凌OA / 实施问题 |

## 问题现象

流程结束但要删除附件

## 问题原因

数据库无法处理，前台存储的是XML文件

## 解决方案

先将流程视图从view变成edit，再按F12再控制台输入Com\_Submit(document.kmReviewMainForm, 'update')再进行操作，注意：此方法不适用于低代码平台

## 引用来源

- 来源类型: `doc`
- 来源链接: https://alidocs.dingtalk.com/i/nodes/G1DKw2zgV2gP63q3cqbO9eA9JB5r9YAn?utm_scene=team_space
- 知识库路径: `/蓝凌OA/实施问题/流程结束但要删除附件`
