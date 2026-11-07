---
name: "principle-redesign-from-first-principles"
version: "1.0.0"
display_name: "原则：第一性原理重设计"
description: "把新需求整合进既有设计时：从第一性原理重新设计。"
description_zh: "把新需求整合进既有设计时：从第一性原理重新设计。"
description_en: "Apply when integrating a new requirement into an existing design."
---

# Redesign From First Principles

When integrating a change, don't bolt it onto the existing design. Redesign as if the requirement had been a foundational assumption from the start.

- Read all affected files and understand the current design
- Ask: "if we were writing this from scratch with this new requirement, what would we build?"
- Propagate the change through every reference: types, docs, examples, rationale sections
- Think about the whole redesign, then deliver it incrementally

This is the method for preserving option value when integrating changes into an existing design.
