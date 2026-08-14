<!-- META: {"nodeId": "oP0MALyR8kmlqNaNhYX0ML7QV3bzYmDO", "title": "系统每隔十分钟无操作会自动下线修改Tomcat参数不生效", "docUrl": "https://alidocs.dingtalk.com/i/nodes/oP0MALyR8kmlqNaNhYX0ML7QV3bzYmDO?utm_scene=team_space", "path": "/蓝凌OA/应用操作/系统每隔十分钟无操作会自动下线修改Tomcat参数不生效", "fetchTime": "2026-08-14 00:06:04"} -->

## 问题现象

系统每隔十分钟无操作会自动下线，根据手册修改Tomcat参数重启服务后不生效

## 问题原因

无操作自动下线不调用Tomcat中的参数，需要在admin.do中、多服务器配置中调整。

## 解决方案

开启多服务器配置，调整对应有效期即可。
