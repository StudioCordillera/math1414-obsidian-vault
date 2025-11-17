---
layout: concept
title: Synthetic Division
topic: General Math
type: Method
status: review
importance: high
tags:
- concept/algebra
- chapter-3
- math/polynomials
- method/division
sources:
- Textbook Chapter 3
source_refs:
- Ch.3 — Polynomial functions
relations:
  broader:
  - '[[Finding_Polynomial_Roots]]'
  - '[[Division_Algorithm]]'
  narrower: []
  depends_on:
  - '[[Remainder_Theorem]]'
  - '[[Factor_Theorem]]'
  defines: []
  related:
  - '[[Rational_Root_Theorem]]'
  - '[[Constructing_Polynomials_from_Roots]]'
  used_in:
  - '[[Finding_Polynomial_Roots]]'
created: 2025-10-21
updated: 2025-11-16
qa_certified: true
qa_date: 2025-11-16
qa_migration: v2.0
related:
- '[[Factor_Theorem]]'
- '[[Factoring_Polynomials]]'
- '[[Polynomial_Long_Division]]'
- '[[Remainder_Theorem]]'
---
# Synthetic Division and the Remainder Theorem
*The Fast-Track Method for Polynomial Division*

---

## 🎯 CORE INSIGHT

**Synthetic Division is Polynomial Long Division on Steroids**

When dividing a polynomial by a linear factor (x - c), synthetic division gives you the quotient AND remainder in seconds—no variables, no subtraction, just elegant arithmetic.

**The Pattern:**
```
Divide P(x) by (x - c):
1. Use only coefficients
2. Multiply and add (no subtraction!)
3. Last number = remainder = P(c)
```

**Why This Matters:**
- Speed: faster than long division
- Power: tests if (x - c) is a factor instantly
- Connection: the Remainder Theorem links division to function evaluation

**The Remainder Theorem Bridge:** When you divide P(x) by (x - c), the remainder equals P(c). This means synthetic division IS function evaluation.

---

## 📐 THE MATHEMATICAL FOUNDATION

### Division Algorithm (context)
For any polynomials f(x), d(x) (d ≠ 0):
```
f(x) = d(x)·q(x) + r(x),   deg r < deg d
```

### The Remainder Theorem
If P(x) is divided by (x - c), remainder R = P(c).

### Factor Theorem
(x - c) is a factor of P(x) if and only if P(c) = 0.

---

## 🔧 PROCEDURE (step-by-step)

1) Put coefficients in descending-power order; include 0 for missing powers.
2) Use c from (x - c): if dividing by (x + 3), use c = -3.
3) Bring down the first coefficient.
4) Multiply by c; write under next coefficient; add the column.
5) Repeat to the end. The last number is the remainder; the others are quotient coefficients.

---

## 📋 WORKED EXAMPLES

### Example 1: Divide and Interpret
Divide P(x) = 2x³ - 5x² + 3x - 7 by (x - 2).
```
     2 |  2   -5    3   -7
       |      4   -2    2
       |____________________
         2   -1    1   -5
```
Quotient: 2x² - x + 1,  Remainder: -5.
Verification: P(x) = (x - 2)(2x² - x + 1) - 5.

### Example 2: Factor Test
Is (x + 3) a factor of x³ + 2x² - 5x + 6?
```
    -3 |  1   2  -5   6
       |     -3   3   6
       |________________
         1  -1  -2  12
```
Remainder 12 ≠ 0 → Not a factor.

### Example 3: Evaluate P(c)
Use synthetic division to find P(4) for P(x) = 3x⁴ - 2x² + 7.
```
     4 |  3   0  -2   0   7
       |     12  48 184 736
       |____________________
         3  12  46 184 743
```
P(4) = 743 (remainder).

---

## ⚠️ COMMON PITFALLS
- Wrong sign for c: (x + 5) ⇒ c = -5.
- Missing coefficients: include 0s for missing powers.
- Subtracting instead of adding: synthetic division uses addition because c is signed.
- Misreading the last number: final entry is the remainder, not part of the quotient.

---

## 🔗 CONNECTIONS
- Prerequisites: [[Division_Algorithm]], [[Remainder_Theorem]]
- Related: [[Factor_Theorem]], [[Rational_Root_Theorem]], [[Finding_Polynomial_Roots]], [[Constructing_Polynomials_from_Roots]]
- Applications: testing candidates, evaluating P(c), progressive factorization

---

## 🎓 EXAM STRATEGIES
- Choose synthetic division when divisor is linear (x - c) or can be written as a(x - b) → use c = b/a after factoring out a.
- Test easy candidates first (±1, small integers) when searching for roots.
- After finding one root, divide and continue with the quotient.
