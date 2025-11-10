---
layout: concept
title: "Logistic Growth"
topic: "Exponential & Logarithmic"
type: Topic
status: in-progress
importance: medium
tags:
  - concept/modeling
  - chapter-4
  - math/exponential
  - modeling/logistic
relations:
  broader:
    - [[Growth_and_Decay_Models]]
  depends_on:
    - [[Exponential_Functions]]
    - [[Logarithmic_Functions]]
  related:
    - [[Doubling_Time]]
    - [[Half_Life]]
  used_in: []
created: 2025-10-30
updated: 2025-10-30
---

# Logistic Growth

Definition
- Logistic growth models populations or quantities with limiting capacity: P(t) = L / (1 + A e^{-kt}), where L is carrying capacity, k>0 growth rate, and A depends on initial condition P(0)=P_0 via A=(L-P_0)/P_0.

Key facts
- Inflection at P=L/2; early behavior approximates exponential; later behavior saturates near L.

Methods
- Parameter fitting: Given L, P_0, and P(t_1), solve for k using algebra and logarithms.

Common pitfalls
- Treating logistic as pure exponential indefinitely; mis-solving for k due to algebraic errors.

See also: [[Growth_and_Decay_Models]], [[Exponential_Functions]]
