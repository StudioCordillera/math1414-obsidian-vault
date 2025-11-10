---
type: Definition
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
  narrower: []
  depends_on:
    - [[Exponential_Functions]]
    - [[Inverse_Functions]]
    - [[Function_Notation]]
  related:
    - [[Change_of_Base_Formula]]
    - [[Logarithmic_Equations]]
    - [[Exponential_Equations]]
  used_in:
    - [[Logarithmic_Equations]]
    - [[Exponential_Equations]]
  defined_in:
    - [[01_Course/Textbook/Chapter4_Exponential_Logarithmic]]
sources:
  - Textbook/Algebra_by_section
source_refs:
  - [[00_Books/Algebra_by_section/pages/p446]]
---

# Properties of Logarithms — Full Spec

Definition (b>0, b≠1; x, y>0)
- Product: log_b(xy) = log_b(x) + log_b(y)
- Quotient: log_b(x/y) = log_b(x) − log_b(y)
- Power: log_b(x^r) = r·log_b(x)
- Change of base (preview): log_b(x) = log_k(x) / log_k(b) for any k>0, k≠1

Why they hold (sketch)
- From inverse property b^{log_b(x)} = x and exponential laws: apply log_b to both sides of b^{m+n} = b^m·b^n, etc.

Procedures
- Expand: Repeatedly apply product/quotient/power with domain checks (arguments > 0).
- Condense: Factor numeric coefficients into powers, combine sums/differences into single log, ensure one log at the end.
- Solve (structure-first): Combine to single log if possible → convert to exponential → solve algebraically → domain check (arguments > 0).

Worked examples
1) Expand log_3(27x^2/√y)
   = log_3 27 + 2log_3 x − (1/2)log_3 y = 3 + 2log_3 x − (1/2)log_3 y.
2) Condense 2ln(x) − ln(x+1)
   = ln(x^2) − ln(x+1) = ln(x^2/(x+1)), domain x>0 and x+1>0 ⇒ x>0.
3) Solve log_5(x) + log_5(x−4) = 2 → log_5(x(x−4)) = 2 → x(x−4) = 25 → x^2 − 4x − 25 = 0 → x = 2 ± √29; domain x>4 ⇒ x = 2 + √29.

Common misconceptions/errors
- Structure error: Using a false rule for sums: log_b(x ± y) ≠ log_b x ± log_b y.
- Domain omission: Forgetting that all log arguments must be positive.
- Coefficient confusion: Misreading r·log_b x as log_b(x^r) only valid when converting, not when r depends on x.
- Base blindness: Mixing bases within the same manipulation without converting (use change of base if needed).

Connections (relational map)
- Depends on: [[Exponential_Functions]] (laws), [[Inverse_Functions]].
- Used in: [[Exponential_Equations]], [[Logarithmic_Equations]].
- Related: [[Change_of_Base_Formula]].

Summary
The properties transform products, quotients, and powers inside logs into sums, differences, and multiples outside, enabling simplification and equation solving—always under the constraint that arguments remain positive.
