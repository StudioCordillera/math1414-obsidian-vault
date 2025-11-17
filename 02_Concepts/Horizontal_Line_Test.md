---
type: concept
status: active
tags:
  - concept/functions
  - concept/properties
  - math/functions
  - math/analysis
  - chapter-4
created: 2025-10-25
updated: 2025-11-17
---

# Horizontal Line Test

Definition
A function f is one-to-one on a domain D if and only if every horizontal line y = c intersects the graph of f at most once for x ∈ D.

Procedure (how to use it)
- Step 1: Establish the intended domain D for f (state it!).
- Step 2: Sketch/plot f over D (parent + transformations, or sampled graph).
- Step 3: Conceptually sweep horizontal lines y = c across the range. If any y = c meets the graph in more than one point within D, f is not one-to-one on D.
- Step 4: If it fails globally but you need an inverse, choose an interval on which f is monotone, restrict to that interval, and re-apply the test.

Worked examples
- Linear: f(x) = 2x + 1 (D = ℝ). Any horizontal y = c hits exactly once → passes → one-to-one on ℝ.
- Quadratic: q(x) = x^2 (D = ℝ). y = 4 hits twice at x = −2 and x = 2 → fails. Restrict to D = [0, ∞) or (−∞, 0] to pass.
- Absolute value: g(x) = |x| (D = ℝ). y = 3 hits at x = −3 and x = 3 → fails. Restrict to x ≥ 0 (or x ≤ 0) to pass.
- Exponential: E(x) = 3^x (D = ℝ). Strictly increasing → passes.
- Logarithm: L(x) = ln x (D = (0, ∞)). Strictly increasing → passes.

Common misconceptions
- Confusing tests: Vertical Line Test checks whether a graph is a function; Horizontal Line Test checks whether a function is one-to-one.
- Ignoring domain: Declaring failure without noting that a domain restriction could make the function injective.
- Asymptotes: Misinterpreting asymptotic behavior as multiple intersections; HLT counts actual intersections only.

Connections (relational map)
- Depends on: [[Graphing_Functions]], [[Domain_and_Range]].
- Certifies: [[One_to_One_Function]].
- Used in: [[Inverse_Functions]] (to justify invertibility on a chosen domain).
- Chapter context: [[01_Course/Textbook/Chapter4_Exponential_Logarithmic|Chapter 4]] (Inverse/Exp/Log section 4.1).

Summary
Horizontal Line Test is the graphical criterion for injectivity on a stated domain. If it fails on ℝ for a non-monotone function (parabola, |x|), restrict the domain to a monotone interval to make an inverse function possible.
