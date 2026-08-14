#!/usr/bin/env python3
"""
小福 · 客服知识库问答机器人（单聊 + 群聊 @触发）
==================================================
模式一（单聊）: 用户直接与小福私聊 → 全部消息视为提问
模式二（群聊）: 群成员 @小福 提问 → 小福在群内回复

数据源:
  - 知识库: kb/knowledge (2485 条知识条目)
  - 机器人: 小福 (robotCode: dingdeesmx44yfklx5uh)
  - 单聊会话: cidC1/t2j1EX+Xr8i40h+jG7Hb/jjJSz3G3oM3R3sOCOJw= (王旭峰)
  - 群聊会话: cidLfO5CVsV7joZMTocGowUSA== (新火沟通)

用法:
  python3 bot_xiaofu.py                    # 常驻：单聊 + 群聊
  python3 bot_xiaofu.py --mode chat        # 仅群聊模式
  python3 bot_xiaofu.py --mode dm          # 仅单聊模式
  python3 bot_xiaofu.py --once             # 单次检查
  python3 bot_xiaofu.py --dry-run          # 只读模式
"""
import argparse, json, os, re, subprocess, sys, time

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
QUERY_PY = os.path.join(ROOT, "scripts", "query.py")
STATE_FILE = os.path.join(ROOT, "knowledge", "bot_state.json")

ENV = dict(os.environ)
ENV["HOME"] = "/home/admin/deepseek-harness/DSH-workspace/.dws-home"
ENV["DWS_CONFIG_DIR"] = "/home/admin/deepseek-harness/DSH-workspace/.dws-config"

ROBOT_CODE = "dingdeesmx44yfklx5uh"
ROBOT_NAME = "小福"
ROBOT_OPEN_DINGTALK_ID = "DagsQRmO3ORR2iivJm7kvk8JknU8KDkuIb"   # 群内小福的 openDingTalkId
DM_CHAT_ID = "cidC1/t2j1EX+Xr8i40h+jG7Hb/jjJSz3G3oM3R3sOCOJw="  # 与小福的单聊
# 小福监听的群聊（可多个）：会话ID -> 群名
GROUP_CHAT_IDS = {
    "cidLfO5CVsV7joZMTocGowUSA==": "新火沟通群",
    "cidgAVDbrDwR4Q/mV9wzlP7XA==": "客服机器人测试群",
}
MY_USER_ID = "432315419731"                                        # 王旭峰

def dws(*args, timeout=60):
    r = subprocess.run(["dws", *args, "--format", "json"], capture_output=True,
                       text=True, env=ENV, timeout=timeout)
    try:
        return json.loads(r.stdout)
    except Exception:
        return {"raw": r.stdout[:500], "err": r.stderr[:500]}

def load_state():
    if os.path.exists(STATE_FILE):
        try:
            return json.load(open(STATE_FILE))
        except Exception:
            return {}
    return {}

def save_state(s):
    with open(STATE_FILE, "w") as f:
        json.dump(s, f, ensure_ascii=False, indent=1)

# ---------------- 消息拉取 ----------------
def fetch_dm_messages(limit=30):
    """拉取与小福的单聊最近消息"""
    d = dws("chat", "message", "list-all", "--limit", str(limit))
    convs = d.get("result", {}).get("conversationMessagesList") or []
    for c in convs:
        if c.get("openConversationId") == DM_CHAT_ID:
            return c.get("messages") or []
    return []

def fetch_group_messages(limit=30):
    """拉取所有监听群聊的最近消息"""
    out = []
    for gid in GROUP_CHAT_IDS:
        d = dws("chat", "message", "list", "--group", gid, "--limit", str(limit))
        res = d.get("result", d)
        items = res.get("list") or res.get("messages") or res.get("items") or res.get("value") or []
        for m in items:
            if isinstance(m, dict):
                m = dict(m)
                m.setdefault("_group_id", gid)
                out.append(m)
    return out

