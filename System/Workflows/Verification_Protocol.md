---
type: Workflow
status: active
importance: critical
tags:
  - system/workflow
  - verification
  - quality-assurance
sources:
  - "Node Standard v2.0"
  - "Quality_Assurance_Checklist"
standards_authority: "System/Specs/Node Standard v2.0"
reference_docs:
  - "[[System/STANDARDS_AUTHORITY|Standards Authority Hierarchy]]"
  - "[[New_Content_Checklist|QA Checklist]]"
relations:
  broader:
    - "[[Quality_Assurance_Checklist]]"
  related:
    - "[[New_Content_Checklist]]"
    - "[[Migration_Procedure]]"
created: 2025-11-16
updated: 2025-11-16
---

# ✓ VERIFICATION PROTOCOL
**Purpose**: Post-migration and post-edit node verification  
**Time**: 3-5 minutes per node  
**Authority**: [[Node Standard v2.0]]

---

## 🎯 WHEN TO USE THIS PROTOCOL

### Required Verification Points
- ✅ After migrating a node to v2.0
- ✅ Before advancing status from `review` to `stable`
- ✅ After significant content edits
- ✅ During Phase gate quality checks
- ✅ Quarterly maintenance reviews

### Optional Verification Points
- After minor edits (quick spot check)
- Before exam prep resource publication
- When quality concerns raised

---

## 📋 VERIFICATION CHECKLIST

### LEVEL 1: STRUCTURAL COMPLIANCE (1 min)

**Frontmatter Verification**

Run through required fields:

- [ ] `type:` field present and valid
- [ ] `status:` field present and appropriate
- [ ] `importance:` field present and accurate
- [ ] `tags:` array present with ≥ 2 tags
- [ ] `sources:` array present (not empty)
- [ ] `relations:` object present
- [ ] `created:` date present (YYYY-MM-DD format)
- [ ] `updated:` date present and current

**Deprecated Elements Check**

- [ ] NO `dv_type:` field
- [ ] NO `dv_*` fields of any kind
- [ ] NO `node/*` tags
- [ ] NO `domain/*` tags
- [ ] NO `status/*` tags

**Quick Fix**: If any deprecated elements found, this node was not properly migrated. Return to [[Migration_Procedure]].

---

### LEVEL 2: TAG TAXONOMY COMPLIANCE (1 min)

**Required Tag Structure**

- [ ] At least one `concept/*` tag present
- [ ] At least one `math/*` OR `chapter-*` tag present
- [ ] All tags use approved namespaces:
  - ✅ `concept/*`
  - ✅ `math/*`
  - ✅ `chapter-*`
  - ✅ `method/*`
  - ✅ `system/*` (system docs only)
  - ✅ `pedagogy/*` (optional)

**Tag Accuracy Check**

- [ ] Tags accurately describe node content
- [ ] Most specific appropriate tags used
- [ ] No redundant/duplicate tags
- [ ] No overly generic tags (e.g., just `concept/math`)

**Documentation**: If tags adjusted, note reason in node history comment.

---

### LEVEL 3: CONTENT QUALITY (1-2 min)

**Type-Specific Requirements**

For **Definition** nodes:
- [ ] Clear, precise definition statement
- [ ] At least 1 concrete example
- [ ] Key properties or characteristics listed
- [ ] Common misconceptions addressed (if applicable)

For **Claim** nodes (theorems, properties):
- [ ] Precise mathematical statement
- [ ] Conditions/hypotheses clear
- [ ] Proof or justification provided or referenced
- [ ] Examples demonstrating the claim

For **Method** nodes (procedures):
- [ ] Step-by-step procedure outlined
- [ ] At least 1 worked example
- [ ] Common errors/pitfalls noted
- [ ] When to use this method explained

For **Topic** nodes (overviews):
- [ ] Comprehensive overview of topic
- [ ] Key subtopics identified
- [ ] Connections between concepts explained
- [ ] Learning progression outlined

**General Content Standards**

- [ ] Mathematical notation correct and consistent
- [ ] Examples are clear and relevant
- [ ] Cross-references use `[[Node_Name]]` format
- [ ] No placeholder text ("TBD", "TODO", "XXX")
- [ ] Formatting clean and readable
- [ ] Citations match `sources:` list

