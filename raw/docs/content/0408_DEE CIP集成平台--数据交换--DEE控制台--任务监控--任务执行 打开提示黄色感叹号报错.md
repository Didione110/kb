<!-- META: {"nodeId": "r1R7q3QmWeXe3YkYCNym7pqP8xkXOEP2", "title": "DEE CIP集成平台--数据交换--DEE控制台--任务监控--任务执行 打开提示黄色感叹号报错", "docUrl": "https://alidocs.dingtalk.com/i/nodes/r1R7q3QmWeXe3YkYCNym7pqP8xkXOEP2?utm_scene=team_space", "path": "/致远OA/数据错误问题/DEE CIP集成平台--数据交换--DEE控制台--任务监控--任务执行 打开提示黄色感叹号报错", "fetchTime": "2026-08-14 00:00:10"} -->

## 问题现象

【DEE】CIP集成平台--数据交换--DEE控制台--任务监控--任务执行 打开提示黄色感叹号报错

## 问题原因

DEE的日志文件受损导致的

## 解决方案

## 8.0——8.0SP2LTS版本处理方式：

1、停止OA服务，windows系统了，打开任务管理器，排查一下OA进程是否释放，没释放掉人为"杀掉oa进程"
2、将A8\\base\\dee\\data下除了dee.mv.db或dee.h2.db外的，其他2个文件(dee.trace.db、dee.lock.db) 删除
3、删除A8\\base\\dee\\history下所有文件(没有history文件夹则不用管这个)
4、重启OA，连接上dee数据库
备注:集群OA的话每个节点需要做一次上面的操作

## 8.0以下版本：

由于8.0以下版本，dee任务的数据和执行记录同在一个数据库文件里面，所以处理步骤如下：
第一步：从A8的base/dee/drpHistory文件中取最新日期的备份dee任务drp文件，为避免最新日期的也受损了无法使用，就挨个日期往下测试，那天可以使用就使用那天的。

---

## 附加信息

**对应版本**: A8企业版

**对应模块**: dee数据引擎

**问题类型**: 数据错误问题

**解决方案类型**: 重启服务, 替换文件

**技术栈**: DEE

**问题关键字**: DEE任务监控

**单据编号**: FX-20241031-050

**提交人**: 李冲  \|  **提交部门**: 成功部创新组-停用  \|  **提交日期**: 2024-10-31
