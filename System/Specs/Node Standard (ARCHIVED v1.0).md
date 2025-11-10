---
type: Spec
status: archived
importance: critical
tags:
  - system/specs
  - deprecated
  - archived
created: 2025-11-04
updated: 2025-11-04
superseded_by: "[[Node Standard]]"
archival_reason: "Replaced by Node Standard v2.0 - contains deprecated fields and tag namespaces"
---

# Node Standard (ARCHIVED - v1.0)

> **⚠️ DEPRECATED**: This specification has been superseded by [[Node Standard]] v2.0
> 
> **Archive Date**: 2025-11-04  
> **Replacement**: [[Node Standard]] (authoritative version)  
> **Reason**: Contains deprecated `dv_type` field and outdated tag namespaces

---

## Original Specification (Archived)

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

---

## Migration Notes

**Deprecated Elements**:
- `dv_type` field → replaced with `type`
- Tag namespaces `node/*` → replaced with `concept/*`
- Tag namespaces `domain/*` → replaced with `math/*`

**For Current Specification**: See [[Node Standard]]

---

**Archive Metadata**:
- **Original Creation**: ~2025-10-19
- **Archive Date**: 2025-11-04
- **Superseded By**: Node Standard v2.0
- **Archive Authority**: Audit-based revision implementation