---
layout: concept
title: Quadratic in Form
topic: Polynomials
type: Method
status: review
importance: high
tags:
- concept/algebra
- chapter-1
- math/equations
- method/solving
sources:
- miller-gerken
source_refs:
- Ch.1 §1.6 More Equations and Applications
relations:
  broader:
  - '[[Polynomial_Equations]]'
  narrower: []
  depends_on:
  - '[[Quadratic_Formula]]'
  - '[[Completing_the_Square]]'
  related:
  - '[[Solving_Higher_Degree_Equations]]'
  used_in:
  - '[[Polynomial_Equations]]'
review:
  next: 2025-11-25
updated: 2025-11-16
qa_certified: true
qa_date: 2025-11-16
qa_migration: v2.0
related:
- '[[Completing_the_Square]]'
- '[[Polynomial_Equations]]'
---
# Equations Quadratic in Form

Pattern: au^{2} + bu + c = 0 after substitution u = g(x). Common: u = x² for x⁴ terms; u = 1/x for rational; u = √x when both √x and x appear.

Procedure:
1) Identify repeated structure g(x) and set u = g(x)
2) Rewrite as quadratic in u
3) Solve for u (factor or quadratic formula)
4) Back-substitute to x and solve each case
5) Check solutions in original equation (domain issues, extraneous roots)

Example: x⁴ − 5x² + 4 = 0 → let u = x²: u² − 5u + 4 = 0 → u = 1 or 4 → x = ±1, ±2.

Errors to Avoid:
- Failing to revert substitution
- Missing all solution branches after back-substitution
- Ignoring domain restrictions introduced by substitution
