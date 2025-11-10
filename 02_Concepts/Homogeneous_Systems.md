---
layout: concept
title: "Homogeneous Systems"
topic: "Systems & Matrices"
title: Homogeneous Systems
type: Topic
status: in-progress
importance: high
tags:
  - concept/algebra
  - chapter-5
  - math/systems
  - method/solving
relations:
  broader:
    - [[Linear_Systems]]
  depends_on:
    - [[Row_Echelon_Form]]
    - [[Gaussian_Elimination]]
  related:
    - [[Particular_and_General_Solutions]]
    - [[Equivalent_Systems]]
    - [[Row_Space]]
  used_in:
    - [[Chapter5_Core_Set_Checklist]]
review:
  next: 2025-11-25
updated: 2025-10-25
---
# Homogeneous Systems

Definition
- A linear system Ax = 0. Always consistent; at least the trivial solution x = 0.

Key facts
- If number of variables > rank(A), there are infinitely many solutions (free variables).
- Solution set is a subspace of R^n; spans the null space of A.

Method (solve)
1) Form augmented matrix [A|0].
2) Row-reduce to RREF.
3) Parametrize general solution using free variables.

Examples
- Example with two free variables producing a solution family.

Common pitfalls
- Claiming “unique solution” for homogeneous systems with fewer pivots than variables.
- Forgetting that Ax=0 is always consistent.

See also
- [[Linear_Systems]] · [[Row_Echelon_Form]] · [[Reduced_Row_Echelon_Form]] · [[Gaussian_Elimination]] · [[Null_Space]] · [[Particular_and_General_Solutions]]
