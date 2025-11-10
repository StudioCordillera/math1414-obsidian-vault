---
layout: concept
title: "Continuity"
topic: "General Math"
title: Continuity
type: Definition
status: review
importance: high
tags:
  - node/definition
  - domain/functions
  - chapter2
sources:
  - MillerGerken_AlgTrig2e
source_refs:
  - Ch2 §2.8 Continuity (precalculus scope)
relations:
  broader:
    - "[[Functions_Relations_Graphs]]"
  narrower: []
  depends_on:
    - "[[Function_Notation]]"
    - "[[Domain_and_Range]]"
    - "[[Piecewise_Functions]]"
  defines: []
  related:
    - "[[Piecewise_Functions]]"
    - "[[Average_Rate_of_Change]]"
    - "[[Graphing_Functions]]"
    - "[[Function_Transformations]]"
  used_in:
    - "[[01_Course/Textbook/Chapter2_Functions_Relations]]"
review:
  cadence: semester
  next: 2026-01-10
created: 2025-10-21
updated: 2025-10-21
---

# Continuity
Informal notion: a function you can draw without lifting your pencil on an interval.

---

## Definition (precalculus scope)
A function f is continuous at x = c if all three hold:
- f(c) is defined
- lim(x→c) f(x) exists
- lim(x→c) f(x) = f(c)

Types of discontinuities
- Removable (hole): left and right limits agree but differ from f(c) or f(c) undefined
- Jump: left and right limits exist but are unequal
- Infinite: function grows without bound near c (vertical asymptote)

On intervals
- Continuous on (a, b) if continuous at every point in (a, b)
- Continuous on [a, b] if continuous on (a, b) and has appropriate one-sided continuity at a and b

---

## Methods
1) Check continuity at a point c
- Compute f(c), left/right limits (from formula or graph), compare

2) Piecewise joins
- Match boundary values: require left rule value at c equals right rule value at c equals f(c)

3) Recognize continuous building blocks
- Polynomials are continuous everywhere
- Rational functions: continuous where denominator ≠ 0
- Roots, absolute value: continuous where defined

4) Domain first
- Discuss continuity only on the domain of f; points outside the domain are not candidates for continuity

---

## Examples
1) Polynomial
- f(x) = 3x² − x + 5 → continuous ∀x ∈ ℝ

2) Rational with hole
- g(x) = (x² − 4)/(x − 2) → simplifies to x + 2 for x ≠ 2; removable discontinuity at x = 2

3) Jump
- h(x) = { 1 for x < 0; 2 for x ≥ 0 } → jump at 0

4) Infinite
- p(x) = 1/(x − 1) → infinite discontinuity (vertical asymptote x = 1)

5) Absolute value
- q(x) = |x| → continuous ∀x ∈ ℝ (not differentiable at 0, but still continuous)

6) Hole removed by definition
- r(x) = (x² − 4)/(x − 2) for x ≠ 2, and define r(2) = 4 → becomes continuous at x = 2

---

## Common Misconceptions
- Assuming lim f(x) exists whenever f(c) exists
- Believing absolute value or a square root creates discontinuity everywhere (they are continuous where defined)
- Confusing “differentiable” with “continuous” (differentiable ⇒ continuous, but not conversely)
- Calling a point outside the domain “a discontinuity” (it is not part of the function’s domain)

---

## Connections
- Domain and range constrain where continuity can be considered
- Function transformations preserve continuity on their domains
- Piecewise definitions require matching boundary values for continuity
- Average rate of change via secant lines approaches instantaneous rate only when continuity holds

---

## See Also
- [[Piecewise_Functions]]
- [[Domain_and_Range]]
- [[Function_Notation]]
- [[Average_Rate_of_Change]]
- [[Function_Transformations]]
