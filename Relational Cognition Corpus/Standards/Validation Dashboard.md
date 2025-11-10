Title: Validation Dashboard (Dataview)

Instructions
- Use the following DataviewJS blocks in this note to audit node quality.

Missing Required Properties
```dataview
TABLE type, status, sources, file.link as Note
FROM "Relational Cognition Corpus/Topics"
WHERE !type OR !status OR !sources
SORT file.name ASC
```

Missing Relations
```dataview
TABLE broader, requires, related, file.link as Note
FROM "Relational Cognition Corpus/Topics"
WHERE (!broader AND !requires AND !related)
SORT file.name ASC
```

Needs Citation
```dataview
TABLE sources, pages, file.link as Note
FROM "Relational Cognition Corpus/Topics"
WHERE contains(status, "needs-citation") OR !sources OR !pages
SORT file.name ASC
```

In-Progress Nodes
```dataview
TABLE status, updated, tags, file.link as Note
FROM "Relational Cognition Corpus/Topics"
WHERE contains(status, "in-progress") OR contains(tags, "#in-progress")
SORT updated DESC
```

Requires → This Node (Inverse)
```dataview
TABLE requires, file.link as Note
FROM "Relational Cognition Corpus/Topics"
WHERE contains(requires, this.file.link)
```
# Open Tasks

- [ ] Normalize frontmatter across Topics & Publications (dv_type, type, status, tags)
- [ ] Ensure relations.broader/narrower/depends_on are present where applicable
- [ ] Add missing source_refs with page/section anchors for GRL and L&S
- [ ] Check Claims Dashboard for missing importance or status fields
- [ ] Review orphan nodes (no inbound/outbound relations)
