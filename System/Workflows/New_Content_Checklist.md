---
type: Workflow
status: active
importance: critical
tags:
  - system/workflow
  - quality-assurance
  - checklist
sources:
  - "Quality_Assurance_Checklist"
  - "Node Standard v2.0"
standards_authority: "System/Specs/Node Standard v2.0"
reference_docs:
  - "[[System/STANDARDS_AUTHORITY|Standards Authority Hierarchy]]"
  - "[[Quality_Assurance_Checklist|Full QA SOP]]"
relations:
  broader:
    - "[[Quality_Assurance_Checklist]]"
  related:
    - "[[Migration_Procedure]]"
    - "[[Verification_Protocol]]"
created: 2025-11-16
updated: 2025-11-16
---

# ✅ NEW CONTENT CHECKLIST
**Purpose**: Quick daily validation for concept nodes  
**Time**: 3-5 minutes per node  
**Authority**: [[Node Standard v2.0]]

> **Note**: This is a streamlined checklist for daily use. For comprehensive QA, see [[Quality_Assurance_Checklist]].

---

## 🚀 QUICK START

### When to Use This Checklist
- ✅ Creating a new concept node
- ✅ Migrating a node to v2.0 standards
- ✅ Reviewing content before changing status
- ✅ Quality check before Phase gate

### Status Progression Requirements
- **Draft → In-Progress**: Sections A + B
- **In-Progress → Review**: Sections A + B + C
- **Review → Stable**: All sections (A + B + C + D)

---

## 📋 SECTION A: FRONTMATTER ESSENTIALS (2 min)

### Required Fields Present
- [ ] `type:` (Definition | Claim | Topic | Method | Publication)
- [ ] `status:` (draft | in-progress | review | stable)
- [ ] `importance:` (low | medium | high | critical)
- [ ] `tags:` (array with at least 2 tags)
- [ ] `sources:` (array, not empty)
- [ ] `relations:` (object with relationships)
- [ ] `created:` (YYYY-MM-DD)
- [ ] `updated:` (YYYY-MM-DD)

### No Deprecated Fields
- [ ] NO `dv_type:` field
- [ ] NO `dv_domain:` field
- [ ] NO other `dv_*` fields

**Quick Fix**: If deprecated fields found, remove them and ensure modern equivalents are present.

---

## 🏷️ SECTION B: TAG COMPLIANCE (1 min)

### Required Tags
- [ ] At least one `concept/*` tag (e.g., `concept/algebra`, `concept/functions`)
- [ ] At least one `math/*` OR `chapter-*` tag
- [ ] NO deprecated tags: `node/*`, `domain/*`, `status/*`

### Common Tag Migrations
| ❌ Old (Deprecated) | ✅ New (v2.0) |
|---------------------|---------------|
| `node/definition` | `concept/[topic]` |
| `node/method` | `method/[technique]` or `concept/[topic]` |
| `node/claim` | `concept/[topic]` |
| `node/topic` | `concept/[topic]` |
| `domain/algebra` | `math/algebra` |
| `domain/functions` | `math/functions` |
| `domain/analysis` | `math/analysis` |
| `status/draft` | Remove (use frontmatter `status:` field) |

**Quick Fix**: Replace deprecated tags with modern equivalents from table above.

---

## 📝 SECTION C: CONTENT QUALITY (1 min)

### Structure Check
- [ ] Content matches `type:` field (Definition has definition, etc.)
- [ ] At least 1 meaningful example present
- [ ] Clear, readable formatting
- [ ] No placeholder text (e.g., "TBD", "TODO")

### Accuracy Check
- [ ] Math notation correct
- [ ] Cross-references use correct `[[Node_Name]]` format
- [ ] No broken links
- [ ] Citations match source list

**Quick Fix**: If content is incomplete, set `status: in-progress` or `status: draft`.

---

## 🔗 SECTION D: RELATIONSHIPS (1 min)

### Minimum Requirements
- [ ] At least **3 relationships** present
- [ ] All linked nodes actually exist
- [ ] Relationship types used correctly:
  - `broader`: Parent concepts (more general)
  - `narrower`: Child concepts (more specific)
  - `depends_on`: Prerequisites needed
  - `related`: Connected concepts (same level)
  - `used_in`: Where this concept is applied

