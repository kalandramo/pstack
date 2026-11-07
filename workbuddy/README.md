# pstack × WorkBuddy 移植版

本目录是 [backnotprop/pstack](https://github.com/backnotprop/pstack)（Poteto 的 AI 严谨工程方法论技能集）中**已移植**的 49 个技能，针对 **WorkBuddy** 技能格式做的移植：

- **17 个独立技能**（自包含，不依赖其他技能）
- **24 条工程原则**（`principle-*`，每条一条规则，是方法论骨架）
- **6 个依赖型技能**（`why` `teach` `technical-writing` `architect` `blast-radius` `no-comments`）
- **1 个自动路由元技能**（`poteto-mode`：总路由 + 24 个 playbook 剧本 + 子代理定义，实现"说一句需求自动选剧本编排子代理"）
- **1 个 UI 去 AI 味封装技能**（`impeccable`：封装 `npx impeccable detect` 的 62 条确定性规则引擎，是 `unslop` 在 **UI 层** 的等价物，已接入 `poteto-mode` 自动路由）

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
- `playbooks/`（24 个剧本）：Investigation、Bug fix、Perf issue、Hillclimb、Feature、Refactoring、Prototype、Visual parity、**UI design**（impeccable 去 AI 味闸门）、Eval、Babysit、Shipping、Autonomous run、Orchestrate、Autopilot-full/stack、Session pickup、Pause safely、Multi-phase plan、Worktree cleanup、Opening a PR 等。
- `references/`：`bugbot-triage.md`（评审意见分类）、`poteto-agent.md` 与 `comment-sicko.md`（原仓库 `agents/` 下的两个子代理定义，并入此处）。
- `scripts/`（可选）：PR 监控等 TS 工程（`watch-pr/`、`check-plan.mjs`、`worktree-audit.sh`），运行需 Node/bun 环境。

**针对 WorkBuddy 的改写点**：

- 子代理 `poteto-agent`（Cursor 注册式）→ 改为 WorkBuddy `Agent` 工具（`subagent_type: general-purpose`），每个子代理 prompt 开头先完整阅读 `~/.workbuddy/skills/poteto-mode/SKILL.md`。
- 模型 slug（`grok-4.7-xhigh-fast`、`claude-opus-5-5-xhigh`）→ 说明由 WorkBuddy 自动选模型与 effort，无需配置。
- `deslop` / `control-cli` / `control-ui`（Cursor `cursor-team-kit` 插件）→ 分别用 `unslop` 技能、`workbuddy-browser-use` 能力替代。
- `/loop`、`/setup-pstack`、`create-skill` 等 Cursor 专属命令 → 改写或标注 WorkBuddy 对应方案。

> 注意：`statechart` 与 `poteto-mode/scripts/` 自带 TypeScript 工程，运行前需 `npm install` 及 Node/bun 环境。

## impeccable：UI 去 AI 味（已接入自动路由）

[pbakaus/impeccable](https://github.com/pbakaus/impeccable)（Apache-2.0）是确定性 AI-slop 检测器：扫描 HTML / 目录 / URL，按 62 条规则（Rust 编译，无 LLM、无 API key）标记"AI 设计味"（紫色渐变、卡片套卡片、Inter 字体、奶油底、破折号饱和等）。本移植**不搬**其完整的 `/impeccable` harness skill（PRODUCT.md / DESIGN.md / 24 命令 / 编辑 hook，对 WorkBuddy 过重且 hook 有 telemetry），而是做成一层薄封装 skill，只调用跨 harness 的 `npx impeccable detect`：

```bash
export DO_NOT_TRACK=1            # 关闭匿名 telemetry 记录（仅 detect 本身无需网络）
npx impeccable detect <path|dir|url>   # 退出码 2=有 findings，0=干净，1=无法扫描
```

**自动路由**：在 `poteto-mode` 路由表新增 **UI design / frontend polish** 条目，并新增 `playbooks/ui-design.md` 剧本——当用户说「设计一个落地页 / 做个 dashboard / 改这个组件」时，`poteto-mode` 自动匹配该剧本，生成或评审界面后调用 `impeccable` 技能跑 `detect`、修正被标记的 AI 味、复扫直到干净。`Feature` 剧本也加了交叉引用：若功能包含 Web/UI 界面，收尾前先过 `impeccable` 闸门。

它和 pstack 的关系：`unslop` 管**文字**层去 AI 味，`impeccable` 管 **UI / 视觉**层，两者互补。

## 尚未移植（小众 / 非必需）

以下在 WorkBuddy 场景下基本用不上，刻意未搬：`setup-pstack`（别的 harness 安装器，已手动装完）、`ketchup` / `ketchup-video`（生成视频）、`make-bot-ui`、`recall`（WorkBuddy 自有记忆）、`create/maintain-verification-skill` 与 `create/maintain-formal-verification-skill`（造验证技能的脚手架）。

## 安装

本仓库同时提供两套格式，按你用的 harness 选对应安装方式。

### A. WorkBuddy 用户（推荐）

一键安装 + 自动校验（幂等、不破坏其他技能如 `superpowers`）：

```bash
python3 workbuddy/manage_skills.py install
```

仅复制（`cp`）：

```bash
cp -R workbuddy/* ~/.workbuddy/skills/
```

软链（方便随本仓库更新）：

```bash
for d in workbuddy/*/; do
  ln -s "$(pwd)/$d" ~/.workbuddy/skills/"$(basename "$d")"
done
```

### B. Claude Code / Cursor / OpenCode 用户（agentskills.io 原生）

根目录 `skills/` 仍是原版 agentskills.io 格式，可直接用 skillhub 工具安装：

```bash
npx skills add kalandramo/pstack          # 默认扫根 skills/（agentskills.io 格式）
npx skills add -g kalandramo/pstack       # 装到全局
```

### C. 用 skillhub 工具拉取 WorkBuddy 版

本仓库根目录有 `skillhub.json` 清单（目录化 `workbuddy/` 下 49 个技能）。若想用 `npx skills add` 精确拉取 WorkBuddy 版目录：

```bash
npx skills add https://github.com/kalandramo/pstack/tree/workbuddy-port/workbuddy
```

> 注意：`npx skills add` 属于 agentskills.io 生态，会把技能装到对应 harness 的技能目录（`.claude/skills`、`.cursor/skills` 等），**并不认识 WorkBuddy 的 `~/.workbuddy/skills`**。所以 WorkBuddy 用户请优先用上面的 **方式 A**（`manage_skills.py` 直接装入 `~/.workbuddy/skills`）。

安装后**重启/刷新 WorkBuddy 会话**，技能即会出现在可用列表：

- 进入自动路由：「进入 poteto 模式」「按 pstack 方式做」「poteto 风格来一遍」
- 单独调用：「用 unslop 润色一下」「用 architect 给我设计」「用 principle-prove-it-works 的原则复查」

## 校验工具 `manage_skills.py`

仓库根 `workbuddy/manage_skills.py` 是纯标准库的单文件 CLI，管理这套移植包：

| 命令 | 作用 |
|------|------|
| `install` | 幂等复制 `workbuddy/*` 到 `~/.workbuddy/skills/`，装后自动 `validate` |
| `validate` | 校验已安装技能：`SKILL.md` frontmatter 必含 `name/version/display_name/description/description_zh/description_en` + `_skillhub_meta.json` 合法 |
| `status` | 只读报告：已装 / 未装 / 孤儿 / 外来（如 `superpowers`） |
| `lint` | 校验**源目录** `workbuddy/` 的 frontmatter+meta（CI / 提交前用，不需先安装） |

CI（`.github/workflows/validate.yml`）在每次 push/PR 到 `workbuddy-port` 时自动跑 `lint`，frontmatter 或 meta 不合规会让流水线变红。

## 格式差异说明

WorkBuddy 的 `SKILL.md` frontmatter 字段：`name` / `version` / `display_name` / `description`(中文主描述) / `description_zh` / `description_en`。已剔除原版 Cursor 专属字段（`disable-model-invocation`、`icon`、`color`、`paths`），并为每个技能生成 `_skillhub_meta.json`。根目录 `skillhub.json` 是供 skillhub 发现/发布的清单（指向 `workbuddy/*`）。
