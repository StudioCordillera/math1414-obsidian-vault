---
layout: concept
title: Domain and Range
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
- Ch2 §2.3 Functions and Relations
- Ch2 §2.4 Linear Equations in Two Variables
relations:
  broader:
  - '[[What_IS_a_Function]]'
  narrower: []
  depends_on:
  - '[[Interval_Notation]]'
  - '[[Domain_Restrictions]]'
  defines: []
  related:
  - '[[Function_Notation]]'
  - '[[Piecewise_Functions]]'
  - '[[Graphing_Functions]]'
  used_in:
  - '[[01_Course/Textbook/Chapter2_Functions_Relations]]'
review:
  cadence: semester
  next: 2026-01-10
created: 2025-10-20
updated: 2025-11-16
qa_certified: true
qa_date: 2025-11-16
qa_migration: v2.0
related:
- '[[Average_Rate_of_Change]]'
- '[[Function_Transformations]]'
- '[[Graphing_Quadratic_Functions]]'
- '[[Rectangular_Coordinate_System]]'
- '[[Vertex_Form]]'
narrower:
- '[[Domain_Restrictions]]'
used_in:
- '[[Interval_Notation]]'
---
# Domain and Range
Understanding what inputs are allowed and what outputs occur

---

## Definition
- Domain: The set of all inputs x for which f(x) is defined (in the specified number system, typically ℝ).
- Range: The set of all actual output values y attained by the function (a subset of the codomain).
- Codomain: The declared target set of the function; the range is contained within the codomain.

Notes
- Changing the domain changes the function. “Restricting the domain” creates a new function.
- Range depends on both the rule and the domain.

Formal
- For f: A → B, Dom(f) = A; Range(f) = { f(x) | x ∈ A } ⊆ B.

---

## Methods: Finding the Domain (Real-valued functions)
Use the natural-domain principle: include all real x for which the rule makes sense; exclude where it does not. Then apply function-specific constraints.

1) Polynomial functions
- Domain: (−∞, ∞)
- Rationale: Polynomials are defined for every real x.

2) Rational functions P(x)/Q(x)
- Exclude: Zeros of Q(x)
- Method: Factor Q(x), solve Q(x) = 0, exclude those points
- Express domain in interval notation

3) Radical functions √[n]{g(x)}
- Even index n: require g(x) ≥ 0 (in ℝ)
- Odd index n: domain inherits from g(x) (no additional restriction)

4) Logarithmic functions log_a(g(x))
- Require g(x) > 0

5) Exponential functions a^{g(x)} (a>0)
- Domain usually all real numbers; watch for embedded restrictions in g

6) Composition h(x) = f(g(x))
- Domain: all x such that x ∈ Dom(g) AND g(x) ∈ Dom(f)

7) Piecewise functions
- Union of subdomains specified by the cases, ensuring consistency at boundaries if required

Special constraints
- Physical modeling: inputs limited by context (time ≥ 0, lengths ≥ 0, etc.)

---

## Methods: Finding the Range
Principles
- Graph-based: Project the graph’s y-values (vertical extent) onto the y-axis
- Algebra-based: Solve y = f(x) for x in terms of y and impose domain conditions
- Behavior-based: Use monotonicity, symmetry, and end behavior

Common strategies
1) Vertex method (quadratics):
- y = ax^2 + bx + c with a ≠ 0
- Vertex (h,k) → If a>0: Range [k, ∞); if a<0: (−∞, k]

2) Inverse relation method:
- Try to solve y = f(x) for x; enforce domain constraints so y-values are attainable

3) Monotonicity:
- If f is strictly increasing on its domain, Range = (inf f, sup f)

4) Asymptotics:
- Horizontal asymptote y = L suggests L is a limiting value (often excluded unless attained)

5) Radicals and squares:
- √g(x) ≥ 0 ⇒ Range is [0, ∞) possibly shifted/scaled
- Squares f(x)=h(x)^2 ⇒ Range is [0, ∞) possibly shifted

---

## Examples
1) f(x) = 2x + 3
- Domain: (−∞, ∞) (linear)
- Range: (−∞, ∞) (surjective onto ℝ)

2) g(x) = 1/(x−2)
- Domain: (−∞, 2) ∪ (2, ∞)
- Range: (−∞, 0) ∪ (0, ∞) (y ≠ 0)
- Reason: No x makes g(x)=0; horizontal asymptote y=0 not attained

3) h(x) = √(x−4)
- Domain: [4, ∞)
- Range: [0, ∞)

4) q(x) = x^2 − 6x + 5 = (x−3)^2 − 4
- Vertex: (3, −4), a = 1 > 0
- Domain: (−∞, ∞)
- Range: [−4, ∞)

5) p(x) = (x−1)/(x^2 + 1)
- Domain: (−∞, ∞) (denominator never 0)
- Range: (−1/2, 1) (compute via calculus or algebraic bounding; sketch reasoning)

---

## Common Misconceptions
- Confusing codomain with range: declaring ℝ as output set does not imply surjectivity.
- Assuming every horizontal asymptote value is attained: often the limit is excluded from the range.
- Forgetting domain restrictions induced by composition: inner function outputs must lie in the outer’s domain.
- Treating a restricted-domain function as equivalent to the unrestricted version.

---

## Applications and Connections
- Solution sets of inequalities correspond to domains of validity for expressions.
- Inverse functions: y in the range of f corresponds to domain of f^{-1}.
- Modeling: Domain and range encode physical constraints.

---

## Summary
- Domain: all allowed x; Range: all produced y.
- Determine domain by excluding where expressions are undefined and honoring modeling constraints.
- Determine range via graph, algebraic inversion, monotonicity, and asymptotics.
- Precise domain/range statements use interval notation.

---

## See Also
- [[What_IS_a_Function]]
- [[Function_Notation]]
- [[Interval_Notation]]
- [[Domain_Restrictions]]
- [[Function_Composition]]
- [[Piecewise_Functions]]
- [[Continuity]]
- [[Graphing_Functions]]