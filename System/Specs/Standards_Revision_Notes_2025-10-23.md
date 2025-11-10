---
type: Spec
status: active
importance: high
tags: [system/specs, tracking]
version: 1.0
created: 2025-10-24
updated: 2025-10-24
---

# Standards Revision Notes — 2025-10-23

Purpose: Summarize changes introduced by the revised standards/SOP and identify concrete actions to align the vault. This note does not modify any SOP/templates; it documents what changed and what to do.

---

## What Changed (Authoritative Sources)

1) Node Standard (AUTHORITATIVE VERSION 2.0)
- Location: System/Specs/Node Standard CORRECTED.md
- Status: Official, supersedes older versions that used `dv_type`
- Key shifts:
  - Frontmatter uses `type` rather than `dv_type`
  - Status values standardized: draft | in-progress | review | stable
  - Importance uses semantic values (low | medium | high | critical) rather than 1–5
  - Relations map remains typed and required for concept nodes
  - Emphasis on 5–6 typed relations and bidirectional links; See Also encouraged

2) Tags Taxonomy (AUTHORITATIVE VERSION 2.0)
- Location: System/Specs/Tags Taxonomy.md
- Status: Official, supersedes legacy namespaces
- Approved namespaces:
  - concept/*, chapter-*, math/*, method/*, system/*
- Deprecated namespaces:
  - node/*, domain/*, cat/*, logic/*, status/*, pedagogy/*
- Tag count guidance: min 3 (concept + chapter + domain), recommended 4–8

3) Relation Types
- Location: System/Specs/Relations - Relation Types.md
- Controlled keys unchanged: broader, narrower, related, depends_on, defines, defined_in, proves, about, uses, exemplifies, equivalent_to, contradicts
- Guidance: prefer typed relations; keep depends_on acyclic

---

## Immediate Alignment Actions

- New/edited concept nodes must:
  - Use `type`, `status`, `importance` (semantic), and approved tag namespaces
  - Include relations with 5–6 typed connections and See Also section
  - Set review.next when marking review/stable where practical

- Migration (incremental, as touched):
  - Replace deprecated tag namespaces with v2.0 tags
  - Migrate numeric importance → semantic (e.g., 3 → medium, 5 → critical)
  - Remove legacy `dv_type` in favor of `type`

- Tracking/logging remains append-only; do not alter SOP/templates.

---

## Notes on Scope and Caution

- Do not edit System/Templates/* or framework SOP files without explicit instruction.
- Apply revisions opportunistically during concept-node edits (no bulk rewrites without a plan).
- Record all changes in Project_Dashboard and Concept_Node_Task_Queues audit log.

---

## Next Concrete Task from Queue

- Fix missing frontmatter on 02_Concepts/Polynomial_Degree_and_Shape.md per Node Standard v2.0 and Tags Taxonomy v2.0 (identified in 2025-10-23 Batch C audit).

Actions to perform now:
- Add full YAML frontmatter (type: Topic, status: review, importance: high)
- Apply approved tags (concept/functions or concept/algebra; chapter-3; math/polynomials; method/analyzing)
- Add relations to existing nodes (e.g., What_IS_a_Polynomial, End_Behavior, Root_Multiplicity, Constructing_Polynomials_from_Roots, Finding_Polynomial_Roots, Graphing_Functions)
- Update Connections section links to existing notes; keep content intact otherwise
- Log changes in Dashboard and Queue
