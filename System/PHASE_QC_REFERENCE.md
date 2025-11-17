---
type: System
status: active
importance: critical
tags:
  - system/specs
  - system/qc
  - emergency-sprint
created: 2025-11-16
updated: 2025-11-16
---

# 🎯 PHASE QC REFERENCE — Emergency Sprint Standards

**PURPOSE**: Hard-required QC checklist for beginning & end of EACH phase  
**USAGE**: Reference before starting AND after completing each phase  
**AUTHORITY**: Synthesizes all vault standards for rapid deployment

---

## 📚 FOUNDATIONAL DOCUMENTS MAP

### ⚠️ MUST READ FIRST

**[[System/CONCEPT_NODE_MANIFESTO]]** 🔥 **SUPREME AUTHORITY**  
**Read this document BEFORE doing ANY concept work.**
- The six-layer complete package philosophy
- Why concept nodes are self-contained knowledge modules
- The difference between concepts (nouns) and methods (verbs)
- How to create publication-quality database entries
- Required reading for all content creators and auditors

### Standards & Specifications (AUTHORITATIVE)

1. **`System/Specs/Node Standard v2.0.md`** ⭐ PRIMARY TECHNICAL AUTHORITY
   - Frontmatter structure (type, status, tags)
   - Content sections required per node type
   - Relationship mapping requirements (min 3, bidirectional)
   - Deprecated elements to NEVER use
   - **NOTE**: Node Standard v2.0 is the TECHNICAL implementation of the Manifesto

2. **`System/Specs/Tags Taxonomy.md`** ⭐ TAG AUTHORITY
   - Approved tag namespaces: `concept/*`, `chapter-*`, `math/*`, `method/*`
   - Forbidden namespaces: `node/*`, `domain/*`, `dv_type`, `layout`
   - 3-8 tags per node (min 3, max 12)

3. **`System/Specs/Relations - Relation Types.md`**
   - Relationship semantics: broader, narrower, depends_on, related, used_in
   - Bidirectional linking requirements

### Dashboards & Tracking
4. **`00_Index/Dashboard.md`**
   - Chapter extraction progress
   - Vault-wide status tracking

5. **`__USER_MANAGED__/Chapter*_Core_Set_Checklist.md`**
   - Per-chapter concept completion logs
   - Date tracking for completed nodes

6. **`__USER_MANAGED__/EXAM3_PRIORITY_SPRINT.md`**
   - 41-node gap analysis and priorities
   - Tier classifications (missing, stub, QC)

7. **`__USER_MANAGED__/EXAM3_EMERGENCY_SPRINT_DASHBOARD.md`** ⭐ THIS SPRINT
   - 6-phase execution plan
   - 19 critical nodes for immediate deployment

### Pedagogy & Theory
8. **`00_Index/SYSTEM_OVERVIEW.md`** ⭐ MISSION STATEMENT
   - Relational cognition principles
   - Three-level architecture: Insight → Theory → Practice
   - Why/How answers to procedural What

9. **`03_Relational_Cognition/README.md`**
   - Topic-centric approach (vs source-centric)
   - Multi-source synthesis principles

10. **`Relational Cognition Corpus/Framework.md`**
    - Cross-linking conventions
    - Source trail requirements

---

## 🧠 RELATIONAL COGNITION MISSION

**FROM `SYSTEM_OVERVIEW.md` — THE NORTH STAR:**

> **"To take the relational cognitive theory elements and package the presentation of the concepts and related sub-methods, procedures, and dependent concepts that construct such a concept you are instructed to create in order to describe the relations between all conceptual parties of target information together to create a record which serves as a WHY? and HOW? answer to the WHAT? level procedural perspective that is so commonly forced upon students such that the reader may walk away understanding how this new concept is constructed and relates to others."**

### Implementation Principles

**1. Three-Level Architecture** (MUST follow in every node)
- **Level 1: Core Insight** — The "Aha!" moment in Definition section
- **Level 2: Foundation** — The "Why?" in Mathematical Expression + Properties
- **Level 3: Procedures** — The "How?" in Examples with step-by-step work

**2. Morphism-Based Thinking**
- Every method is a transformation: Input → [Operation] → Output
- Examples show WHAT changes and WHAT stays the same
- Enable chaining: compose operations, reverse operations

