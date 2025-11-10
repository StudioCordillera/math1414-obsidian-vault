---
type: Method
status: review
importance: high
tags:
  - concept/algebra
  - chapter-4
  - math/logarithms
  - method/skills
created: 2025-10-25
updated: 2025-11-05
review:
  next: 2025-12-05
  cadence: monthly
relations:
  broader:
    - [[Logarithmic_Functions]]
    - [[Properties_of_Logarithms]]
  narrower: []
  depends_on:
    - [[Inverse_Functions]]
    - [[Exponential_Functions]]
  related:
    - [[Logarithmic_Equations]]
    - [[Exponential_Equations]]
  used_in:
    - [[Properties_of_Logarithms]]
  defined_in:
    - [[01_Course/Textbook/Chapter4_Exponential_Logarithmic]]
sources:
  - Textbook/Algebra_by_section
source_refs:
  - [[00_Books/Algebra_by_section/pages/p452]]
---

# Change of Base Formula

Definition/Statement
For bases b, k > 0 with b ≠ 1, k ≠ 1 and x > 0:
log_b(x) = log_k(x) / log_k(b)

Why it works (derivation)
Let y = log_b(x). Then b^y = x. Taking log base k of both sides:
log_k(b^y) = log_k(x) ⇒ y·log_k(b) = log_k(x) ⇒ y = log_k(x)/log_k(b).
This follows from the power property of logs and invertibility of exponential/log functions on their domains.

Procedures (how to use it)
1) Calculator evaluation (no direct base available)
   - Choose k = 10 (log) or k = e (ln) supported by your calculator.
   - Compute log_k(x) and log_k(b), then divide.
   - Domain check: x > 0 and b > 0, b ≠ 1.
2) Base conversion in algebraic work
   - To compare or combine logs with different bases, convert all to the same base using change of base, then apply properties.
3) Solving equations with an unusual base
   - Convert log_b expressions into ln or log to apply standard manipulations or to isolate variables numerically.

Worked examples
- Evaluate log_2(10): log_2(10) = ln(10)/ln(2) ≈ 2.302585093/0.693147181 ≈ 3.32193.
- Evaluate log_7(3): log_7(3) = log(3)/log(7) ≈ 0.4771/0.8451 ≈ 0.5646.
- Compare bases: Which is larger, log_3(5) or log_5(3)?
  Convert both to base e: ln(5)/ln(3) ≈ 1.609/1.099 ≈ 1.464 > ln(3)/ln(5) ≈ 0.683, so log_3(5) > log_5(3).

Applications
- Calculator computations when only ln/log are available.
- Standardizing base across an expression to apply [[Properties_of_Logarithms]].
- Numerical solution strategies in [[Logarithmic_Equations]] and [[Exponential_Equations]].

Common misconceptions and errors
- Treating base change as optional for domain: It doesn’t change the domain requirement x > 0.
- Forgetting that the denominator log_k(b) is a constant (with respect to x) once b and k are fixed.
- Mixing bases mid-problem without converting, leading to invalid combinations of terms.

Connections (relational map)
- Depends on: [[Exponential_Functions]], [[Inverse_Functions]]
- Related: [[Properties_of_Logarithms]], [[Logarithmic_Equations]], [[Exponential_Equations]]
- Used in: Evaluating logs on calculators; simplifying mixed-base expressions.

Summary
Change of base rewrites log_b(x) in any convenient base (usually e or 10): log_b(x) = ln(x)/ln(b) or log(x)/log(b). It enables calculator evaluation and unifies bases for algebraic manipulation while preserving domain conditions (x > 0).
