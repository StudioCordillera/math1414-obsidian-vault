---
type: concept
status: active
tags:
  - concept/linear_systems
  - math/algebra
  - math/matrices
  - chapter-5
created: 2025-10-25
updated: 2025-11-16
---

# Augmented Matrix

## Definition

An **augmented matrix** is a matrix representation of a system of linear equations, formed by appending the constants column to the coefficient matrix, separated by a vertical bar. This compact notation enables systematic solution methods through row operations while preserving the relationship between coefficients and constants.

## Mathematical Expression

For a general system of $m$ equations in $n$ variables:
$$
\begin{cases}
a_{11}x_1 + a_{12}x_2 + \cdots + a_{1n}x_n = b_1 \\
a_{21}x_1 + a_{22}x_2 + \cdots + a_{2n}x_n = b_2 \\
\vdots \\
a_{m1}x_1 + a_{m2}x_2 + \cdots + a_{mn}x_n = b_m
\end{cases}
$$

The augmented matrix is written as:
$$
\left[\begin{array}{cccc|c}
a_{11} & a_{12} & \cdots & a_{1n} & b_1 \\
a_{21} & a_{22} & \cdots & a_{2n} & b_2 \\
\vdots & \vdots & \ddots & \vdots & \vdots \\
a_{m1} & a_{m2} & \cdots & a_{mn} & b_m
\end{array}\right]
$$

## Example

Convert the system to augmented matrix form and apply one row operation:

**Original System:**
$$
\begin{cases}
2x - 3y + z = 5 \\
x + 4y - 2z = -1 \\
3x + y + z = 7
\end{cases}
$$

**Augmented Matrix:**
$$
\left[\begin{array}{ccc|c}
2 & -3 & 1 & 5 \\
1 & 4 & -2 & -1 \\
3 & 1 & 1 & 7
\end{array}\right]
$$

**After swapping Row 1 and Row 2:**
$$
\left[\begin{array}{ccc|c}
1 & 4 & -2 & -1 \\
2 & -3 & 1 & 5 \\
3 & 1 & 1 & 7
\end{array}\right]
$$

This corresponds to reordering the equations—a valid transformation that produces an equivalent system.

## Key Properties

- **Row-equivalence**: Two augmented matrices are row-equivalent if one can be obtained from the other through elementary row operations
- **Equivalent systems**: Row-equivalent augmented matrices represent systems with identical solution sets
- **Compact notation**: Each row encodes one equation; the vertical bar distinguishes coefficients from constants

## Relations

- `[[Elementary_Row_Operations]]` - three operations that transform augmented matrices while preserving solutions
- `[[Row_Echelon_Form]]` - intermediate form achieved through row operations on augmented matrices
- `[[Reduced_Row_Echelon_Form]]` - unique simplified form revealing the solution structure
- `[[Gauss_Jordan_Elimination]]` - systematic algorithm using augmented matrices to solve linear systems
- `[[System_of_Linear_Equations]]` - the algebraic form that augmented matrices represent compactly