**3. Relational Cross-Linking** (Minimum 3, Target 5)
- **depends_on**: Prerequisites (must understand first)
- **related**: Peer concepts (same level)
- **used_in**: Applications (where deployed)
- **broader/narrower**: Hierarchy (generalization/specialization)

**4. No Isolated Facts**
- Every concept links to knowledge network
- Show multiple angles/perspectives
- Connect abstract to concrete (examples bridge theory to practice)

---

## ✅ PRE-PHASE QC CHECKLIST

**BEFORE starting ANY phase, verify:**

### Context Review
- [ ] Read relevant chapter's learning objectives from `COMPREHENSIVE_LEARNING_OBJECTIVES_EXAM3.md`
- [ ] Check `Chapter*_Core_Set_Checklist.md` for existing nodes
- [ ] Review 1-2 recent completed nodes as template reference
- [ ] Confirm which concepts in this phase are NEW vs UPGRADES

### Standards Refresh
- [ ] **Node Standard v2.0**: Required frontmatter fields clear
- [ ] **Tags Taxonomy**: Approved namespaces memorized
- [ ] **Relational Mission**: Three levels (Insight/Why/How) top of mind
- [ ] **Minimum Quality**: Definition + Math + Example + 3 relations

### Template Selection
- [ ] Identify best existing node to use as structure template
- [ ] For new concepts: Use recently created variation nodes
- [ ] For upgrades: Open existing stub, plan expansion

---

## ✅ POST-PHASE QC CHECKLIST

**AFTER completing phase batch, verify ALL nodes:**

### Frontmatter Compliance
- [ ] **type: concept** (NOT Definition, NOT dv_type)
- [ ] **status: active** (NOT draft, NOT in-progress)
- [ ] **tags**: 3-8 tags minimum, approved namespaces only
  - [ ] At least 1 `concept/*` tag
  - [ ] At least 1 `chapter-*` tag
  - [ ] At least 1 `math/*` tag
  - [ ] NO `node/*`, `domain/*`, `layout`, `dv_type`, `review:`
