---
title: Linear Functions
type: Definition
status: review
importance: critical
tags:
  - node/definition
  - domain/functions
  - chapter2
sources:
  - MillerGerken_AlgTrig2e
source_refs:
  - "Ch2 §2.4 Linear Equations in Two Variables"
relations:
  broader:
    - "[[Functions_Relations_Graphs]]"
  narrower: []
  depends_on:
    - "[[Rectangular_Coordinate_System]]"
    - "[[Linear_Equations]]"
  defines: []
  related:
    - "[[Graphing_Functions]]"
    - "[[Parallel_and_Perpendicular_Lines]]"
    - "[[Point_Conditions_Method]]"
    - "[[Average_Rate_of_Change]]"
  used_in:
    - "[[01_Course/Textbook/Chapter2_Functions_Relations]]"
review:
  cadence: semester
  next: 2026-01-10
created: 2025-10-21
updated: 2025-10-21
---

# Linear Functions
First-order models with constant rate of change

---

## Definition
A linear function is a function whose graph is a straight line. Its common forms:
- Slope–intercept: y = mx + b (m = slope, b = y-intercept)
- Point–slope: y − y₁ = m(x − x₁)
- Standard form: Ax + By = C (A, B, C real; B ≠ 0 for function of x)

Key property
- Constant rate of change: For equal changes in x, the change in y is constant (= m).

Domain/Range (typical)
- Domain: (−∞, ∞)
- Range: (−∞, ∞) unless m = 0 (constant), then Range = {b}

---

## Methods
1) Find slope from two points (x₁, y₁), (x₂, y₂), x₂ ≠ x₁
- m = (y₂ − y₁)/(x₂ − x₁)

2) Find equation from two points
- Compute m, then use point–slope; convert to slope–intercept if desired

3) Find equation from slope and point
- y − y₁ = m(x − x₁)

4) Intercepts
- y-intercept: set x = 0 → y = b
- x-intercept: set y = 0 → 0 = mx + b → x = −b/m (if m ≠ 0)

5) Parallel/Perpendicular
- Parallel: same slope m
- Perpendicular: m₂ = −1/m₁ (when both slopes defined)

---

## Examples
1) Through (2, 5) and (−1, −4)
- m = (−4 − 5)/(−1 − 2) = (−9)/(−3) = 3
- y − 5 = 3(x − 2) → y = 3x − 1

2) Slope −2, through (3, 7)
- y − 7 = −2(x − 3) → y = −2x + 13

3) Intercepts of y = 4x − 8
- y-intercept (0, −8); x-intercept: 0 = 4x − 8 → x = 2 → (2, 0)

---

## Common Misconceptions
- Treating a vertical line x = a as a function (fails vertical line test)
- Confusing perpendicular slope (forgetting negative reciprocal)
- Mixing up x- and y-intercepts

---

## Connections
- Average rate of change equals slope for linear functions
- Parallel and perpendicular line relationships
- Linear models in applications use slope–intercept and point conditions

---

## See Also
- [[Parallel_and_Perpendicular_Lines]]
- [[Point_Conditions_Method]]
- [[Graph_to_Equation]]
- [[Rectangular_Coordinate_System]]
- [[Average_Rate_of_Change]]
