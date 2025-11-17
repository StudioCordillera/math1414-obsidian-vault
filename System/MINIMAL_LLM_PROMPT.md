---
type: Template
status: active
importance: critical
tags:
  - system/prompt
  - system/minimal
created: 2025-11-16
updated: 2025-11-16
---

# 🎯 MINIMAL LLM PROMPT (Copy-Paste Ready)

**Use Case**: Instant onboarding, no context needed  
**Time**: < 30 seconds to copy and paste  
**Result**: LLM starts working immediately

---

## ⚡ THE PROMPT

**Copy everything in the box below and paste into your LLM:**

```
VAULT: c:\Users\WORK_ADMIN\Documents\Obsidian Vault\

WORKFLOW:
1. Read 00_Index/Dashboard.md - check current chapter focus and status
2. Read __USER_MANAGED__/Chapter*_Core_Set_Checklist.md for active chapter
3. Read System/Specs/Node Standard v2.0.md - learn frontmatter format
4. Pick unchecked concept from checklist
5. Check if 02_Concepts/[Name].md exists (upgrade if yes, create if no)
6. Write node: definition, LaTeX math, example, min 3 relations
7. Update checklist - mark complete with date
8. Update dashboard if chapter complete
9. Repeat

RULES:
- NO deprecated: node/*, domain/*, dv_type
- Min 3 relationships per concept
- Check 02_Concepts/ for duplicates first

START: Read dashboard, find active chapter, begin extraction.
```

---

## ✅ WHAT THIS DOES

The LLM will:
1. ✅ Open Chapter 5 checklist
2. ✅ Pick first concept (Augmented_Matrix)
3. ✅ Check for existing file
4. ✅ Create/upgrade with proper frontmatter
5. ✅ Write definition + math + example
6. ✅ Map 3+ relationships
7. ✅ Update checklist
8. ✅ Move to next concept

No hand-holding, no long explanations, just work.

---

## 🚨 IF PROBLEMS OCCUR

**LLM asks "What's Node Standard v2.0?"**
→ Point to: `System/Specs/Node Standard v2.0.md`

**LLM uses deprecated tags (node/*, domain/*)**
→ Say: "Use concept/* and math/* instead"

**LLM creates duplicate**
→ Say: "Search 02_Concepts/ first, upgrade existing"

**LLM skips relationships**
→ Say: "Add minimum 3 in relations: section"

---

**Version**: 1.0  
**Last Updated**: 2025-11-16  
**Tokens**: ~150 (minimal prompt)
