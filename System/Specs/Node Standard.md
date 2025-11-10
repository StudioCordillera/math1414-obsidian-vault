---
dv_type: Spec
status: active
importance: 1
tags: [node/spec, system/specs]
---

Title: Node Standard

Purpose
- Define consistent frontmatter, tags, and typed relations for all notes in this vault.

Frontmatter (required keys)
- dv_type: Topic | Definition | Claim | Publication | Dashboard | Spec | Log
- status: draft | active | review | done
- importance: 1 (lowest) … 5 (highest)
- tags: short list of controlled tags (see Tags Taxonomy)

Frontmatter (recommended keys)
- sources: list of cite keys (e.g., [FongSpivak2019])
- source_refs: list of page/section anchors (e.g., ["§2", "Ch.2 p.41"]) 
- relations: map of relation-type → array of wiki links, e.g.
  relations:
    broader: [[Topics/Regular Logic and Graphical Regular Logic — Overview]]
    narrower: []
    related: []
    depends_on: []
    defines: []
    defined_in: []
    proves: []
    about: []
    uses: []
    exemplifies: []
    equivalent_to: []

Conventions
- Filename patterns:
  - Topics/<Topic Name>.md
  - Definitions/<Term>.md
  - Claims/<Short Statement>.md
  - Publications/<CiteKey>.md (optional; primary publication list lives in Publications Index)
- Topic notes are content-first: aggregate across multiple sources. Only mark single-source when the topic is genuinely single-sourced.
- Use typed relations instead of plain links when the relationship type is known.
- Prefer plural folders: Topics, Definitions, Claims, Publications, Dashboards, Logs.

Review cadence
- Add review.next: YYYY-MM-DD on active/high-importance notes
- Use Dashboards/QA - Node Compliance to surface missing fields and orphaned nodes

API note
- Obsidian and Dataview support YAML arrays/maps. Some APIs may require strings. We keep rich YAML here. If a tooling write requires strings, serialize temporarily and restore afterward.
