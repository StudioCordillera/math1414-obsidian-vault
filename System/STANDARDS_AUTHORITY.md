---
type: Policy
status: active
importance: critical
tags:
  - system/policy
  - system/standards
  - authoritative
created: 2025-11-16
updated: 2025-11-16
---

# 🏛️ STANDARDS AUTHORITY HIERARCHY
**Purpose**: Establish single source of truth for all vault standards  
**Authority**: System-level policy  
**Effective Date**: 2025-11-16

---

## 📜 AUTHORITY DECLARATION

### PRIMARY STANDARD (Math 1414 Vault)
**Location**: `System/Specs/Node Standard v2.0.md`  
**Scope**: All content in Math 1414 Obsidian Vault  
**Version**: 2.0 (Current)  
**Status**: ✅ AUTHORITATIVE

**This document is the SINGLE SOURCE OF TRUTH for**:
- Concept node frontmatter structure
- Tag taxonomy requirements
- Relationship type definitions
- Content structure standards
- Quality assurance criteria

**Applies to**:
- All files in `02_Concepts/`
- All course materials in `01_Course/`
- All system documentation in `System/`
- All index files in `00_Index/`
- All templates in `System/Templates/`

---

## 🔬 THEORETICAL STANDARD (Separate Scope)
**Location**: `Relational Cognition Corpus/Standards/Node Spec.md`  
**Scope**: Academic corpus of category theory and relational cognition research  
**Status**: ✅ VALID (for corpus only)

**This document governs**:
- Theoretical publications in `Relational Cognition Corpus/Publications/`
- Theory topics in `Relational Cognition Corpus/Topics/`
- Formal definitions in `Relational Cognition Corpus/Definitions/`
- Theoretical claims in `Relational Cognition Corpus/Claims/`

**Does NOT apply to**: Math 1414 course content or concept nodes

---

## ❌ DEPRECATED STANDARDS (Deleted)

### Deleted Specifications:
- ~~`System/Specs/Node Standard (ARCHIVED v1.0).md`~~ - **To be deleted after Phase 2**
- ~~`Relational Cognition Corpus/00_Specs/`~~ - **DELETED 2025-11-17** (conflicting duplicates)
- ~~`00_Specs/RECOVERY.md`~~ - **DELETED 2025-11-17** (outdated)

**Policy**: Deprecated standards are DELETED, not archived, to prevent confusion and ensure clean migration.

---

## 🧭 DECISION FLOWCHART

### "Which Standard Do I Use?"

```
Are you creating/editing...
│
├─ Concept node in 02_Concepts/?
│  └─ USE: System/Specs/Node Standard v2.0 ✓
│
├─ Course material in 01_Course/?
│  └─ USE: System/Specs/Node Standard v2.0 ✓
│
├─ System document in System/?
│  └─ USE: System/Specs/Node Standard v2.0 ✓
│
├─ Theoretical publication in Relational Cognition Corpus/?
│  └─ USE: Relational Cognition Corpus/Standards/Node Spec ✓
│
└─ If unsure?
   └─ DEFAULT: System/Specs/Node Standard v2.0 ✓
```

---

## 📋 SUPPORTING SPECIFICATIONS

### Complementary Standards (All under System/Specs/):
| Document | Purpose | Authority Level |
|----------|---------|-----------------|
| **Node Standard v2.0** | Content structure | ⭐⭐⭐ PRIMARY |
| **Tags Taxonomy** | Approved tag list | ⭐⭐⭐ REQUIRED |
| **Relations - Relation Types** | Relationship definitions | ⭐⭐⭐ REQUIRED |

### Standard Operating Procedures (System/SOPs/):
| Document | Purpose | Authority Level |
|----------|---------|-----------------|
| **Quality_Assurance_Checklist** | Validation procedures | ⭐⭐ RECOMMENDED |
| **Compression_Methodology** | Content layering | ⭐ OPTIONAL (advanced) |
| **Review_Schedule_Management** | Maintenance tracking | ⭐⭐ RECOMMENDED |
| **Template_Maintenance_Workflow** | Template updates | ⭐⭐ RECOMMENDED |

---

## 🔄 STANDARDS EVOLUTION

