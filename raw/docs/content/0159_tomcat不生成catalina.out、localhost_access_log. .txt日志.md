<!-- META: {"nodeId": "R1zknDm0WREaD2O2h0p1N1xa8BQEx5rG", "title": "tomcat不生成catalina.out、localhost_access_log. .txt日志", "docUrl": "https://alidocs.dingtalk.com/i/nodes/R1zknDm0WREaD2O2h0p1N1xa8BQEx5rG?utm_scene=team_space", "path": "/自研/安装部署问题/tomcat不生成catalina.out、localhost_access_log. .txt日志", "fetchTime": "2026-08-13 23:56:54"} -->

## 问题现象

tomcat不生成catalina.out、localhost\_access\_log.\*.txt日志

## 问题原因

tomcat反复启动，会生成很多启动日志占用空间，这部分日志不会查看，客户再找项目日志时经常会找错，并占用空间。

## 解决方案

将/bin/catalina.sh 中的CATALINA\_OUT="\$CATALINA\_BASE"/logs/catalina.out修改为
if \[ -z "\$CATALINA\_OUT" \] ; then
 CATALINA\_OUT=/dev/null
fi
将/conf/server.xml 文件中的下面的语句注释调 \<-- --/\> 

---

## 附加信息

**对应版本**: 电商接口

**问题类型**: 安装部署问题

**解决方案类型**: 配置修改

**技术栈**: Tomcat

**问题关键字**: 日志缺失

**单据编号**: FX-20221230-057

**提交人**: 刘文豪  \|  **提交部门**: 产品开发部  \|  **提交日期**: 2022-12-30
