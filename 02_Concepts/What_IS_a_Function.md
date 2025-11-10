---
layout: concept
title: "What IS a Function"
topic: "Functions"
title: What IS a Function?
type: Definition
status: review
importance: critical
tags:
  - node/definition
  - domain/functions
  - chapter2
sources:
  - MillerGerken_AlgTrig2e
  - LawvereSchanuel_ConceptualMathematics
source_refs:
  - Ch2 §2.3 Functions and Relations
  - Lawvere & Schanuel Article I p.16
relations:
  broader:
    - "[[Functions_Relations_Graphs]]"
  narrower: []
  depends_on:
    - "[[Equality_Properties]]"
    - "[[Order_of_Operations]]"
  defines: []
  related:
    - "[[Function_Composition]]"
    - "[[Master_Transformation_Map]]"
    - "[[Interval_Notation]]"
    - "[[Domain_Restrictions]]"
  used_in:
    - "[[01_Course/Textbook/Chapter2_Functions_Relations]]"
review:
  cadence: semester
  next: 2026-01-10
created: 2025-10-20
updated: 2025-10-21
---

# What IS a Function?
A function is a rule that assigns to each input in a specified set (the domain) exactly one output in a target set (the codomain).

---

## Core Idea
- Same input → same output (deterministic, single-valued)
- Defined for every allowed input in the domain (total)
- Written as f: A → B, x ↦ f(x)

Machine picture: INPUT (domain) → [rule] → OUTPUT (codomain)

---

## Formal Definition
A function f from set A to set B is a relation with the uniqueness property:

For every x ∈ A, there exists exactly one y ∈ B such that y = f(x).

Notation: f: A → B. Domain Dom(f) = A. Range(f) = { f(x) | x ∈ A } ⊆ B (codomain).

---

## Representations
- Formula: f(x) = 2x + 1
- Table: list ordered pairs (x, f(x))
- Arrow (mapping) diagram: arrows from domain elements to codomain
- Graph: set of points (x, y) with y = f(x); vertical line test checks “function-ness”

---

## Structure and Operations
- Composition: If f: A → B and g: B → C then (g ∘ f)(x) = g(f(x)); associative
- Identity: id_A(x) = x; f ∘ id_A = f = id_B ∘ f
- Inverse (when it exists): f⁻¹ ∘ f = id_A and f ∘ f⁻¹ = id_B (requires bijection)

---

## Key Properties (by output coverage)
- Injective (one-to-one): f(a) = f(b) ⇒ a = b (horizontal line test passes)
- Surjective (onto): every b ∈ B is hit by some a ∈ A
- Bijective: both injective and surjective; has an inverse f⁻¹

---

## Domain • Range • Codomain
- Domain: allowed inputs (part of a function’s specification)
- Codomain: declared target set
- Range: actual outputs produced; always a subset of the codomain

Notes
- Changing the domain creates a different function (restricted-domain versions are new functions)
- Composition domain rule: need x ∈ Dom(g) and g(x) ∈ Dom(f)

---

## Examples
1) Linear: f: ℝ → ℝ, f(x) = 2x − 3
   - Domain: ℝ; Range: ℝ
2) Radical: g(x) = √(x − 4) over ℝ
   - Domain: [4, ∞); Range: [0, ∞)
3) Rational: h(x) = 1/(x − 2)
   - Domain: ℝ \ {2}; Range: ℝ \ {0}

---

## Common Misconceptions
- Confusing f with f(x): f is the function, f(x) is the output at x
- Thinking every equation defines y as a function of x (e.g., x² + y² = 1 fails vertical line test)
- Assuming f(x + 2) = f(x) + 2 (input shift ≠ output shift)
- Ignoring domain restrictions during evaluation (division by zero, even roots of negatives in ℝ)

---

## See Also
- [[Domain_and_Range]]
- [[Function_Notation]]
- [[Function_Composition]]
- [[Piecewise_Functions]]
- [[Average_Rate_of_Change]]
- [[Graphing_Functions]]
# See Also
- [[Domain_and_Range]]
- [[Function_Notation]]
- [[Functions_Relations_Graphs]]
- [[Linear_Functions]]
- [[Piecewise_Functions]]
- [[Graphing_Functions]]