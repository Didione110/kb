<!-- META: {"nodeId": "N7dx2rn0JbjY0oMoFZp111rlJMGjLRb3", "title": "Mybatis+Oracle批量插入数据，存在即更新语句", "docUrl": "https://alidocs.dingtalk.com/i/nodes/N7dx2rn0JbjY0oMoFZp111rlJMGjLRb3?utm_scene=team_space", "path": "/自研/效率问题/Mybatis+Oracle批量插入数据，存在即更新语句", "fetchTime": "2026-08-13 23:56:16"} -->

## 问题现象

Mybatis\+Oracle批量插入数据，存在即更新语句

## 问题原因

Mybatis\+Oracle批量插入数据，存在即更新语句

## 解决方案

示例：
MERGE into kq\_erp\_u8c\_log t1
 USING (
 
        select
        #\{item.pkName\} as pkName
        ,#\{item.code\} as pkName
        ,#\{item.ResultMsg\} as pkName
        ,#\{item.RequestBody\} as pkName
        ,#\{item.taskName\} as pkName
        ,#\{item.lastTime\} as pkName
        ,#\{item.remark1\} as pkName
        ,#\{item.remark2\} as pkName
        ,#\{item.remark3\} as pkName
        ,#\{item.remark4\} as pkName
        from dual
        ) t2
        ON (t1.pkName=t2.pkName)
        when matched then
        update set t1.code=#\{code\},t1.ResultMsg=#\{ResultMsg\},
        t1.RequestBody=#\{RequestBody\},t1.lastTime=#\{lastTime\},
        t1.taskName=#\{taskName\},t1.remark1=#\{remark1\},t1.remark2=#\{remark2\}
        ,t1.remark3=#\{remark3\},t1.remark4=#\{remark4\}
        where t1.pkName=t2.pkName
        when not matched then
        insert (
        pkName,
        code,
        ResultMsg,
        RequestBody,
        taskName,
        lastTime,
        remark1,
        remark2,
        remark3,
        remark4) values (
        #\{t2.pkName\},
        #\{t2.code\},
        #\{t2.ResultMsg\},
        #\{t2.RequestBody\},
        #\{t2.taskName\},
        #\{t2.lastTime\},
        #t2.\{remark1\},
        #\{t2.remark2\},
        #\{t2.remark3\},
        #\{t2.remark4\}
        )

---

## 附加信息

**对应版本**: 供应商平台

**问题类型**: 效率问题

**解决方案类型**: SQL脚本, 数据库操作

**技术栈**: Oracle, Java

**技术关键词**: 接口

**问题关键字**: Mybatis Oracle 批量 插入 更新

**单据编号**: FX-20240403-024

**提交人**: 程时红  \|  **提交部门**: 研发2部  \|  **提交日期**: 2024-04-03
