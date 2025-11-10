---
layout: concept
title: "Function Operations"
topic: "Functions"
title: Function Operations
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
  - Ch2 §2.8 Algebra of Functions and Composition
relations:
  broader:
    - "[[Functions_Relations_Graphs]]"
  narrower: []
  depends_on:
    - "[[Function_Notation]]"
    - "[[Domain_and_Range]]"
    - "[[Domain_Restrictions]]"
  defines: []
  related:
    - "[[Function_Composition]]"
    - "[[Graphing_Functions]]"
  used_in:
    - "[[01_Course/Textbook/Chapter2_Functions_Relations]]"
review:
  cadence: semester
  next: 2026-01-10
created: 2025-10-21
updated: 2025-10-21
---

# Function Operations
Sum, difference, product, and quotient of functions with correct domains.

---

## Definitions (Real-valued functions)
Given functions f and g with domains Dom(f), Dom(g):
- (f + g)(x) = f(x) + g(x)       with domain Dom(f) ∩ Dom(g)
- (f − g)(x) = f(x) − g(x)       with domain Dom(f) ∩ Dom(g)
- (f · g)(x) = f(x) · g(x)       with domain Dom(f) ∩ Dom(g)
- (f / g)(x) = f(x) / g(x)       with domain Dom(f) ∩ Dom(g) minus {x | g(x) = 0}

Notes
- Domains intersect; quotient excludes zeros of g.
- If the context restricts inputs (e.g., time ≥ 0), incorporate those constraints.

---

## Method (General)
1) Determine Dom(f) and Dom(g) separately.
2) Compute the intersection Dom(f) ∩ Dom(g).
3) For quotient, additionally exclude points where g(x) = 0.
4) Form the new function rule and simplify if appropriate.
5) State the final domain in interval notation.

---

## Examples
1) Intersection-only restriction
- f(x) = √(x − 1)  → Dom(f) = [1, ∞)
- g(x) = x + 2      → Dom(g) = (−∞, ∞)
- (f + g)(x) = √(x − 1) + x + 2, Dom = [1, ∞)

2) Quotient with additional exclusion
- f(x) = x^2 − 1         → Dom(f) = (−∞, ∞)
- g(x) = x − 2           → Dom(g) = (−∞, ∞)
- (f / g)(x) = (x^2 − 1)/(x − 2), Dom = (−∞, ∞) \ {2}

3) Both functions restricted
- f(x) = 1/(x − 1)       → Dom(f) = (−∞, 1) ∪ (1, ∞)
- g(x) = √(x + 3)        → Dom(g) = [−3, ∞)
- (f · g)(x) = √(x + 3)/(x − 1)
- Dom = [−3, 1) ∪ (1, ∞) (intersection plus exclusion x ≠ 1)

---

## Common Misconceptions
- Using union instead of intersection for domains of sums/products.
- Forgetting to exclude g(x) = 0 in quotients.
- Cancelling factors in (f/g) and then claiming the cancelled point is allowed (it remains excluded from the domain).
- Assuming simplification changes the domain; it does not (state original domain).

---

## Connections
- Pairs naturally with [[Function_Composition]] (algebra vs chaining).
- Domain analysis relies on [[Domain_and_Range]] and [[Domain_Restrictions]].
- Graph behavior under arithmetic combines shapes and asymptotics.

---

## See Also
- [[Function_Notation]]
- [[Function_Composition]]
- [[Domain_and_Range]]
- [[Graphing_Functions]]