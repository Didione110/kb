<!-- META: {"nodeId": "a9E05BDRVQr29yxytDz12xvwJ63zgkYA", "title": "导出大量数据excel效率太慢", "docUrl": "https://alidocs.dingtalk.com/i/nodes/a9E05BDRVQr29yxytDz12xvwJ63zgkYA?utm_scene=team_space", "path": "/时空/应用操作/导出大量数据excel效率太慢", "fetchTime": "2026-08-14 00:02:35"} -->

## 问题现象

导出大量数据excel效率太慢

## 问题原因

客户电脑配置较低，一次性导出几十万条数据需要等待很长时间

## 解决方案

使用以下函数导出CSV文件，导出后需要另存为excel文件
FormUtil.exportCsv(openparam,openmode,filename ,variables,\{charset:"gb2312",isExpCNFildName:"Y"\});
/\*\*
- openparam sql语句
- openmode 打开模式：'sql'
- filename 文件名
- variables sql参数
- /

---

## 附加信息

**对应版本**: 时空智友

**对应模块**: RM模块

**问题类型**: 应用操作

**解决方案类型**: 数据库操作

**技术栈**: JavaScript

**技术关键词**: 接口

**问题关键字**: 导出慢

**单据编号**: FX-20240901-006

**提交人**: 蒋志斌  \|  **提交部门**: 实施2部  \|  **提交日期**: 2024-09-01
