---
type: Template
status: active
importance: critical
tags:
  - system/prompt
  - system/llm
  - template/onboarding
created: 2025-11-16
updated: 2025-11-16
---

# 🤖 ZERO-SHOT PROMPT: Chapter Concept Extraction

**Purpose**: Copy-paste prompt to onboard new LLM agents to chapter extraction work  
**Use Case**: Starting fresh session, context switch, or new AI assistant  
**Authority**: [[System/ENTRY_POINT_Chapter_Concept_Extraction]]

---

## 📋 COPY-PASTE PROMPT (Lean Version)

**Copy everything between the ``` markers below:**

---

```
You're extracting Chapter 5 (Systems & Matrices) concepts for a College Algebra knowledge base in Obsidian.

WORKSPACE: c:\Users\WORK_ADMIN\Documents\Obsidian Vault\

CURRENT STATE:
- Chapters 1-4: Complete (80+ concepts)
- Chapter 5: 15 stub concepts need upgrading
- Standards: 100% v2.0 compliant

YOUR TASK:
Pick concepts from __USER_MANAGED__/Chapter5_Core_Set_Checklist.md and upgrade to full nodes.

REQUIRED FRONTMATTER:
```yaml
type: Definition | Method | Topic
status: in-progress
importance: high
tags:
  - concept/linear-algebra
  - math/matrices
  - chapter-5
sources: ["textbook-ch5"]
relations:
  broader: []
  depends_on: []
  related: []
created: 2025-11-16
updated: 2025-11-16
```

