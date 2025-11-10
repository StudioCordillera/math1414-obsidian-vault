---
Type: Dashboard
Title: Topics Overview
Tags: [#dashboard]
---

```dataview
TABLE file.link AS Topic, status, importance, length(file.outlinks) AS Outlinks, relations.broader AS Broader, relations.narrower AS Narrower
FROM "Relational Cognition Corpus/Topics"
SORT importance DESC, file.name ASC
```

Missing properties
```dataview
TABLE file.link WHERE !type OR !status OR !tags
FROM "Relational Cognition Corpus/Topics"
```

Orphaned topics
```dataview
TABLE file.link WHERE relations.broader = [] AND relations.related = [] AND relations.depends_on = []
FROM "Relational Cognition Corpus/Topics"
```