**Content Issues Found**: 
- Minor issues: Fix now
- Major issues: Downgrade status to `in-progress`

---

### LEVEL 4: RELATIONSHIP VERIFICATION (1 min)

**Relationship Density**

- [ ] Node has ≥ 3 total relationships
- [ ] Relationships use correct `[[Link]]` format
- [ ] All linked nodes actually exist (no broken links)

**Relationship Type Accuracy**

- [ ] `broader`: Points to more general parent concepts ✓
- [ ] `narrower`: Points to more specific child concepts ✓
- [ ] `depends_on`: Points to prerequisite concepts ✓
- [ ] `related`: Points to connected concepts (same level) ✓
- [ ] `used_in`: Points to applications/contexts ✓

**Bidirectional Integrity Spot Check**

Pick 2 relationships at random:

1. **Relationship 1**: _______________
   - [ ] Open linked node
   - [ ] Verify reverse relationship exists
   - [ ] If missing: Add reverse relationship

2. **Relationship 2**: _______________
   - [ ] Open linked node
   - [ ] Verify reverse relationship exists
   - [ ] If missing: Add reverse relationship

**Relationship Quality**

- [ ] Relationships are logical and accurate
- [ ] No circular dependencies (A depends on B, B depends on A)
- [ ] Hierarchy makes sense (broader/narrower)
- [ ] Related concepts are truly related

**If Relationship Issues Found**:
- Fix obvious errors now
- Flag complex issues for separate relationship review
- Minimum 3 relationships must remain

---

### LEVEL 5: INTEGRATION CHECK (30 sec)

**System Integration**

- [ ] Node appears in [[Standards_Compliance_Dashboard]] as compliant
- [ ] Node listed correctly in [[Migration_Inventory]] (if migrated)
- [ ] Node doesn't appear in deprecated field queries
- [ ] Node doesn't appear in missing field queries

**Cross-System Verification**

Open [[Standards_Compliance_Dashboard]] and confirm:
- [ ] Not in "Deprecated dv_type" list
- [ ] Not in "Deprecated node/* tags" list
- [ ] Not in "Deprecated domain/* tags" list
- [ ] Not in "Missing required fields" list
- [ ] Not in "Sparse relationships (< 3)" list (or acceptably sparse)

**If Still Appears in Queries**:
- Refresh dashboard (may be cached)
- Review previous verification steps
- Ensure file saved properly
- Check for typos in tags/fields

---

## ✅ CERTIFICATION

### Self-Certification Statement

Upon passing all 5 levels:

> "I certify that this node:
> - Meets Node Standard v2.0 requirements
> - Contains no deprecated elements
> - Has accurate, appropriate tags
> - Meets content quality standards for its type
> - Has verified bidirectional relationships
> - Is properly integrated into the system
> 
> This node is ready for `stable` status."

**Signed**: [Your Name/Initials]  
**Date**: [YYYY-MM-DD]  
**Node**: [Node Name]

---

### Certification Recording

Add to node frontmatter:

```yaml
qa_certified: true
qa_date: 2025-11-16
qa_verifier: [your-initials]
certification_level: full  # full | structural-only | pending
```

Update node status if appropriate:

```yaml
status: stable  # if passed all checks
updated: 2025-11-16
review:
  last: 2025-11-16
  next: 2025-12-16
  cadence: monthly
```

---

## 🔄 VERIFICATION WORKFLOWS

### Post-Migration Verification

After using [[Migration_Procedure]]:

1. Run **Level 1** (Structural) - should pass 100%
2. Run **Level 2** (Tags) - should pass 100%
3. Run **Level 3** (Content) - quick spot check
4. Run **Level 4** (Relationships) - verify ≥ 3
5. Run **Level 5** (Integration) - check dashboard

**Time**: 3-5 minutes  
**Pass Criteria**: Levels 1-2 must be 100%, Level 4 minimum 3 relationships

---

### Status Advancement Verification

Before advancing `review` → `stable`:

1. Run **Full Protocol** (Levels 1-5)
2. All levels must pass
3. Content must be complete and accurate
4. Relationships must be bidirectional (spot check)
5. Add certification to frontmatter

**Time**: 5-7 minutes  
**Pass Criteria**: 100% on all levels

---

