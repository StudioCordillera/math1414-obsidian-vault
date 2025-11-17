---
layout: concept
title: "System Types"
topic: "Systems & Matrices"
title: System Types
type: Topic
status: in-progress
importance: high
tags:
  - concept/algebra
  - chapter-5
  - math/systems
  - method/classification
relations:
  broader:
    - [[Linear_Systems]]
  depends_on:
    - [[Row_Echelon_Form]]
    - [[Gaussian_Elimination]]
  related:
    - [[Consistent_vs_Inconsistent_Systems]]
    - [[Equivalent_Systems]]
    - [[Reduced_Row_Echelon_Form]]
  used_in:
    - [[Chapter5_Core_Set_Checklist]]
review:
  next: 2025-11-25
updated: 2025-11-16
qa_certified: true
qa_date: 2025-11-16
qa_migration: v2.0
---
# System Types

Definition
- Classifies linear systems by number of equations vs unknowns and by solution structure.
  - Consistent: at least one solution; Inconsistent: no solution.
  - Independent: exactly one solution; Dependent: infinitely many solutions.
  - Underdetermined: fewer pivots than variables; Overdetermined: more equations (may be consistent or not).

Method (diagnose from row-reduced form)
1) Form the augmented matrix and row-reduce to REF or RREF.
2) Look for contradictory rows (0 … 0 | nonzero) → inconsistent.
3) Count pivots vs variables → if pivots < variables and no contradiction → infinite solutions (dependent).
4) If pivots = variables and no contradiction → unique solution (independent).

Examples
- Unique solution: pivots in every variable column; no contradictions.
- Infinite solutions: a free variable appears; express general solution parametrically.
- No solution: row [0 0 … 0 | c], c ≠ 0.

Common pitfalls
- Confusing overdetermined with inconsistent; extra equations can be redundant.
- Declaring “no solution” just because variables > equations (not necessarily true).

See also
- [[Consistent_vs_Inconsistent_Systems]] · [[Linear_Systems]] · [[Gaussian_Elimination]] · [[Row_Echelon_Form]] · [[Reduced_Row_Echelon_Form]] · [[Equivalent_Systems]]