def fetch_mentions(start=None, end=None):
    """拉取@我的消息（群聊）"""
    args = ["chat", "message", "list-mentions", "--limit", "30"]
    if start:
        args += ["--start", start]
    if end:
        args += ["--end", end]
    d = dws(*args)
    convs = d.get("result", {}).get("conversationMessagesList") or []
    out = []
    for c in convs:
        if c.get("openConversationId") in GROUP_CHAT_IDS:
            out.extend(c.get("messages") or [])
    return out

# ---------------- 知识库检索 ----------------
KB_API_URL = os.environ.get("KB_API_URL", "http://127.0.0.1:8787/api/search")

def search_kb(question):
    """优先调用 REST API（与门户/服务共享同一数据源），失败时回退本地 query.py"""
    import urllib.request, urllib.parse
    url = KB_API_URL + "?" + urllib.parse.urlencode({"q": question, "top_k": 3})
    try:
        with urllib.request.urlopen(url, timeout=15) as resp:
            data = json.loads(resp.read().decode("utf-8"))
            results = data.get("results", [])
            # 归一化字段：REST API 的 source_url 在 citation 中
            for r in results:
                if not r.get("source_url") and r.get("citation"):
                    r["source_url"] = r["citation"].get("source_url", "")
            return results
    except Exception:
        pass
    # 回退：本地 query.py
    try:
        r = subprocess.run([sys.executable, QUERY_PY, question, "--top", "3", "--format", "json"],
                           capture_output=True, text=True, env=ENV, timeout=60)
        return json.loads(r.stdout)
    except Exception:
        return []

# ---------------- 回复构建 ----------------
# 问候 / 询问能力 → 返回知识库简介
# 注意: 用户可能带称呼（"你好小福"），用 search 而非 match 全串匹配
GREETINGS = re.compile(
    r"(^|[^一-龥])(你好|您好|hi|hello|嗨|哈喽|在吗|在么|早上好|下午好|晚上好|你好呀|"
    r"谢谢|感谢|收到)([!！。.~～\s]*$|[一-龥，,。!！？?\s]*$)",
    re.I)
# 询问"你能解答哪些问题 / 你会什么 / 你能做什么 / 介绍一下你"
ASK_ABILITY = re.compile(
    r"(你能|可以|会|能).{0,8}(解答|回答|处理|解决|帮|做什么|干什么|干嘛|哪些问题|什么问题|"
    r"哪些|什么|介绍一下|介绍下|简介|帮我|问问你)|"
    r"(有什么|哪些).{0,4}(问题|事).{0,4}(可以|能|可)?.{0,3}(问|找|咨询)你|"
    r"(介绍|说说|讲下).{0,4}(自己|你|能力|功能|作用)", re.I)

# 闲聊 / 与知识库无关 → 礼貌拒绝
# 覆盖口语化表达："在干啥/在干嘛/忙什么/干什么呢/你累不累/你烦不烦" 等
# 注意: 避免把"工资条打印/加班审批"等含技术词的问题误判为闲聊
CHITCHAT = re.compile(
    r"(在干啥|在干嘛|在干什么|干嘛呢|干吗|干啥|干什么呢|做什么呢|忙什么|忙啥|"
    r"你.{0,3}(干啥|干嘛|干吗|忙啥|忙什么)|"
    r"吃饭了吗|吃了吗|睡觉没|睡了吗|天气怎么样|天气如何|今天天气|"
    r"心情不好|心情好|好开心|好难过|好烦|烦死了|"
    r"工资多少|工资高|工资低|加薪|涨工资|"
    r"加班多|老加班|天天加班|"
    r"老板骂|老板凶|同事好|同事坏|八卦一下|聊聊天|聊聊|"
    r"讲个笑话|说个笑话|讲个故事|说个故事|推荐电影|推荐音乐|推荐歌|"
    r"玩游戏|打游戏|看电影|看剧|追剧|听歌|唱歌|跳舞|"
    r"结婚了吗|离婚|恋爱|处对象|女朋友|男朋友|多大了|几岁了|"
    r"你是谁|你叫什么|你多高|你多重|你住在哪|你爸妈|你有男朋友|你有女朋友|"
    r"你累不累|你烦不烦|你无聊不|你寂寞不|你开心不|你高兴不|你在不在|你出来|你上线|"
    r"拜拜|再见|晚安|早安|午安|睡觉了|下班了|上班了|回家了)",
    re.I)
