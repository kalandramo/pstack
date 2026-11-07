---
name: "principle-outcome-oriented-execution"
version: "1.0.0"
display_name: "原则：结果导向执行"
description: "在带明确阶段边界的计划重写/迁移中：向目标架构收敛，别用一次性兼容代码保平滑的中间态。"
description_zh: "在带明确阶段边界的计划重写/迁移中：向目标架构收敛，别用一次性兼容代码保平滑的中间态。"
description_en: "Apply during planned rewrites and migrations with explicit phase boundaries. Converge on the target architecture; don't preserve smooth intermediate states with throwaway compatibility code."
---

# Outcome-Oriented Execution

Optimize for the intended, verifiable end state rather than preserving smooth intermediate states.

**Why:** Keeping every intermediate step fully stable often creates temporary compatibility code that becomes long-lived debt. Converge on the target architecture and prove correctness at explicit verification boundaries.

**Core rule:**
- Prioritize end-state integrity over transitional stability
- Intermediate breakage is acceptable when it is planned, scoped, and reversible

**Guardrails:**
- Use this for planned rewrites and migrations with explicit phase boundaries
- Declare where temporary breakage is acceptable
- Keep high-signal checks for actively touched areas while migrating
- Require full static and runtime verification at plan completion
