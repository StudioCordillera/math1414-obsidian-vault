---
layout: concept
title: "Algebraic Test for One to One"
topic: "General Math"
type: Method
status: review
importance: high
tags:
  - method/algebraic
  - chapter-4
  - math/functions
  - property/injectivity
created: 2025-11-05
updated: 2025-11-05
review:
  next: 2025-12-05
  cadence: monthly
relations:
  broader:
    - [[One_to_One_Function]]
  narrower: []
  depends_on:
    - [[Equality_Properties]]
    - [[Function_Notation]]
    - [[Domain_and_Range]]
  defines: []
  related:
    - [[Horizontal_Line_Test]]
    - [[Inverse_Functions]]
  used_in:
    - [[Inverse_Functions]]
    - [[01_Course/Textbook/Chapter4_Exponential_Logarithmic]]
sources:
  - Textbook/Algebra_by_section
source_refs:
  - [[00_Books/Algebra_by_section/pages/p440]]–[[00_Books/Algebra_by_section/pages/p448]]
updated: 2025-11-16
qa_certified: true
qa_date: 2025-11-16
qa_migration: v2.0
---

# Algebraic Test for One-to-One (Injectivity)

Purpose
Provide an equation-manipulation procedure to certify that a function f is one-to-one on a stated domain D without graphing.

Method (procedure)
- Input: Rule for f and domain D.
- Output: Decision: one-to-one on D? (Yes/No) with justification.

Steps
1) Start with f(a) = f(b) where a, b are arbitrary elements of D.
2) Apply algebraic operations that are reversible on D (e.g., add/subtract, multiply/divide by nonzero expressions valid on D, apply a strictly monotone function on D like exp or ln with valid domains).
3) Aim to deduce a = b. If the only way the equality can hold is when a = b, then f is one-to-one on D.
4) If any non-invertible step is used (e.g., squaring), you must split into cases and back-check to ensure no distinct a, b satisfy the equation.
5) Conclude: If f(a) = f(b) ⇒ a = b for all a, b ∈ D, then f is one-to-one on D.

Worked examples
- Linear (nonzero slope): f(x) = 2x − 5 on ℝ. Suppose 2a − 5 = 2b − 5 ⇒ a = b. Therefore injective.
- Rational: f(x) = (x − 3)/(x + 2), D = ℝ \ {−2}. Assume (a − 3)/(a + 2) = (b − 3)/(b + 2). Cross-multiply (valid since denominators ≠ 0 on D): (a − 3)(b + 2) = (b − 3)(a + 2). Expand and simplify ⇒ a = b.
- Cubic: f(x) = x^3 + 2x. f(a) − f(b) = (a − b)(a^2 + ab + b^2 + 2). Since a^2 + ab + b^2 + 2 > 0 for all real a, b, we must have a − b = 0 ⇒ a = b. Injective on ℝ.
- Exponential: f(x) = 3^x on ℝ. 3^{a} = 3^{b} ⇒ apply ln (strictly increasing): a ln 3 = b ln 3 ⇒ a = b. Injective.
- Quadratic (counterexample on ℝ): f(x) = x^2. f(−2) = f(2) = 4 with −2 ≠ 2 ⇒ not injective on ℝ. But on D = [0, ∞): if a^2 = b^2 and a, b ≥ 0 ⇒ a = b; injective on D.

Checks and caveats
- Domain matters: Every step must be legal on D. State D up front.
- Reversibility: Prefer operations with two-sided inverses on D. If you square (not one-to-one), check for spurious equalities.
- Case splits: If an operation introduces cases (e.g., absolute values), analyze each case on D.

Connections
- Certifies: [[One_to_One_Function]].
- Complements: [[Horizontal_Line_Test]] (graphical counterpart).
- Enables: [[Inverse_Functions]] (construct and validate inverses).

Summary
To prove injectivity algebraically, start from f(a) = f(b), use only domain-valid reversible steps, and force a = b. If that implication holds for all a, b in the domain, f is one-to-one on that domain.