# 敏感 / 不合适内容 → 礼貌拒绝
SENSITIVE = re.compile(
    r"(色情|黄片|裸照|裸体|a片|av|性交|做爱|赌博|毒品|枪支|炸弹|杀人|自杀|诈骗|黑客|入侵|破解|"
    r"翻墙|政治|法轮|邪教|攻击|骂人|脏话|傻逼|操你|去死|诅咒|滚蛋|你妈|他妈|草你)",
    re.I)

# 可选: LLM 语义分类（设置 LLM_API_KEY 后启用，见 classify_intent_llm）
LLM_API_KEY = os.environ.get("LLM_API_KEY", "")
LLM_BASE_URL = os.environ.get("LLM_BASE_URL", "https://api.deepseek.com/v1/chat/completions")
LLM_MODEL = os.environ.get("LLM_MODEL", "deepseek-chat")

HELP_MSG = ("## 🤖 我是小福 · 科情客服知识助手\n\n"
            "我是基于「**科情客服知识库**」训练的问答机器人，专门解答公司各产品的技术问题。\n\n"
            "### 📚 我能解答什么\n"
            "- **产品线**：用友、致远OA、时空、自研、蓝凌OA、钉钉 等\n"
            "- **问题类型**：应用操作、环境问题、数据接口、软件补丁、安装部署、数据错误 等\n"
            "- **知识规模**：2485 条技术问题知识（问题现象 → 原因 → 解决方案，附引用来源）\n\n"
            "### 💡 使用方法\n"
            "直接描述你遇到的问题，例如：\n"
            "- `U8 登录失败怎么办`\n"
            "- `致远OA 表单附件上传报错`\n"
            "- `WMS 打印出库单报错 Clodop`\n"
            "- `时空智友 数据库连接失败`\n\n"
            "我会检索知识库并给出解决方案（附引用来源）。\n"
            "如果未命中，建议转人工客服。")

DECLINE_MSG = ("## 🤖 小福 · 抱歉\n\n"
               "这个问题超出了我的能力范围，我主要负责解答「科情客服知识库」中的产品技术问题"
               "（用友 / 致远OA / 时空 / 自研 / 蓝凌OA / 钉钉 等的操作、环境、接口、补丁等）。\n\n"
               "建议：\n"
               "1) 换个技术问题描述，我会尽力检索解答；\n"
               "2) 或转人工客服协助。")

def strip_mention(content):
    """去掉消息中的@提及文本（如 @小福）"""
    return re.sub(r"@[^\s@]{1,30}", "", content or "").strip()

def classify_intent_llm(question):
    """用 LLM 判断意图（需设置 LLM_API_KEY）。返回: intro / chitchat / sensitive / technical / unknown"""
    if not LLM_API_KEY:
        return None
    import urllib.request
    payload = {
        "model": LLM_MODEL,
        "messages": [
            {"role": "system",
             "content": "你是意图分类器。判断用户对客服机器人的提问属于哪一类，只输出一个词："
                        "intro(询问你能做什么/问候/自我介绍), chitchat(闲聊寒暄/与工作无关), "
                        "sensitive(违法/色情/辱骂/政治敏感), technical(产品技术问题), unknown(无法判断)。"},
            {"role": "user", "content": question},
        ],
        "temperature": 0,
        "max_tokens": 10,
    }
    req = urllib.request.Request(
        LLM_BASE_URL, data=json.dumps(payload).encode("utf-8"),
        headers={"Content-Type": "application/json", "Authorization": f"Bearer {LLM_API_KEY}"})
    try:
        with urllib.request.urlopen(req, timeout=10) as resp:
            data = json.loads(resp.read().decode("utf-8"))
            label = data["choices"][0]["message"]["content"].strip().lower()
            for k in ("intro", "chitchat", "sensitive", "technical", "unknown"):
                if k in label:
                    return k
    except Exception:
        pass
    return None

