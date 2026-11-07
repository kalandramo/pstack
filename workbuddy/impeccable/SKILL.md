---
name: impeccable
version: 1.0.0
display_name: Impeccable UI 去 AI 味检测器
description: 前端/UI 页面的 AI slop 检测与修正。调用 `npx impeccable detect` 按 62 条确定性规则（无需 LLM）发现 AI 设计味，并在生成或改动 UI 时据此修正。
description_zh: 前端/UI 页面的 AI slop 检测与修正。调用 `npx impeccable detect` 按 62 条确定性规则（无需 LLM）发现 AI 设计味，并在生成或改动 UI 时据此修正。
description_en: Deterministic AI-slop detector for web UI. Wraps `npx impeccable detect` (62 rules, no LLM) to flag and fix AI-generated design tells (purple gradients, nested cards, Inter font, cream palettes, em-dash overuse).
---

# Impeccable — UI 去 AI 味

Impeccable（[pbakaus/impeccable](https://github.com/pbakaus/impeccable)，Apache-2.0）的**确定性检测器**封装。它扫描 HTML / 目录 / URL，按 62 条规则（Rust 编译，无 LLM、无 API key）标记 "AI 设计味" 与排版质量问题。这是 pstack `unslop`（文字层）在 **UI 层** 的等价物——生成或改动任何前端界面时用来当最后一道闸。

## 何时用

任何涉及**前端 / UI / 网页 / H5 / 组件**生成或改动的场景：
- 生成落地页、dashboard、组件、营销页
- 审阅或改写别人（或模型）写的页面
- 作为 `poteto-mode` 的 **UI design** 剧本的收尾闸门

不要把它当万能设计器——它只负责"**不要什么**"（负面清单），"要什么"仍由人和设计意图决定。

## 调用方式（跨 harness 的 CLI，无需装进任何编码器）

```bash
# 扫描文件 / 目录 / URL；退出码 2=有 findings，0=干净，1=无法扫描
npx impeccable detect <path|dir|url>

# 机器可读
npx impeccable detect --json .

# 输出 GitHub Actions 标注（挂 CI 用）
npx impeccable detect --github src/

# 列出全部 62 条规则及 id / 描述
npx impeccable detect --list-rules

# 渲染后检测（低对比度、字号、滚动动画失败等运行时问题；需本机 Chrome/Edge）
npx impeccable detect http://localhost:5173
```

## 关键规则族（slop 类，最可识别的 AI UI 标志）

- **side-tab** — 卡片单侧粗色边。规则原文称其为"AI 生成 UI 最可识别的标志"。
- **icon-tile-stack** — 圆角小方块图标叠在标题正上方。
- **cream-palette** — 奶油色 / 米色页面背景（"反射式伸手就来的有品味 AI 底色"）。
- **overused-font** — Inter / Arial / 系统默认字体。
- **em-dash-overuse** — 破折号（—）饱和（约每 500 字符一个、≥8 个）才报；属 advisory，不拦 CI。
- **aphoristic-cadence** — "X. No Y." 这类对仗短句出现 ≥3 次。
- 其它：`flat-type-hierarchy`（层级未拉开）、`cramped-padding`（贴边内边距）、`marketing-buzzword`、`radial-halo`（径向光晕）等。
- **Quality 类**：低对比度（WCAG 硬指标，算失败）、跳级标题、tiny text。

完整清单以 `npx impeccable detect --list-rules` 为准（规则数随版本浮动，4.8.0 约 62 条）。

## 工作流（与生成配合）

1. 生成 / 改动 UI。
2. 跑 `npx impeccable detect <target>`。
3. 按 findings 修正：去掉单侧色边、换掉 Inter、拉开字号层级、去奶油底、收敛破折号、去营销套话。
4. 复扫直到 **0 findings**（或仅剩有正当理由的 advisory）。

## 边界与注意

- **这是 CLI 封装，需要本机有 Node 且能访问 npm registry。** 首次运行会下载自检二进制到 `~/.impeccable/bin/`（一次性）。
- **隐私 / telemetry**：impeccable 的 `init` 与"视觉世界抽取"会向 `impeccable.style` 发匿名记录。我们**只用 `detect`**（纯规则、无网络请求），但保险起见调用前先设：
  ```bash
  export DO_NOT_TRACK=1          # 或 IMPECCABLE_NO_TELEMETRY=1
  ```
- `detect` 对源码（HTML/JSX/TSX）只跑 pattern 规则；低对比度 / 字号等需渲染的规则只对 **URL** 生效——要查运行时问题就指向你的 dev server。
- **合理误报**用 ignore 机制处理：`npx impeccable ignores add-value overused-font Inter --reason "Brand font"`；单文件行内注释可豁免单条规则。

## 与 pstack 的关系

- `unslop`：文字 / 写作层的去 AI 味 → 本 skill 是 **UI / 视觉层** 的对应物。
- `technical-writing`：文档规范，互补。
- 在 `poteto-mode` 下，UI 类任务路由到 **UI design** 剧本，由该剧本调用本 skill 作为收尾闸门。
