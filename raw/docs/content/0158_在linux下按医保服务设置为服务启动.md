<!-- META: {"nodeId": "6LeBq413JA0w1YkYC3O0XmpPVDOnGvpb", "title": "在linux下按医保服务设置为服务启动", "docUrl": "https://alidocs.dingtalk.com/i/nodes/6LeBq413JA0w1YkYC3O0XmpPVDOnGvpb?utm_scene=team_space", "path": "/自研/安装部署问题/在linux下按医保服务设置为服务启动", "fetchTime": "2026-08-13 23:56:53"} -->

## 问题现象

在linux下按医保服务设置为服务启动

## 问题原因

在linux下按医保服务设置为服务启动

## 解决方案

-----linux 服务添加

--编辑医保服务内容
vi /lib/systemd/system/yinhaiv4\_1.service

加入以下内容

\[Unit\]
Description=YINHAIPlus\_v41
After=network.target

\[Service\]
WorkingDirectory=/opt/YINHAIPlus\_78
ExecStart=/usr/local/bin/dotnet /opt/YINHAIPlus\_78/YINHAIPlus.dll
Restart=always
RestartSec=5

\[Install\]
WantedBy=multi-user.target

--开机启动
systemctl enable yinhaiv4\_1

--启动
systemctl start yinhaiv4\_1

---

## 附加信息

**对应版本**: 医保接口

**问题类型**: 安装部署问题

**解决方案类型**: 配置修改

**技术栈**: Linux, C# (.NET)

**问题关键字**: 医保服务

**单据编号**: FX-20240326-050

**提交人**: 黄振兴  \|  **提交部门**: 需求&KA部  \|  **提交日期**: 2024-03-26
