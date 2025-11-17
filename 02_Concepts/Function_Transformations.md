---
layout: concept
title: Function Transformations
topic: Functions
type: Method
status: review
importance: high
tags:
- method/functions
- math/functions
- chapter-2
sources:
- MillerGerken_AlgTrig2e
source_refs:
- Ch2 §2.6 Transformations of Graphs
relations:
  broader:
  - '[[Functions_Relations_Graphs]]'
  narrower: []
  depends_on:
  - '[[Function_Notation]]'
  defines: []
  related:
  - '[[Master_Transformation_Map]]'
  - '[[Graphing_Functions]]'
  - '[[Domain_and_Range]]'
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
related:
- '[[Continuity]]'
---
# Function Transformations
Rules for shifting, reflecting, and scaling graphs from a base function.

---

## Core Rules (y = f(x))
- Vertical shift: y = f(x) + k → shift up k (k>0) / down |k| (k<0)
- Horizontal shift: y = f(x − h) → shift right h (h>0) / left |h| (h<0)
- Vertical stretch/shrink: y = a·f(x) → stretch if |a|>1, shrink if 0<|a|<1; reflect across x-axis if a<0
- Horizontal stretch/shrink: y = f(bx) → shrink horizontally if |b|>1; stretch if 0<|b|<1; reflect across y-axis if b<0
- Reflections: y = −f(x) (x-axis), y = f(−x) (y-axis)
- Absolute value wrapper: y = |f(x)| reflects negative y parts above x-axis

Order sensitivity
- Horizontal transformations (inside x) act before vertical; when in doubt, map key points in order: input shift/scale → apply f → output scale/shift.

---

## Method (from base function)
1) Identify base function g (e.g., x^2, |x|, √x, 1/x).
2) Parse transformation in the form y = A·g(B(x − h)) + k.
3) Apply in this conceptual order on points:
   - Input: scale by 1/B, shift by h (x → (x − h)/B)
   - Output: compute g, then scale by A, then shift by k
4) Transform key features (intercepts, vertex/asymptotes, domain/range).
5) Sketch accurately using transformed features.

---

## Examples
1) Parabola
- y = 2(x − 3)^2 − 5 → from y = x^2
- Transformations: right 3, vertical stretch ×2, down 5; vertex (3, −5)

2) Absolute value
- y = −|x + 1| + 4 → from y = |x|
- Left 1, reflect x-axis, up 4; vertex (−1, 4)

3) Square root
- y = √(2x − 6) → from y = √x
- Inside: 2x − 6 = 2(x − 3) → right 3, horizontal shrink by factor 1/2
- Domain: x ≥ 3; Range: y ≥ 0

4) Reciprocal
- y = (1/(x + 2)) − 3 → from y = 1/x
- Left 2, down 3; vertical asymptote x = −2; horizontal asymptote y = −3

---

## Common Misconceptions
- Treating f(x + h) as a right shift (it is left by h)
- Ignoring order: applying vertical scale before identifying horizontal effects can misplace points
- Forgetting asymptote shifts for rational functions
- Assuming domain/range unchanged under transformations

---

## Connections
- Integrates with [[Master_Transformation_Map]] for route planning
- Requires precise [[Function_Notation]] understanding of inside vs outside operations
- Affects [[Domain_and_Range]] and intercepts/asymptotes

---

## See Also
- [[Master_Transformation_Map]]
- [[Graphing_Functions]]
- [[Domain_and_Range]]