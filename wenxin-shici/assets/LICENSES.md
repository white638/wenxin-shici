# 数据来源、知识渊源与许可声明

本技能「文心诗坊（wenxin-shici）」在架构设计、诗学方法论与格律校验引擎上融合参考并重构自以下开源项目（均采用 MIT 许可）：

- [hlulu123/shici-studio](https://github.com/hlulu123/shici-studio)（MIT）：离线平水韵/中华新韵/词林正韵引擎、撞句与原文检索工具、立意先行创作工作流及诗类/风格参考框架。
- [Aether-liusiqi/moqing](https://github.com/Aether-liusiqi/moqing)（MIT）：古典诗/词/骈/赋/古文全景框架、意象词典、赏析与格律教学流程及多轮改稿协作思路。

## 第三方数据与词库许可

| 文件 | 来源 | 许可 |
|---|---|---|
| `rhyme/pingshui.json` | 平水韵韵目与字表：[rbnyng/pingshui_rhyme](https://github.com/rbnyng/pingshui_rhyme)（取自维基文库《平水韻》）；源数据漏收的字，由 [charlesix59/chinese_word_rhyme](https://github.com/charlesix59/chinese_word_rhyme) 的词林正韵补齐平仄，韵目按今音推定（见文件内 `inferred` 字段） | MIT；MIT |
| `rhyme/pingshui.json`（简体键） | 繁简转换用 [OpenCC](https://github.com/BYVoid/OpenCC) 字表 | Apache-2.0 |
| `rhyme/xinyun.json` | 中华新韵十四部，由 [pypinyin](https://github.com/mozillazg/python-pinyin) 的拼音数据推导 | MIT |
| `cipai.json` | 40 个基础词牌源自 `shici-studio`（句读韵位依通行正体，逐字平仄据 chinese-poetry 全宋词同调统计）；新增 `十六字令`、`南歌子`、`诉衷情`、`鹊桥仙`、`玉楼春`、`行香子`、`满庭芳`、`扬州慢`、`桂枝香`、`摸鱼儿` 共 10 个词牌依《钦定词谱》《唐宋词格律》并结合全宋词同调统计校核 | 数据 MIT；谱为本技能整理 |
| `corpus/poems.json`、`corpus/extended.txt.gz`、`charfreq.json` | [chinese-poetry](https://github.com/chinese-poetry/chinese-poetry)：唐诗三百首、千家诗、宋词三百首、全唐诗名家、全宋词名家（已转简体、去夹注） | MIT |

古典诗词原文本身属于公有领域。上述仓库的 MIT / Apache-2.0 许可要求保留版权与来源声明，本文件即为声明。
