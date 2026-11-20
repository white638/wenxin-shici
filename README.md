# 文心诗坊 · wenxin-shici

集大成的古典中文诗文创作、改诗、校律、赏析与教学 Agent Skill：**立意与审美先导，格律与查证交由零依赖离线 Python 脚本验证。**

本技能融会贯通了 [shici-studio](https://github.com/hlulu123/shici-studio) 的高精度离线韵书引擎（平水韵 106 韵 / 词林正韵 19 部 / 中华新韵 14 部 / 三万余首唐宋诗库防撞句）与 [moqing（墨卿）](https://github.com/Aether-liusiqi/moqing) 的古典文体广度（赋、古文、赏析、格律教学、意象词典与多轮协同打磨），并剔除了冗余模板、古风中二说教及若干传统格律文档误区。

## 核心能力（五位一体）

| 能力 | 覆盖范围 | 核心亮点 |
|---|---|---|
| **写诗填词作古文** | 五七言绝/律/排、古风歌行、**50 个内置词牌**（+ 自定义 `--pattern`）、对联、藏头嵌字、定场诗、骈文、赋、铭、古文 | 立意先行，先一气成稿再换编辑眼精修；优先吸纳用户真实地名细节；至多追问 1 轮 |
| **改诗与多轮打磨** | 纯校律、只修格律、炼字提升、换风格、换体裁、多轮协同推敲 | 保留原诗骨架与好句，对照展示“原句 → 改句 → 理由”，修改稿重跑脚本验真 |
| **格律与声律校验** | 平仄、粘对、孤平、三平尾、拗救、特拗、入声字、撞句、骈赋句脚 | 仅依赖 Python 3 标准库；识别《静夜思》（古绝）、《黄鹤楼》（拗律）等变格不误判 |
| **古诗文赏析评点** | 诗、词、骈、赋、古文 | 先用 `dupcheck.py` 核实原文、用 `meter.py` 验声律，再展开六维深度解读 |
| **格律教学与问答** | 入声辨析、对仗、韵部、词牌结构、九大流派、诗史与典故考据 | 援引韵书诗话，搭配 `lookup --rusheng` / `rhymes` / `cipai` 即席演练 |

## 目录结构

```text
wenxin-shici/
├── wenxin-shici/               ← 技能本体（安装时复制此目录即可）
│   ├── SKILL.md                ← 核心入口：五条总则、任务总路由、主流程与命令速查
│   ├── scripts/
│   │   ├── meter.py            ← 格律校验 / 查字查入声 / 列韵 / 标平仄 / 50词谱 / 自定义谱
│   │   ├── dupcheck.py         ← 三万余首唐宋名家诗库撞句检查与原文检索
│   │   └── shici_data.py       ← 韵书、词牌与语料数据接口（含 UTF-8 兼容）
│   ├── assets/                 ← 平水韵、中华新韵、50 词牌谱、字频表与唐宋诗库
│   ├── references/
│   │   ├── craft/              ← 立意作法、用典法则、典故库、意象词典、改校、赏析教学、poem.json
│   │   ├── forms/              ← 近体诗、古体诗、词、对联藏头、骈文赋铭、古文
│   │   ├── types/              ← 12 类实用生活与应酬题材指南
│   │   └── styles/             ← 风格总览（九大流派+模仿三部曲）及 11 篇风格专论
│   └── examples/               ← 7 篇经脚本实证的标杆输出示例
├── evals/                      ← 8 组 skill-creator 评测用例
└── tools/test_meter.py         ← 构造用例与唐诗三百首/宋词三百首回归测试
```

## 安装与使用

克隆仓库后，只复制内部的 `wenxin-shici/` 技能本体目录即可：

```bash
git clone https://github.com/white638/wenxin-shici.git
```

### Antigravity（全局生效）

将 `wenxin-shici/` 目录复制到 `~/.gemini/config/skills/wenxin-shici/`（或工作区 `.agents/skills/wenxin-shici/`）。

### Claude Code / Codex CLI / OpenCode

将 `wenxin-shici/` 复制到对应技能目录（如 `~/.claude/skills/wenxin-shici/`、`~/.agents/skills/wenxin-shici/` 或 `~/.config/opencode/skills/wenxin-shici/`）。

**环境要求**：Python 3.9+（纯标准库，零第三方包依赖）。若所在对话环境不允许运行命令行，技能仍可完整创作与赏析，但会在交付时诚实注明“格律未经脚本校验”。

## 命令行工具速查

```bash
python wenxin-shici/scripts/meter.py check "白日依山尽，黄河入海流。欲穷千里目，更上一层楼。"
python wenxin-shici/scripts/meter.py check --form 词:鹊桥仙 "……"
python wenxin-shici/scripts/meter.py check --pattern "平a，中仄平平中仄平a。中平仄，中仄仄平平a。" "……"
python wenxin-shici/scripts/meter.py check --form 骈文 "……"
python wenxin-shici/scripts/meter.py check --form 赋 "……"
python wenxin-shici/scripts/meter.py lookup --rusheng "风急天高猿啸哀，渚清沙白鸟飞回"
python wenxin-shici/scripts/meter.py rhymes 下平七阳 --common 60
python wenxin-shici/scripts/meter.py cipai
python wenxin-shici/scripts/dupcheck.py --find 大鹏一日同风起
```

运行回归测试：

```bash
python tools/test_meter.py
```

## 许可证

[MIT](LICENSE)。第三方数据许可声明见 [`wenxin-shici/assets/LICENSES.md`](wenxin-shici/assets/LICENSES.md)。
