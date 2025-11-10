---
dv_type: dashboard
---

## Claims by status and importance
```dataview
TABLE without id file.link as Claim, importance, status, sources
FROM "Relational Cognition Corpus/Claims"
WHERE dv_type = "claim"
SORT importance desc, file.name asc
```

## Claims lacking page refs
```dataview
TABLE without id file.link as Claim, sources, source_refs
FROM "Relational Cognition Corpus/Claims"
WHERE dv_type = "claim" AND (source_refs = null OR length(join(source_refs, ", ")) = 0)
```

## Claims by topic
```dataview
TABLE without id file.link as Claim, join(relations.about, ", ") as About
FROM "Relational Cognition Corpus/Claims"
WHERE dv_type = "claim"
GROUP BY About
```
