---
layout: concept
title: "Doubling Time"
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
    - - - Half_Life
    - - - Properties_of_Logarithms
    - - - Change_of_Base_Formula
  defined_in:
    - - - Chapter4_Exponential_Logarithmic
review:
  next: 2025-11-25
updated: 2025-10-25
---

# Doubling Time

Definition
- The doubling time d of a growing quantity is the time needed for the amount to double.

Model
- y(t) = a·2^{t/d}.
- Equivalently y(t) = ae^{kt} with k = ln 2 / d.

Solving for d or t
- If y(t) = 2a, then d = t.
- Given two data points (t1,y1), (t2,y2): d = (t2 − t1) / log_2(y2/y1) = (t2 − t1) · ln 2 / ln(y2/y1).

Example
- Population doubles every 9 months: y = a·2^{t/9}. Time to triple: solve a·2^{t/9} = 3a ⇒ t = 9 log_2 3.

Pitfalls
- Confusing percentage growth per period r with doubling time d; d depends on r via d = ln 2 / ln(1+r).

See also
- Growth_and_Decay_Models, Exponential_Functions, Change_of_Base_Formula, Properties_of_Logarithms, Exponential_Equations.
