---
title: Average Rate of Change
type: Method
status: review
importance: high
tags:
  - node/method
  - domain/functions
  - chapter2
sources:
  - MillerGerken_AlgTrig2e
source_refs:
  - "Ch2 §2.8 (rate of change, secant lines)"
relations:
  broader:
    - "[[Functions_Relations_Graphs]]"
  narrower: []
  depends_on:
    - "[[Function_Notation]]"
    - "[[Linear_Functions]]"
  defines: []
  related:
    - "[[Graphing_Functions]]"
    - "[[Domain_and_Range]]"
    - "[[Continuity]]"
  used_in:
    - "[[01_Course/Textbook/Chapter2_Functions_Relations]]"
review:
  cadence: semester
  next: 2026-01-10
created: 2025-10-21
updated: 2025-10-21
---

# Average Rate of Change
Secant slope between two inputs

---

## Definition
For a function f on an interval [a, b], the average rate of change from a to b is

- (f(b) − f(a)) / (b − a)

Interpretations
- Slope of the secant line through (a, f(a)) and (b, f(b))
- Average change in output per unit change in input over [a, b]

Units
- If x has units Ux and f(x) has units Uy, then ARoC units are Uy per Ux

---

## Method
1) Verify a and b are in the domain of f
2) Compute f(a) and f(b)
3) Compute Δy = f(b) − f(a) and Δx = b − a (ensure b ≠ a)
4) Form ARoC = Δy/Δx; simplify units if applicable
5) Interpret in context when modeling

---

## Examples
1) f(x) = x^2 on [1, 4]
- f(4) − f(1) = 16 − 1 = 15; 4 − 1 = 3 → ARoC = 15/3 = 5

2) g(t) = √t on [4, 9]
- g(9) − g(4) = 3 − 2 = 1; 9 − 4 = 5 → ARoC = 1/5

3) Linear h(x) = −2x + 5 on [a, b]
- ARoC = (h(b) − h(a))/(b − a) = −2 (constant slope)

4) Real-world example
- s(t) distance (meters) at time t (seconds); on [2, 7], average velocity is (s(7) − s(2))/(7 − 2) meters per second

---

## Common Misconceptions
- Mixing order: using (a − b) in denominator with (f(b) − f(a)) numerator (sign error)
- Interpreting ARoC as instantaneous rate (derivative concept)
- Dropping units in applications

---

## Connections
- Equals slope for linear functions
- Approximates instantaneous rate of change (calculus link)
- Useful for monotonicity and average velocity interpretations

---

## See Also
- [[Linear_Functions]]
- [[Graphing_Functions]]
- [[Function_Notation]]
- [[Continuity]]
# See Also
- [[Linear_Functions]]
- [[Function_Notation]]
- [[Secant_Line]]
- [[Slope]]
# # See Also
- [[Secant_Line]]