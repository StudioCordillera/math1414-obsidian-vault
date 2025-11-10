---
layout: concept
title: "Gaussian Elimination"
topic: "Systems & Matrices"
type: Method
status: in-progress
importance: high
tags:
  - concept/algebra
  - chapter-5
  - math/matrices
  - method/solving
relations:
  broader:
    - [[Linear_Systems]]
  depends_on:
    - [[Row_Operations]]
    - [[Augmented_Matrix]]
  related:
    - [[Row_Echelon_Form]]
    - [[Reduced_Row_Echelon_Form]]
    - [[Matrix_Inverse_Method]]
  used_in:
    - [[Systems_Applications]]
review:
  next: 2025-11-25
created: 2025-10-25
updated: 2025-10-25
---

# Gaussian Elimination

Method (outline)
1) Form augmented matrix
2) Pivot: create leading 1 in column 1 (swap/scale if needed)
3) Zero out entries below pivot using row operations
4) Move to next column/row (stair-step), repeat
5) Back-substitute to obtain solution (or continue to RREF)

Interpretation
- Row-echelon form reveals consistency and solution class (unique/infinitely many/none)

Pitfalls
- Division by zero when scaling (check pivot)
- Arithmetic errors during elimination (track fractions carefully)

See also
- [[Row_Operations]], [[Augmented_Matrix]], [[Row_Echelon_Form]], [[Reduced_Row_Echelon_Form]]
