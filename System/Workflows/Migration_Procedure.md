---
type: Workflow
status: active
importance: critical
tags:
  - system/workflow
  - migration
  - procedures
sources:
  - "Node Standard v2.0"
  - "Migration_Inventory"
standards_authority: "System/Specs/Node Standard v2.0"
reference_docs:
  - "[[System/STANDARDS_AUTHORITY|Standards Authority Hierarchy]]"
  - "[[New_Content_Checklist|QA Checklist]]"
relations:
  broader:
    - "[[RESTORATION_MASTER_DASHBOARD]]"
  related:
    - "[[New_Content_Checklist]]"
    - "[[Verification_Protocol]]"
    - "[[Migration_Inventory]]"
created: 2025-11-16
updated: 2025-11-16
---

# 🔄 MIGRATION PROCEDURE
**Purpose**: Step-by-step guide for migrating nodes to v2.0 standards  
**Time**: 5-8 minutes per node  
**Authority**: [[Node Standard v2.0]]

---

## 🎯 OVERVIEW

### What This Procedure Covers
- Migrating nodes with deprecated tags (`node/*`, `domain/*`)
- Updating frontmatter to v2.0 standards
- Verifying relationship integrity
- Quality assurance certification
- Recording migration completion

### What This Does NOT Cover
- Creating new content (use templates)
- Major content rewrites (separate task)
- Bidirectional link repairs (separate procedure)

### Success Criteria
✅ Node passes all sections of [[New_Content_Checklist]]  
✅ No deprecated fields or tags  
✅ All relationships verified  
✅ Migration recorded in [[Migration_Inventory]]

---

## 📋 PRE-MIGRATION CHECKLIST

### Before You Start
- [ ] [[Migration_Inventory]] open for reference
- [ ] [[New_Content_Checklist]] open for validation
- [ ] [[Standards_Compliance_Dashboard]] open to verify baseline
- [ ] Node identified from Migration Inventory as needing migration

### Information to Gather
1. **Current node name**: _________________
2. **Current importance**: _________________
3. **Deprecated issues**: _________________
4. **Phase assignment**: Phase 2 / Phase 3

---

## 🚀 MIGRATION STEPS

### STEP 1: Open and Review Node (1 min)

1. Open the node file in editor
2. Review frontmatter for issues
3. Note any deprecated elements:
   - [ ] `node/*` tags present?
   - [ ] `domain/*` tags present?
   - [ ] `dv_type:` field present?
4. Scan content for quality (no action yet, just awareness)

---

### STEP 2: Fix Deprecated Tags (2-3 min)

#### Tag Migration Reference Table

| ❌ Deprecated Tag | ✅ Replacement | Notes |
|-------------------|----------------|-------|
| `node/definition` | `concept/[topic]` | Use specific topic area |
| `node/method` | `method/[technique]` OR `concept/[topic]` | Use `method/*` for procedures |
| `node/claim` | `concept/[topic]` | Theorems, properties |
| `node/topic` | `concept/[topic]` | Overview/synthesis notes |
| `domain/algebra` | `math/algebra` | Direct replacement |
| `domain/functions` | `math/functions` | Direct replacement |
| `domain/analysis` | `math/analysis` | Direct replacement |
| `domain/cat` | `math/category-theory` | Direct replacement |
| `status/draft` | **REMOVE** | Use `status:` field instead |
| `status/stable` | **REMOVE** | Use `status:` field instead |

#### Migration Process

**If tags are in array format:**
```yaml
# BEFORE (deprecated)
tags:
  - node/definition
  - domain/functions
  - chapter-2

# AFTER (v2.0 compliant)
tags:
  - concept/functions
  - math/functions
  - chapter-2
```

**If tags are in inline format:**
```yaml
# BEFORE (deprecated)
tags: [node/method, domain/algebra, pedagogy/exercise]

# AFTER (v2.0 compliant)
tags:
  - method/problem-solving
  - math/algebra
  - pedagogy/exercise
```

**Action Steps:**
1. Locate `tags:` section in frontmatter
2. Identify deprecated tags using table above
3. Replace with appropriate v2.0 tags
4. Ensure at least one `concept/*` tag remains
5. Ensure at least one `math/*` or `chapter-*` tag remains

---

### STEP 3: Verify Required Fields (1 min)

