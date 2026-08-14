<!-- META: {"nodeId": "2Amq4vjg8920o545UmAbvzKzW3kdP0wQ", "title": "ORACLE备份库导入到新环境后，查询报表效率大幅降低", "docUrl": "https://alidocs.dingtalk.com/i/nodes/2Amq4vjg8920o545UmAbvzKzW3kdP0wQ?utm_scene=team_space", "path": "/时空/效率问题/ORACLE备份库导入到新环境后，查询报表效率大幅降低", "fetchTime": "2026-08-14 00:02:20"} -->

## 问题现象

ORACLE备份库导入到新环境后，查询报表效率大幅降低

## 问题原因

如果统计信息不准确或过时，优化器可能会选择不理想的执行计划（未命中索引），导致查询性能下降。

## 解决方案

执行收集统计信息过程，优化新能
begin
 dbms\_stats.gather\_table\_stats(ownname =\> 'RACE',
 tabname =\> 'K\_YINHAI\_MESSAGE',
 estimate\_percent =\> DBMS\_STATS.AUTO\_SAMPLE\_SIZE,
 method\_opt =\> 'FOR ALL COLUMNS SIZE AUTO');
end; 
参数说明：
ownname:要分析表的拥有者
tabname:要分析的表名.
partname:分区的名字,只对分区表或分区索引有用.
estimate\_percent:采样行的百分比,取值范围\[0.000001,100\],null为全部分析,不采样. 常量:DBMS\_STATS.AUTO\_SAMPLE\_SIZE是默认值,由oracle决定最佳取采样值.
method\_opt:决定histograms信息是怎样被统计的.method\_opt的取值如下(默认值为FOR ALL COLUMNS SIZE AUTO):

---

## 附加信息

**对应版本**: 时空智友

**对应模块**: 供应链管理系统

**问题类型**: 效率问题

**解决方案类型**: 数据库操作

**技术栈**: Oracle

**问题关键字**: 性能下降

**单据编号**: FX-20240506-019

**提交人**: 王棒  \|  **提交部门**: 实施1部  \|  **提交日期**: 2024-05-06
