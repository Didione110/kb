# 明细表通过公式定义器不生效

> 知识条目 | 可被客服机器人引用

## 元信息

| 字段 | 值 |
|------|----|
| 知识ID | doc-a7a64f099c |
| 产品线 | 蓝凌OA |
| 产品系列 |  |
| 版本 |  |
| 模块 |  |
| 问题类型 |  |
| 解决方案类型 |  |
| 技术栈 |  |
| 技术关键词 |  |
| 问题关键字 |  |
| 分类路径 | 蓝凌OA / 应用操作 |

## 问题现象

明细表通过公式定义器不生效

## 问题原因

低代码语法不一样，明细表计算是list算法，产品未考虑，需要单独增加JS

## 解决方案

增加JS片段，并对计算控件进行动态监控，然后循环计算后进行赋值 [xform:editShow](xform:editShow)

\</xform:editShow\>

## 引用来源

- 来源类型: `doc`
- 来源链接: https://alidocs.dingtalk.com/i/nodes/r1R7q3QmWeXe3YkYCNy0Nxvz8xkXOEP2?utm_scene=team_space
- 知识库路径: `/蓝凌OA/应用操作/明细表通过公式定义器不生效`
