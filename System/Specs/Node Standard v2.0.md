---
type: Spec
status: active
importance: critical
tags:
  - system/specs
  - node/standard
  - authoritative
version: 2.0
created: 2025-10-23
updated: 2025-11-04
supersedes: "Node Standard (ARCHIVED v1.0)"
archival_note: "Updated during audit revision implementation 2025-11-04"
---

# Node Standard (AUTHORITATIVE VERSION 2.0)

**STATUS**: This is the OFFICIAL and ONLY standard for all Math 1414 concept nodes.  
**SUPERSEDES**: All previous versions (v1.0 archived 2025-11-16)  
**LAST VERIFIED**: 2025-11-16 during comprehensive vault audit  
**VERSION**: 2.0 (Current and Authoritative)

---

## Purpose

**⚠️ REQUIRED READING**: [[System/CONCEPT_NODE_MANIFESTO]] — Read this first to understand the complete package philosophy.

This document defines the **technical implementation** of the Manifesto philosophy. It specifies:
- Machine-tractable knowledge representation
- Consistent cross-linking and relationships
- Automated quality assurance capability
- Scalable content creation workflows

**Relationship to Manifesto**:
- **Manifesto** = The VISION (six-layer complete package philosophy)
- **Node Standard v2.0** = The IMPLEMENTATION (technical specifications)

---

## Required Frontmatter Fields

### Core Identity
```yaml
type: Definition | Claim | Topic | Example | Method | Question
status: draft | in-progress | review | stable
importance: low | medium | high | critical
```

### Classification and Discovery
```yaml
tags:
  - concept/[category]     # REQUIRED: At least one concept tag
  - chapter-[n]            # RECOMMENDED: Source chapter
  - math/[domain]          # RECOMMENDED: Mathematical domain
  - method/[type]          # OPTIONAL: If describes a method
  - system/[type]          # ONLY for system documents
```

### Source Attribution
```yaml
sources:
  - source-identifier      # Cite key or identifier
source_refs:
  - "Source §Section p.Page"  # Specific references
```

### Relational Mapping
```yaml
relations:
  broader: []              # Parent concepts (more general)
  narrower: []             # Child concepts (more specific)
  depends_on: []           # Prerequisites (must understand first)
  related: []              # Related concepts (same level)
  used_in: []              # Applications (where this is used)
  defines: []              # What this concept defines
```

---

## Recommended Frontmatter Fields

### Review Management
```yaml
review:
  next: YYYY-MM-DD         # Next review date
  cadence: daily | weekly | monthly  # Review frequency
```

### Creation Tracking
```yaml
created: YYYY-MM-DD        # Creation date
updated: YYYY-MM-DD        # Last update date
```

---

## Content Structure Requirements

### For Definition Nodes
1. **Clear Definition Section**: Mathematical definition with notation
2. **Examples Section**: 3-5 detailed examples showing usage
3. **Applications Section**: Where and how concept is applied
4. **Common Misconceptions**: 5-7 typical errors students make
5. **Related Concepts**: Cross-links to broader knowledge network
6. **Summary Statement**: Concise recap of key points

### For Claim Nodes (Theorems/Properties)
1. **Statement**: Precise mathematical claim
2. **Proof Sketch**: High-level proof approach
3. **Applications**: Where the claim is used
4. **Dependencies**: What must be true for claim to hold
5. **Examples**: Specific instances demonstrating the claim

### For Topic Nodes
1. **Overview**: Aggregate view of related concepts
2. **Key Concepts**: Links to atomic concept definitions
3. **Methods**: Links to procedural knowledge
4. **Applications**: Real-world usage
5. **Integration**: How topic fits in broader curriculum

---

## Tag Taxonomy Compliance

### REQUIRED Tags (Concept Classification)
```yaml
concept/foundational      # Fundamental building blocks
concept/number-system     # Number system extensions
concept/algebra           # Algebraic concepts and structures
concept/functions         # Function-related concepts
concept/geometry          # Geometric concepts
concept/properties        # Mathematical properties and rules
concept/operations        # Operations and procedures
concept/solving           # Solution methods and strategies
```

### RECOMMENDED Tags (Chapter Source)
```yaml
chapter-r     # Chapter R: Prerequisites
chapter-1     # Chapter 1: Equations and Inequalities
chapter-2     # Chapter 2: Functions and Relations
chapter-3     # Chapter 3: Polynomial Functions
chapter-4     # Chapter 4: Exponential and Logarithmic Functions
# ... continuing through chapter-12
```

### RECOMMENDED Tags (Mathematical Domain)
```yaml
math/equations        # Equation solving
math/inequalities     # Inequality solving and analysis
math/polynomials      # Polynomial expressions and functions
math/functions        # Function theory and applications
math/properties       # Mathematical properties
math/operations       # Mathematical operations
math/algebra          # General algebra
math/geometry         # Geometric concepts
math/trigonometry     # Trigonometric concepts
math/relations        # Relations and mappings
math/complex          # Complex numbers
math/rational         # Rational expressions
math/radicals         # Radical expressions
```

