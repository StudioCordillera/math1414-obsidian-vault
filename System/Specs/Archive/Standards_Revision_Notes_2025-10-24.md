---
type: Log
status: active
importance: medium
tags: [system/specs, system/tracking]
created: 2025-10-24
updated: 2025-10-24
---
# Standards Revision Notes — 2025-10-24

Purpose: Summarize observed standards/SOP changes without modifying authoritative spec files.

Reviewed Documents
- System/Specs/Node Standard.md (Spec): uses dv_type/status/importance(1–5) and relations map example; appears to be legacy-style fields used for system/spec notes.
- System/Specs/Tags Taxonomy.md (AUTHORITATIVE v2.0): defines approved tag namespaces concept/*, chapter-*, math/*, method/*, system/*; deprecates node/*, domain/*, cat/*, logic/*, status/*, pedagogy/*.
- System/NEW_SESSION_START.md: entry guide emphasizes concept node frontmatter with type/status/importance and relations map; aligns with working practice across concept nodes.

Working Interpretation
- For concept nodes in 02_Concepts: continue using frontmatter keys: type, status, importance (semantic), tags (from Tags v2.0), and relations (typed arrays). Maintain 5–6 relations and acyclic depends_on.
- For system/spec files in System/Specs: do not edit. Node Standard spec remains the source of truth for structure guidance; Tags Taxonomy v2.0 is authoritative for tag namespaces.

Action Items Applied (no SOP/spec edits)
- Continue aligning concept nodes to: type/status/importance (string) + Tags v2.0 + 5–6 relations.
- Avoid deprecated tag namespaces; ensure minimum 3 tags per concept (concept/* + chapter-* + math/*; method/* as applicable).

Next
- Proceed with Chapter 3 concept node alignment per above; log all progress in dashboard and queue.
