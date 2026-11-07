# pstack × WorkBuddy 移植版

本目录是 [backnotprop/pstack](https://github.com/backnotprop/pstack)（Poteto 的 AI 严谨工程方法论技能集）中**可独立运行**的 17 个技能，针对 **WorkBuddy** 技能格式做的移植。

原仓库遵循 `agentskills.io` / Cursor 的 `SKILL.md` 规范，WorkBuddy 无法直接识别，因此这里把每个技能的 frontmatter 重写为 WorkBuddy 规范，并保留原始方法论正文、references 与 scripts。

## 与根目录 `skills/` 的区别

- 根目录 `skills/`：原版 agentskills.io 格式，供 Cursor / Claude Code / OpenCode 等使用。
- 本目录 `workbuddy/`：WorkBuddy 原生格式，供 WorkBuddy 使用。

两者并存，互不影响；本 fork 仍可正常同步上游 pstack。

## 包含的 17 个独立技能

| 技能 | 作用 |
|------|------|
| `unslop` | 清除文本中的 AI 写作痕迹（套路化表达、空话、机器腔） |
| `bro` | 用大白话重述上一条消息，去掉术语 |
| `how` | 讲解子系统如何运作：架构、运行时流程、心智模型 |
| `tdd` | 有廉价测试路径时，先写失败测试再改生产代码 |
| `typescript-best-practices` | 编辑 .ts/.tsx 时的类型纪律与模式 |
| `arena` | 并行多候选竞技，选基版并嫁接落败者强项 |
| `swarm` | 并行扇出覆盖：覆盖矩阵、竞速、夹击、分区 |
| `interrogate` | 多模型对抗评审，只采纳被运行证明的发现 |
| `reflect` | 把长任务经验沉淀为新技能/教训 |
| `show-me-your-work` | 长任务/无人值守的可审阅决策日志（TSV） |
| `figure-it-out` | 无合适剧本时临场设计可审计工作流 |
| `automate-me` | 把用户工作习惯提炼成专属 -mode 技能 |
| `correct` | 用架构/类型/lint/测试消除智能体反复犯的错 |
| `benchmark-checklist` | 报告性能数字前的测量审查清单 |
| `in-your-own-words` | 用自己话复述用户目标，确认理解一致 |
| `sharpen` | 把任务做深不做大，重写提示词 |
| `statechart` | TLA+ 风格状态图与形式化验证可视化（自带 TS 工程） |

> 未移植 `poteto-mode` 等依赖型技能（它们依赖约 58 个技能 + 24 条原则 + 2 个子代理的耦合图）。

## 安装到 WorkBuddy

方式一：直接复制
```bash
cp -R workbuddy/* ~/.workbuddy/skills/
```

方式二：软链（方便随本仓库更新）
```bash
for d in workbuddy/*/; do
  ln -s "$(pwd)/$d" ~/.workbuddy/skills/"$(basename "$d")"
done
```

安装后**重启/刷新 WorkBuddy 会话**，技能即会出现在可用列表，例如直接说「用 unslop 润色一下」「用 arena 给我几个方案」即可触发。

## 格式差异说明

WorkBuddy 的 `SKILL.md` frontmatter 字段：`name` / `version` / `display_name` / `description`(中文主描述) / `description_zh` / `description_en`。已剔除原版 Cursor 专属字段（`disable-model-invocation`、`icon`、`color`、`paths`），并为每个技能生成 `_skillhub_meta.json`。

`statechart` 自带 TypeScript 工程（在 `statechart/scripts/`），运行前需 `npm install` 及 Node 环境。
