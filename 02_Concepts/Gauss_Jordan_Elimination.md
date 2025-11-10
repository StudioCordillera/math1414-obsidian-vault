---
layout: concept
title: "Gauss Jordan Elimination"
topic: "General Math"
type: Method
status: in-progress
importance: high
tags:
  - concept/algebra
  - chapter-5
  - math/matrices
  - method/elimination
relations:
  broader:
    - [[Gaussian_Elimination]]
  depends_on:
    - [[Row_Operations]]
    - [[Augmented_Matrix]]
    - [[Row_Echelon_Form]]
  related:
    - [[Reduced_Row_Echelon_Form]]
    - [[Matrix_Inverse_Method]]
    - [[Consistent_vs_Inconsistent_Systems]]
  used_in:
    - [[Cramers_Rule]]
review:
  next: 2025-11-25
updated: 2025-10-25
---

# Gauss–Jordan Elimination

Definition
- An algorithm that extends Gaussian Elimination to continue pivot operations until the augmented matrix is in reduced row echelon form (RREF), yielding the solution directly.

Method (high-level)
1) Form the augmented matrix [A|b].
2) Forward phase: use row operations to get leading 1s (pivots) and zeros below (REF).
3) Backward phase: continue row operations to zero out entries above pivots and scale pivots to 1 (RREF).
4) Read the solution from the final augmented matrix.

Notes
- Row operations: swap rows, scale a row by a nonzero constant, add a multiple of one row to another.
- Pivoting on zero requires row swaps to avoid division by zero.
- Inconsistent system ↔ a row of the form [0 0 … 0 | c] with c ≠ 0.
- Free variables arise when a column of A lacks a pivot (infinitely many solutions).

Worked micro-example
- Solve x + 2y = 5, 3x + 8y = 17.
  [1 2 | 5] → R2 ← R2 − 3R1 → [0 2 | 2] → scale R2 → [0 1 | 1] → R1 ← R1 − 2R2 → [1 0 | 3].
  Solution: (x, y) = (3, 1).

Common pitfalls
- Dividing by zero when a pivot is zero (swap first).
- Forgetting to scale pivots to 1 in the Jordan phase.
- Misreading solution type (unique vs infinite vs none).

See Also
- [[Gaussian_Elimination]], [[Reduced_Row_Echelon_Form]], [[Row_Operations]], [[Augmented_Matrix]], [[Matrix_Inverse_Method]], [[Cramers_Rule]], [[Consistent_vs_Inconsistent_Systems]]
