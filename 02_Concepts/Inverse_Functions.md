---
type: Topic
status: review
importance: high
tags:
  - concept/algebra
  - chapter-4
  - math/functions
  - method/algebraic
created: 2025-10-25
updated: 2025-11-05
review:
  next: 2025-12-05
  cadence: monthly
relations:
  broader:
    - [[What_IS_a_Function]]
  depends_on:
    - [[Function_Notation]]
    - [[One_to_One_Function]]
    - [[Domain_and_Range]]
  related:
    - [[Function_Composition]]
    - [[Exponential_Functions]]
    - [[Logarithmic_Functions]]
    - [[Horizontal_Line_Test]]
  used_in:
    - [[Exponential_Equations]]
    - [[Logarithmic_Equations]]
  defined_in:
    - [[01_Course/Textbook/Chapter4_Exponential_Logarithmic]]
sources:
  - Textbook/Algebra_by_section
source_refs:
  - [[00_Books/Algebra_by_section/pages/p440]]–[[00_Books/Algebra_by_section/pages/p448]]
---

# Inverse Functions

Definition
Two functions f and g are inverses if f(g(x)) = x on g’s domain and g(f(x)) = x on f’s domain. The graph of g is the reflection of the graph of f across y = x.

Method: Find f^{-1}(x)
- Verify f is one-to-one (horizontal line test or monotonicity). If not, restrict domain.
- Replace f(x) with y.
- Swap x and y, then solve for y.
- Rename y as f^{-1}(x).
- State the domain and range of f^{-1} explicitly.

Examples
- f(x) = 3x − 7 → f^{-1}(x) = (x + 7)/3
- f(x) = x^2, x ≥ 0 → f^{-1}(x) = √x

Common Misconceptions
- Assuming every function has an inverse without domain restriction.
- Treating (f(x))^{-1} as 1/f(x) instead of f^{-1}(x).

See Also
- [[Horizontal_Line_Test]], [[Function_Composition]], [[Domain_and_Range]], [[One_to_One_Function]], [[Algebraic_Test_for_One_to_One]]
