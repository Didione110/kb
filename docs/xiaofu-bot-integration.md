# 小福 · 知识库问答机器人接入说明

## 一、机器人信息

| 项目 | 值 |
|------|-----|
| 机器人名称 | 小福 |
| robotCode | `dingdeesmx44yfklx5uh` |
| botOpenDingTalkId | `DagsQRmO3ORQzjpUaTLchii9HSMii6KtPEC` |
| App ID | `4ea2141e-dd77-4183-a3d3-bb0cc37392b3` |
| AgentId | `4862965822` |
| 服务会话（单聊） | `cidC1/t2j1EX+Xr8i40h+jG7Hb/jjJSz3G3oM3R3sOCOJw=`（王旭峰） |
| 服务会话（群聊） | `cidLfO5CVsV7joZMTocGowUSA==`（新火沟通） |
| 服务用户 | 王旭峰 (userId: `432315419731`) |

## 二、工作方式（双模式）

**模式一 · 单聊自动应答**：用户直接与小福私聊发问题 → 本地服务每 15 秒轮询单聊新消息 → 检索知识库 → 小福自动回复。

**模式二 · 群聊 @触发**：用户在群内 `@小福 问题` → 服务拉取群消息识别 @小福 → 检索知识库 → 小福在群内回复并 @提问者、引用原消息。

```
用户(钉钉) ──私聊/群@──▶ 小福
                          │
                    轮询(list / list-all)
                          ▼
              本地服务 bot_xiaofu.py
                          │
                   query.py 检索知识库
                          ▼
              小福回复(dm: batch_send / group: send_robot_group_message)
                          │
                          ▼
                   用户收到答案
```

## 三、服务管理

```bash
# 启动（常驻，单聊+群聊，每 15 秒轮询）
cd kb/scripts
setsid nohup python3 bot_xiaofu.py --mode both --interval 15 > ../knowledge/bot_xiaofu.log 2>&1 < /dev/null &

# 仅单聊 / 仅群聊
python3 bot_xiaofu.py --mode dm
python3 bot_xiaofu.py --mode group

# 单次检查（调试）
python3 bot_xiaofu.py --once -v

# 只读演练（不发送）
python3 bot_xiaofu.py --once --dry-run -v

# 停止
pkill -f "bot_xiaofu.py"

# 查看日志
tail -f ../knowledge/bot_xiaofu.log
```

## 四、应答逻辑

1. **单聊**：所有用户文本消息视为提问（问候语除外，回复引导）。
2. **群聊**：仅响应消息中包含 `@小福` 的文本，其他消息静默跳过（不干扰群内其他机器人如罗丝钉/AI小钉的对话）。
3. **知识库命中** → 返回 Top-3 匹配（标题、知识ID、产品线/版本/模块、问题现象、解决方案摘要、引用来源）。
4. **未命中** → 提示换关键词或转人工，不编造答案。

去重机制：已处理消息 ID 记录在 `knowledge/bot_state.json`，同一消息不会重复回复（含历史消息）。

## 五、检索质量

- 评分优化：产品线(×8)/版本(×6)/模块(×3) 精确匹配权重最高，标题/问题现象次之。
- 已验证（真实运行）：「时空智友 数据库连接」「用友U8 销售发票保存报错」「时空智友数字千位符」等均正确命中。

## 六、注意事项

- 服务依赖 dws 登录凭证（`kb/.dws-home`、`kb/.dws-config`），凭证过期需重新 `dws auth login`。
- 服务需保持运行；服务器重启后需重新启动（可配置 systemd/cron 守护）。
- 群聊模式仅响应 @小福，避免与其他机器人冲突。
- 每次知识库同步（`sync_from_dingtalk.sh`）后无需重启服务，检索实时读取最新索引。