Check frontmatter has all required fields:

```yaml
---
type: [Definition|Claim|Topic|Method|Publication]
status: [draft|in-progress|review|stable]
importance: [low|medium|high|critical]
tags:
  - concept/[topic]
  - math/[domain]
  - [additional tags]
sources:
  - [cite key or reference]
source_refs:
  - "[citation details]"
relations:
  broader: []
  narrower: []
  depends_on: []
  related: []
  used_in: []
review:
  next: [YYYY-MM-DD]
  cadence: [weekly|monthly|semester]
created: [YYYY-MM-DD]
updated: [YYYY-MM-DD]
---
```

**If any required fields missing:**
- Add them with appropriate values
- For empty arrays, use `[]` rather than deleting the key
- For dates, use YYYY-MM-DD format

---

### STEP 4: Update Metadata (30 sec)

1. Update `updated:` field to today's date
2. If migration changes content significantly, update `review.next:` date
3. Verify `importance:` field is accurate
4. Verify `status:` field matches content completeness

```yaml
updated: 2025-11-16
review:
  next: 2025-12-16
  cadence: monthly
```

---

### STEP 5: Content Quality Spot Check (1 min)

Quick verification (not comprehensive edit):

- [ ] Definition/claim is clear and accurate
- [ ] At least 1 example present
- [ ] No placeholder text ("TBD", "TODO", etc.)
- [ ] Math notation renders correctly
- [ ] Cross-references use `[[Node_Name]]` format

**If major content issues found:**
- Note in status field: `status: in-progress`
- Flag for separate content review
- Continue migration (structural fixes separate from content fixes)

---

### STEP 6: Verify Relationships (1 min)

Check `relations:` section:

1. **Count relationships**: Should have ≥ 3 total
2. **Verify link format**: All use `[[Node_Name]]` format
3. **Check relationship types**:
   - `broader`: Parent concepts (more general)
   - `narrower`: Child concepts (more specific)  
   - `depends_on`: Prerequisites
   - `related`: Connected concepts
   - `used_in`: Applications

**If relationships sparse (< 3):**
- Review content for mentioned concepts
- Add 1-2 obvious relationships
- Flag for deeper relationship work in Phase 4

**If link format wrong:**
```yaml
# WRONG
related: [Complex Numbers, Quadratic Formula]

# RIGHT
related:
  - "[[Complex_Numbers]]"
  - "[[Quadratic_Formula]]"
```

---

### STEP 7: Run QA Checklist (1-2 min)

Open [[New_Content_Checklist]] and verify:

- [ ] **Section A**: Frontmatter essentials ✅
- [ ] **Section B**: Tag compliance ✅
- [ ] **Section C**: Content quality ✅
- [ ] **Section D**: Relationships ✅

**If any section fails:**
- Fix the issue
- Re-run that section
- Do not proceed until all sections pass

---

### STEP 8: Save and Verify (30 sec)

1. Save the file
2. Open [[Standards_Compliance_Dashboard]]
3. Verify node no longer appears in:
   - Deprecated `node/*` tags query
   - Deprecated `domain/*` tags query
   - Missing required fields query

**If still appears in dashboard:**
- Review previous steps
- Check for typos in tags
- Ensure all deprecated elements removed

---

### STEP 9: Record Migration (30 sec)

1. Open [[Migration_Inventory]]
2. Find node in table
3. Update its row:
   - Change `Compliance` from 🔴 to ✅
   - Update `Issues` to "None"
   - Add checkmark to phase progress section

**Example entry:**
```markdown
| Node_Name | Type | Status | Importance | ✅ Compliant | Phase 2 | 5 | 12.3 |
```

---

## ✅ POST-MIGRATION VERIFICATION

### Final Checks

After migration complete:

1. **Dashboard Check**:
   - [ ] Node removed from "Deprecated Tags" list
   - [ ] Node appears in "Fully Compliant" count
   - [ ] Compliance % increased

2. **Spot Test Relationships**:
   - [ ] Open 1 linked node
   - [ ] Verify reverse link exists or add it
   - [ ] Close and continue

3. **Migration Inventory Update**:
   - [ ] Node marked complete
   - [ ] Phase progress updated
   - [ ] Running tally incremented

### Quality Certification

Add to node frontmatter (optional but recommended):

