<!-- META: {"nodeId": "YMyQA2dXW7XeBZGZCZmb9QLMVzlwrZgb", "title": "使用delphi制作一个http服务", "docUrl": "https://alidocs.dingtalk.com/i/nodes/YMyQA2dXW7XeBZGZCZmb9QLMVzlwrZgb?utm_scene=team_space", "path": "/自研/数据接口问题/使用delphi制作一个http服务", "fetchTime": "2026-08-13 23:56:04"} -->

## 问题现象

使用delphi制作一个http服务

## 问题原因

使用delphi制作一个http服务

## 解决方案

使用IdHTTPServer控件提供服务，入参使用CreatePostStream事件获取
procedure TFormmain.IdHTTPServer1CreatePostStream(ASender: TIdPeerThread;
 var VPostStream: TStream);
begin
 VPostStream := TMemoryStream.Create;
end;

---

## 附加信息

**对应版本**: 医保接口

**问题类型**: 数据接口问题

**解决方案类型**: 代码修改

**技术栈**: REST API

**技术关键词**: 接口

**问题关键字**: Delphi HTTP服务

**单据编号**: FX-20241202-002

**提交人**: 黄芳  \|  **提交部门**: 研发1部  \|  **提交日期**: 2024-12-02
