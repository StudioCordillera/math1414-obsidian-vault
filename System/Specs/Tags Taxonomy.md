---
type: Spec
status: active
importance: critical
tags: [system/specs, taxonomy, authoritative]
version: 2.0
created: 2025-10-23
updated: 2025-10-23
supersedes: Previous versions with node/*, domain/*, cat/* namespaces
---

# Tags Taxonomy (AUTHORITATIVE VERSION 2.0)

> **STATUS**: This is the OFFICIAL controlled vocabulary for all Math 1414 tags.  
> **SUPERSEDES**: All previous versions with `node/*`, `domain/*`, `cat/*`, `logic/*` namespaces  
> **LAST VERIFIED**: 2025-10-23 against actual vault implementation

---

## Purpose

Define controlled tag vocabulary for Math 1414 vault to ensure consistent categorization, enable reliable queries, and support knowledge graph navigation.

---

## Approved Tag Namespaces

**CRITICAL**: Only use tags from these approved namespaces. Do NOT create custom namespaces.

---

### **1. Concept Category Tags** (`concept/*`)

**Purpose**: Categorize by mathematical concept type

**Approved Tags**:
```
concept/foundational      - Fundamental building blocks (equality properties, number systems)
concept/number-system     - Number system extensions (reals, complex, etc.)
concept/algebra           - Algebraic concepts and structures
concept/functions         - Function-related concepts
concept/geometry          - Geometric concepts
concept/properties        - Mathematical properties and rules
concept/operations        - Operations and procedures
concept/solving           - Solution methods and strategies
```

**Usage**: Every concept node should have at least ONE `concept/*` tag

**Examples**:
- `Complex_Numbers.md` → `concept/number-system`
- `Equality_Properties.md` → `concept/foundational`, `concept/properties`
- `Quadratic_Formula.md` → `concept/solving`, `concept/algebra`

---

### **2. Chapter Tags** (`chapter-*`)

**Purpose**: Link concepts to textbook chapters

**Approved Tags**:
```
chapter-r     - Chapter R: Prerequisites
chapter-1     - Chapter 1: Equations and Inequalities
chapter-2     - Chapter 2: Functions and Relations
chapter-3     - Chapter 3: Polynomial Functions
chapter-4     - Chapter 4: Exponential and Logarithmic Functions
chapter-5     - Chapter 5: Trigonometric Functions
chapter-6     - Chapter 6: Trigonometric Identities
chapter-7     - Chapter 7: Applications of Trigonometry
chapter-8     - Chapter 8: Systems of Equations
chapter-9     - Chapter 9: Matrices and Determinants
chapter-10    - Chapter 10: Analytic Geometry
chapter-11    - Chapter 11: Sequences and Series
chapter-12    - Chapter 12: Additional Topics
```

**Usage**: Tag concepts with source chapter(s)

**Examples**:
- `Complex_Numbers.md` → `chapter-1` (introduced in Chapter 1.3)
- `Exponent_Properties.md` → `chapter-r` (prerequisite material)
- Concepts used in multiple chapters get multiple chapter tags

---

### **3. Domain Tags** (`math/*`)

**Purpose**: Categorize by mathematical domain

**Approved Tags**:
```
math/equations        - Equation solving
math/inequalities     - Inequality solving and analysis
math/polynomials      - Polynomial expressions and functions
math/functions        - Function theory and applications
math/properties       - Mathematical properties
math/operations       - Mathematical operations
math/algebra          - General algebra
math/geometry         - Geometric concepts
math/trigonometry     - Trigonometric concepts
math/relations        - Relations and mappings
math/complex          - Complex numbers
math/rational         - Rational expressions
math/radicals         - Radical expressions
```

**Usage**: 1-2 domain tags per concept to categorize mathematical area

**Examples**:
- `Quadratic_Formula.md` → `math/equations`, `math/algebra`
- `Complex_Numbers.md` → `math/complex`, `math/algebra`
- `Pythagorean_Theorem.md` → `math/geometry`, `math/properties`

---

### **4. Method Tags** (`method/*`)

**Purpose**: Categorize by type of mathematical method

**Approved Tags**:
```
method/solving        - Solution procedures
method/graphing       - Graphing techniques
method/factoring      - Factoring methods
method/simplifying    - Simplification procedures
method/analyzing      - Analysis techniques
method/verifying      - Verification and checking
method/translating    - Word problem translation
method/modeling       - Mathematical modeling
```

**Usage**: Add if node describes or teaches a method

**Examples**:
- `Completing_the_Square.md` → `method/solving`
- `Factoring_Strategies.md` → `method/factoring`
- `Graphing_Functions.md` → `method/graphing`, `method/analyzing`

---

### **5. System Tags** (`system/*`)

**Purpose**: Mark system/administrative documents

**Approved Tags**:
```
system/specs          - Specification documents
system/tracking       - Status and progress tracking
system/templates      - Template files
system/dashboard      - Dashboard and index files
system/maintenance    - Maintenance procedures
system/archive        - Archived materials
```

**Usage**: Only for system documents in `System/` folder

**Examples**:
- `Node Standard.md` → `system/specs`
- `Project_Dashboard.md` → `system/dashboard`, `system/tracking`
- `Migration_Status.md` → `system/tracking`, `system/archive`

---

### **6. Status Tags** (OPTIONAL - prefer frontmatter status field)

**Purpose**: Quick visual status indicators

**Approved Tags**:
```
status/needs-review   - Requires review
status/incomplete     - Missing content
status/verified       - Quality checked
status/priority       - High priority for work
```

**Usage**: Supplement frontmatter `status:` field when needed

**Note**: Prefer using frontmatter `status:` field. Only add status tags for special workflows or visual indicators.

---

## Tag Usage Guidelines

### **How Many Tags Per Node?**

**Minimum**: 3 tags (1 concept + 1 chapter + 1 domain)  
**Recommended**: 4-8 tags  
**Maximum**: 12 tags (excessive tagging reduces value)

### **Tag Selection Process**

When tagging a new concept node:

1. **Start with concept category** (1-2 tags from `concept/*`)
   - What kind of concept is this?
   
2. **Add chapter tag(s)** (1-3 tags from `chapter-*`)
   - Where is it taught in the textbook?
   
3. **Add domain tag(s)** (1-2 tags from `math/*`)
   - What area of mathematics?
   
4. **Add method tag if applicable** (0-2 tags from `method/*`)
   - Does it teach a procedure?
   
5. **Add system tag if applicable** (0-1 tag from `system/*`)
   - Is it a system document?

### **Tag Priority Order**

When limited to fewer tags, prioritize:
1. concept/* (REQUIRED)
2. chapter-* (HIGHLY RECOMMENDED)
3. math/* (RECOMMENDED)
4. method/* (OPTIONAL)
5. system/* (ONLY if system document)

---

## Examples of Well-Tagged Nodes

### Example 1: Complex_Numbers.md
```yaml
tags:
  - concept/number-system
  - concept/algebra
  - chapter-1
  - math/complex
  - math/algebra
```
**Analysis**: 
- 2 concept tags (number system type + algebraic structure)
- 1 chapter tag (introduced in Chapter 1)
- 2 domain tags (complex numbers + algebra)
- Total: 5 tags ✅

---

### Example 2: Quadratic_Formula.md
```yaml
tags:
  - concept/solving
  - concept/foundational
  - chapter-1
  - math/equations
  - math/algebra
  - method/solving
```
**Analysis**:
- 2 concept tags (solving method + foundational tool)
- 1 chapter tag (Chapter 1)
- 2 domain tags (equations + algebra)
- 1 method tag (solving procedure)
- Total: 6 tags ✅

---

### Example 3: Zero_Product_Property.md
```yaml
tags:
  - concept/properties
  - concept/foundational
  - chapter-r
  - chapter-1
  - math/properties
  - math/algebra
  - method/solving
```
**Analysis**:
- 2 concept tags (property + foundational)
- 2 chapter tags (prerequisite material + used in Chapter 1)
- 2 domain tags (properties + algebra)
- 1 method tag (used in solving)
- Total: 7 tags ✅

---

### Example 4: Node Standard.md (System Document)
```yaml
tags:
  - system/specs
  - system/tracking
```
**Analysis**:
- 2 system tags (specification + tracking-related)
- No concept/chapter/domain tags (not a math concept)
- Total: 2 tags ✅

---

## Deprecated Tags (DO NOT USE)

### **REMOVED Namespaces**

These tag namespaces are DEPRECATED and should NOT be used:

❌ `node/*` (node/topic, node/definition, etc.)  
→ Use `type:` frontmatter field instead

❌ `domain/*` (domain/cat, domain/logic, domain/db, etc.)  
→ Use `math/*` namespace instead

❌ `cat/*` (cat/relations, cat/limits, etc.)  
→ These were category theory specific, not relevant to Math 1414

❌ `logic/*` (logic/regular, logic/eq, etc.)  
→ Not relevant to Math 1414 curriculum

❌ `status/*` (status/draft, status/active, etc.)  
→ Use `status:` frontmatter field instead

❌ `pedagogy/*` (pedagogy/motivation, pedagogy/pattern, etc.)  
→ Use `method/*` namespace instead

### **Migration from Deprecated Tags**

If you encounter nodes with deprecated tags:

| Old Tag | New Approach |
|---------|-------------|
| `node/definition` | Set `type: Definition` in frontmatter |
| `node/claim` | Set `type: Claim` in frontmatter |
| `domain/logic` | Remove (not relevant) |
| `cat/relations` | Remove (not relevant) |
| `status/draft` | Set `status: draft` in frontmatter |
| `pedagogy/pattern` | Add `method/solving` or similar |

---

## Tag Queries (Dataview Examples)

### **Find all foundational concepts**:
```dataview
LIST
FROM #concept/foundational 
SORT file.name ASC
```

### **Find all Chapter 1 concepts**:
```dataview
TABLE type, importance, status
FROM #chapter-1 
WHERE type = "Definition" OR type = "Claim"
SORT importance DESC, file.name ASC
```

### **Find all solving methods**:
```dataview
TABLE tags, sources
FROM #method/solving 
SORT file.name ASC
```

### **Find concepts needing review**:
```dataview
TABLE review.next, status, importance
FROM "02_Concepts"
WHERE review.next < date(today)
SORT review.next ASC
```

### **Tag coverage analysis**:
```dataview
TABLE length(tags) as "Tag Count", tags
FROM "02_Concepts"
WHERE type = "Definition"
SORT length(tags) ASC
```

---

## Tag Maintenance Protocol

### **Weekly Checks**
- [ ] Verify new nodes use approved tag namespaces
- [ ] Check for custom/unapproved tags
- [ ] Ensure minimum 3 tags per concept node

### **Monthly Audits**
- [ ] Run tag coverage analysis query
- [ ] Identify under-tagged nodes (< 3 tags)
- [ ] Identify over-tagged nodes (> 12 tags)
- [ ] Check for deprecated tag usage

### **Quarterly Reviews**
- [ ] Review tag namespace effectiveness
- [ ] Consider new tag additions if patterns emerge
- [ ] Update this taxonomy document
- [ ] Migrate any deprecated tags found

---

## Adding New Tags to Taxonomy

**Process for proposing new tags**:

1. **Identify need**: Multiple nodes need same categorization
2. **Check existing tags**: Does an existing tag suffice?
3. **Document rationale**: Why is new tag needed?
4. **Propose to appropriate namespace**: Choose correct `*/` prefix
5. **Update this document**: Add to approved list
6. **Announce change**: Update Project Dashboard
7. **Apply retroactively**: Tag relevant existing nodes

**Example**:
```
Need: Categorize modeling/application problems
Check: No existing tag covers this
Rationale: 15+ nodes involve real-world modeling
Namespace: method/modeling (method-based activity)
Update: Add to method/* section
Announce: Dashboard activity log
Apply: Tag relevant nodes
```

---

## Common Tagging Mistakes

### ❌ WRONG: Creating Custom Namespace
```yaml
tags:
  - myown/category
  - custom/tag
```
**Problem**: Breaks categorization system, can't be queried reliably

### ✅ CORRECT: Use Approved Namespace
```yaml
tags:
  - concept/algebra
  - math/equations
```

---

### ❌ WRONG: Duplicating Frontmatter in Tags
```yaml
type: Definition
status: draft
tags:
  - node/definition
  - status/draft
```
**Problem**: Redundant, deprecated tag namespaces

### ✅ CORRECT: Use Frontmatter Fields
```yaml
type: Definition
status: draft
tags:
  - concept/algebra
  - math/equations
```

---

### ❌ WRONG: Using Spaces or Capitals
```yaml
tags:
  - Concept/Algebra
  - math/Equations and Inequalities
```
**Problem**: Inconsistent casing, spaces break linking

### ✅ CORRECT: Lowercase, Hyphens for Multi-Word
```yaml
tags:
  - concept/algebra
  - math/equations
```

---

### ❌ WRONG: Too Many Tags (Overtagging)
```yaml
tags:
  - concept/foundational
  - concept/number-system
  - concept/algebra
  - concept/operations
  - chapter-r
  - chapter-1
  - chapter-2
  - math/algebra
  - math/equations
  - math/complex
  - math/properties
  - math/operations
  - method/solving
  - method/simplifying
  - method/verifying
```
**Problem**: 15 tags! Dilutes categorization, hard to maintain

### ✅ CORRECT: Focused, Essential Tags Only
```yaml
tags:
  - concept/number-system
  - concept/algebra
  - chapter-1
  - math/complex
  - math/algebra
```

---

## Tag Visualization

### Namespace Hierarchy
```
Math 1414 Vault Tags
├── concept/*           [REQUIRED - at least 1]
│   ├── foundational
│   ├── number-system
│   ├── algebra
│   ├── functions
│   ├── geometry
│   ├── properties
│   ├── operations
│   └── solving
├── chapter-*           [HIGHLY RECOMMENDED - 1-3]
│   ├── chapter-r
│   ├── chapter-1
│   ├── chapter-2
│   └── [...]
├── math/*              [RECOMMENDED - 1-2]
│   ├── equations
│   ├── inequalities
│   ├── polynomials
│   ├── functions
│   ├── properties
│   └── [...]
├── method/*            [OPTIONAL - 0-2]
│   ├── solving
│   ├── graphing
│   ├── factoring
│   └── [...]
└── system/*            [ONLY for system docs]
    ├── specs
    ├── tracking
    └── dashboard
```

---

## Migration Notes

### Version History

**Version 2.0** (2025-10-23):
- Corrected namespaces to match actual vault usage
- Removed deprecated namespaces: `node/*`, `domain/*`, `cat/*`, `logic/*`, `status/*`, `pedagogy/*`
- Added current namespaces: `concept/*`, `chapter-*`, `math/*`, `method/*`, `system/*`
- Added comprehensive examples and migration guide
- Declared as AUTHORITATIVE version

**Version 1.0** (Previous):
- Used namespaces that didn't match implementation
- Included category theory specific tags not relevant to Math 1414
- Missing usage guidelines and examples

### For Existing Nodes

If you find nodes with deprecated tags:

1. Check the migration table above
2. Remove deprecated tag
3. Add appropriate new tag from approved namespace
4. Update `updated:` date in frontmatter
5. Verify minimum 3 tags present

**Automated Migration Query**:
```dataview
TABLE tags
FROM "02_Concepts"
WHERE contains(string(tags), "node/") 
   OR contains(string(tags), "domain/") 
   OR contains(string(tags), "cat/")
   OR contains(string(tags), "logic/")
SORT file.name ASC
```

This will surface any nodes needing tag migration.

---

## Document Metadata

**Version**: 2.0 (AUTHORITATIVE)  
**Status**: Active - Official Standard  
**Last Updated**: 2025-10-23  
**Last Verified Against Vault**: 2025-10-23  
**Next Review**: 2025-11-23  
**Supersedes**: All previous versions  

**Authority**: This document defines the OFFICIAL controlled vocabulary for tags. In case of conflict between this document and any other specification or example, THIS DOCUMENT TAKES PRECEDENCE.

---

## References

- [[Node Standard]] - Frontmatter structure and node types
- [[Relations - Relation Types]] - Semantic relationships
- [[Project_Dashboard]] - Current project status
- [[NEW_SESSION_START]] - Onboarding guide

---

*This Tags Taxonomy is based on systematic analysis of actual vault usage patterns and represents the working controlled vocabulary for the Math 1414 knowledge system.*