### Version Control Policy:
1. **Major Changes** (breaking): Increment version number (v2.0 → v3.0)
2. **Minor Updates** (non-breaking): Update in place, note in changelog
3. **Clarifications**: Update immediately without version change

### Update Process:
1. Identify need for standards update
2. Draft proposed changes
3. Review impact on existing content
4. Update Node Standard v2.0
5. Update affected templates
6. Update this authority document
7. Communicate changes to all stakeholders

### Change Log:
| Date | Change | Version | Impact |
|------|--------|---------|--------|
| 2025-11-04 | Node Standard v2.0 created | 2.0 | Replaced v1.0 `dv_type` with `type` |
| 2025-11-16 | Authority hierarchy established | - | Clarified single source of truth |

---

## 🚨 CONFLICT RESOLUTION

### If Multiple Standards Disagree:

**Priority Order**:
1. `System/Specs/Node Standard v2.0` (Math 1414 vault)
2. `Relational Cognition Corpus/Standards/Node Spec` (theoretical corpus only)
3. Standard Operating Procedures (recommended practices)
4. Template examples (implementation guidance)

**Resolution Process**:
1. Identify the conflict
2. Check which scope applies (vault vs. corpus)
3. Apply appropriate standard
4. If still unclear: Use Node Standard v2.0 as default
5. Document decision and update standards if needed

---

## 📊 COMPLIANCE ENFORCEMENT

### Compliance Levels:
- **REQUIRED**: Must follow to be considered compliant
  - Node Standard v2.0 frontmatter requirements
  - Tag Taxonomy approved namespaces
  - Relation Types definitions

- **RECOMMENDED**: Should follow for quality
  - Quality Assurance procedures
  - Review Schedule management
  - Template usage

- **OPTIONAL**: May use for advanced features
  - Compression Methodology
  - Advanced relationship patterns

### Verification:
- Active compliance dashboard: `System/Dashboards/Standards_Compliance_Dashboard.md`
- Automated checking where possible
- Phase gate quality reviews
- Quarterly system audits

---

## 📖 REFERENCE GUIDE

### Quick Reference Card:

**For Concept Nodes (02_Concepts/)**:
```yaml
Standard: System/Specs/Node Standard v2.0
Required: type, status, importance, tags, sources, relations
Tags must use: concept/*, math/*, chapter-*, method/*
No deprecated: dv_type, node/*, domain/*
```

**For Course Materials (01_Course/)**:
```yaml
Standard: System/Specs/Node Standard v2.0
Applies same frontmatter requirements
Enhanced with: relational framework integration
Cross-link to: concept nodes extensively
```

**For System Documents (System/)**:
```yaml
Standard: System/Specs/Node Standard v2.0
Special tags: system/* namespace
Type values: Spec, SOP, Dashboard, Template, etc.
```

**For Theoretical Corpus (Relational Cognition Corpus/)**:
```yaml
Standard: Relational Cognition Corpus/Standards/Node Spec
Different scope: Academic publications
Frontmatter: Academic citation focus
Cross-references: Between publications
```

---

## ✅ STANDARDS AUTHORITY VALIDATION

### This Document Establishes:
- ✅ Single authoritative standard for Math 1414 vault
- ✅ Clear separation between vault and corpus standards
- ✅ Explicit deprecation and deletion of conflicting specs
- ✅ Decision flowchart for standard selection
- ✅ Conflict resolution procedures
- ✅ Compliance enforcement mechanisms

### Effectiveness:
**Effective immediately** for all new content and migrations.

### Review Schedule:
- **Next Review**: After Phase 2 completion (2025-12-21)
- **Routine Review**: Quarterly
- **Ad-hoc Review**: When significant changes needed

---

## 📞 AUTHORITY CONTACTS

**Primary Standard Location**: `System/Specs/Node Standard v2.0.md`  
**Supporting Documents**: `System/Specs/` folder  
**Standards Questions**: Reference this document first  
**Conflict Resolution**: Use priority order above  

---

**Document Status**: ✅ Active  
**Authority Level**: System Policy  
**Compliance**: Mandatory  
**Next Review**: 2025-12-21
