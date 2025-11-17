---
layout: concept
title: "Growth and Decay Models"
topic: "Exponential & Logarithmic"
type: Application
status: review
importance: high
tags:
  - concept/algebra
  - chapter-4
  - math/exponentials
  - method/modeling
relations:
  broader:
    - - - Real_World_Applications
    - - - Exponential_Functions
  depends_on:
    - - - Exponential_Functions
    - - - Logarithmic_Functions
    - - - Function_Notation
    - - - Domain_and_Range
  related:
    - - - Properties_of_Logarithms
    - - - Change_of_Base_Formula
    - - - Graphing_Functions
    - - - Average_Rate_of_Change
    - - - Continuity
  defined_in:
    - - - Chapter4_Exponential_Logarithmic
review:
  next: 2025-11-25
updated: 2025-11-16
qa_certified: true
qa_date: 2025-11-16
qa_migration: v2.0
---

# Growth and Decay Models

Definition
- An exponential model describes quantities that change by a constant percentage rate per unit time: y = a·b^t with base b > 0, b ≠ 1. Growth if b > 1; decay if 0 < b < 1.

Common model forms
- Discrete compounding (per period k): y(t) = a·(1 + r)^t where r is per-period rate.
- Continuous compounding: y(t) = a·e^{kt}, with k > 0 growth, k < 0 decay.
- Parameter meaning: a (initial value), r or k (relative rate), t (time), b = 1 + r (discrete) or b = e^k (continuous).

Method (model → predict)
1) Identify initial value a and growth/decay parameter (r or k) from context data.
2) Choose model: discrete y = a(1+r)^t or continuous y = ae^{kt}.
3) Plug t to predict y(t); respect units.

Method (data → fit model)
1) Compute ratios y_{t+1}/y_t to test exponential plausibility (approximate constant ratio).
2) Estimate b by average ratio; set r = b − 1, or estimate k = ln(b).
3) Use a from initial measurement (or solve via y(0)).
4) Validate by residual check or R^2 on log-linearized data (ln y vs t should be roughly linear).

Solving for time or rate
- Time to reach target Y: 
  a·b^t = Y ⇒ b^t = Y/a ⇒ t = log_b(Y/a) = ln(Y/a)/ln b.
- Continuous form: a·e^{kt} = Y ⇒ e^{kt} = Y/a ⇒ t = (1/k)·ln(Y/a).
- Find rate r from two data points (t1,y1), (t2,y2): b = (y2/y1)^{1/(t2−t1)}, r = b − 1.

Examples
- Bacterial culture doubles every 6 hours: y = a·2^{t/6}. Time to 10a: t = 6·log_2(10).
- Radioactive decay with half-life 12 years: y = a·(1/2)^{t/12}. Time to 10%: t = 12·log_{1/2}(0.1) = 12·ln(0.1)/ln(1/2).

Common pitfalls
- Mixing percent and decimal (e.g., using r = 5 instead of r = 0.05).
- Using linear model y = a + kt when ratio is constant (exponential) not difference.
- Dropping units or misinterpreting t’s unit (years vs months).

Checks
- Ratio test: y_{t+1}/y_t should be approximately constant for exponential data.
- For decay, ensure 0 < b < 1 or k < 0; for growth, b > 1 or k > 0.

See also
- Exponential_Functions, Logarithmic_Functions, Properties_of_Logarithms, Change_of_Base_Formula, Graphing_Functions, Average_Rate_of_Change, Continuity.
