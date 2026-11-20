"""Regression tests for wenxin-shici/scripts/meter.py.

    python tools/test_meter.py            # constructed cases + corpus pass rates
    python tools/test_meter.py -v         # also list corpus poems that fail
"""
import collections
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "wenxin-shici", "scripts"))

import dupcheck  # noqa: E402
import meter  # noqa: E402
import shici_data as D  # noqa: E402

D.ensure_utf8_stdio()
VERBOSE = "-v" in sys.argv

# (name, text, form, expect_kinds_present, expect_no_errors)
CASES = [
    ("合律·登鹳雀楼", "白日依山尽，黄河入海流。欲穷千里目，更上一层楼。", None, [], True),
    ("合律·登高", "风急天高猿啸哀，渚清沙白鸟飞回。无边落木萧萧下，不尽长江滚滚来。"
                 "万里悲秋常作客，百年多病独登台。艰难苦恨繁霜鬓，潦倒新停浊酒杯。", None, ["今音听感"], True),
    ("特拗·宿建德江", "移舟泊烟渚，日暮客愁新。野旷天低树，江清月近人。", None, ["特拗"], True),
    ("对句救·赋得古原草", "离离原上草，一岁一枯荣。野火烧不尽，春风吹又生。", None, ["拗救"], True),
    ("失粘", "白日依山尽，黄河入海流。远树连天碧，孤舟向晚收。", None, ["失粘"], False),
    ("失对", "白日依山尽，落日照江流。欲穷千里目，更上一层楼。", None, ["失对"], False),
    ("孤平", "白日依山尽，大河入海流。欲穷千里目，更上一层楼。", None, ["孤平"], False),
    ("三平尾", "白日依山尽，黄河入海流。欲穷千里目，更上高楼头。", None, ["三平尾"], False),
    ("出韵", "白日依山尽，黄河入海流。欲穷千里目，更上一层台。", None, ["出韵"], False),
    ("平仄", "白日依山尽，黄河入海流。欲穷千里目，更上一级楼。", None, ["平仄"], False),
    ("首句借邻韵", "清明时节雨纷纷，路上行人欲断魂。借问酒家何处有，牧童遥指杏花村。", None, [], True),
    ("句数", "白日依山尽，黄河入海流。欲穷千里目。", "五绝", ["字数"], False),
    ("宽式只看押韵", "白日依山尽，大河入海流。欲穷千里目，更上高楼头。", None, ["孤平"], True),
    ("对联", "风声雨声读书声声声入耳\n家事国事天下事事事关心", "对联", [], True),
    ("对联收尾", "春风送暖入屠苏\n爆竹一声除旧岁", "对联", ["仄起平收"], False),
    # 新韵里入声字“一”归平声，“一层楼”成三平尾；平水韵下则合律
    ("新韵", "白日依山尽，黄河入海流。欲穷千里目，更上一层楼。", None, ["三平尾"], False),
    # ---- 新增融合特性测试 ----
    ("新词牌·十六字令", "天。休使圆蟾照客眠。人何在，桂影自婵娟。", "词:十六字令", [], True),
    ("新词牌·鹊桥仙", "纤云弄巧，飞星传恨，银汉迢迢暗度。金风玉露一相逢，便胜却、人间无数。"
                   "柔情似水，佳期如梦，忍顾鹊桥归路。两情若是久长时，又岂在、朝朝暮暮。", "词:鹊桥仙", [], True),
    ("新词牌·桂枝香", "登临送目。正故国晚秋，天气初肃。千里澄江似练，翠峰如簇。"
                   "归帆去棹残阳里，背西风、酒旗斜矗。彩舟云淡，星河鹭起，画图难足。"
                   "念往昔、繁华竞逐。叹门外楼头，悲恨相续。千古凭高，对此漫嗟荣辱。"
                   "六朝旧事随流水，但寒烟、芳草凝绿。至今商女，时时犹唱，後庭遗曲。", "词:桂枝香", [], True),
    ("新词牌·满庭芳", "山抹微云，天连衰草，画角声断谯门。暂停征棹，聊共引离尊。"
                   "多少蓬莱旧事，空回首、烟霭纷纷。斜阳外，寒鸦万点，流水绕孤村。"
                   "销魂。当此际，香囊暗解，罗带轻分。谩赢得、青楼薄幸名存。"
                   "此去何时见也，襟袖上、空惹啼痕。伤情处，高城望断，灯火已黄昏。", "词:满庭芳", [], True),
    ("古风律句偏多", "白日依山尽，黄河入海流。欲穷千里目，更上一层楼。"
                     "野火烧不尽，春风吹又生。朝辞白帝彩，暮入长安城。", "古风", ["律句偏多"], True),
    ("古风通篇律句警", "国破山河在，城春草木深。感时花溅泪，恨别鸟惊心。"
                     "烽火连三月，家书抵万金。白头搔更短，浑欲不胜簪。", "古风", ["通篇律句"], True),
    ("骈文检查", "落霞与孤鹜齐飞，秋水共长天一色。", "骈文", [], True),
    ("铭文检查", "山不在高，有仙则名。水不在深，有龙则灵。斯是陋室，惟吾德馨。苔痕上阶绿，草色入帘青。", "铭", [], True),
    ("今音听感提示", "残灯照壁影初斜，旧燕辞梁巢已赊。三载温存书未冷，一宵寒雨梦先遮。"
                 "杯深不敌心头涩，衾薄偏逢鬓角华。起看中庭秋月白，梧桐叶落各天涯。", None, ["今音听感"], True),
]
LOOSE = {"宽式只看押韵"}
XINYUN = {"新韵"}


