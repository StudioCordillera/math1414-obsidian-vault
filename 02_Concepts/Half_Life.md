---
layout: concept
title: "Half Life"
topic: "General Math"
type: Application
status: review
importance: medium
tags:
  - concept/algebra
  - chapter-4
  - math/exponentials
  - method/modeling
relations:
  broader:
    - - - Growth_and_Decay_Models
  depends_on:
    - - - Exponential_Functions
    - - - Logarithmic_Functions
  related:
    - - - Doubling_Time
    - - - Change_of_Base_Formula
    - - - Properties_of_Logarithms
  defined_in:
    - - - Chapter4_Exponential_Logarithmic
review:
  next: 2025-11-25
updated: 2025-10-25
---

# Half-Life

Definition
- The half-life h of a decaying quantity is the time for the amount to reduce to half its initial value.

Model
- y(t) = a(1/2)^{t/h}.
- Equivalently y(t) = ae^{kt} with k = ln(1/2)/h.

Solving for h or t
- Given y(t) = a/2 at t = h ⇒ h = t when y(t) = a/2.
- Given two data points, h = (t2 − t1) / log_{1/2}(y2/y1) = (t2 − t1) · ln(y2/y1) / ln(1/2).

Example
- A sample has half-life 12 years: y(t) = a(1/2)^{t/12}. Time to reach 10%: t = 12·log_{1/2}(0.1).

Pitfalls
- Using linear decay a − kt for processes that are exponential.
- Confusing base-10 log with natural log when solving for t.

See also
- Growth_and_Decay_Models, Exponential_Functions, Change_of_Base_Formula, Properties_of_Logarithms, Logarithmic_Equations.
