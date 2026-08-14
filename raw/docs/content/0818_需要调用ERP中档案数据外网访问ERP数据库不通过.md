<!-- META: {"nodeId": "ydxXB52LJqYnqNbNiKg1oRRaJqjMp697", "title": "需要调用ERP中档案数据外网访问ERP数据库不通过", "docUrl": "https://alidocs.dingtalk.com/i/nodes/ydxXB52LJqYnqNbNiKg1oRRaJqjMp697?utm_scene=team_space", "path": "/蓝凌OA/数据接口问题/需要调用ERP中档案数据外网访问ERP数据库不通过", "fetchTime": "2026-08-14 00:05:38"} -->

## 问题现象

需要调用ERP中档案数据，但是外网访问ERP数据库一直不通过

## 问题原因

防火墙不允许调用数据库端口

## 解决方案

经与软件厂商沟通使用数据源要保证服务器之间能够互通即可，经与服务器厂家沟通两台服务器在同一子网内，随即更换为内网地址即可访问成功，随即在表单上经过配置即可直接调用ERP档案数据，注意配置过程尽量有熟悉数据库的同事协助，因为是直接对数据库表进行操作