### OPTIONAL Tags (Method Classification)
```yaml
method/solving        # Solution procedures
method/graphing       # Graphing techniques
method/factoring      # Factoring methods
method/simplifying    # Simplification procedures
method/analyzing      # Analysis techniques
method/verifying      # Verification and checking
method/translating    # Word problem translation
method/modeling       # Mathematical modeling
```

### SYSTEM Tags (Administrative Only)
```yaml
system/specs          # Specification documents
system/tracking       # Status and progress tracking
system/templates      # Template files
system/dashboard      # Dashboard and index files
system/maintenance    # Maintenance procedures
system/archive        # Archived materials
```

---

## Relational Mapping Standards

### Relationship Types and Usage

**broader/narrower**: Hierarchical concept relationships
- Use for taxonomic relationships
- Example: `Quadratic_Functions` broader than `Vertex_Form`

**depends_on**: Prerequisite knowledge
- Must understand these concepts first
- Example: `Quadratic_Formula` depends_on `Completing_the_Square`

**related**: Peer-level connections
- Concepts at similar complexity level
- Example: `Complex_Numbers` related to `Imaginary_Unit`

**used_in**: Application contexts
- Where this concept appears in practice
- Example: `Zero_Product_Property` used_in `Factoring_Strategies`

**defines**: What this concept creates/establishes
- For foundational concepts that establish terminology
- Example: `Real_Number_System` defines number classifications

### Bidirectional Linking Requirements

**ALL relationships must be bidirectional**:
- If A depends_on B, then B should list A in used_in
- If A is broader than B, then B should list A in broader
- If A is related to B, then B should list A in related

### Relationship Density Targets

**Minimum**: 3 relationships per concept node
**Recommended**: 5-6 relationships per concept node
**Maximum**: 12 relationships (avoid over-linking)

---

## Filename and Location Conventions

### Directory Structure
```
02_Concepts/
├── [Concept_Name].md           # Atomic concept nodes
├── Vocabulary/                 # Term definitions
└── [Support files]             # Checklists, indices
```

### Naming Conventions
- **PascalCase**: `Complex_Numbers.md`, `Quadratic_Formula.md`
- **Descriptive**: Name clearly indicates concept content
- **Unique**: No duplicate concept names across vault
- **Consistent**: Similar concepts use parallel naming

---

## Quality Assurance Requirements

### Before Creating New Concept Node
1. **Search existing vault**: Ensure concept doesn't already exist
2. **Identify relationships**: Plan at least 3 cross-links
3. **Review tag taxonomy**: Select appropriate tags from approved list
4. **Validate sources**: Ensure proper citation format

### Before Marking Status as 'review' or 'stable'
1. **Frontmatter complete**: All required fields populated
2. **Content comprehensive**: Meets section requirements for node type
3. **Cross-links validated**: All referenced concepts exist
4. **Bidirectional links**: Confirm reverse relationships established
5. **Tag compliance**: Only approved tag namespaces used

### Regular Maintenance
1. **Review schedule compliance**: Update nodes according to review cadence
2. **Link validation**: Ensure no broken cross-references
3. **Content updates**: Incorporate new examples and applications
4. **Relationship refinement**: Add new cross-links as vault grows

---

## Migration from Previous Standards

### Deprecated Elements (DO NOT USE)
```yaml
# DEPRECATED FIELDS
dv_type: Definition              # → use type: Definition
dv_domain: cat                   # → use appropriate math/* tag

# DEPRECATED TAG NAMESPACES
node/definition                  # → use concept/* tags
domain/cat                       # → use math/* tags
status/draft                     # → use status: draft field
```

### Migration Process
1. **Identify deprecated patterns**: Search for `dv_type`, `node/*`, `domain/*` tags
2. **Update frontmatter**: Replace with current standard fields
3. **Update tags**: Map to approved tag taxonomy
4. **Validate relationships**: Ensure all cross-links use current concept names
5. **Update timestamps**: Set updated: field to current date

---

## Examples of Compliant Node Frontmatter

### Example 1: Mathematical Definition
```yaml
type: Definition
status: stable
importance: high
tags:
  - concept/number-system
  - concept/algebra
  - chapter-1
  - math/complex
  - math/algebra
sources:
  - MillerGerken2023
source_refs:
  - "Miller & Gerken §1.3 p.108-115"
relations:
  broader:
    - "[[Real_Number_System]]"
  narrower:
    - "[[Imaginary_Unit]]"
    - "[[Complex_Conjugates]]"
  depends_on:
    - "[[Real_Number_System]]"
    - "[[Imaginary_Unit]]"
  related:
    - "[[Quadratic_Formula]]"
    - "[[The_Discriminant]]"
  used_in:
    - "[[Complex_Equations]]"
    - "[[Complex_Graphing]]"
review:
  next: 2025-11-25
  cadence: monthly
created: 2025-10-19
updated: 2025-11-04
```

