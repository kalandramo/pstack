---
name: "principle-migrate-callers-then-delete-legacy-apis"
version: "1.0.0"
display_name: "原则：先迁调用方再删旧 API"
description: "引入新内部 API 而旧调用方还在时：在同一波里迁移调用方并删除旧 API，而不是保留兼容层。"
description_zh: "引入新内部 API 而旧调用方还在时：在同一波里迁移调用方并删除旧 API，而不是保留兼容层。"
description_en: "Apply when introducing a new internal API while old callers still exist. Migrate callers and delete the old API in the same wave instead of preserving compatibility layers."
---

# Migrate Callers Then Delete Legacy APIs

- Update tests to assert the new contract, and delete tests that only protect pre-refactor implementation details

**When this applies:**
- No external users depend on backward compatibility
- The project can absorb coordinated breaking changes
- The new API is part of a simplification or refactor initiative
