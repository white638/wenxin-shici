# poem.json 数据格式

`poem.json` 用一份结构化数据记录作品的全部信息：诗文、类型、体裁、风格、格律校验结果、典故注、创作说明，以及给视觉化预留的分镜。

只在下面两种情况下生成这个文件：
- 用户明确要求保存作品数据，或需要交给其他工具处理。
- 用户提到之后要把这首诗做成视频、海报、网页或朗诵卡片。

普通的写诗、改诗、赏析对话，不需要生成它。

## 文件命名

`<题目>.poem.json`，例如 `夜半馄饨.poem.json`。题目里有文件名不允许的字符时，替换为下划线。

## 结构

```json
{
  "version": 1,
  "title": "浣溪沙·夜半馄饨",
  "author": "作者名或留空",
  "created": "2026-11-20",

  "type": {
    "main": "记事・生活",
    "secondary": ["抒情・柔情"]
  },
  "form": "词:浣溪沙",
  "style": "闲适浅切",
  "liyi": "一句话立意：深夜加班后，一碗路边馄饨让人觉得这座城市还是暖的。",

  "text": {
    "sections": [
      { "name": "上片", "lines": ["……", "……", "……"] },
      { "name": "下片", "lines": ["……", "……", "……"] }
    ]
  },

  "meter": {
    "rhyme_book": "词林正韵",
    "rhyme": ["第七部平"],
    "verdict": "合律",
    "lines": [
      { "text": "……", "marks": "●●○○●●○", "pattern": "⊙仄平平仄仄平" }
    ],
    "errors": [],
    "warnings": [],
    "info": [],
    "notes": []
  },

  "allusions": [
    {
      "anchor": "诗中对应的字词",
      "name": "典名",
      "source": "《书名·篇名》",
      "quote": "出处原文短句",
      "meaning": "在本诗中取的意思",
      "verified": true,
      "url": "查证时用到的网址，可省略"
    }
  ],

  "notes": {
    "annotations": ["字词注释……"],
    "translation": "白话大意……",
    "commentary": "创作说明：立意、用典、炼字，三到五句。"
  },

  "context": {
    "occasion": "使用场合，如生日宴、发朋友圈",
    "audience": "写给谁",
    "user_materials": "用户提供的素材摘要"
  },

  "scenes": [
    {
      "lines": [0, 1],
      "imagery": ["路灯", "热气", "馄饨"],
      "mood": "疲惫中的暖意",
      "palette": ["#1f2a44", "#f2c14e"],
      "motion": "热气缓缓升起",
      "duration": 4.0
    }
  ]
}
```

## 字段说明

| 字段 | 说明 |
|---|---|
| `version` | 格式版本，目前是 `1` |
| `title` | 题目。词写成“词牌·题目” |
| `type.main` | 主类型，取 [../types/index.md](../types/index.md) 里的类型名；对不上时写“自由” |
| `type.secondary` | 借用了方法的其他类型，可以为空 |
| `form` | 体裁：五绝、七绝、五律、七律、五排、七排、古风、对联、词:词牌名、骈文、赋、古文等 |
| `style` | 风格，取 `../styles/` 里的风格名；无明显风格时写空字符串 |
| `liyi` | 一句话立意（见 [liyi-and-craft.md](liyi-and-craft.md) 第一节） |
| `text.sections` | 正文，按片或段落分组；不分段的诗只有一组，`name` 写“正文” |
| `meter` | 直接放入 `python scripts/meter.py check --json` 的输出；散体古文可省略 |
| `allusions` | 典故注（格式见 [yongdian.md](yongdian.md)）；`verified` 表示是否核对过出处 |
| `notes` | 注释、白话大意、创作说明 |
| `context` | 场合、对象、用户素材摘要 |
| `scenes` | 视觉分镜预留：`lines`（从 0 起连续行号）、`imagery`、`mood`、`palette`、`motion`、`duration`（秒） |

## 写入注意

- 文件用 UTF-8 编码，`ensure_ascii` 设为 `false`。
- `meter` 直接用脚本 JSON 输出，勿手工拼写平仄。
- `allusions` 只收核对过出处的典故；未联网核实的，`verified` 置 `false` 并在 `meaning` 注明“出处凭记忆，建议核对”。
- 不要把用户未提供的个人隐私写入 `context`。