### Example 2: Mathematical Claim/Property
```yaml
type: Claim
status: stable
importance: critical
tags:
  - concept/properties
  - concept/foundational
  - chapter-r
  - chapter-1
  - math/properties
  - math/algebra
  - method/solving
sources:
  - MillerGerken2023
source_refs:
  - "Miller & Gerken §R.5 p.35-40"
relations:
  broader:
    - "[[Algebraic_Properties]]"
  depends_on:
    - "[[Real_Number_System]]"
    - "[[Multiplication]]"
  related:
    - "[[Factoring_Strategies]]"
  used_in:
    - "[[Polynomial_Equations]]"
    - "[[Quadratic_Equations]]"
    - "[[Factoring_Methods]]"
review:
  next: 2025-11-18
  cadence: monthly
created: 2025-10-19
updated: 2025-11-04
```

### Example 3: System Specification
```yaml
type: Spec
status: active
importance: critical
tags:
  - system/specs
  - system/tracking
sources:
  - internal
source_refs:
  - "Audit findings 2025-11-04"
relations:
  related:
    - "[[Tags Taxonomy]]"
    - "[[Relations - Relation Types]]"
  used_in:
    - "[[Quality_Assurance_Checklist]]"
    - "[[Template_System]]"
review:
  next: 2025-12-04
  cadence: monthly
created: 2025-10-23
updated: 2025-11-04
```

---

## Tools and Automation Support

### Dataview Queries Enabled
The standardized frontmatter supports rich Dataview queries:

```javascript
// Find all concepts needing review
TABLE review.next, status, importance
FROM "02_Concepts"
WHERE review.next < date(today)
SORT review.next ASC

// Find concepts by mathematical domain
LIST
FROM #math/equations 
WHERE type = "Definition"
SORT file.name ASC

// Analyze relationship density
TABLE length(relations.broader) + length(relations.narrower) + 
      length(relations.depends_on) + length(relations.related) + 
      length(relations.used_in) as "Relationships"
FROM "02_Concepts"
WHERE type = "Definition"
SORT Relationships DESC
```

### Quality Assurance Scripts
Standard structure enables automated checking:
- Required field validation
- Tag taxonomy compliance
- Bidirectional link verification
- Review schedule monitoring

---

## Compliance Verification

### Self-Check Questions
Before submitting any concept node:

1. **Structure**: Does frontmatter include all required fields?
2. **Tags**: Are all tags from approved taxonomy namespaces?
3. **Relationships**: Are there at least 3 meaningful cross-links?
4. **Content**: Does content match the node type requirements?
5. **Sources**: Are all claims properly attributed?
6. **Links**: Do all cross-references point to existing concepts?
7. **Bidirectional**: Are reverse relationships established?

### Quality Gates
- **Draft → In-Progress**: Frontmatter complete, basic content present
- **In-Progress → Review**: Content complete, relationships established
- **Review → Stable**: Quality verified, cross-links validated

---

## Version History

**Version 2.0** (2025-11-04):
- Updated during audit revision implementation
- Clarified frontmatter requirements and content structure
- Added comprehensive examples and quality gates
- Established clear migration path from v1.0

**Version 2.0** (2025-10-23):
- Replaced `dv_type` with `type` field
- Updated tag namespaces to match implementation
- Added relational mapping requirements
- Established bidirectional linking standards

**Version 1.0** (2025-10-19):
- Initial specification with `dv_type` field
- Basic frontmatter structure
- Limited tag taxonomy

---

## Authority and Enforcement

**This document represents the AUTHORITATIVE specification for all Math 1414 concept nodes.**

In case of conflicts between this document and any other specification, template, or example, **THIS DOCUMENT TAKES PRECEDENCE**.

All new concept nodes MUST comply with this standard. All existing nodes SHOULD be migrated to this standard during regular maintenance cycles.

**Compliance is verified through:**
- Manual quality reviews
- Automated validation scripts
- Template system alignment
- Cross-reference integrity checks

---

## References

- [[Tags Taxonomy]] - Controlled vocabulary system
- [[Relations - Relation Types]] - Semantic relationship definitions
- [[Quality_Assurance_Checklist]] - Verification procedures
- [[Template_System]] - Implementation templates

---

*This specification was last updated during the audit revision implementation initiative.*

**Document Status**: ✅ Active - Official Standard
**Next Review**: 2025-12-04
**Version**: 2.0 (Authoritative)