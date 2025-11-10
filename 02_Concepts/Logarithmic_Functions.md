---
type: Topic
status: review
importance: high
tags:
  - concept/algebra
  - chapter-4
  - math/logarithms
  - method/analyzing
relations:
  broader:
    - "[[Functions_Relations_Graphs]]"
  depends_on:
    - "[[Inverse_Functions]]"
    - "[[One_to_One_Function]]"
    - "[[Exponential_Functions]]"
    - "[[Function_Notation]]"
    - "[[Domain_and_Range]]"
  related:
    - "[[Properties_of_Logarithms]]"
    - "[[Change_of_Base_Formula]]"
    - "[[Graphing_Functions]]"
    - "[[Continuity]]"
  defined_in:
    - "[[Chapter4_Exponential_Logarithmic]]"
review:
  next: 2025-11-25
updated: 2025-10-25
---

Definition
- A logarithmic function with base b>0, b≠1 is f(x) = log_b(x), the inverse of the exponential function g(x) = b^x. It satisfies b^{log_b(x)} = x for x>0 and log_b(b^x) = x for all real x.

Key facts
- Domain: (0, ∞). Range: (−∞, ∞). Base constraint: b>0, b≠1.
- Inverse relationship: f and g are reflections across y = x.
- Equivalent forms: y = log_b(x) ⇔ b^y = x.
- Common bases: log (base 10), ln (base e≈2.71828).

Graph features
- Vertical asymptote x = 0.
- Increasing if b>1; decreasing if 0<b<1.
- Passes through (1, 0) and (b, 1).

Methods and skills
- Rewrite between logarithmic and exponential forms to solve for variables.
- Apply properties of logarithms to expand/condense expressions.
- Determine domain constraints from arguments of logarithms.

Examples
- Solve log_3(x) = 2 ⇒ x = 3^2 = 9.
- Solve log(x−1) + log(x+1) = 1 ⇒ log((x−1)(x+1)) = 1 ⇒ (x−1)(x+1) = 10 ⇒ x^2−1=10 ⇒ x^2=11 ⇒ x=±√11; domain requires x>1 ⇒ x=√11.

Common misconceptions
- Treating log_b(x+y) as log_b(x)+log_b(y) (false). Only products/quotients/powers distribute via log rules.
- Forgetting the domain x>0 for log arguments.
- Assuming log bases can be negative or 1.

See also
- [[Exponential_Functions]]
- [[Properties_of_Logarithms]]
- [[Change_of_Base_Formula]]
- [[Inverse_Functions]]
# Methods and skills

Injectivity & Inverses (explicit)
- Certification: log_b(x) is strictly monotone on (0,∞) for b>0, b≠1 → injective; passes [[Horizontal_Line_Test]] on its domain.
- Consequence: Safe to apply exponential both sides when solving: if log_b(u)=log_b(v) with u,v>0, then u=v.
- Inverse domain/range: dom log_b = (0,∞), range ℝ; inverse is b^x with dom ℝ, range (0,∞).
- See: [[One_to_One_Function]], [[Inverse_Functions]].
# # Logarithmic Functions

Injectivity & Inverses (Chapter 4 integration)
- For b>0, b≠1, g(x)=\log_b x is strictly monotone on (0,∞), hence one-to-one.
- Inverse function is b^x: g^{-1}(x)=b^x with domain ℝ and range (0,∞).
- Solving: If \log_b(f(x))=\log_b(g(x)) with both sides defined (f(x),g(x)>0), then f(x)=g(x) (by injectivity). Applying b^{(\cdot)} to both sides is justified by monotonicity.
- See also: [[One_to_One_Function]], [[Inverse_Functions]], [[Exponential_Functions]].