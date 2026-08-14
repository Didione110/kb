<!-- META: {"nodeId": "93NwLYZXWyAnqw5wcNM3lOBRWkyEqBQm", "title": "U8 客户设置系统管理admin密码后忘记了，无法登陆系统管理", "docUrl": "https://alidocs.dingtalk.com/i/nodes/93NwLYZXWyAnqw5wcNM3lOBRWkyEqBQm?utm_scene=team_space", "path": "/用友/软件无法使用/U8 客户设置系统管理admin密码后忘记了，无法登陆系统管理", "fetchTime": "2026-08-14 00:04:14"} -->

## 问题现象

U8 客户设置系统管理admin密码后忘记了，无法登陆系统管理

## 问题原因

忘记密码

## 解决方案

找一个知道密码的用户将这个用户的cpassword值复制到admin用户相应字段中即可
（select \* from UA\_User 查所有用户信息，已知用户003的密码为123456，所以复制查出结果中003的cpassword：fEqNCco3Yq9h5ZUglD3CZJT4lBs即可；
 update UA\_User set cpassword= fEqNCco3Yq9h5ZUglD3CZJT4lBs=? where cuser\_id= admin ，将用户003的cpassword值设置到admin用户中），此时admin的密码与003用户一致为123456，
 登录系统管理admin用户勾选修改密码为空，即可将admin密码置空

---

## 附加信息

**对应版本**: U8

**对应模块**: 财务会计

**问题类型**: 软件无法使用

**解决方案类型**: 数据库操作

**技术栈**: SQL Server

**技术关键词**: 加密, 权限

**问题关键字**: 密码遗忘

**单据编号**: FX-20221201-001

**提交人**: 汪心文  \|  **提交部门**: 客户成功部  \|  **提交日期**: 2022-12-01
