---
title: Secant Line
type: Definition
status: in-progress
importance: medium
tags:
  - node/definition
  - domain/functions
  - chapter2
sources:
  - MillerGerken_AlgTrig2e
source_refs:
  - Ch2 §2.8 Rate of Change and Secant Lines
relations:
  broader:
    - "[[Functions_Relations_Graphs]]"
  narrower: []
  depends_on:
    - "[[Function_Notation]]"
    - "[[Linear_Functions]]"
  defines: []
  related:
    - "[[Average_Rate_of_Change]]"
    - "[[Slope]]"
    - "[[Graphing_Functions]]"
  used_in:
    - "[[01_Course/Textbook/Chapter2_Functions_Relations]]"
review:
  cadence: semester
  next: 2026-01-10
created: 2025-10-21
updated: 2025-10-21
---

# Secant Line
A secant line to the graph of y = f(x) over points x = a and x = b is the line passing through the two points (a, f(a)) and (b, f(b)).

---

## Definition and Formula
- Slope of the secant line on [a, b]: m_sec = (f(b) − f(a)) / (b − a)
- The secant line equation through (a, f(a)) with slope m_sec:
  - y − f(a) = m_sec (x − a)

---

## Examples
1) f(x) = x^2 on [1, 4]
- m_sec = (16 − 1)/(4 − 1) = 15/3 = 5
- Line: y − 1 = 5(x − 1) → y = 5x − 4

2) f(x) = √x on [4, 9]
- m_sec = (3 − 2)/(9 − 4) = 1/5
- Line: y − 2 = (1/5)(x − 4)

---

## Common Misconceptions
- Confusing secant slope with instantaneous rate (tangent slope)
- Reversing point order inconsistently (sign errors)
- Using points not in the domain of f

---

## Connections
- Average rate of change equals the slope of the secant line on [a, b]
- As b → a, the secant line approaches the tangent line (calculus preview)

---

## See Also
- [[Average_Rate_of_Change]]
- [[Slope]]
- [[Graphing_Functions]]