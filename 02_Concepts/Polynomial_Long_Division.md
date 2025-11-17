---
layout: concept
title: "Polynomial Long Division"
topic: "Polynomials"
type: Method
status: in-progress
importance: high
tags:
  - concept/algebra
  - chapter-3
  - math/polynomials
  - method/division
sources:
  - Textbook Chapter 3
source_refs:
  - Ch.3 — Polynomial functions (division)
relations:
  broader:
    - "[[Division_Algorithm]]"
  narrower: []
  depends_on:
    - "[[Polynomial_Equations]]"
    - "[[Standard_Form]]"
  defines: []
  related:
    - "[[Remainder_Theorem]]"
    - "[[Synthetic_Division]]"
    - "[[Factor_Theorem]]"
  used_in:
    - "[[Finding_Polynomial_Roots]]"
review:
  next: 2025-11-25
created: 2025-10-25
updated: 2025-11-16
qa_certified: true
qa_date: 2025-11-16
qa_migration: v2.0
---
# Polynomial Long Division

Purpose: Divide one polynomial by another to obtain a quotient and remainder, following the Division Algorithm.

Core idea (Division Algorithm): For polynomials P(x) and D(x) ≠ 0,
there exist unique Q(x) and R(x) with deg R < deg D such that:
P(x) = D(x)·Q(x) + R(x).

Method (steps):
1) Order both polynomials in descending powers; fill missing terms with 0 coefficients.
2) Divide leading term by leading term to get the next term of the quotient.
3) Multiply the divisor by that term and subtract from the dividend.
4) Bring down the next term; repeat until degree of remainder < degree of divisor.
5) Write result as Q(x) with remainder R(x) over divisor: P/D = Q + R/D.

Worked micro-example:
Divide 2x^3 - 3x + 4 by x - 1.
- Ensure standard form: 2x^3 + 0x^2 - 3x + 4
- 2x^3 ÷ x = 2x^2 → subtract (2x^2)(x - 1) = 2x^3 - 2x^2
- New row: 0x^2 - (−2x^2) = 2x^2; bring down −3x → 2x^2 − 3x
- 2x^2 ÷ x = 2x → subtract (2x)(x − 1) = 2x^2 − 2x
- New row: (−3x) − (−2x) = −x; bring down +4 → −x + 4
- −x ÷ x = −1 → subtract (−1)(x − 1) = −x + 1
- Remainder: 3 (degree 0 < 1)
Answer: Q(x) = 2x^2 + 2x − 1, R(x) = 3 ⇒ (2x^3 − 3x + 4)/(x − 1) = 2x^2 + 2x − 1 + 3/(x − 1)

Common pitfalls:
- Skipping placeholder terms (breaks alignment)
- Subtracting sign errors (remember “subtract the product”)
- Stopping before remainder degree is strictly less than divisor’s degree

See Also: [[Division_Algorithm]], [[Remainder_Theorem]], [[Synthetic_Division]], [[Finding_Polynomial_Roots]]
