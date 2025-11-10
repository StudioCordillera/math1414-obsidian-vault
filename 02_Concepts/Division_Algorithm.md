---
layout: concept
title: "Division Algorithm"
topic: "General Math"
type: Claim
status: review
importance: high
tags:
  - node/claim
  - domain/analysis
  - pedagogy/foundation
  - status/review
sources:
  - "Textbook Chapter 3"
source_refs:
  - "Ch.3 — Polynomial functions"
relations:
  broader:
    - "[[Polynomial_Equations]]"
  narrower:
    - "[[Remainder_Theorem]]"
    - "[[Factor_Theorem]]"
    - "[[Synthetic_Division]]"
    - "[[Polynomial_Long_Division]]"
  depends_on: []
  defines: []
  related:
    - "[[Finding_Polynomial_Roots]]"
    - "[[Rational_Root_Theorem]]"
  used_in:
    - "[[Finding_Polynomial_Roots]]"
    - "[[Graphing_Rational_Functions]]"
created: 2025-10-21
updated: 2025-10-21
---
# The Division Algorithm for Polynomials
*Dividend = Divisor × Quotient + Remainder, always and uniquely*

---

## Core Insight
For any polynomials f(x) and d(x) with d(x) ≠ 0, there exist unique polynomials q(x) and r(x) such that
```
f(x) = d(x) · q(x) + r(x),
```
with deg r < deg d (or r(x) = 0). This is the foundation under Remainder Theorem, Factor Theorem, synthetic division, and long division.

Why it matters
- Existence: you can always divide with remainder
- Uniqueness: the quotient and remainder are determined
- Degree constraint: guarantees “no more division is possible”

---

## Method (how it’s used)
- Long division (general d): compute q(x), r(x) with deg r < deg d
- Synthetic division (linear d = x − c): fast coefficients-only algorithm
- Remainder-only: when d = x − c, r = f(c) (Remainder Theorem)
- Factor test: r = 0 implies d divides f (Factor Theorem)

---

## Worked examples
1) Nonlinear divisor (long division)
Divide f(x) = 2x⁴ + 3x³ − x² + 5x − 2 by d(x) = x² + x − 1.
Result: q(x) = 2x² + x, r(x) = 6x − 2, and
```
2x⁴ + 3x³ − x² + 5x − 2 = (x² + x − 1)(2x² + x) + (6x − 2)
```
Check: deg r = 1 < deg d = 2.

2) Linear divisor (synthetic division)
Divide f(x) = 3x³ − 5x² + 2x − 7 by x − 2. Synthetic division gives q(x) = 3x² + x + 4, r = 1, so
```
3x³ − 5x² + 2x − 7 = (x − 2)(3x² + x + 4) + 1
```

---

## Common pitfalls
- Forgetting zero placeholders in long/synthetic setups
- Stopping with deg r ≥ deg d (can still divide)
- Sign errors when subtracting rows in long division
- Using c with wrong sign for (x − c)

---

## Connections
- Specialize to d = x − c → [[Remainder_Theorem]]
- If r = 0 → [[Factor_Theorem]] (exact division)
- Efficient algorithm for d = x − c → [[Synthetic_Division]]
- General algorithm → [[Polynomial_Long_Division]]

See also: [[Rational_Root_Theorem]], [[Finding_Polynomial_Roots]]
