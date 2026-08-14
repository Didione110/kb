# OA对接诺诺发票接口蓝凌OA特性xml处理问题

> 知识条目 | 可被客服机器人引用

## 元信息

| 字段 | 值 |
|------|----|
| 知识ID | doc-10051ddea8 |
| 产品线 | 蓝凌OA |
| 产品系列 |  |
| 版本 |  |
| 模块 |  |
| 问题类型 |  |
| 解决方案类型 |  |
| 技术栈 |  |
| 技术关键词 |  |
| 问题关键字 |  |
| 分类路径 | 蓝凌OA / 数据接口问题 |

## 问题现象

OA对接诺诺发票接口蓝凌OA特性xml处理问题

## 问题原因

数据库处理过程中需要引入xml格式，以诺诺发票开票完成后回写代码举例

## 解决方案

SELECT @cnt\_clientcode = 1 , @cnt\_invoicecode = 1 , @Bigcnt = 1 ,
 @totCnt = @FPXml.value('count(java\[@class="java.beans.XMLDecoder"\]/object/void\[string ="fd\_3cd24ad452b3b2"\]/object\[@class="java.util.ArrayList"\]/void\[@method="add"\]\[1\]/object\[@class="java.util.HashMap"\]/void\[@method="put"\])' ,
 'INT') ,
 @BigtotCnt = @FPXml.value('count(java\[@class="java.beans.XMLDecoder"\]/object/void\[string ="fd\_3cd24ad452b3b2"\]/object\[@class="java.util.ArrayList"\]/void\[@method="add"\])' ,
 'INT')
 --定义大循环 5次 大循环判断客户 
 WHILE @Bigcnt \<= @BigtotCnt
 BEGIN
 --定义小循环 每个单子33次 小循环获取到客户编号的大小循环的坐标
 WHILE @cnt\_clientcode \<= @totCnt
 BEGIN
 SELECT @attValue = @FPXml.value('(/java\[@class="java.beans.XMLDecoder"\]/object/void\[string ="fd\_3cd24ad452b3b2"\]/object\[@class="java.util.ArrayList"\]/void\[@method="add"\]\[position()=sql:variable("@Bigcnt")\]/object\[@class="java.util.HashMap"\]/void\[position()=sql:variable("@cnt\_clientcode")\]/string)\[1\]' ,
 'VARCHAR(MAX)') ,
 @attValue\_next = @FPXml.value('(/java\[@class="java.beans.XMLDecoder"\]/object/void\[string ="fd\_3cd24ad452b3b2"\]/object\[@class="java.util.ArrayList"\]/void\[@method="add"\]\[position()=sql:variable("@Bigcnt")\]/object\[@class="java.util.HashMap"\]/void\[position()=sql:variable("@cnt\_clientcode")\]/string)\[2\]' ,
 'VARCHAR(MAX)')
 IF ( @attValue = 'fd\_3cd24b9e3e6704'
 AND @attValue\_next = @ClientCode
 ) --当走到客户编号的时候，记录当前客户值
 BEGIN
 SET @cnt\_clientcode\_end = @Bigcnt
 BREAK;
 END
 SELECT @cnt\_clientcode = @cnt\_clientcode \+ 1
 END 
 SET @cnt\_clientcode = 1 --客户小循环恢复初始化
```
--定义小循环 每个单子33次 小循环判断发票号

 WHILE @cnt_invoicecode <= @totCnt
 BEGIN 
 SELECT @attValue = @FPXml.value('(/java[@class="java.beans.XMLDecoder"]/object/void[string ="fd_3cd24ad452b3b2"]/object[@class="java.util.ArrayList"]/void[@method="add"][position()=sql:variable("@Bigcnt")]/object[@class="java.util.HashMap"]/void[position()=sql:variable("@cnt_invoicecode")]/string)[1]' ,
 'VARCHAR(MAX)') ,
 @attValue_next = @FPXml.value('(/java[@class="java.beans.XMLDecoder"]/object/void[string ="fd_3cd24ad452b3b2"]/object[@class="java.util.ArrayList"]/void[@method="add"][position()=sql:variable("@Bigcnt")]/object[@class="java.util.HashMap"]/void[position()=sql:variable("@cnt_invoicecode")]/string)[2]' ,
 'VARCHAR(MAX)')
 IF ( @attValue = 'fd_3cd24bcb385562'
 AND @Bigcnt = @cnt_clientcode_end
 )--当走到发票号的时候,且发票号不会空的时候,开始插入更新xml数据 AND @attValue_next = ''
 BEGIN
 -- PRINT '发票大循环位置: ' + CAST(@Bigcnt AS VARCHAR(MAX)) + ' 小循环位置：' + CAST(@cnt_invoicecode AS VARCHAR(MAX)) 
 -- PRINT 'fap 值: ' + @attValue + ' 值：' + @attValue_next

```

## 引用来源

- 来源类型: `doc`
- 来源链接: https://alidocs.dingtalk.com/i/nodes/G1DKw2zgV2gP63q3cqbOd3M7JB5r9YAn?utm_scene=team_space
- 知识库路径: `/蓝凌OA/数据接口问题/OA对接诺诺发票接口蓝凌OA特性xml处理问题`
