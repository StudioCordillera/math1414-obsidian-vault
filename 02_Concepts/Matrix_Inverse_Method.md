---
type: Method
status: in-progress
importance: medium
tags:
  - concept/algebra
  - chapter-5
  - math/matrices
  - method/solving
relations:
  broader:
    - [[Linear_Systems]]
  depends_on:
    - [[Inverse_Matrix]]
    - [[Matrix_Multiplication]]
  related:
    - [[Determinant]]
    - [[Cramers_Rule]]
review:
  next: 2025-11-25
created: 2025-10-25
updated: 2025-10-25
---

# Inverse Matrix Method (AX = B)

Method
- If A is invertible, the unique solution is X = A^{-1}B.

Requirements
- Square coefficient matrix A; det(A) ≠ 0

Pitfalls
- Attempting to use when det(A)=0 (no inverse)
- Order matters: A^{-1}B ≠ BA^{-1}

See also
- [[Inverse_Matrix]], [[Matrix_Multiplication]], [[Determinant]], [[Cramers_Rule]]
