<!-- META: {"nodeId": "20eMKjyp81D3BY5YFe0ganEGJxAZB1Gv", "title": "早期mssql可以用存储过程魔改使用动态t-sql查询 现在dherp之后数据库是oracle，前期有些方法不支持了 改用前端js进行处理", "docUrl": "https://alidocs.dingtalk.com/i/nodes/20eMKjyp81D3BY5YFe0ganEGJxAZB1Gv?utm_scene=team_space", "path": "/时空/实施问题/早期mssql可以用存储过程魔改使用动态t-sql查询 现在dherp之后数据库是oracle，前期有些方法不支持了 改用前端js进行处理", "fetchTime": "2026-08-14 00:03:11"} -->

## 问题现象

早期mssql可以用存储过程魔改使用动态t-sql查询
现在dherp之后数据库是oracle，前期有些方法不支持了
改用前端js进行处理

## 问题原因

客户的需求，有些查询是需要动态列，利用js的特性，进行循环拼接处理，时空智友的SQL宏支持js对象传入，进行拆解分析

## 解决方案

以js参数为例
async function uf\_query()\{
	dataset1.openEmpty();
	var params = \{\};
 	var month\_list = uf\_getMonthsBetweenDates(textbox9.getValue(), textbox8.getValue()); //获取月份列表
 	//获取起始日期
 	params.StartDate = textbox9.getValue().substring(0, 8) \+ "01";
 	params.EndDate = uf\_getLastDayOfMonth(textbox8.getValue().substring(0, 7));
```
for (var i = 0; i < month_list.length; i++) {
	await dataset1.addField(month_list[i],month_list[i],"RealNum","20"); 
	await dataset1.field(month_list[i]).setAlignment("center");

```

// 	 await dataset1.field(month\_list\[i\]).setSummed("true"); 
 	\}
 	await dataset1.update();
 	await dataset1.updateGrid();
 	params.month\_list = JSON.stringify(month\_list); 
 	await dataset1.open("uf\_sql\_query", "sql", params); 
\}
对应的查询SQl如下，各位同仁可以参考
select b.k\_areacode,b.k\_province,b.k\_city,b.k\_area,b.businesscode,b.businessname,sum(d.num) as Total\_num 
#\_\_sql \+= ", sum(d.num) / " \+ JSON.parse(month\_list).length \+" as Avg\_Num" 
#for (var i = 0 ; i \< JSON.parse(month\_list).length ; i\+\+) \{ 
	#\_\_sql \+= " , SUM(CASE WHEN a.dates like '" \+ JSON.parse(month\_list)\[i\] \+"%' THEN d.num ELSE 0 END) AS "" \+ JSON.parse(month\_list)\[i\] \+ """ 
#\}
from SaleOutmt a 
join BusinessDoc b on a.clientid = b.businessid and a.entid = b.entid 
join ClientDoc c on c.clientid = a.clientid and c.entid = a.entid 
join SaleOutDt d on d.billno = a.billno and d.entid = a.entid 
where a.ruleid in ('4szcn61oa8b0tz79','3cc08h3z7cnkrv2q')
and a.dates \>= :StartDate
and a.dates \<= :EndDate

group by b.k\_areacode,b.k\_province,b.k\_city,b.k\_area,b.businesscode,b.businessname

---

## 附加信息

**对应版本**: 时空智友

**对应模块**: 供应链管理系统

**问题类型**: 实施问题

**解决方案类型**: SQL脚本

**技术栈**: Oracle, SQL Server, JS

**技术关键词**: 接口

**问题关键字**: Oracle迁移

**单据编号**: FX-20250303-002

**提交人**: 汪松  \|  **提交部门**: 经理办  \|  **提交日期**: 2025-03-03
