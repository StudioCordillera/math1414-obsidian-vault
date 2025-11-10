---
layout: concept
title: "Linear Systems"
topic: "Systems & Matrices"
type: Topic
status: in-progress
importance: high
tags:
  - concept/algebra
  - chapter-5
  - math/systems
  - method/solving
relations:
  broader: []
  narrower: []
  depends_on:
    - - - Linear_Equations
    - - - Literal_Equations
  related:
    - - - Gaussian_Elimination
    - - - Row_Operations
    - - - Augmented_Matrix
    - - - Matrix_Multiplication
    - - - Cramers_Rule
  used_in:
    - - - Systems_Applications
review:
  next: 2025-11-25
created: 2025-10-25
updated: 2025-10-25
relations.broader: |-
  - [[What_IS_a_Function]]
  - [[System_Types]]
relations.depends_on: |-
  - [[Linear_Equations]]
  - [[Literal_Equations]]
  - [[Row_Operations]]
  - [[Augmented_Matrix]]
relations.related: |-
  - [[Gaussian_Elimination]]
  - [[Reduced_Row_Echelon_Form]]
  - [[Row_Echelon_Form]]
  - [[Equivalent_Systems]]
  - [[Consistent_vs_Inconsistent_Systems]]
  - [[System_Types]]
---

# Linear Systems

Definition
- A linear system is a set of two or more linear equations in the same variables. A solution is an assignment of values to the variables that satisfies every equation in the system simultaneously.

Solution sets and consistency
- Exactly one solution (independent, consistent)
- Infinitely many solutions (dependent, consistent)
- No solution (inconsistent)

Methods (overview)
- Graphing (intersection interpretation)
- Substitution and elimination (algebraic)
- Matrix methods (augmented matrix + row operations → row-echelon form; inverse matrix method; Cramer’s Rule when determinant ≠ 0)

Examples (sketch)
- 2×2 system: solve by elimination and by augmented-matrix row reduction
- 3×3 system: outline Gaussian elimination steps

Common misconceptions
- Treating a system as separate unrelated equations (forgetting simultaneous satisfaction)
- Row operations that change the solution set (illegal operations)
- Using inverse method when matrix is non-invertible (determinant = 0)

See also
- [[Row_Operations]], [[Augmented_Matrix]], [[Gaussian_Elimination]], [[Matrix_Multiplication]], [[Inverse_Matrix]], [[Cramers_Rule]]
