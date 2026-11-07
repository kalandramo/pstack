# pstack × WorkBuddy 移植版

本目录是 [backnotprop/pstack](https://github.com/backnotprop/pstack)（Poteto 的 AI 严谨工程方法论技能集）中**已移植**的 48 个技能，针对 **WorkBuddy** 技能格式做的移植：

- **17 个独立技能**（自包含，不依赖其他技能）
- **24 条工程原则**（`principle-*`，每条一条规则，是方法论骨架）
- **6 个依赖型技能**（`why` `teach` `technical-writing` `architect` `blast-radius` `no-comments`）
- **1 个自动路由元技能**（`poteto-mode`：总路由 + 23 个 playbook 剧本 + 子代理定义，实现"说一句需求自动选剧本编排子代理"）

原仓库遵循 `agentskills.io` / Cursor 的 `SKILL.md` 规范，WorkBuddy 无法直接识别，因此这里把每个技能的 frontmatter 重写为 WorkBuddy 规范，并保留原始方法论正文、references 与 scripts。

## 与根目录 `skills/` 的区别

- 根目录 `skills/`：原版 agentskills.io 格式，供 Cursor / Claude Code / OpenCode 等使用。
- 本目录 `workbuddy/`：WorkBuddy 原生格式，供 WorkBuddy 使用。

两者并存，互不影响；本 fork 仍可正常同步上游 pstack。

## 独立技能（17 个，自包含）

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

## 工程原则与依赖技能（30 个）

**24 条原则**（每条一句话规则，被 `poteto-mode` 引用，也可单独用作原则库）：

`principle-attack-the-premise`（攻击前提）、`principle-boundary-discipline`（边界纪律）、`principle-build-the-lever`（造杠杆）、`principle-encode-lessons-in-structure`（把教训编码进结构）、`principle-exhaust-the-design-space`（穷尽设计空间）、`principle-experience-first`（体验优先）、`principle-explain-the-number`（解释数字）、`principle-fix-root-causes`（修根因）、`principle-foundational-thinking`（基础思维）、`principle-guard-the-context-window`（守护上下文窗口）、`principle-laziness-protocol`（懒惰协议）、`principle-make-operations-idempotent`（操作幂等）、`principle-migrate-callers-then-delete-legacy-apis`（先迁调用方再删旧 API）、`principle-minimize-reader-load`（最小化读者负担）、`principle-model-the-domain`（建模领域）、`principle-never-block-on-the-human`（别卡在人身上）、`principle-outcome-oriented-execution`（结果导向执行）、`principle-prove-it-works`（证明它有效）、`principle-redesign-from-first-principles`（第一性原理重设计）、`principle-separate-before-serializing-shared-state`（先分离再串行化共享状态）、`principle-sequence-verifiable-units`（编排可验证单元）、`principle-subtract-before-you-add`（先减后加）、`principle-test-behavior-not-implementation`（测行为不测实现）、`principle-type-system-discipline`（类型系统纪律）。

**6 个依赖型技能**：`why`（追溯设计动机）、`teach`（讲解传授）、`technical-writing`（技术写作规范）、`architect`（架构草图）、`blast-radius`（影响范围分析）、`no-comments`（去注释审查）。

## poteto-mode：自动路由元技能（1 个）

`poteto-mode` 是总入口。用户说「poteto / 进入 poteto 模式 / 按 pstack 方式做」时触发，它把这套方法论加载进上下文，然后**按任务类型自动选剧本（playbook）并编排子代理**——这是原版 pstack "一句话自动编排"体验的 WorkBuddy 版。

包含内容：

- `SKILL.md`：Non-negotiables（强制规范）、24 条 Principles 索引、Autonomy（自主度）、Writing the reply（写作规范）、Harness（已新增 **WorkBuddy 优先**的映射）、Playbooks 路由表。
- `playbooks/`（23 个剧本）：Investigation、Bug fix、Perf issue、Hillclimb、Feature、Refactoring、Prototype、Visual parity、Eval、Babysit、Shipping、Autonomous run、Orchestrate、Autopilot-full/stack、Session pickup、Pause safely、Multi-phase plan、Worktree cleanup、Opening a PR 等。
- `references/`：`bugbot-triage.md`（评审意见分类）、`poteto-agent.md` 与 `comment-sicko.md`（原仓库 `agents/` 下的两个子代理定义，并入此处）。
- `scripts/`（可选）：PR 监控等 TS 工程（`watch-pr/`、`check-plan.mjs`、`worktree-audit.sh`），运行需 Node/bun 环境。

**针对 WorkBuddy 的改写点**：

- 子代理 `poteto-agent`（Cursor 注册式）→ 改为 WorkBuddy `Agent` 工具（`subagent_type: general-purpose`），每个子代理 prompt 开头先完整阅读 `~/.workbuddy/skills/poteto-mode/SKILL.md`。
- 模型 slug（`grok-4.7-xhigh-fast`、`claude-opus-5-5-xhigh`）→ 说明由 WorkBuddy 自动选模型与 effort，无需配置。
- `deslop` / `control-cli` / `control-ui`（Cursor `cursor-team-kit` 插件）→ 分别用 `unslop` 技能、`workbuddy-browser-use` 能力替代。
- `/loop`、`/setup-pstack`、`create-skill` 等 Cursor 专属命令 → 改写或标注 WorkBuddy 对应方案。

> 注意：`statechart` 与 `poteto-mode/scripts/` 自带 TypeScript 工程，运行前需 `npm install` 及 Node/bun 环境。

## 尚未移植（小众 / 非必需）

以下在 WorkBuddy 场景下基本用不上，刻意未搬：`setup-pstack`（别的 harness 安装器，已手动装完）、`ketchup` / `ketchup-video`（生成视频）、`make-bot-ui`、`recall`（WorkBuddy 自有记忆）、`create/maintain-verification-skill` 与 `create/maintain-formal-verification-skill`（造验证技能的脚手架）。

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

安装后**重启/刷新 WorkBuddy 会话**，技能即会出现在可用列表：

- 进入自动路由：「进入 poteto 模式」「按 pstack 方式做」「poteto 风格来一遍」
- 单独调用：「用 unslop 润色一下」「用 architect 给我设计」「用 principle-prove-it-works 的原则复查」

## 格式差异说明

WorkBuddy 的 `SKILL.md` frontmatter 字段：`name` / `version` / `display_name` / `description`(中文主描述) / `description_zh` / `description_en`。已剔除原版 Cursor 专属字段（`disable-model-invocation`、`icon`、`color`、`paths`），并为每个技能生成 `_skillhub_meta.json`。
