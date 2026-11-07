---
name: "principle-subtract-before-you-add"
version: "1.0.0"
display_name: "原则：先减后加"
description: "安排新增/重构/重写顺序时：先删死代码、冗余校验器、桩引用，再在更简单的基底上构建。"
description_zh: "安排新增/重构/重写顺序时：先删死代码、冗余校验器、桩引用，再在更简单的基底上构建。"
description_en: "Apply when sequencing an addition, refactor, or rewrite. Remove dead code, redundant validators, and stub references first, then build on the simpler base."
---

# Subtract Before You Add

When evolving a system, remove complexity first, then build. Default to subtraction.

Make simplification a continual investment. Leave the design slightly simpler and more capable behind the same or smaller surface than you found it.

- Sequence removal before construction
- Cut before you polish (get to the minimum before investing in quality)
- Design for observed usage, not speculative edge cases
- No speculative validators, parsers, or guards beyond what the spec demands
- Simplify prompts (remove redundant instructions, excessive templates)
- When a reference has no novel content, delete it rather than leaving a stub
