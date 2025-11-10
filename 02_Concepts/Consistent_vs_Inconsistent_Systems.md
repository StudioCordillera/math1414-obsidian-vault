---
type: Definition
status: in-progress
importance: medium
tags:
  - concept/algebra
  - chapter-5
  - math/systems
  - method/classification
relations:
  broader:
    - [[Linear_Systems]]
  related:
    - [[Gaussian_Elimination]]
    - [[Gauss_Jordan_Elimination]]
    - [[Row_Echelon_Form]]
    - [[Reduced_Row_Echelon_Form]]
  used_in:
    - [[Cramers_Rule]]
    - [[Matrix_Inverse_Method]]
review:
  next: 2025-11-25
updated: 2025-10-25
---

# Consistent vs Inconsistent Systems

Definition
- A linear system is consistent if it has at least one solution (unique or infinitely many). It is inconsistent if it has no solution.

Diagnostics (matrix form)
- Consistent: no row of the form [0 0 … 0 | c] with c ≠ 0.
- Inconsistent: at least one row [0 0 … 0 | c] with c ≠ 0 appears after elimination.
- Infinitely many solutions: at least one free variable (a non-pivot column of A).
- Unique solution: every column of A has a pivot.

Geometric diagnostics (R^2 and R^3)
- R^2: lines intersect once (unique), overlap (infinitely many), or are parallel distinct (none).
- R^3: planes intersect at a point (unique), line/plane of intersection (infinitely many), or are parallel/inconsistent (none).

See Also
- [[Linear_Systems]], [[Gaussian_Elimination]], [[Gauss_Jordan_Elimination]], [[Row_Echelon_Form]], [[Reduced_Row_Echelon_Form]], [[Cramers_Rule]], [[Matrix_Inverse_Method]]
