---
Type: Spec
Title: Dataview Dashboards
Version: 0.1
Status: draft
Tags: [#spec, #dashboard]
---

Purpose
- Describe standard Dataview queries for project dashboards

Dashboards
- Topics Overview (Relational Cognition Corpus/Dashboards/Topics Overview.md)
  - Table: file.link, status, importance, length(file.outlinks)
  - FROM "Relational Cognition Corpus/Topics"
- Claims & Proof Dependencies (Relational Cognition Corpus/Dashboards/Claims.md)
  - Table: statement, status, length(relations.depends_on)
  - FROM "Relational Cognition Corpus/Claims"
- Extraction Queue (Relational Cognition Corpus/Extraction Queue.md)
  - Status histogram by source

Dataview snippets
```dataview
TABLE file.link, type, status, importance, sources
FROM "Relational Cognition Corpus"
WHERE type AND status
SORT importance DESC
```

```dataview
TABLE file.link AS Topic, relations.broader AS Broader, relations.narrower AS Narrower
FROM "Relational Cognition Corpus/Topics"
```

```dataview
TABLE file.link AS Claim, statement, relations.depends_on AS DependsOn
FROM "Relational Cognition Corpus/Claims"
WHERE status != "draft"
```

Notes
- Use DataviewJS for advanced graphs (typed edges) when needed
- Keep queries within folders to avoid noise from other vault sections