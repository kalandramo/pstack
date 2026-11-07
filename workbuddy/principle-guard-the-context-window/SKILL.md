---
name: "principle-guard-the-context-window"
version: "1.0.0"
display_name: "原则：守护上下文窗口"
description: "上下文快满时（大输出、长文件、重复读取、扇出规划）：把大块工作路由给子代理；主线程只留摘要，不放原始负载。"
description_zh: "上下文快满时（大输出、长文件、重复读取、扇出规划）：把大块工作路由给子代理；主线程只留摘要，不放原始负载。"
description_en: "Apply when context is filling up: large outputs, long files, repeated reads, fan-out planning. Route bulk to subagents; keep summaries in the main thread, not raw payloads."
---

# Guard the Context Window

**Why:** Context overflow degrades reasoning quality, creates compression artifacts, and halts progress.

**Pattern:**
- **Size phases and cap scope.** Limit files per phase, set turn budgets, account for mechanism costs.
