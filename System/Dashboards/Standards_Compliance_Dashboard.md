---
type: Dashboard
status: active
importance: critical
tags:
  - system/dashboard
  - system/monitoring
  - standards-compliance
  - quality-assurance
standards_authority: "System/Specs/Node Standard v2.0"
reference_docs:
  - "[[System/STANDARDS_AUTHORITY|Standards Authority Hierarchy]]"
review:
  next: 2025-11-23
  cadence: weekly
created: 2025-11-16
updated: 2025-11-16
---

# 📊 STANDARDS COMPLIANCE DASHBOARD
**Purpose**: Real-time monitoring of vault-wide standards compliance  
**Authority**: [[System/STANDARDS_AUTHORITY|Standards Authority]] → [[Node Standard v2.0]]  
**Last Updated**: 2025-11-16

---

## 🎯 COMPLIANCE OVERVIEW

### Overall Health Score
*Target: 100% compliance across all dimensions*

```dataview
TABLE WITHOUT ID
  "Standards Compliance" as "Metric",
  round((length(file.lists.status = "active") / length(file.lists)) * 100, 1) + "%" as "Score"
WHERE file.folder = "02_Concepts"
LIMIT 1
```

---

## 🔴 CRITICAL ISSUES

### 1. Deprecated Field Usage (`dv_type:`)

**Status**: 🔴 **BLOCKING ISSUE**  
**Target**: 0 nodes with deprecated fields  
**Impact**: Breaks standards compliance, causes confusion

```dataview
TABLE WITHOUT ID
  file.link as "File",
  dv_type as "Deprecated Field",
  type as "Current Type",
  importance as "Priority"
FROM "02_Concepts"
WHERE dv_type
SORT importance DESC, file.name ASC
```

**Count Query**:
```dataview
TABLE WITHOUT ID
  ("Total Deprecated Fields: " + length(rows)) as "Status"
FROM "02_Concepts"
WHERE dv_type
```

---

### 2. Deprecated Tag Namespaces

**Status**: 🔴 **HIGH PRIORITY**  
**Target**: 0 nodes with `node/*`, `domain/*`, or `status/*` tags  
**Impact**: Tag taxonomy violations

#### Deprecated `node/*` Tags
```dataview
TABLE WITHOUT ID
  file.link as "File",
  filter(file.tags, (t) => contains(t, "node/")) as "Deprecated Tags",
  importance as "Priority"
FROM "02_Concepts"
WHERE any(file.tags, (t) => contains(t, "node/"))
SORT importance DESC, file.name ASC
```

#### Deprecated `domain/*` Tags
```dataview
TABLE WITHOUT ID
  file.link as "File",
  filter(file.tags, (t) => contains(t, "domain/")) as "Deprecated Tags",
  importance as "Priority"
FROM "02_Concepts"
WHERE any(file.tags, (t) => contains(t, "domain/"))
SORT importance DESC, file.name ASC
```

#### Deprecated `status/*` Tags (should be in frontmatter)
```dataview
TABLE WITHOUT ID
  file.link as "File",
  filter(file.tags, (t) => contains(t, "status/")) as "Deprecated Tags",
  status as "Frontmatter Status"
FROM "02_Concepts"
WHERE any(file.tags, (t) => contains(t, "status/"))
SORT file.name ASC
```

**Count Summary**:
```dataview
TABLE WITHOUT ID
  "Metric" as "Deprecated Tag Type",
  "Count" as "Nodes Affected"
WHERE file = this.file
FLATTEN [
  ["node/* tags", length(filter(file.lists.file.tags, (t) => contains(t, "node/")))],
  ["domain/* tags", length(filter(file.lists.file.tags, (t) => contains(t, "domain/")))],
  ["status/* tags", length(filter(file.lists.file.tags, (t) => contains(t, "status/")))]
] as row
FLATTEN row[0] as "Metric"
FLATTEN row[1] as "Count"
```

---

## 🟡 TAG TAXONOMY COMPLIANCE

### 3. Required Tag Categories

**Status**: 🟡 **ATTENTION NEEDED**  
**Target**: 100% of concept nodes have required tags  
**Standard**: At least one `concept/*` + one `math/*` or `chapter-*` tag

#### Missing `concept/*` Tag
```dataview
TABLE WITHOUT ID
  file.link as "File",
  file.tags as "Current Tags",
  type as "Type",
  importance as "Priority"
FROM "02_Concepts"
WHERE !any(file.tags, (t) => contains(t, "concept/"))
SORT importance DESC, file.name ASC
```

