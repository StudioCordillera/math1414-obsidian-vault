---
layout: concept
title: "Exponential Equations"
topic: "Exponential & Logarithmic"
title: Exponential Equations
type: Method
status: review
importance: high
updated: 2025-10-25
review.next: 2025-11-25
tags:
  - concept/algebra
  - chapter-4
  - math/exponentials
  - method/solving
relations:
  broader:
    - - - Exponential_Functions
  depends_on:
    - - - Exponent_Properties
    - - - Function_Notation
    - - - Domain_and_Range
    - - - Logarithmic_Functions
  related:
    - - - Properties_of_Logarithms
    - - - Change_of_Base_Formula
    - - - Logarithmic_Equations
  defined_in:
    - - - Chapter4_Exponential_Logarithmic
see_also:
  - - - Exponential_Functions
  - - - Logarithmic_Functions
  - - - Properties_of_Logarithms
  - - - Change_of_Base_Formula
updated: 2025-11-16
qa_certified: true
qa_date: 2025-11-16
qa_migration: v2.0
---

Definition
- An exponential equation is one in which the unknown appears in the exponent, e.g., b^{f(x)} = c or a·b^{kx} = c with b > 0, b ≠ 1.

Core methods
1) Equal bases → equate exponents
   - If b^{f(x)} = b^{g(x)} with b > 0, b ≠ 1, then f(x) = g(x).
2) Take logarithms (any base > 0, ≠ 1)
   - Apply log to both sides. Use log rules to isolate x (product/quotient/power rules).
   - Choose natural log or log base b conveniently; consistency matters more than base.
3) Linearize via ln for e^kx forms
   - If y = Ae^{kx}, then ln y = ln A + kx (a line in x).
4) Numerical solve when algebra fails
   - Use graphing or iterative methods when no algebraic isolation is possible.

Worked examples
- Equal bases: 3^{2x+1} = 3^{7} ⇒ 2x + 1 = 7 ⇒ x = 3.
- Log method: 5^{x} = 17 ⇒ x = log_5 17 = ln 17 / ln 5.
- Mixed constants: 7·2^{3x} = 40 ⇒ 2^{3x} = 40/7 ⇒ 3x ln 2 = ln(40/7) ⇒ x = ln(40/7)/(3 ln 2).

Common mistakes
- Dropping the base restriction b > 0, b ≠ 1.
- Taking logs but forgetting to apply the power rule to move the exponent down.
- Mixing bases mid-solution causing arithmetic slips.
- Ignoring domain restrictions from earlier steps (e.g., dividing by an expression that could be zero).

Checks and strategy
- Confirm domain: if you later take logs, ensure both sides are positive.
- If bases can be matched cleanly, avoid logs for a quicker path.
- After solving, verify solutions in the original equation (especially if transformations changed domains).

See also
- [[Logarithmic_Equations]], [[Properties_of_Logarithms]], [[Change_of_Base_Formula]], [[Exponential_Functions]]
