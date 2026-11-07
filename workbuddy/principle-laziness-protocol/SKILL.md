---
name: "principle-laziness-protocol"
version: "1.0.0"
display_name: "原则：懒惰协议"
description: "重构、评估 diff 大小、或想加抽象/层/信号透传时：偏向删除，偏向能解决问题的最小改动。"
description_zh: "重构、评估 diff 大小、或想加抽象/层/信号透传时：偏向删除，偏向能解决问题的最小改动。"
description_en: "Apply when refactoring, evaluating diff size, or tempted to add abstractions, layers, or signal threading. Bias toward deletion and the smallest change that solves the problem."
---

# Laziness Protocol

- **Consolidate decisions.** Do not repeat the same choice in several places. Put it behind one source of truth and pass the result as a simple flag.
- **Minimize the diff.** Make the smallest change that solves the problem. Fewer lines beat "elegant" boilerplate.
