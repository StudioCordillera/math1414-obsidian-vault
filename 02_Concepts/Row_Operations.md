---
type: Method
status: in-progress
importance: high
tags:
  - concept/algebra
  - chapter-5
  - math/matrices
  - method/row-operations
relations:
  broader:
    - [[Gaussian_Elimination]]
  depends_on:
    - [[Linear_Equations]]
  related:
    - [[Augmented_Matrix]]
    - [[Row_Echelon_Form]]
    - [[Reduced_Row_Echelon_Form]]
    - [[Equivalent_Systems]]
  used_in:
    - [[Linear_Systems]]
review:
  next: 2025-11-25
created: 2025-10-25
updated: 2025-10-25
---

# Row Operations (Elementary)

Allowed operations (preserve solution set)
- Swap two rows (Ri ↔ Rj)
- Multiply a row by a nonzero scalar (k·Ri)
- Add a multiple of one row to another (Ri + k·Rj → Ri)

Method (Gaussian elimination outline)
- Form augmented matrix
- Use leading 1s (pivots) and zeros below to reach row echelon form
- Back-substitute (or continue to RREF via Gauss-Jordan)

Common mistakes
- Multiplying a row by 0 (destroys information)
- Forgetting to apply operations to the entire row (both coefficient and constant parts)

See also
- [[Gaussian_Elimination]], [[Augmented_Matrix]], [[Row_Echelon_Form]], [[Reduced_Row_Echelon_Form]], [[Equivalent_Systems]]
