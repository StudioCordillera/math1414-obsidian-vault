---
layout: concept
title: Revenue and Profit Models
topic: General Math
type: Topic
status: review
importance: high
tags:
- applications
- quadratics
- optimization
- revenue
- profit
- modeling
sources:
- miller-gerken
source_refs:
- Ch.1 §1.5 Applications of Quadratics
relations:
  broader:
  - '[[Quadratic_Applications]]'
  narrower: []
  depends_on:
  - '[[Linear_Equations]]'
  - '[[Quadratic_Formula]]'
  - '[[Vertex_Form]]'
  - '[[Quadratic_Optimization]]'
  - '[[Translation_Patterns]]'
  related:
  - '[[Projectile_Motion_Model]]'
  - '[[Absolute_Value]]'
  used_in:
  - '[[Real_World_Applications]]'
review:
  next: 2025-10-27
  cadence: semester
updated: 2025-11-16
qa_certified: true
qa_date: 2025-11-16
qa_migration: v2.0
defines:
- '[[Literal_Equations]]'
---
# Revenue and Profit Models

Definition: Models where revenue R(x) and cost C(x) are functions of quantity x; profit P(x) = R(x) − C(x). In many entry-level scenarios, R(x) and/or P(x) are quadratic, enabling vertex-based optimization (max/min).

Key Forms:
- Price-demand: p(x) = a + bx (often decreasing with x)
- Revenue: R(x) = x · p(x)
- Profit: P(x) = R(x) − C(x)

Method (Maximize/Minimize Quadratic):
1) Write R(x) or P(x) in ax² + bx + c form
2) Vertex x* = −b/(2a)
3) Evaluate value at vertex to get R(x*) or P(x*)
4) Interpret in context; check domain constraints (x ≥ 0, integer if units)
5) Break-even: Solve R(x) = C(x) to find quantities where P(x) = 0; apply feasibility/integer constraints.

Example (Revenue): p = 100 − 0.5x → R(x) = 100x − 0.5x², max at x = 100, R_max = 5000.

Common Misconceptions:
- Forgetting that a < 0 gives a maximum; a > 0 gives a minimum
- Ignoring feasibility (negative x, non-integer units)
- Using −b/2a without confirming a ≠ 0 or quadratic form

Relations:
- Depends on: [[Linear_Equations]], [[Quadratic_Optimization]], [[Vertex_Form]]
- Related to: [[Projectile_Motion_Model]], [[Absolute_Value]]

Summary: Treat revenue/profit models as quadratic optimization with domain/context checks.