### Bidirectional Check (Sampling)
- [ ] Pick 2 random relationships
- [ ] Open linked nodes
- [ ] Verify reverse relationship exists

**Quick Fix**: If relationships sparse (< 3), add at least 1-2 more before advancing status.

---

## ⚡ COMMON ISSUES & QUICK FIXES

### Issue 1: Missing Required Fields
**Symptoms**: Dashboard shows node in "incomplete" list  
**Fix**: Add missing fields with sensible defaults:
```yaml
type: Definition
status: draft
importance: medium
tags:
  - concept/[your-topic]
  - math/[your-domain]
sources: ["textbook-ch1"]
relations:
  broader: []
  narrower: []
  depends_on: []
  related: []
```

### Issue 2: Deprecated Tags
**Symptoms**: Dashboard shows node in "deprecated tags" list  
**Fix**: Use table in Section B to migrate tags

### Issue 3: Sparse Relationships
**Symptoms**: Node feels isolated, dashboard shows low density  
**Fix**: 
1. Look at content - what concepts are mentioned?
2. Link to 2-3 mentioned concepts
3. Check those concepts for potential reverse links

### Issue 4: Status Mismatch
**Symptoms**: Status doesn't match content completeness  
**Fix**: Adjust status to match reality:
- Incomplete content → `draft` or `in-progress`
- Complete but not verified → `review`
- Verified and stable → `stable`

---

## 🎯 CERTIFICATION

### Self-Certification Statement
After completing checklist:

**For Status Advancement**:
> "I certify this node meets v2.0 standards for [target status] level and has been validated against all applicable sections (A-D) of the New Content Checklist."

**Record in Node Frontmatter** (optional):
```yaml
review:
  last: 2025-11-16
  next: 2025-12-16
  cadence: monthly
qa_certified: true
qa_date: 2025-11-16
```

---

## 📊 BATCH CHECKING

### For Multiple Nodes
When checking many nodes (e.g., during migration):

1. **Batch Section A** (all nodes):
   - Run dashboard query to find missing required fields
   - Fix all at once

2. **Batch Section B** (all nodes):
   - Run dashboard query to find deprecated tags
   - Fix systematically using migration table

3. **Individual C + D** (per node):
   - Check content and relationships individually
   - Can't be batch-automated

**Time Estimate**: 
- Batch A+B: ~10-15 nodes/hour
- Individual C+D: ~8-10 nodes/hour
- **Total**: ~5-7 complete nodes/hour

---

## 🔄 WORKFLOW INTEGRATION

### Daily Workflow
1. Create/edit node
2. Run checklist Sections A-B immediately
3. Complete content (Section C)
4. Add relationships (Section D)
5. Advance status if all sections pass
6. Record QA date in frontmatter

### Migration Workflow
1. Open node to migrate
2. Run checklist Section A (deprecated fields)
3. Run checklist Section B (deprecated tags)
4. Verify Section C (content quality)
5. Verify Section D (relationships)
6. Update `updated:` date
7. Mark as migrated in [[Migration_Inventory]]

### Review Workflow
1. Open node for review
2. Run full checklist (A-D)
3. Note any issues
4. Fix issues
5. Re-run checklist
6. If passes: advance to `stable`
7. If fails: downgrade to appropriate status

---

## 📖 REFERENCE

### Quick Links
- [[Node Standard v2.0]] - Full specification
- [[Quality_Assurance_Checklist]] - Comprehensive SOP
- [[Standards_Compliance_Dashboard]] - Live metrics
- [[Migration_Inventory]] - Node tracking
- [[Tags Taxonomy]] - Approved tag list

### Status Definitions
- **draft**: Initial creation, structure only
- **in-progress**: Content being developed
- **review**: Content complete, needs verification
- **stable**: Verified, complete, meets all standards

### Relationship Types Quick Reference
- **broader**: More general parent concepts
- **narrower**: More specific child concepts
- **depends_on**: Prerequisites required to understand this
- **related**: Connected concepts at same level
- **used_in**: Applications of this concept
- **defines**: Concepts this node formally defines

---

**Checklist Version**: 1.0  
**Last Updated**: 2025-11-16  
**Authority**: [[Node Standard v2.0]]  
**Maintenance**: Update when Node Standard changes