#### Missing Math/Chapter Tag
```dataview
TABLE WITHOUT ID
  file.link as "File",
  file.tags as "Current Tags",
  type as "Type"
FROM "02_Concepts"
WHERE !any(file.tags, (t) => contains(t, "math/") OR contains(t, "chapter-"))
SORT file.name ASC
```

**Compliance Rate**:
```dataview
TABLE WITHOUT ID
  "Required Tags Compliance" as "Metric",
  round((length(filter(rows.file, (f) => 
    any(f.tags, (t) => contains(t, "concept/")) AND 
    any(f.tags, (t) => contains(t, "math/") OR contains(t, "chapter-"))
  )) / length(rows)) * 100, 1) + "%" as "Rate"
FROM "02_Concepts"
GROUP BY true
```

---

### 4. Tag Taxonomy Distribution

**Status**: 🟢 **INFORMATIONAL**  
**Purpose**: Understand current tag usage patterns

#### Concept Tags Distribution
```dataview
TABLE WITHOUT ID
  tag as "Concept Category",
  length(rows) as "Count"
FROM "02_Concepts"
FLATTEN file.tags as tag
WHERE contains(tag, "concept/")
GROUP BY tag
SORT length(rows) DESC
```

#### Math Tags Distribution
```dataview
TABLE WITHOUT ID
  tag as "Math Category",
  length(rows) as "Count"
FROM "02_Concepts"
FLATTEN file.tags as tag
WHERE contains(tag, "math/")
GROUP BY tag
SORT length(rows) DESC
```

#### Chapter Tags Distribution
```dataview
TABLE WITHOUT ID
  tag as "Chapter",
  length(rows) as "Count"
FROM "02_Concepts"
FLATTEN file.tags as tag
WHERE contains(tag, "chapter-")
GROUP BY tag
SORT tag ASC
```

---

## 🔗 RELATIONAL INTEGRITY

### 5. Bidirectional Link Verification

**Status**: 🔴 **HIGH PRIORITY**  
**Target**: 95%+ bidirectional integrity  
**Current Baseline**: ~65%

#### Nodes with Broken Bidirectional Links
```dataview
TABLE WITHOUT ID
  file.link as "File",
  length(file.outlinks) as "Outlinks",
  length(file.inlinks) as "Inlinks",
  round((length(file.inlinks) / (length(file.outlinks) + 0.001)) * 100, 0) + "%" as "Reciprocity"
FROM "02_Concepts"
WHERE length(file.outlinks) > 0
SORT (length(file.inlinks) / (length(file.outlinks) + 0.001)) ASC
LIMIT 30
```

**Bidirectional Integrity Rate**:
```dataview
TABLE WITHOUT ID
  "Average Reciprocity" as "Metric",
  round(average(rows.reciprocity), 1) + "%" as "Rate"
FROM "02_Concepts"
FLATTEN ((length(file.inlinks) / (length(file.outlinks) + 0.001)) * 100) as reciprocity
WHERE length(file.outlinks) > 0
GROUP BY true
```

---

### 6. Relationship Density

**Status**: 🟡 **BELOW TARGET**  
**Target**: 5.0 average relationships per node  
**Current Baseline**: 2.8 average

#### Relationship Density by Node
```dataview
TABLE WITHOUT ID
  file.link as "File",
  length(broader) + length(narrower) + length(depends_on) + length(related) + length(used_in) + length(defines) as "Total Relations",
  importance as "Priority"
FROM "02_Concepts"
WHERE type
SORT (length(broader) + length(narrower) + length(depends_on) + length(related) + length(used_in) + length(defines)) ASC
LIMIT 30
```

#### Nodes Below Minimum (< 3 relationships)
```dataview
TABLE WITHOUT ID
  file.link as "File",
  length(broader) + length(narrower) + length(depends_on) + length(related) + length(used_in) + length(defines) as "Relations",
  type as "Type",
  importance as "Priority"
FROM "02_Concepts"
WHERE (length(broader) + length(narrower) + length(depends_on) + length(related) + length(used_in) + length(defines)) < 3
SORT importance DESC
```

**Average Relationship Density**:
```dataview
TABLE WITHOUT ID
  "Average Relations per Node" as "Metric",
  round(average(rows.total_relations), 2) as "Average"
FROM "02_Concepts"
FLATTEN (length(broader) + length(narrower) + length(depends_on) + length(related) + length(used_in) + length(defines)) as total_relations
WHERE type
GROUP BY true
```

---

## 📋 FRONTMATTER COMPLETENESS

### 7. Required Fields Validation

**Status**: 🟡 **ATTENTION NEEDED**  
**Target**: 100% of nodes have all required fields  
**Required**: `type`, `status`, `importance`, `tags`, `sources`, `created`, `updated`