- [ ] **created**: YYYY-MM-DD format
- [ ] **updated**: YYYY-MM-DD format (today's date)

### Content Structure (v2.0 Required Sections)
- [ ] **# [Concept Name]** — Title matches filename
- [ ] **## Definition** — Clear statement, formal if needed
- [ ] **## Mathematical Expression** — LaTeX with $ or $$ delimiters
- [ ] **## Example** — At least 1 complete worked problem with REAL NUMBERS
  - [ ] NO placeholders like "x = a" or "k = constant"
  - [ ] Shows input → transformation → output
- [ ] **## Key Properties** (or similar) — Bullet list of characteristics
- [ ] **## Relations** — Minimum 3 `[[Wikilinks]]` with brief descriptions

### Relational Cognition Quality
- [ ] **Level 1 (Insight)**: Definition gives "aha" understanding
- [ ] **Level 2 (Why)**: Mathematical expression explains structure
- [ ] **Level 3 (How)**: Example shows step-by-step application
- [ ] **Morphism clarity**: Transformation input/output visible
- [ ] **Network integration**: Links show concept's place in knowledge web

### Markdown Linting (Fix These)
- [ ] Blank line BEFORE every heading
- [ ] Blank line AFTER every heading
- [ ] Blank line BEFORE every list
- [ ] Blank line AFTER every list
- [ ] No trailing spaces at line ends
- [ ] File ends with single newline

### Relationship Verification
- [ ] All `[[Wikilinks]]` point to existing OR planned concepts
- [ ] Minimum 3 relationships present
- [ ] Each relationship has brief explanation (not just link)
- [ ] Mix of relationship types (not all "related")

### Examples Quality
- [ ] Uses concrete numbers: `2x + 3 = 7` NOT `ax + b = c`
- [ ] Shows complete work: intermediate steps visible
- [ ] Result clearly stated: **Solution: x = 2**
- [ ] Verification shown when relevant

---

## 🚀 EMERGENCY SPRINT ADAPTATIONS

### Speed Optimizations (Approved Shortcuts)
✅ **Can defer until Phase 6:**
- Fixing all linting errors (blank lines)
- Bidirectional link updates in target nodes
- Adding 4th, 5th relationship (if 3 solid ones exist)
- Polishing prose in Key Properties section

✅ **Can use from proven templates:**
- Frontmatter structure from recent completed nodes
- Section ordering from similar concept type
- Relationship phrasing patterns

### Non-Negotiable (NEVER Skip)
❌ **Must be present BEFORE marking phase complete:**
- V2.0 frontmatter (type, status, tags with approved namespaces)
- Definition section with substance
- Mathematical Expression with LaTeX
- At least 1 complete example with real numbers
- Minimum 3 relationships

---

## 📋 TRACKING UPDATE PROTOCOL

**After EACH phase, update these files IN ORDER:**

### 1. Chapter Checklist
```
File: __USER_MANAGED__/Chapter*_Core_Set_Checklist.md

Action: Add to "Completed v2.0 Nodes" section:
- [x] [Concept_Name] — 2025-11-16

If section doesn't exist, create it:
## Completed v2.0 Nodes

- [x] [Concept_Name] — 2025-11-16
```

### 2. Sprint Dashboard
```
File: __USER_MANAGED__/EXAM3_EMERGENCY_SPRINT_DASHBOARD.md

Action: 
1. Check [x] all completed nodes in phase section
2. Update Sprint Metrics table with completion %
3. Update phase status from ⏳ Pending to ✅ Complete
```

### 3. Priority Sprint
```
File: __USER_MANAGED__/EXAM3_PRIORITY_SPRINT.md

Action: Check [x] corresponding items in Tier 1 or Tier 2 lists
```

### 4. Main Dashboard (Final phase only)
```
File: 00_Index/Dashboard.md

Action: Update "Current Work" section with sprint summary
```

---

## 🎯 PHASE COMPLETION CRITERIA

**A phase is complete when:**

✅ All nodes created/upgraded per phase specification  
✅ Every node passes Post-Phase QC Checklist  
✅ All tracking files updated with completion status  
✅ Phase marked complete in Emergency Sprint Dashboard  
✅ No critical quality gates failed

**If ANY criterion fails:**
1. Note the failure in sprint dashboard
2. Fix immediately before proceeding
3. Re-run QC checklist
4. Mark complete only when all criteria pass

---

## 🔥 EMERGENCY MODE REMINDERS

**You are in EXAM PREP EMERGENCY MODE. Remember:**

1. **Good Enough Beats Perfect** — Ship functional nodes, refine later
2. **Examples > Theory** — Worked problems matter more than exhaustive properties
3. **Speed With Standards** — Fast deployment, but v2.0 non-negotiables ALWAYS
4. **Student First** — Every node must answer: "How does this help me solve problems?"

**Mission Success = 19 exam-ready concept nodes in student's hands**

---

## 📖 QUICK REFERENCE LINKS

### Before Starting Phase
- [[System/Specs/Node Standard v2.0|Node Standard]] — Structure requirements
- [[System/Specs/Tags Taxonomy|Tags]] — Approved vocabulary
- [[00_Index/SYSTEM_OVERVIEW|Mission]] — Why we do this

### During Phase
- Recent completed node in `02_Concepts/` — Template
- `COMPREHENSIVE_LEARNING_OBJECTIVES_EXAM3.md` — Context

### After Phase
- `EXAM3_EMERGENCY_SPRINT_DASHBOARD.md` — Check off items
- `Chapter*_Core_Set_Checklist.md` — Log completion

---

## 🎓 SUCCESS METRICS

**Each node should enable the student to:**
1. ✅ Understand WHAT the concept is (Definition)
2. ✅ Understand WHY it works (Mathematical Expression + Properties)
3. ✅ Know HOW to apply it (Example with real numbers)
4. ✅ See WHERE it fits (Relations showing network)

**If a node achieves all 4, it's exam-ready. Ship it.**

---

**REFERENCE THIS DOCUMENT:**
- ⏰ Before starting each phase
- ✅ After completing each phase
- 🚨 Whenever quality questions arise

**AUTHORITY**: Synthesizes Node Standard v2.0 + Tags Taxonomy + Relational Cognition Mission

**VERSION**: Emergency Sprint Edition 1.0  
**CREATED**: 2025-11-16  
**STATUS**: Active for Exam 3 Emergency Sprint