### Quarterly Maintenance Verification

For nodes in `stable` status:

1. Run **Level 1** (quick structural check)
2. Run **Level 3** (content accuracy check)
3. Run **Level 4** (relationship validity check)
4. Update `review.last` and `review.next` dates

**Time**: 2-3 minutes per node  
**Pass Criteria**: Content still accurate, links not broken

---

## 🚨 FAILURE HANDLING

### If Node Fails Verification

**Level 1 Failure** (Structural):
- Critical issue - must fix immediately
- Do not advance status
- Return to [[Migration_Procedure]]
- Re-verify after fixes

**Level 2 Failure** (Tags):
- Critical for compliance - must fix
- Use [[Migration_Procedure]] tag migration table
- Re-verify after fixes

**Level 3 Failure** (Content):
- **Minor issues**: Fix now, continue verification
- **Major issues**: 
  - Downgrade status to `in-progress`
  - Flag for content review
  - Complete structural verification
  - Schedule content improvement

**Level 4 Failure** (Relationships):
- **< 3 relationships**: Add 1-2 minimum, flag for deeper work
- **Broken links**: Fix immediately
- **Wrong relationship types**: Correct now
- **Missing reverse links**: Add to linked nodes

**Level 5 Failure** (Integration):
- Indicates previous level wasn't properly completed
- Review Levels 1-4 again
- Ensure file saved
- Check for hidden characters or formatting issues

---

## 📊 VERIFICATION METRICS

### Track Your Verification Work

**Daily Tracking**:
- Nodes verified today: _______
- Nodes passed: _______
- Nodes failed: _______
- Common failure type: _______

**Quality Metrics**:
- Average time per verification: _______ minutes
- Pass rate (first attempt): _______ %
- Most common issue: _______

**Report In**:
- [[RESTORATION_MASTER_DASHBOARD]] daily log
- [[Weekly_Progress_Template]] weekly summary
- Phase gate reports

---

## 🎯 BEST PRACTICES

### Verification Tips

1. **Do verification immediately after migration**
   - Catches issues while context fresh
   - Prevents error propagation

2. **Don't skip levels**
   - Each level builds on previous
   - Skipping wastes time on re-work

3. **Fix as you go**
   - Don't just note issues - fix them
   - Small fixes now prevent big problems later

4. **Verify in batches**
   - Do 5-10 migrations
   - Then verify the batch
   - Finds systematic errors

5. **Use dashboard for efficiency**
   - Dashboard shows all nodes at once
   - Batch-check compliance
   - Individual verification for content

### Common Verification Mistakes

❌ **Mistake 1**: Skipping bidirectional check  
✅ **Fix**: Always spot-check at least 2 relationships

❌ **Mistake 2**: Not checking dashboard integration  
✅ **Fix**: Always verify node removed from issue lists

❌ **Mistake 3**: Passing content with placeholders  
✅ **Fix**: Flag incomplete content, don't certify as stable

❌ **Mistake 4**: Not recording certification  
✅ **Fix**: Always add QA fields to frontmatter

---

## 📖 REFERENCE

### Quick Decision Tree

```
Node needs verification?
│
├─ Just migrated? → Run Levels 1-2-4-5 (skip 3 for now)
├─ Advancing status? → Run all Levels 1-5
├─ Quarterly review? → Run Levels 1-3-4
└─ Minor edit? → Run Level 1 + spot check Level 3
```

### Pass/Fail Criteria Summary

| Level | Must Pass | Can Flag for Later |
|-------|-----------|-------------------|
| 1. Structural | 100% | No |
| 2. Tags | 100% | No |
| 3. Content | Major issues only | Minor issues yes |
| 4. Relationships | ≥ 3 relationships | Density improvement |
| 5. Integration | Dashboard clean | No |

### Quick Links
- [[Node Standard v2.0]] - Full specification
- [[New_Content_Checklist]] - Quick daily QA
- [[Migration_Procedure]] - How to migrate
- [[Standards_Compliance_Dashboard]] - Live metrics
- [[Quality_Assurance_Checklist]] - Comprehensive SOP

---

**Protocol Version**: 1.0  
**Last Updated**: 2025-11-16  
**Authority**: [[Node Standard v2.0]]  
**Next Review**: After first 20 verifications