```yaml
qa_certified: true
qa_date: 2025-11-16
qa_migration: v2.0
```

---

## 🔄 BATCH MIGRATION TIPS

### For Migrating Multiple Nodes

**Efficiency Strategy:**
1. **Batch Phase**: Fix all tag issues first (Steps 1-2)
   - Process 5-10 nodes in one session
   - Use find/replace for common patterns
   - ~3-4 min per node

2. **Individual Phase**: Verify content/relationships (Steps 5-6)
   - Do these one at a time
   - Can't be automated
   - ~2-3 min per node

3. **Verification Phase**: Run QA and record (Steps 7-9)
   - Batch verify in dashboard
   - Update inventory in one pass
   - ~1 min per node

**Time Estimates:**
- Single node (complete): 5-8 minutes
- Batch of 10 nodes (tags only): 30-40 minutes
- Batch of 10 nodes (complete): 60-80 minutes

### Priority Order

Migrate in this order:
1. **Critical importance** nodes first (exam material)
2. **High importance** nodes second (core concepts)
3. **Referenced frequently** nodes (high inlink count)
4. **Medium/Low importance** nodes last

---

## 🚨 COMMON ISSUES & SOLUTIONS

### Issue 1: Tag Migration Uncertainty

**Problem**: Not sure which new tag to use  
**Solution**: 
1. Read node content
2. Identify primary mathematical domain
3. Use most specific `concept/*` tag available
4. When in doubt, use parent topic
5. Check [[Tags Taxonomy]] for approved list

### Issue 2: Missing Sources

**Problem**: Node has no `sources:` field  
**Solution**:
```yaml
# If from textbook
sources: ["textbook-ch2"]
source_refs: ["Miller & Gerken §2.3"]

# If system-generated
sources: ["system"]

# If unknown
sources: ["legacy"]
```

### Issue 3: Relationships Don't Make Sense

**Problem**: Existing relationships seem wrong  
**Solution**:
- Don't delete existing relationships during migration
- Flag for separate relationship review
- Add note in node: `<!-- TODO: Review relationships -->`
- Continue migration

### Issue 4: Content is Outdated/Incorrect

**Problem**: Found errors during migration  
**Solution**:
- Migration ≠ content editing
- Set `status: in-progress`
- Add comment: `<!-- TODO: Update content -->`
- Complete structural migration
- Flag for content review separately

### Issue 5: Duplicate Tags

**Problem**: Tags list has duplicates or redundancies  
**Solution**:
```yaml
# BEFORE (redundant)
tags:
  - concept/functions
  - concept/algebra
  - math/functions
  - math/algebra
  - domain/functions  # also deprecated

# AFTER (cleaned)
tags:
  - concept/functions
  - math/functions
  - chapter-2
```
Keep most specific tags, remove deprecated and duplicates.

---

## 📊 TRACKING PROGRESS

### Daily Tracking

At end of each migration session:

1. Count nodes migrated: _______
2. Update [[Migration_Inventory]] progress counters
3. Check [[Standards_Compliance_Dashboard]] for improvement
4. Record in [[RESTORATION_MASTER_DASHBOARD]] daily log

### Weekly Tracking

Use [[Weekly_Progress_Template]] to report:
- Total nodes migrated this week
- Compliance % change
- Issues encountered
- Time per node (actual vs. estimate)

---

## 📖 REFERENCE

### Quick Links
- [[Node Standard v2.0]] - Full specification
- [[New_Content_Checklist]] - QA validation
- [[Migration_Inventory]] - Node tracking
- [[Standards_Compliance_Dashboard]] - Live metrics
- [[Tags Taxonomy]] - Approved tag list

### Tag Migration Quick Reference
```
node/definition     → concept/[topic]
node/method         → method/[technique] or concept/[topic]
node/claim          → concept/[topic]
node/topic          → concept/[topic]
domain/algebra      → math/algebra
domain/functions    → math/functions
domain/analysis     → math/analysis
status/*            → REMOVE (use status: field)
```

### Status Progression
- **draft**: Structure only, incomplete content
- **in-progress**: Content being developed
- **review**: Complete, needs verification
- **stable**: Verified and certified

---

**Procedure Version**: 1.0  
**Last Updated**: 2025-11-16  
**Authority**: [[Node Standard v2.0]]  
**Next Review**: After first 10 migrations