def run_cases():
    fails = 0
    for name, text, form, kinds, no_err in CASES:
        rep = meter.run_check(text, form, "xinyun" if name in XINYUN else "pingshui", name in LOOSE)
        got = {i["kind"] for i in rep.issues}
        errs = [i for i in rep.issues if i["level"] == "error"]
        ok = all(k in got for k in kinds) and (not errs if no_err else bool(errs))
        fails += not ok
        print("%s %-16s %s  %s" % ("✓" if ok else "✗", name, rep.verdict, "；".join(sorted(got)) or "—"))
        if not ok:
            print(rep.render())

    # Custom --pattern & rusheng & dupcheck checks
    rep_pat = meter.run_check("天。休使圆蟾照客眠。人何在，桂影自婵娟。",
                              pattern="平a，中仄平平中仄平a。中平仄，中仄仄平平a。")
    ok_pat = not [i for i in rep_pat.issues if i["level"] == "error"]
    fails += not ok_pat
    print("%s %-16s %s" % ("✓" if ok_pat else "✗", "自定义谱--pattern", rep_pat.verdict))

    rep_pat_bad = meter.run_check("天。休使圆蟾照客眠。", pattern="平a，中仄平平中仄平a。中平仄，中仄仄平平a。")
    ok_pat_bad = any(i["kind"] == "字数" for i in rep_pat_bad.issues)
    fails += not ok_pat_bad
    print("%s %-16s %s" % ("✓" if ok_pat_bad else "✗", "自定义谱字数错", rep_pat_bad.verdict))

    ok_ru = (D.is_rusheng("白") and D.is_modern_ping("白")
             and D.is_rusheng("十") and D.is_modern_ping("十")
             and not D.is_rusheng("春"))
    fails += not ok_ru
    print("%s %-16s 白十入声=%s 春非入声=%s" % ("✓" if ok_ru else "✗", "入声识别", D.is_rusheng("白"), not D.is_rusheng("春")))

    hits = dupcheck.check("大鹏一日同风起，扶摇直上九万里。", 5)
    ok_dup = bool(hits and any("李白" in s for h in hits for s in h["sources"]))
    fails += not ok_dup
    print("%s %-16s 检出=%d" % ("✓" if ok_dup else "✗", "撞句检索", len(hits)))

    ok_count = len(D.cipai_table()) == 50
    fails += not ok_count
    print("%s %-16s count=%d" % ("✓" if ok_count else "✗", "内置词牌50首", len(D.cipai_table())))
    return fails


def corpus_rates():
    forms = {"五言绝句": "五绝", "七言绝句": "七绝", "五言律诗": "五律", "七言律诗": "七律"}
    stats = collections.defaultdict(collections.Counter)
    kinds = collections.defaultdict(collections.Counter)
    for p in D.corpus():
        if p["type"] not in forms:
            continue
        rep = meter.run_check(p["text"], forms[p["type"]])
        stats[p["type"]][rep.verdict] += 1
        for i in rep.issues:
            if i["level"] == "error":
                kinds[p["type"]][i["kind"]] += 1
        if VERBOSE and rep.verdict == "不合律":
            errs = "；".join(i["msg"] for i in rep.issues if i["level"] == "error")
            print("  [%s] %s《%s》 %s" % (p["type"], p["author"], p["title"], errs))
    print("\n选集近体诗校验（唐诗三百首＋千家诗；含古绝、拗律，不可能 100%）：")
    for t in forms:
        c = stats[t]
        total = sum(c.values())
        ok = c["合律"] + c["小疵"]
        print("  %s  %3d 首  无错误 %3d（%.0f%%）  错误类型 %s" % (
            t, total, ok, 100.0 * ok / max(total, 1), dict(kinds[t].most_common(6))))


def ci_rates():
    table = D.cipai_table()
    ci = [p for p in D.corpus() if p["type"] == "词"]
    print("\n宋词三百首按词牌校验（含新增词牌）：")
    for name in table:
        poems = [p for p in ci if p["title"] == name or p["title"] in table[name].get("alias", [])]
        if not poems:
            continue
        c = collections.Counter()
        for p in poems:
            rep = meter.run_check(p["text"], "词:" + name)
            c[rep.verdict] += 1
            if VERBOSE and rep.verdict == "不合律":
                errs = "；".join(i["msg"] for i in rep.issues if i["level"] == "error")
                print("  [%s] %s：%s" % (name, p["author"], errs[:200]))
        print("  %-6s %2d 首  合律 %d  小疵 %d  不合律 %d" % (name, len(poems), c["合律"], c["小疵"], c["不合律"]))


if __name__ == "__main__":
    f = run_cases()
    corpus_rates()
    ci_rates()
    print("\n构造用例失败：%d" % f)
    sys.exit(1 if f else 0)
