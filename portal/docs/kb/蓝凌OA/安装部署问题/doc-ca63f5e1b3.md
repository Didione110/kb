---
{
  "title": "全文检索服务安装完成索引无法新建生成",
  "kbId": "doc-ca63f5e1b3",
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
    "安装部署问题"
  ],
  "submitter": "",
  "department": "",
  "date": "",
  "sourceType": "doc",
  "sourceUrl": "https://alidocs.dingtalk.com/i/nodes/QOG9lyrgJPEzvGyGhv5ZjyDj8zN67Mw4?utm_scene=team_space",
  "sourcePath": "/蓝凌OA/安装部署问题/全文检索服务安装完成索引无法新建生成",
  "status": "active",
  "updatedAt": "",
  "outDir": "蓝凌OA/安装部署问题"
}
---

# 全文检索服务安装完成索引无法新建生成

> 知识条目 · 可被客服机器人引用

## 元信息

| 字段 | 值 |
|------|----|
| 知识ID | `doc-ca63f5e1b3` |
| 产品线 | 蓝凌OA |
| 产品系列 | - |
| 版本 | - |
| 模块 | - |
| 问题类型 | - |
| 解决方案类型 |  |
| 技术栈 |  |
| 技术关键词 |  |
| 问题关键字 |  |
| 分类路径 | 蓝凌OA / 安装部署问题 |
| 提交人 | - |
| 提交部门 | - |
| 提交日期 | - |
| 状态 | active |

## 问题现象

全文检索服务安装完成索引无法新建生成

## 问题原因

如果不设置全文检索默认密码的情况下，需要更改配置文件的elasticsearch.yml 文件中的 xpack.security.enabled: true 是开启状态，关闭它。

## 解决方案

需要更改配置文件的elasticsearch.yml 文件中的 xpack.security.enabled: true 是开启状态，关闭它。

## 引用来源

- 来源类型: `doc`
- 来源链接: https://alidocs.dingtalk.com/i/nodes/QOG9lyrgJPEzvGyGhv5ZjyDj8zN67Mw4?utm_scene=team_space
- 知识库路径: `/蓝凌OA/安装部署问题/全文检索服务安装完成索引无法新建生成`
