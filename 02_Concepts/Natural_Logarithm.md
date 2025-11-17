---
layout: concept
title: "Natural Logarithm"
topic: "Exponential & Logarithmic"
type: Definition
status: in-progress
importance: high
tags:
  - concept/algebra
  - chapter-4
  - math/logarithms
  - definition
relations:
  broader:
    - [[Logarithmic_Functions]]
  depends_on:
    - [[Exponential_Functions]]
    - [[Inverse_Functions]]
    - [[e (constant)]]
    - [[Domain_and_Range]]
  related:
    - [[Change_of_Base_Formula]]
    - [[Properties_of_Logarithms]]
    - [[Common_Logarithm]]
  used_in:
    - [[Logarithmic_Equations]]
    - [[Exponential_Equations]]
    - [[Growth_and_Decay_Models]]
    - [[Compound_Interest]]
created: 2025-10-30
updated: 2025-11-16
qa_certified: true
qa_date: 2025-11-16
qa_migration: v2.0
---

# Natural Logarithm (ln)

Definition
- The natural logarithm ln(x) = log_e(x) is the inverse of the natural exponential e^x. It satisfies:
  - e^{ln x} = x for x > 0
  - ln(e^x) = x for all real x

Core facts
- Domain: (0, ∞); Range: (−∞, ∞)
- Base: e ≈ 2.71828
- Identities: ln(1) = 0, ln(e) = 1
- Change of base: ln_b(x) = ln x / ln b; in particular, log_b(x) = ln x / ln b

Uses
- Solving exponential equations (bring down exponents)
- Modeling continuous growth/decay and finance (A = Pe^{rt})

Common pitfalls
- Attempting ln of nonpositive numbers; mixing ln and log without change-of-base.

See also: [[Exponential_Functions]], [[Change_of_Base_Formula]], [[Properties_of_Logarithms]], [[Common_Logarithm]]
