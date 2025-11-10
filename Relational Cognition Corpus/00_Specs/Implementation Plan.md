---
Type: Spec
Title: Implementation Plan for Node Standard
Version: 0.1
Status: draft
Tags: [#spec, #workflow]
---

Phases
1) Spec & templates (this commit)
2) Retrofit existing notes to standard
3) Deep extraction with page anchors
4) Build dashboards and semantic views
5) Review and refine

Immediate actions
- Add properties to existing Topic notes (type, status, importance, sources, relations)
- Create Publication records for each PDF
- Instantiate key Claim and Definition nodes referenced by multiple Topics
- Add tags per taxonomy

Dataview checks
- Missing properties report
```dataview
TABLE file.link WHERE !type OR !status OR !tags
```

- Orphaned nodes (no relations)
```dataview
TABLE file.link WHERE relations.broader = [] AND relations.related = [] AND relations.depends_on = []
```

- Claims without dependencies
```dataview
TABLE file.link, statement WHERE type="Claim" AND length(relations.depends_on)=0
```

Publishing notes
- Maintain a Changelog under Logs/
- Use review.next to schedule revisits on critical nodes