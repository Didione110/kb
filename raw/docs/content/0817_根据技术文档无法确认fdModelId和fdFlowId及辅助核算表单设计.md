<!-- META: {"nodeId": "EpGBa2Lm8aMGRNgNcw76qOZ48gN7R35y", "title": "根据技术文档无法确认fdModelId和fdFlowId及辅助核算表单设计", "docUrl": "https://alidocs.dingtalk.com/i/nodes/EpGBa2Lm8aMGRNgNcw76qOZ48gN7R35y?utm_scene=team_space", "path": "/蓝凌OA/数据接口问题/根据技术文档无法确认fdModelId和fdFlowId及辅助核算表单设计", "fetchTime": "2026-08-14 00:05:37"} -->

## 问题现象

1、根据技术文档无法确认fdModelId、fdFlowId；
2、凭证中辅助核算在科目下级的表单无法设计

## 问题原因

1、fdModelId、fdFlowId文档没有明显说明；
2、明细表不支持嵌套明细表

## 解决方案

1、fdModelId从"表单设计地址栏获取fdAppModelId"、fdFlowId从"流程配置界面获取fdid"；
2、理论上低代码公式写自定义代码可实现（实践中代码未生效），后采用中台程序自动补全。