#### Missing Required Fields
```dataview
TABLE WITHOUT ID
  file.link as "File",
  choice(!type, "❌ type", "✅") as "Type",
  choice(!status, "❌ status", "✅") as "Status",
  choice(!importance, "❌ importance", "✅") as "Importance",
  choice(!tags OR length(tags) = 0, "❌ tags", "✅") as "Tags",
  choice(!sources, "❌ sources", "✅") as "Sources",
  choice(!created, "❌ created", "✅") as "Created"
FROM "02_Concepts"
WHERE !type OR !status OR !importance OR !tags OR length(tags) = 0 OR !sources OR !created
SORT file.name ASC
```

**Completeness Rate**:
```dataview
TABLE WITHOUT ID
  "Frontmatter Completeness" as "Metric",
  round((length(filter(rows.file, (f) => 
    f.type AND f.status AND f.importance AND f.tags AND length(f.tags) > 0 AND f.sources AND f.created
  )) / length(rows)) * 100, 1) + "%" as "Rate"
FROM "02_Concepts"
GROUP BY true
```

---

## 📊 STATUS DISTRIBUTION

### 8. Node Status Overview

**Status**: 🟢 **INFORMATIONAL**  
**Purpose**: Understand content maturity distribution

```dataview
TABLE WITHOUT ID
  status as "Status",
  length(rows) as "Count",
  round((length(rows) / 140) * 100, 1) + "%" as "Percentage"
FROM "02_Concepts"
WHERE status
GROUP BY status
SORT length(rows) DESC
```

---

## 🎯 IMPORTANCE DISTRIBUTION

### 9. Priority Categorization

**Status**: 🟢 **INFORMATIONAL**  
**Purpose**: Understand content priority distribution for migration planning

```dataview
TABLE WITHOUT ID
  importance as "Importance",
  length(rows) as "Count",
  round((length(rows) / 140) * 100, 1) + "%" as "Percentage"
FROM "02_Concepts"
WHERE importance
GROUP BY importance
SORT 
  choice(importance = "critical", 4,
  choice(importance = "high", 3,
  choice(importance = "medium", 2, 1))) DESC
```

---

## 📈 MIGRATION READINESS

### 10. Migration Priority Summary

**Status**: 🟢 **READY FOR PLANNING**  
**Purpose**: Identify Phase 2 and Phase 3 candidates

#### Critical + High Priority Nodes (Phase 2 Candidates)
```dataview
TABLE WITHOUT ID
  file.link as "File",
  type as "Type",
  importance as "Priority",
  choice(dv_type, "🔴 v1.0", "🟢 v2.0") as "Standards",
  length(broader) + length(narrower) + length(depends_on) + length(related) + length(used_in) + length(defines) as "Relations"
FROM "02_Concepts"
WHERE importance = "critical" OR importance = "high"
SORT importance DESC, file.name ASC
```

#### Medium + Low Priority Nodes (Phase 3 Candidates)
```dataview
TABLE WITHOUT ID
  file.link as "File",
  type as "Type",
  importance as "Priority",
  choice(dv_type, "🔴 v1.0", "🟢 v2.0") as "Standards"
FROM "02_Concepts"
WHERE importance = "medium" OR importance = "low"
SORT importance DESC, file.name ASC
LIMIT 50
```

---

## 🔄 DASHBOARD MAINTENANCE

### Update Schedule
- **Real-time**: All queries execute on dashboard view
- **Review**: Weekly during Phase 1 progress check
- **Baseline Recording**: Every phase transition

### Query Performance Notes
- Total queries: 25+
- Expected load: ~140 concept nodes
- Refresh: Automatic on file open

### Related Dashboards
- [[RESTORATION_MASTER_DASHBOARD|Master Project Dashboard]]
- [[Migration_Inventory|Migration Tracking]]

---

## 📖 INTERPRETATION GUIDE

### Health Indicators
- 🔴 **Critical/Blocking**: Must fix before phase completion
- 🟡 **Attention Needed**: Should fix during phase
- 🟢 **Informational**: Tracking only, no action needed

### Compliance Targets
- **Phase 1 End**: Monitoring operational (this dashboard)
- **Phase 2 End**: 60-70 nodes at 100% compliance
- **Phase 3 End**: All ~140 nodes at 100% compliance
- **Phase 4 End**: System-wide 100% compliance maintained

### Using This Dashboard
1. **Daily**: Check critical issues (sections 1-2)
2. **Weekly**: Review all compliance metrics (sections 1-7)
3. **Phase Transitions**: Document metrics in master dashboard
4. **Migration Planning**: Use section 10 for prioritization

---

**Dashboard Status**: ✅ Operational  
**Next Review**: 2025-11-23  
**Authority**: [[Node Standard v2.0]]
