---
layout: exercise
type: Definition
status: review
importance: critical
title: "Chapter 4 Section 4.1 - Exponential Functions Exercises"
tags:
  - concept/functions
  - chapter-4
  - injectivity
  - inverse-functions
relations:
  broader:
    - "[[Inverse_Functions]]"
  depends_on:
    - "[[Function_Notation]]"
    - "[[Domain_and_Range]]"
  related:
    - "[[Horizontal_Line_Test]]"
    - "[[Algebraic_Test_for_One_to_One]]"
    - "[[Monotonic_Functions]]"
    - "[[Exponential_Functions]]"
    - "[[Logarithmic_Functions]]"
  used_in:
    - "[[Logarithmic_Equations]]"
    - "[[Inverse_Functions]]"
  defined_in:
    - "[[Chapter4_Exponential_Logarithmic]]"
review:
  next: 2025-12-01
created: 2025-10-25
updated: 2025-11-05
---

# One-to-One Function (Injective)

Definition
A function f: D→R is one-to-one (injective) if for all a,b∈D, f(a)=f(b) ⇒ a=b. Equivalently: a≠b ⇒ f(a)≠f(b). If f is injective on D, then f has an inverse function f^{-1}: f(D)→D.

Equivalent characterizations
- Graphical: Horizontal Line Test (any horizontal line intersects the graph at most once).
- Monotonicity: If f is strictly increasing or strictly decreasing on D, then f is injective on D.
- Calculus (preview): If f' does not change sign and f is continuous on D, then f is injective.

Procedures
- Graphical test (HLT): Inspect graph on the stated domain D. If any horizontal line cuts twice or more → not injective.
- Algebraic test: Assume f(a)=f(b). Use reversible steps to deduce a=b. Watch for nonreversible steps (squaring, multiplying by zero divisors, taking even roots) and domain restrictions.
- Make invertible: Identify intervals where f is monotone. Restrict domain to such an interval, then find and verify f^{-1} by composition.

Worked examples
1) Linear: f(x)=−3x+5 on ℝ. Injective (slope≠0). Inverse: f^{-1}(y)=(5−y)/3.
2) Quadratic with restriction: q(x)=x^2 on [0,∞). Injective (monotone). q^{-1}(y)=√y.
3) Absolute value: a(x)=|x−4| on ℝ. Not injective. Restrict to [4,∞) or (−∞,4] to make injective, then invert piecewise.
4) Exponential: E(x)=2^{x+1}−7 on ℝ. Injective (strictly increasing). Inverse: E^{-1}(y)=log_2(y+7)−1.
5) Rational: r(x)=(x−3)/(x+2), x≠−2. Injective (cross-multiply valid since denominators nonzero): r(a)=r(b) ⇒ (a−3)(b+2)=(b−3)(a+2) ⇒ a=b.

Common misconceptions/errors
- Using Vertical Line Test for injectivity (it tests “is a function”, not “one-to-one”).
- Forgetting to state the domain; injectivity depends on D.
- Irreversible steps in algebraic test (e.g., squaring) creating false implications.
- Assuming all polynomials are injective; odd-degree can still fail (e.g., x^3−x).

Relations and cross-links
- Depends on: [[Function_Notation]], [[Domain_and_Range]].
- Related: [[Horizontal_Line_Test]], [[Algebraic_Test_for_One_to_One]], [[Monotonic_Functions]].
- Used in: [[Inverse_Functions]], [[Logarithmic_Equations]].
- See also: [[Exponential_Functions]], [[Logarithmic_Functions]].

Summary
Injectivity guarantees unique outputs per input and enables the existence of an inverse function. Use HLT or an algebraic proof to certify; restrict domain on non-monotone functions to obtain invertibility.