RULES:
- Min 3 relationships per concept
- NO deprecated: node/*, domain/*, dv_type
- Check 02_Concepts/ for duplicates first
- Add definition, example, LaTeX math

START PRIORITY:
1. Augmented_Matrix
2. Gaussian_Elimination  
3. Row_Operations
4. Row_Echelon_Form
5. Reduced_Row_Echelon_Form

WORKFLOW:
1. Read System/Specs/Node Standard v2.0.md (authority)
2. Check if concept exists in 02_Concepts/
3. Write: definition + LaTeX + example + errors
4. Map: broader/depends_on/related (min 3)
5. Cross-link related concepts
6. Update checklist

QA CHECK: System/Workflows/New_Content_Checklist.md

Ready? Pick first concept and create/upgrade the node.
```

---

## 🎯 USAGE INSTRUCTIONS

### When to Use This Prompt

**Use this prompt when**:
- Starting new LLM session for chapter extraction
- Switching AI assistants (Claude → GPT-4, etc.)
- Context has been lost (token limits, session reset)
- Onboarding collaborator to project
- Resuming work after extended break

### How to Use

1. **Copy** everything between the ``` markers above
2. **Paste** into new LLM conversation
3. **Wait** for LLM to read and acknowledge
4. **Confirm** LLM understands by asking it to summarize:
   - Mission
   - Current state
   - Standards authority
   - First action
5. **Begin** extraction workflow

### Expected Response

LLM should:
1. Acknowledge project context
2. Confirm Chapter 5 as current focus (15 stub concepts)
3. Identify Node Standard v2.0 as authority
4. Request to read entry point document
5. Ask which concept to start with (or propose starting with Augmented_Matrix)

### Red Flags

**Stop and re-prompt if LLM**:
- Mentions deprecated fields (`dv_type`)
- Uses deprecated tags (`node/*`, `domain/*`)
- Doesn't know which standard to follow
- Attempts to edit specs/standards files
- Creates nodes without checking for duplicates
- Skips relationship mapping (< 3 relationships)

---

## 🔄 PROMPT VARIANTS

### Variant A: Resume Existing Work

Use when Chapter 5 is partially complete:

```markdown
# RESUME: Chapter 5 Extraction (Partial Progress)

Context: Chapter 5 concept extraction is [X%] complete. 

Completed concepts: [list completed concept names]
Remaining: [list remaining from checklist]

Your mission: Continue from where we left off. Next concept is [Name].

[Rest of standard prompt...]
```

### Variant B: Start New Chapter (6-12)

Use when beginning new chapter:

```markdown
# NEW CHAPTER: Chapter [N] - [Title]

Context: Chapters R-5 complete. Starting Chapter [N].

Your mission: 
1. Create Chapter[N]_Core_Set_Checklist.md
2. Identify 15-25 core concepts from chapter
3. Create stub nodes for each concept
4. Begin extraction workflow

[Adapt rest of prompt with chapter-specific details...]
```

### Variant C: Quality Assurance Pass

Use for QA-only session:

```markdown
# QUALITY ASSURANCE: Chapter [N] Validation

Context: Chapter [N] concepts extracted, needs QA certification.

Your mission:
1. Run Standards Compliance Dashboard queries
2. Fix deprecated tags/fields
3. Verify minimum 3 relationships per node
4. Add missing bidirectional links
5. Promote qualified nodes from review → stable

[Include standards sections, omit extraction workflow...]
```

---

## 📊 SUCCESS METRICS

After using this prompt, successful onboarding means:

- ✅ LLM identifies correct chapter focus (5)
- ✅ LLM knows authoritative standard (Node Standard v2.0)
- ✅ LLM follows 7-step workflow
- ✅ LLM creates compliant frontmatter (no deprecated items)
- ✅ LLM maps minimum 3 relationships per concept
- ✅ LLM updates tracking documents (checklist)
- ✅ LLM runs QA validation before status changes

**Failure rate target**: < 5% (95%+ compliance on first extraction)

---

## 🆘 TROUBLESHOOTING

### Problem: LLM Creates Deprecated Tags

**Symptom**: Uses `node/definition` instead of `concept/algebra`

**Fix**: 
```markdown
STOP. Review System/Specs/Tags Taxonomy.md.

Deprecated tags (DO NOT USE):
- node/*
- domain/*
- status/*

Current v2.0 tags (USE THESE):
- concept/* (required)
- math/* (required)
- chapter-* (recommended)
- method/* (optional)

Regenerate concept with correct tags.
```

### Problem: LLM Creates Duplicate Concept

**Symptom**: Creates `Matrix_Inverse.md` when `Inverse_Matrix.md` exists

**Fix**:
```markdown
STOP. Before creating ANY new concept:
1. Search 02_Concepts/ for existing file
2. Check Chapter[N]_Core_Set_Checklist for stub names
3. If exists: UPGRADE existing node
4. If missing: CREATE new with unique name

Delete duplicate and merge content into existing node.
```

### Problem: LLM Skips Relationships

**Symptom**: Concept has 0-2 relationships (below minimum 3)

**Fix**:
```markdown
STOP. Every concept MUST have minimum 3 relationships.

For [Concept_Name], identify:
- broader: Which parent concept is this a type of?
- depends_on: What must you know to understand this?
- related: What other concepts operate at same level?
- used_in: Where is this concept applied?

Add at least 3 relationships before proceeding.
```

### Problem: LLM Advances Status Prematurely

**Symptom**: Changes `draft` → `stable` without QA

**Fix**:
```markdown
STOP. Status progression requires validation at each stage:

draft → in-progress: Frontmatter + structure complete
in-progress → review: Content + relationships complete
review → stable: QA checklist passed

Run System/Workflows/New_Content_Checklist.md before ANY status change.
```

---

## 📖 VERSION HISTORY

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | 2025-11-16 | Initial prompt template created |

---

## 🔗 RELATED DOCUMENTS

- [[System/ENTRY_POINT_Chapter_Concept_Extraction]] - Full entry point (copy source)
- [[System/Specs/Node Standard v2.0]] - Standards authority
- [[System/Workflows/New_Content_Checklist]] - QA workflow
- [[__USER_MANAGED__/Chapter5_Core_Set_Checklist]] - Current work tracking

---

**Template Status**: ✅ Production-ready  
**Last Updated**: 2025-11-16  
**Authority**: [[System/STANDARDS_AUTHORITY]]
