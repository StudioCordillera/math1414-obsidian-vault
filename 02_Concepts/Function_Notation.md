---
layout: concept
title: "Function Notation"
topic: "Functions"
title: Function Notation
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
relations:
  broader:
    - "[[What_IS_a_Function]]"
  narrower: []
  depends_on:
    - "[[Order_of_Operations]]"
  defines: []
  related:
    - "[[Domain_and_Range]]"
    - "[[Function_Composition]]"
    - "[[Graphing_Functions]]"
  used_in:
    - "[[01_Course/Textbook/Chapter2_Functions_Relations]]"
review:
  cadence: semester
  next: 2026-01-10
created: 2025-10-20
updated: 2025-11-16
qa_certified: true
qa_date: 2025-11-16
qa_migration: v2.0
---

# Function Notation
How we name and evaluate functions

---

## Definition
Function notation uses a letter (often f, g, h) with parentheses to name a function and indicate its input: f(x). It is read “f of x.” The symbol f(x) denotes the output when the input is x; it does not mean f multiplied by x.

Formal
- A function is written as f: A → B with rule x ↦ f(x).
- We often represent the rule by an expression: f(x) = expression in x.

---

## Evaluation Methods
1) Direct substitution
- Replace x with the given value and simplify using order of operations
- Example: If f(x)=2x^2−3x+1, then f(−2)=2(4)+6+1=15

2) Symbolic evaluation
- Substitute an expression
- Example: f(x+h)=2(x+h)^2−3(x+h)+1 → expand and simplify

3) Function inputs that are not numbers
- Tables: if f(blue)=7, then f(blue) is 7
- Sets: f({1,2}) when f is defined on subsets; use the rule given

4) Composition context
- Evaluate inner first: (g∘f)(x)=g(f(x))

---

## Input Shifts vs Output Shifts
Common confusions
- f(x+2) shifts the INPUT left by 2 before applying f (graph shifts left)
- f(x)+2 shifts the OUTPUT up by 2 after applying f (graph shifts up)
- f(−x) reflects across y-axis
- −f(x) reflects across x-axis

---

## Examples
- If f(x)=x^2−4x, compute
  - f(3)=9−12=−3
  - f(a+1)=(a+1)^2−4(a+1)=a^2−2a−3
- Given g(x)=√(x−1), find g(5)=√4=2, g(x+1)=√x
- If h(x)=1/x, then h(2t)=1/(2t), and h(x)+h(−x)=1/x−1/x=0 (for x≠0)

---

## Common Misconceptions
- Interpreting f(x) as multiplication f·x
- Assuming f(x+h)=f(x)+f(h)
- Confusing notation for composition: f(g(x)) is not f(x)g(x)
- Dropping domain restrictions during evaluation (e.g., division by zero)

---

## Connections
- Notation underlies evaluation, composition, and transformations
- Domain/range statements use function notation precisely
- Inverse function notation uses f⁻¹, not 1/f

---

## See Also
- [[What_IS_a_Function]]
- [[Domain_and_Range]]
- [[Function_Composition]]
- [[Master_Transformation_Map]]
# See Also
- [[What_IS_a_Function]]
- [[Domain_and_Range]]
- [[Function_Composition]]
- [[Function_Operations]]
- [[Average_Rate_of_Change]]