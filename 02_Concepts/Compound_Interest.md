---
layout: concept
title: "Compound Interest"
topic: "General Math"
type: Application
status: review
importance: high
tags:
  - concept/algebra
  - chapter-4
  - math/exponentials
  - method/finance
relations:
  broader:
    - - - Growth_and_Decay_Models
    - - - Real_World_Applications
  depends_on:
    - - - Exponential_Functions
    - - - Properties_of_Logarithms
    - - - Change_of_Base_Formula
  related:
    - - - Logarithmic_Equations
    - - - Exponential_Equations
    - - - Function_Notation
  defined_in:
    - - - Chapter4_Exponential_Logarithmic
review:
  next: 2025-11-25
updated: 2025-11-16
qa_certified: true
qa_date: 2025-11-16
qa_migration: v2.0
---

# Compound Interest

Definitions
- Future value with nominal annual rate r, compounding n times per year for t years on principal P:
  A = P(1 + r/n)^{nt}.
- Continuous compounding at rate r for t years:
  A = Pe^{rt}.
- Effective annual rate (EAR): (1 + r/n)^n − 1; continuous EAR: e^{r} − 1.

Methods
- Solve for future value A given P, r, n, t.
- Solve for time t to reach target A: A = P(1 + r/n)^{nt} ⇒ t = (1/(n ln(1 + r/n))) ln(A/P).
- Solve for rate r given A, P, n, t (use logs or numerical methods if needed).

Examples
- P = $1,000, r = 6% (0.06), n = 12, t = 5 ⇒ A = 1000(1 + 0.06/12)^{60}.
- Continuous compounding: P = $2,500, r = 4.5%, t = 3 ⇒ A = 2500 e^{0.045·3}.

Pitfalls
- Mixing nominal and effective rates.
- Using percent in place of decimal.
- Forgetting to convert time units to years when using nominal r.

See also
- Growth_and_Decay_Models, Exponential_Functions, Properties_of_Logarithms, Change_of_Base_Formula, Exponential_Equations, Logarithmic_Equations.
