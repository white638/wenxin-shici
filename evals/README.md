# 评测用例

[skill-creator](https://github.com/anthropics/skills) 格式的评测用例，覆盖写作、改诗、赏析、格律教学与赋体创作，用于回归比较技能效果。每个用例目录包含：

- `prompt.md`：用户原话
- `case.yaml`：期望结果摘要
- `graders/`：逐条评分标准

| 用例 | 考查点 |
|---|---|
| `jishi-huanxisha-wonton` | 记录生活小事，按词谱填《浣溪沙》 |
| `yiqi-qilv-with-allusions` | 意气风发七律，用典并注明真实出处 |
| `dingchang-programmer-birthday` | 寿宴定场诗，将现代人物事迹化入古典语言 |
| `taibai-gexing-dapeng` | 太白体长篇歌行，化用而不照抄李白 |
| `fix-flawed-qilv` | 最小改动修正七律格律错误，附对照与复检 |
| `appreciate-denggao` | 古诗六维赏析，核对原文并用脚本识别平水韵与声律 |
| `teach-rusheng` | 格律教学：入声字辨认规律、破除误区与 `lookup --rusheng` 演示 |
| `wenfu-lowpoint` | 宋调文赋创作，铺陈哲思收束而不滥用现代白话腔 |

本目录用于工程评测，安装技能本体时不需复制。