def classify_intent(question):
    """意图分类：优先 LLM（如启用），否则规则匹配。返回: intro/chitchat/sensitive/technical"""
    q = question.strip()
    # LLM 优先
    llm_label = classify_intent_llm(q)
    if llm_label and llm_label != "unknown":
        return llm_label
    # 规则兜底（顺序重要：敏感 > 闲聊 > 问候/能力 > 技术）
    if SENSITIVE.search(q):
        return "sensitive"
    # 闲聊优先于问候：避免"你好小福，你在干啥？"被当问候
    if CHITCHAT.search(q):
        return "chitchat"
    if GREETINGS.search(q) or ASK_ABILITY.search(q):
        return "intro"
    return "technical"

def build_reply(question, results):
    """构造小福回复内容（Markdown，含引用）"""
    q = question.strip()
    intent = classify_intent(q)
    # 1) 问候 / 询问能力 → 知识库简介
    if intent == "intro":
        return HELP_MSG
    # 2) 闲聊 / 敏感内容 → 礼貌拒绝（不查知识库）
    if intent in ("chitchat", "sensitive"):
        return DECLINE_MSG
    # 3) 检索无结果 → 未命中提示
    if not results:
        return ("## 🤖 小福 · 知识库未命中\n\n"
                f"**问题**: {question}\n\n"
                "很抱歉，我在知识库中没有找到匹配的方案。\n"
                "建议：1) 换个关键词重试；2) 转人工客服协助。")
    # 4) 正常回答
    lines = ["## 📚 知识库回答", "", f"**问题**: {question}", ""]
    for i, r in enumerate(results[:3], 1):
        lines.append(f"### 匹配 {i} · {r.get('title','')}")
        lines.append(f"- **知识ID**: `{r.get('id','')}`")
        lines.append(f"- **产品线**: {r.get('product_line','-')} | **版本**: {r.get('version','-')} | **模块**: {r.get('module','-')}")
        lines.append(f"- **问题类型**: {r.get('problem_type','-')}")
        lines.append(f"- **问题现象**: {r.get('problem','-')}")
        if r.get("solution"):
            sol = r["solution"][:500]
            lines.append(f"- **解决方案**: {sol}")
        lines.append(f"- **引用来源**: {r.get('source_url','')}")
        lines.append("")
    lines.append("---")
    lines.append("> 由小福基于「科情客服知识库」自动回答，点击引用来源可查看原文。")
    return "\n".join(lines)

# ---------------- 发送 ----------------
def send_dm(text):
    """小福发送单聊消息"""
    return dws("mcp", "group", "batch_send_robot_msg_to_users",
               "--robotCode", ROBOT_CODE, "--userIds", MY_USER_ID,
               "--title", "小福 · 知识库问答", "--markdown", text)

def send_group(text, group_id, at_user_ids=None, reference_msg_id=None):
    """小福发送群聊消息（可@人、可引用原消息）"""
    args = ["mcp", "group", "send_robot_group_message",
            "--robotCode", ROBOT_CODE,
            "--openConversationId", group_id,
            "--title", "小福 · 知识库问答",
            "--markdown", text]
    if at_user_ids:
        args += ["--atUserIds", ",".join(at_user_ids)]
    if reference_msg_id:
        args += ["--referenceOpenMessageId", reference_msg_id]
    return dws(*args)

