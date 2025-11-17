---
type: Reference
status: active
importance: critical
tags:
  - system/reference
  - system/quick-start
created: 2025-11-16
updated: 2025-11-16
---

# 🚀 QUICK START: Chapter Extraction (LLM Onboarding)

**Purpose**: Fast reference for starting chapter extraction work with LLM  
**Time to Onboard**: < 5 minutes  
**Full Documentation**: [[System/ENTRY_POINT_Chapter_Concept_Extraction]]

---

## ⚡ FASTEST START (15 seconds)

**Copy-paste this prompt** → LLM discovers current work and starts:

```
VAULT: c:\Users\WORK_ADMIN\Documents\Obsidian Vault\

1. Read 00_Index/Dashboard.md - find current chapter
2. Read __USER_MANAGED__/Chapter*_Core_Set_Checklist.md for that chapter
3. Read System/Specs/Node Standard v2.0.md - learn format
4. Extract unchecked concepts to 02_Concepts/
5. Update checklist and dashboard as you go

RULES: NO node/*, domain/*, dv_type | Min 3 relations | Check duplicates

START: Read dashboard now.
```

**That's it.** The LLM self-orients from the dashboard and tracking files.

---

## 📋 FULL PROMPT (Complete Onboarding)

**Location**: `System/ZERO_SHOT_PROMPT_Chapter_Extraction.md`

**Instructions**:
1. Open the file above
2. Copy the entire prompt between ``` markers
3. Paste into new LLM conversation
4. Wait for acknowledgment
5. Begin extraction

---

## 🎯 CURRENT PROJECT STATE

| Chapter | Status | Concepts | Location |
|---------|--------|----------|----------|
| R-4 | ✅ Complete | 80+ | `02_Concepts/` |
| 5 | 🔄 In Progress | 15 stubs | `__USER_MANAGED__/Chapter5_Core_Set_Checklist.md` |
| 6-12 | ⏳ Not Started | 0 | N/A |

**Standards Compliance**: 100% (122/122 nodes v2.0)

---

## 📚 KEY DOCUMENTS (Priority Order)

### Read First (Essential):
1. `System/ENTRY_POINT_Chapter_Concept_Extraction.md` - **START HERE**
2. `__USER_MANAGED__/Chapter5_Core_Set_Checklist.md` - Current work list
3. `System/Specs/Node Standard v2.0.md` - Standards authority

### Reference During Work:
4. `System/Workflows/New_Content_Checklist.md` - QA validation
5. `System/Specs/Tags Taxonomy.md` - Approved tags
6. `System/Dashboards/Standards_Compliance_Dashboard.md` - Live metrics

### Supporting (As Needed):
7. `System/STANDARDS_AUTHORITY.md` - Conflict resolution
8. `System/SOPs/Quality_Assurance_Checklist.md` - Comprehensive QA
9. `System/Tracking/Phase_4_Completion_Summary.md` - Project history

---

## 🎓 CONCEPT EXTRACTION (7 Steps)

### Minimal Workflow:

1. **Pick Concept** from Chapter5_Core_Set_Checklist.md
2. **Check Existing** in `02_Concepts/[Name].md` (upgrade if exists)
3. **Write Content**: Definition, examples, LaTeX
4. **Map Relations**: Minimum 3 (broader, depends_on, related, used_in)
5. **Update Files**: Chapter note + checklist
6. **Run QA**: New_Content_Checklist validation
7. **Repeat** for next concept

---

## ✅ REQUIRED FRONTMATTER

```yaml
type: Definition | Claim | Topic | Method | Example
status: draft | in-progress | review | stable
importance: low | medium | high | critical
tags:
  - concept/[category]    # ✅ REQUIRED
  - math/[domain]         # ✅ REQUIRED
  - chapter-5             # ✅ RECOMMENDED
sources: ["textbook-ch5"]
relations:
  broader: []       # Parent concepts
  depends_on: []    # Prerequisites
  related: []       # Siblings
  used_in: []       # Applications
created: 2025-11-16
updated: 2025-11-16
```

---

## ❌ PROHIBITED ITEMS

**Never Use**:
- `node/*` tags → Use `concept/*`
- `domain/*` tags → Use `math/*`
- `status/*` tags → Use frontmatter `status:`
- `dv_type:` field → Use `type:`
- `dv_domain:` field → Remove entirely

**Never Do**:
- Create < 3 relationships
- Skip duplicate check
- Edit specs/standards files
- Advance status without QA

---

## 🎯 CHAPTER 5 PRIORITIES

### High Priority (Start Here):
1. `Augmented_Matrix` ⭐ (example in entry point)
2. `Gaussian_Elimination`
3. `Row_Operations`
4. `Row_Echelon_Form`
5. `Reduced_Row_Echelon_Form`

### Medium Priority:
6. `Linear_Systems`
7. `Equivalent_Systems`
8. `Matrix_Multiplication`
9. `Identity_Matrix`
10. `Inverse_Matrix`

### Applications:
11. `Determinant`
12. `Cramers_Rule`
13. `Systems_Applications`
14. `Homogeneous_Systems`
15. `Gauss_Jordan_Elimination`

---

## 📊 QUALITY GATES

### Before Status Change:

**draft → in-progress**:
- ✅ Complete frontmatter
- ✅ No deprecated tags/fields

**in-progress → review**:
- ✅ Content complete
- ✅ Minimum 3 relationships
- ✅ At least 1 example

**review → stable**:
- ✅ QA checklist passed
- ✅ Bidirectional links verified
- ✅ Cross-linked in chapter note

---

## 🆘 QUICK TROUBLESHOOTING

| Problem | Solution |
|---------|----------|
| Wrong tags | Check `System/Specs/Tags Taxonomy.md` |
| Duplicate concept | Search `02_Concepts/` first, upgrade existing |
| Too few relationships | Minimum 3: broader, depends_on, related |
| Status error | Run `System/Workflows/New_Content_Checklist.md` |
| Unknown standard | Use `System/Specs/Node Standard v2.0.md` (only one) |

---

## 🎯 SUCCESS CHECKLIST

After onboarding, verify LLM:
- [ ] Knows Chapter 5 is current focus (15 concepts)
- [ ] Uses Node Standard v2.0 as authority
- [ ] Follows 7-step extraction workflow
- [ ] Creates v2.0 compliant frontmatter
- [ ] Maps minimum 3 relationships
- [ ] Updates tracking documents
- [ ] Runs QA before status changes

---

## 🔗 NAVIGATION

**Main Entry Point**: [[System/ENTRY_POINT_Chapter_Concept_Extraction]]  
**Full Prompt**: [[System/ZERO_SHOT_PROMPT_Chapter_Extraction]]  
**Standards**: [[System/Specs/Node Standard v2.0]]  
**Current Work**: [[__USER_MANAGED__/Chapter5_Core_Set_Checklist]]  
**Dashboard**: [[System/Dashboards/Standards_Compliance_Dashboard]]

---

**Quick Start Version**: 1.0  
**Last Updated**: 2025-11-16  
**Read Time**: 2-3 minutes
