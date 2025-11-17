---
layout: concept
title: "Cramers Rule"
topic: "Systems & Matrices"
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
    - [[Determinant]]
  related:
    - [[Matrix_Inverse_Method]]
    - [[Gaussian_Elimination]]
review:
  next: 2025-11-25
created: 2025-10-25
updated: 2025-11-16
qa_certified: true
qa_date: 2025-11-16
qa_migration: v2.0
---

# Cramer's Rule

Method (2×2, 3×3)
- For AX=B with det(A)≠0, x_i = det(A_i)/det(A) where A_i replaces column i with B.

Pros/Cons
- Useful for theoretical insight and small systems; not efficient for large systems.

See also
- [[Determinant]], [[Matrix_Inverse_Method]], [[Gaussian_Elimination]]
