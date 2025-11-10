---
dv_type: Spec
status: active
importance: 1
tags: [node/spec, system/specs]
---

Title: Relations - Relation Types

Controlled relation vocabulary
- broader, narrower, related
- depends_on (prerequisite, logical or conceptual)
- defines (Definition → Topic/Claim)
- defined_in (Definition ← Topic/Publication/Section)
- proves (Claim → Topic or Claim)
- about (Claim → Topic/Definition)
- uses (Topic/Claim → Definition/Topic)
- exemplifies (Example → Topic/Definition)
- equivalent_to (Claim/Definition ↔ Claim/Definition)
- contradicts (Claim ↔ Claim)

Guidelines
- Prefer typed relations over bare links when the semantics are known.
- Keep relations acyclic for depends_on where possible.
- Aggregate multi-source content at Topic nodes; attach page anchors in source_refs.
