<!-- META: {"nodeId": "gwva2dxOW4jYe3B3FkwNBmbyJbkz3BRL", "title": "ksoa医保接口dll，setup.ini 文件system下增加 iswh=0，1就是要调用武汉医保的各种校验保存，0 是不调用", "docUrl": "https://alidocs.dingtalk.com/i/nodes/gwva2dxOW4jYe3B3FkwNBmbyJbkz3BRL?utm_scene=team_space", "path": "/自研/数据接口问题/ksoa医保接口dll，setup.ini 文件system下增加 iswh=0，1就是要调用武汉医保的各种校验保存，0 是不调用", "fetchTime": "2026-08-13 23:55:49"} -->

## 问题现象

ksoa医保接口dll，setup.ini 文件 \[system\] 下增加 iswh=0，1就是要调用武汉医保的各种校验保存，0 是不调用；
setup.ini 文件 \[system\] 下增加regerName=regerCertno=，处方读取顾客社保卡；

## 问题原因

ksoa医保按要求更新

## 解决方案

修改配置文件，setup.ini 文件 \[system\] 下增加配置参数

---

## 附加信息

**对应版本**: 医保接口

**问题类型**: 数据接口问题

**解决方案类型**: 配置修改

**技术栈**: WebService, DEE, EAI

**技术关键词**: 接口, 打印, 加密

**问题关键字**: 医保校验

**单据编号**: FX-20250603-008

**提交人**: 黄芳  \|  **提交部门**: 研发1部  \|  **提交日期**: 2025-06-03
