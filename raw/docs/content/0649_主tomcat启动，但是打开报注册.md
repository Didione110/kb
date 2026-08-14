<!-- META: {"nodeId": "AR4GpnMqJzAGeZqZckeAaKgwVKe0xjE3", "title": "主tomcat启动，但是打开报注册", "docUrl": "https://alidocs.dingtalk.com/i/nodes/AR4GpnMqJzAGeZqZckeAaKgwVKe0xjE3?utm_scene=team_space", "path": "/时空/安装部署问题/主tomcat启动，但是打开报注册", "fetchTime": "2026-08-14 00:03:18"} -->

## 问题现象

主tomcat启动，但是打开报注册

## 问题原因

主tomcat打开异常，1009无法联通的情况提示注册

## 解决方案

加入linux的守护进程，监控异常时重启，以下是shell程序内容:

# !/bin/sh

declare -a pathName
pathName\[0\]=TomcatV10

declare -a ports
ports\[0\]=8088

for i in \{0..0\}; do
	# tomcat启动程序(这里注意tomcat实际安装的路径) 
	StartTomcat=/opt/${pathName[$
i\]\}/bin/startup.sh
```
# 定义要监控的页面地址
WebUrl=http://localhost:${ports[$i]}
echo $WebUrl
# 解析页面时间设定
TIMETRANSFER=15

# 缓存地址如果不需要可以不配置
#TomcatCache=/opt/${pathName[$i]}/work/Catalina
 
# 获取tomcat进程ID /opt/TomcatV101
TomcatID=$(ps -ef |grep -w ${pathName[$i]}|grep -v 'grep\|cronolog'|awk '{print $2}')

echo $TomcatID
# 日志输出 
TomcatMonitorLog=/opt/${pathName[$i]}/logs/Monitor1009_1009_$(date +%Y%m%d).log

Monitor()
{
  echo "[info]开始监控tomcat注册服务...[$(date +'%F %H:%M:%S')]"
	LicensePortCount=`netstat -an | grep ":1009" | awk '$1 == "tcp" && $NF == "LISTEN" {print $0}' | wc -l`
	if [ $LicensePortCount -eq 0 ];then
		 echo "[error]注册服务端口异常，错误日志已输出到$GetPageInfo"
		 echo "[error]注册服务端口异常，开始重启tomcat"
		 echo "[error]注册服务端口异常，重启tomcat"
		kill -9 $TomcatID  # 杀掉原tomcat进程
		sleep 30s
		#rm -rf $TomcatCache # 清理tomcat缓存
		$StartTomcat
		 
	else
		 echo "[info]注册服务端口测试完成...[$(date +'%F %H:%M:%S')]"
	fi
   
	echo "[info]注册服务监控测试完成tomcat...[$(date +'%F %H:%M:%S')]"
	
	echo "------------------------------"
}
Monitor>>$TomcatMonitorLog

```

done

---

## 附加信息

**对应版本**: 时空智友

**对应模块**: RM模块

**问题类型**: 安装部署问题

**解决方案类型**: 重启服务

**技术栈**: Tomcat, Linux, Shell

**问题关键字**: 注册失败

**单据编号**: FX-20250220-014

**提交人**: 黄振兴  \|  **提交部门**: 需求&KA部  \|  **提交日期**: 2025-02-20
