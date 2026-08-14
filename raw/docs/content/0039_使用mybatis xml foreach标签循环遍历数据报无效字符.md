<!-- META: {"nodeId": "20eMKjyp81D3BY5YFe0gr5lzJxAZB1Gv", "title": "使用mybatis xml foreach标签循环遍历数据报无效字符", "docUrl": "https://alidocs.dingtalk.com/i/nodes/20eMKjyp81D3BY5YFe0gr5lzJxAZB1Gv?utm_scene=team_space", "path": "/自研/数据错误问题/使用mybatis xml foreach标签循环遍历数据报无效字符", "fetchTime": "2026-08-13 23:55:22"} -->

## 问题现象

使用mybatis xml 标签循环遍历数据报：无效字符

## 问题原因

在insert/select/delete中close参数带了‘;’导致报错

## 解决方案

insert/delete close带';'.select close不带
例2 ：
delete K\_YN\_BATCHCOUPON where SCHEMEID in
 
            #\{d.schemeId\}
        
            insert into K\_YN\_BATCHCOUPON
            (SCHEMEID,SCHEMENAME,CREATETIME,EFFECTSTARTTIME,EFFECTENDTIME,DISCOUNT,THRESHOLD,DESCRIPTION)
            values
            (#\{db.schemeId\},#\{db.schemeName\},#\{db.createTime\},#\{db.effectStartTime\},#\{db.effectEndTime\},#\{db.discount\},#\{db.threshold\},#\{db.description\});         

例2：

        select \* from test001 where couponNo in
        
            '\$\{d\}'              

---

## 附加信息

**对应版本**: 电商接口

**问题类型**: 数据错误问题

**解决方案类型**: SQL脚本

**技术栈**: Oracle, Java

**技术关键词**: 凭证

**问题关键字**: 无效字符

**单据编号**: FX-20240604-006

**提交人**: 肖博伦  \|  **提交部门**: 研发1部  \|  **提交日期**: 2024-06-04
