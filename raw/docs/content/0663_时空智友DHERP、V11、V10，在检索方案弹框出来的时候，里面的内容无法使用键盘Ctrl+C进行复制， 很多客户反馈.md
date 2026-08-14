<!-- META: {"nodeId": "dpYLaezmVNEeKkYkhPn16xwgWrMqPxX6", "title": "时空智友DHERP、V11、V10，在检索方案弹框出来的时候，里面的内容无法使用键盘Ctrl+C进行复制， 很多客户反馈过，不方便使用", "docUrl": "https://alidocs.dingtalk.com/i/nodes/dpYLaezmVNEeKkYkhPn16xwgWrMqPxX6?utm_scene=team_space", "path": "/时空/安装部署问题/时空智友DHERP、V11、V10，在检索方案弹框出来的时候，里面的内容无法使用键盘Ctrl+C进行复制， 很多客户反馈过，不方便使用", "fetchTime": "2026-08-14 00:03:28"} -->

## 问题现象

时空智友DHERP、V11、V10，在检索方案弹框出来的时候，里面的内容无法使用键盘Ctrl\+C进行复制，
很多客户反馈过，不方便使用

## 问题原因

标准模板里没有相关配置，检索方案的弹框无法进行设置

## 解决方案

找到tomcat\\webapps\\ROOT\\form\\html\\js\\selecthtmlDiv.js文件
var htmldataset1 = new SDataSet(\{
		"events" : \{
			"dsevent" : \{
				"ondblclick" : "uf\_dbclick()",
				"beforeopen" : "uf\_beforeopen()",
				"afteropen" : "uf\_afteropen()"
			\},
			"fieldevent" : \{\}
```
	},
	"dsid" : "htmldataset1",
	"props" : {
		"idrule" : "serialno"
	},
	"CaptionHeight" : "30"
});

```

htmldataset1.fields = \[ \];

htmldataset1.pageSize = dlgargs.param.select.pagesize;
var hasNav = htmldataset1.pageSize \> -1;
var htmlgrid1 = new HtmlGrid(\{
		nav\_toolbar : hasNav,
		nav\_toolbar\_pagesize : htmldataset1.pageSize,
		"bodyStyle" : "color:Black;background-color:White;",
		"gridid" : "htmlgrid1",
		"CrossInterval" : "1",
		"showCaption" : "False",
		"autoheight" : "Y",
		"tabindex" : "0",
		"fixedStyle" : "color:Black;",
		"class" : "HtmlGrid",
		"bind\_dataset" : "htmldataset1",
		"caption" : "",
		"id" : "htmlgrid1\_elm",
		"height" : "150",
		"width" : "150",
		"dataset" : "htmldataset1",
		"ShowLineNum" : "true",
		/*"CrossStyle": "color:#000000; background-color:#f0f0f0",*/
		"autowidth" : "Y",
		"enablecopy" : "true",
		"onclick" : "return form\_onclick(event)",
		Editable : "false",
		AutoAppend : "N"
	\});

增加了 "enablecopy" : "true", 这个属性后，刷新缓存重启即可生效

---

## 附加信息

**对应版本**: 时空智友

**对应模块**: 供应链管理系统

**问题类型**: 安装部署问题

**解决方案类型**: 代码修改

**技术栈**: Tomcat, JS, 前端配置

**问题关键字**: 复制失效

**单据编号**: FX-20251112-017

**提交人**: 汪松  \|  **提交部门**: 经理办  \|  **提交日期**: 2025-11-12
