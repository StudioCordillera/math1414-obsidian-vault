---
layout: concept
title: Piecewise Functions
topic: Functions
type: Definition
status: review
importance: high
tags:
- concept/functions
- math/functions
- chapter-2
sources:
- MillerGerken_AlgTrig2e
source_refs:
- Ch2 §2.7 Piecewise-Defined Functions
relations:
  broader:
  - '[[Functions_Relations_Graphs]]'
  narrower: []
  depends_on:
  - '[[Function_Notation]]'
  - '[[Domain_and_Range]]'
  - '[[Linear_Functions]]'
  defines: []
  related:
  - '[[Continuity]]'
  - '[[Graphing_Functions]]'
  - '[[Absolute_Value]]'
  used_in:
  - '[[01_Course/Textbook/Chapter2_Functions_Relations]]'
review:
  cadence: semester
  next: 2026-01-10
created: 2025-10-21
updated: 2025-11-16
qa_certified: true
qa_date: 2025-11-16
qa_migration: v2.0
narrower:
- '[[Absolute_Value]]'
defines:
- '[[Compound_Inequalities]]'
related:
- '[[Domain_and_Range]]'
---
# Piecewise Functions
Functions defined by different formulas on different parts of the domain.

---

## Definition
A piecewise function f is specified by a finite list of rule–domain pairs:
- f(x) = rule₁(x) for x in interval/set D₁
- f(x) = rule₂(x) for x in interval/set D₂
- …
where the Dᵢ are disjoint and their union is the intended domain of f.

Key points
- Exactly one rule applies to each x in the domain (intervals should not overlap).
- Endpoints must be assigned carefully (≤ vs <) so every domain point is covered once.

---

## Methods
1) Evaluate f(x)
- Determine which interval contains x (use endpoint inclusion/exclusion), then plug into that rule.

2) Graph from definition
- Draw each rule on its interval only.
- Use open circles for excluded endpoints, closed dots for included endpoints.

3) Domain and range
- Domain is the union of the rule intervals.
- Range is the union of the y-values attained on those intervals (track endpoints and extrema of rules on restricted intervals).

4) Continuity at a boundary c
- Compute left value: L = lim(x→c⁻) rule_left(x) (or direct substitution on left rule).
- Compute right value: R = lim(x→c⁺) rule_right(x).
- Compute f(c) from the rule that includes c.
- Continuous at c when L = R = f(c). Jump if L ≠ R; removable if L = R ≠ f(c) or f(c) undefined.

---

## Examples
1) Basic absolute value (piecewise form)
- f(x) = |x| = { −x for x < 0; x for x ≥ 0 }
- Continuous everywhere; vertex at (0,0)

2) A step function
- g(x) = { 2 for x < 1; −1 for x ≥ 1 }
- Jump discontinuity at x = 1; f(1) = −1, left-limit = 2

3) Smooth join with different lines
- h(x) = { 3x + 1 for x ≤ 2; mx + b for x > 2 }
- To be continuous at x = 2: 3(2) + 1 = 6 + 1 = 7 must equal 2m + b → constraint: 2m + b = 7

4) Quadratic/linear join with removable hole
- p(x) = { (x² − 1)/(x − 1) for x ≠ 1; 1 for x = 1 }
- Simplify left rule to x + 1; left/right limits at 1 are 2, but f(1) = 1 → removable discontinuity (not continuous)

---

## Common Misconceptions
- Overlapping intervals or missing endpoints → ambiguous or partially undefined function
- Forgetting to use open vs closed circles in the graph at rule boundaries
- Assuming piecewise automatically means discontinuous (many piecewise functions are continuous)

---

## Connections
- Continuity at a point and across rule boundaries
- Domain/range analysis with restricted intervals
- Modeling with thresholds (tax brackets, shipping rates, absolute value)

---

## See Also
- [[Function_Notation]]
- [[Domain_and_Range]]
- [[Continuity]]
- [[Graphing_Functions]]