# ---------------- 核心处理 ----------------
def process_once(mode, dry_run=False, verbose=False):
    state = load_state()
    handled = set(state.get("handled_msg_ids", []))
    new_count = 0

    if mode in ("dm", "both"):
        messages = fetch_dm_messages()
        messages = sorted(messages, key=lambda m: m.get("createTime", ""))
        for m in messages:
            mid = m.get("openMessageId", "")
            if not mid or mid in handled:
                continue
            sender = m.get("sender", "")
            content = (m.get("content") or "").strip()
            if "[图片消息]" in content or "[文件]" in content or "[视频]" in content:
                handled.add(mid)
                continue
            if not content or sender == ROBOT_NAME:
                handled.add(mid)
                continue
            new_count += 1
            print(f"[DM {m.get('createTime')}] {sender}: {content[:60]}", flush=True)
            results = search_kb(content)
            reply = build_reply(content, results)
            if dry_run:
                print(f"[dry-run] DM 跳过发送: {mid}", flush=True)
            else:
                resp = send_dm(reply)
                ok = resp.get("response", {}).get("content", {}).get("success")
                print(f"[DM send] {mid} -> success={ok}", flush=True)
            handled.add(mid)

    if mode in ("group", "both"):
        # 群聊：拉群消息，仅响应明确 @小福 的消息
        messages = fetch_group_messages()
        messages = sorted(messages, key=lambda m: m.get("createTime", ""))
        for m in messages:
            mid = m.get("openMessageId", "")
            if not mid or mid in handled:
                continue
            sender = m.get("sender", "")
            content = (m.get("content") or "").strip()
            if not content or sender == ROBOT_NAME:
                handled.add(mid)
                continue
            # 触发条件：消息中明确 @小福（或包含小福名字的提及）
            mentioned = ("@小福" in content) or ("@小福 " in content) or ("@小福\n" in content)
            if not mentioned:
                handled.add(mid)  # 非@小福消息，跳过（不回复）
                continue
            question = strip_mention(content)
            if not question:
                handled.add(mid)
                continue
            # 回复到消息来源群
            gid = m.get("_group_id", "")
            if gid not in GROUP_CHAT_IDS:
                handled.add(mid)
                continue
            new_count += 1
            gname = GROUP_CHAT_IDS.get(gid, gid)
            print(f"[GROUP {gname} {m.get('createTime')}] {sender}: {question[:60]}", flush=True)
            results = search_kb(question)
            reply = build_reply(question, results)
            # @回复提问者
            at_id = m.get("senderOpenDingTalkId", "")
            if dry_run:
                print(f"[dry-run] GROUP 跳过发送: {mid} @{at_id}", flush=True)
            else:
                resp = send_group(reply, gid, at_user_ids=[at_id] if at_id else None,
                                  reference_msg_id=mid)
                ok = resp.get("response", {}).get("content", {}).get("success")
                print(f"[GROUP send] {mid} -> success={ok}", flush=True)
                if ok is False:
                    print(json.dumps(resp, ensure_ascii=False)[:400], flush=True)
            handled.add(mid)

    if new_count:
        state["handled_msg_ids"] = sorted(handled)[-3000:]
        state["last_run"] = time.strftime("%Y-%m-%d %H:%M:%S")
        save_state(state)
    return new_count

def main():
    ap = argparse.ArgumentParser(description="小福知识库问答机器人（单聊+群聊）")
    ap.add_argument("--mode", choices=["both", "dm", "group"], default="both",
                    help="监听模式: both=单聊+群聊(默认) dm=仅单聊 group=仅群聊")
    ap.add_argument("--once", action="store_true")
    ap.add_argument("--interval", type=int, default=15)
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("-v", "--verbose", action="store_true")
    args = ap.parse_args()

    print(f"小福机器人启动: mode={args.mode} robotCode={ROBOT_CODE}", flush=True)
    print(f"  单聊: {DM_CHAT_ID}", flush=True)
    for gid, gname in GROUP_CHAT_IDS.items():
        print(f"  群聊: {gid} ({gname})", flush=True)
    if args.dry_run:
        print("[dry-run] 只读模式", flush=True)
    while True:
        try:
            n = process_once(args.mode, args.dry_run, args.verbose)
            if n and args.verbose:
                print(f"处理 {n} 条新消息", flush=True)
        except Exception as e:
            print(f"错误: {e}", flush=True)
        if args.once:
            break
        time.sleep(args.interval)

if __name__ == "__main__":
    main()
