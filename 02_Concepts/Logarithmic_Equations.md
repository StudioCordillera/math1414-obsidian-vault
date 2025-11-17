---
layout: concept
title: "Logarithmic Equations"
topic: "Exponential & Logarithmic"
title: Logarithmic Equations
type: Method
status: review
importance: high
updated: 2025-11-16
review.next: 2025-11-25
qa_certified: true
qa_date: 2025-11-16
qa_migration: v2.0
tags:
  - concept/algebra
  - chapter-4
  - math/logarithms
  - method/solving
relations:
  broader:
    - - - Logarithmic_Functions
  depends_on:
    - - - Properties_of_Logarithms
    - - - Change_of_Base_Formula
    - - - Function_Notation
    - - - Domain_and_Range
  related:
    - - - Exponential_Equations
    - - - Extraneous_Solutions
    - - - Radical_Equations
  defined_in:
    - - - Chapter4_Exponential_Logarithmic
see_also:
  - - - Logarithmic_Functions
  - - - Exponential_Equations
  - - - Extraneous_Solutions
---

Definition
- A logarithmic equation is one involving a logarithm of an expression with the unknown, e.g., log_b(f(x)) = c or log_b(f(x)) = log_b(g(x)), where b > 0, b ≠ 1.

Core methods
1) One-log form: isolate log_b(f(x)) = c
   - Rewrite as exponential form: f(x) = b^{c}. Solve for x.
2) Log equals log (same base): log_b(f(x)) = log_b(g(x))
   - Equate arguments with domain conditions: f(x) > 0 and g(x) > 0 ⇒ f(x) = g(x).
3) Use log properties to combine/simplify
   - Product/quotient/power rules to consolidate multiple logs to one.
4) Domain screening and extraneous checks
   - After solving, plug back into original to ensure every logged expression stays positive.

Worked examples
- One-log: log_3(2x − 5) = 2 ⇒ 2x − 5 = 3^2 = 9 ⇒ x = 7.
- Two-logs: ln(x + 1) = ln(5 − x) ⇒ x + 1 = 5 − x, with x + 1 > 0 and 5 − x > 0 ⇒ x = 2 (valid).
- Using properties: log(3x) − log(x − 2) = 1 ⇒ log(3x/(x − 2)) = 1 ⇒ 3x/(x − 2) = 10 ⇒ x = 20/7, check x > 2.

Common mistakes
- Ignoring domain: arguments to logs must be strictly positive.
- Dropping parentheses when applying power/product/quotient rules.
- Forgetting to check for extraneous solutions after exponentiating.

Checks and strategy
- Identify domain restrictions before algebraic manipulation.
- Prefer consolidating to a single logarithm when possible to reduce steps.
- If an equation mixes logs and exponentials, consider rewriting everything in exponential form or taking logs consistently.

See also
- [[Exponential_Equations]], [[Extraneous_Solutions]], [[Properties_of_Logarithms]]
