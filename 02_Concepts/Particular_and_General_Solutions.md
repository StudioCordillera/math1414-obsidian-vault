---
layout: concept
title: "Particular and General Solutions"
topic: "General Math"
title: Particular and General Solutions
type: Topic
status: in-progress
importance: medium
tags:
  - concept/algebra
  - chapter-5
  - math/systems
  - method/solving
relations:
  broader:
    - [[Linear_Systems]]
  depends_on:
    - [[Gaussian_Elimination]]
    - [[Row_Echelon_Form]]
  related:
    - [[Consistent_vs_Inconsistent_Systems]]
    - [[Homogeneous_Systems]]
    - [[System_Types]]
  used_in:
    - [[Gaussian_Elimination]]
review:
  next: 2025-11-25
updated: 2025-10-25
---
# Particular and General Solutions

Definition
- Particular solution: any single solution of the system.
- General solution: description of all solutions (unique, none, or infinite family parameterized by free variables).

Method (from RREF)
1) Identify pivot vs free variables.
2) If any contradictory row → no solution.
3) If pivots = variables → unique solution (particular solution is the unique solution).
4) If free variables exist → express basic variables in terms of parameters to give the general solution.

Examples
- Provide an RREF and derive general solution x = x_p + t v1 + s v2.

Pitfalls
- Mixing “particular solution” (one instance) with “general solution” (family).
- Forgetting parameter domain (real numbers unless otherwise stated).

See also
- [[Linear_Systems]] · [[Gaussian_Elimination]] · [[Row_Echelon_Form]] · [[Reduced_Row_Echelon_Form]] · [[Homogeneous_Systems]] · [[System_Types]]
