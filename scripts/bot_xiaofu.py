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
GREETINGS = re.compile(r"^(你好|您好|hi|hello|嗨|在吗|在么|早上好|下午好|晚上好|你好呀|哈喽|谢谢|感谢|好的|ok|收到)[!！。.~～\s]*$", re.I)
HELP_MSG = ("## 🤖 我是小福 · 科情客服知识助手\n\n"
            "我基于「科情客服知识库」（2485 条技术问题知识）自动回答。\n\n"
            "**使用方法**: 直接描述你遇到的问题，例如：\n"
            "- `U8 登录失败怎么办`\n"
            "- `致远OA 表单附件上传报错`\n"
            "- `WMS 打印出库单报错 Clodop`\n"
            "- `时空智友 数据库连接失败`\n\n"
            "我会检索知识库并给出解决方案（附引用来源）。\n"
            "如果未命中，建议转人工客服。")

def strip_mention(content):
    """去掉消息中的@提及文本（如 @小福）"""
    return re.sub(r"@[^\s@]{1,30}", "", content or "").strip()

def build_reply(question, results):
    """构造小福回复内容（Markdown，含引用）"""
    if GREETINGS.match(question.strip()):
        return HELP_MSG
    if not results:
        return ("## 🤖 小福 · 知识库未命中\n\n"
                f"**问题**: {question}\n\n"
                "很抱歉，我在知识库中没有找到匹配的方案。\n"
                "建议：1) 换个关键词重试；2) 转人工客服协助。")
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
