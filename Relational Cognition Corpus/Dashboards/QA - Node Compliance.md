---
dv_type: Dashboard
status: active
importance: 2
tags: [node/dashboard, system/qa]
---

## Missing required frontmatter
```dataview
TABLE file.name AS Note, dv_type, status, importance
WHERE !dv_type OR !status OR !importance
SORT file.name ASC
```

## Orphan nodes (no outbound typed relations)
```dataview
TABLE file.name AS Note, relations
WHERE dv_type AND (!relations OR length(keys(relations)) = 0)
SORT file.name ASC
```

## Missing sources or refs on Definitions/Claims
```dataview
TABLE file.name AS Note, sources, source_refs
WHERE dv_type IN ("Definition", "Claim") AND (!sources OR !source_refs)
SORT file.name ASC
```

- [ ] Merge duplicate claim filename: keep Graphical Rules - Nesting, Breaking, Monotonicity; deprecated redirect exists for em-dash variant.
- [ ] Ensure all Topics have dv_type, status, importance, tags, sources, source_refs, relations.
- [ ] Ensure all Publications have cite_key, file_path, status, tags.
- [ ] Add page/section anchors to: IntRel forms a po-category; R_P is Regular; Free Regular Category - Adjunction; Free Regular Po-Category - Adjunction; Fundamental Lemma.
- [ ] Normalize any API-sensitive frontmatter temporarily when patching via API; restore rich YAML as needed.
