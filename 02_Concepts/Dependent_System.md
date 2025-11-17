---
type: concept
status: active
tags:
  - concept/linear_systems
  - math/algebra
  - math/systems
  - chapter-5
created: 2025-11-16
updated: 2025-11-16
---

# Dependent System

## Definition

A **dependent system** of linear equations is a consistent system that has **infinitely many solutions**. This occurs when the equations are not all independent—some equations can be derived from combinations of others, resulting in at least one **free variable** that can take any value.

In a dependent system, the solution set forms a line, plane, or higher-dimensional subspace rather than a single point.

## Matrix Diagnostic

After row reduction to REF or RREF, a dependent system is identified by:

1. **No contradiction row** (system is consistent)
2. **At least one free variable:** A column without a pivot position

The free variable(s) can be assigned any value, and the pivot variables are expressed in terms of the free variables.

## Mathematical Structure

For a system with $n$ variables and $m$ equations in RREF:

- **Pivot variables:** Variables corresponding to columns with leading 1s
- **Free variables:** Variables corresponding to columns without pivots
- **Solution form:** Pivot variables = expressions involving free variables

If there are $r$ pivots and $n$ variables, then there are $n - r$ free variables.

## Examples

### Example 1: Two-Variable Dependent System

$$
\begin{cases}
x + 2y = 3 \\
2x + 4y = 6
\end{cases}
$$

**Augmented matrix and reduction:**
$$
\left[\begin{array}{cc|c}
1 & 2 & 3 \\
2 & 4 & 6
\end{array}\right]
\xrightarrow{R_2 - 2R_1 \to R_2}
\left[\begin{array}{cc|c}
1 & 2 & 3 \\
0 & 0 & 0
\end{array}\right]
$$

**Analysis:**

- Column 1 has a pivot (corresponds to $x$)
- Column 2 has no pivot ($y$ is free)

**Solution:** $x = 3 - 2y$ where $y$ is free

**Parametric form:** $(x, y) = (3 - 2t, t)$ for $t \in \mathbb{R}$

### Example 2: Three-Variable Dependent System

$$
\begin{cases}
x + 2y - z = 4 \\
2x + 4y - 2z = 8 \\
-x - 2y + z = -4
\end{cases}
$$

**RREF:**
$$
\left[\begin{array}{ccc|c}
1 & 2 & -1 & 4 \\
0 & 0 & 0 & 0 \\
0 & 0 & 0 & 0
\end{array}\right]
$$

**Analysis:**

- Column 1 has pivot ($x$ is pivot variable)
- Columns 2 and 3 have no pivots ($y$ and $z$ are free)

**Solution:** $x = 4 - 2y + z$ where $y, z$ are free

**Parametric form:** $(x, y, z) = (4 - 2s + t, s, t)$ for $s, t \in \mathbb{R}$

### Example 3: System with One Free Variable

$$
\begin{cases}
x + 2y + 3z = 9 \\
2x + 5y + 8z = 23 \\
x + 3y + 5z = 14
\end{cases}
$$

**RREF:**
$$
\left[\begin{array}{ccc|c}
1 & 0 & 1 & 1 \\
0 & 1 & 2 & 4 \\
0 & 0 & 0 & 0
\end{array}\right]
$$

**Solution:**

- $x = 1 - z$
- $y = 4 - 2z$
- $z$ is free

**Parametric form:** $(x, y, z) = (1 - t, 4 - 2t, t)$ for $t \in \mathbb{R}$

## Geometric Interpretation

### In $\mathbb{R}^2$

Two dependent equations represent the **same line** (coincident lines):

- Example: $x + y = 1$ and $2x + 2y = 2$
- Solution: all points on the line $y = 1 - x$

### In $\mathbb{R}^3$

Three dependent equations can represent:

- **Three identical planes:** All equations describe the same plane
- **Planes intersecting in a line:** Equations are consistent but not independent
- **Planes intersecting in a plane:** When some equations are redundant

**Example:** $x + y + z = 1$, $2x + 2y + 2z = 2$, $3x + 3y + 3z = 3$ all represent the same plane.

## Classification Summary

| **Condition After RREF** | **Solution Type** | **Name** |
|---|---|---|
| No contradiction; all columns have pivots | Unique solution | Consistent, independent |
| **No contradiction; at least one free variable** | **Infinitely many solutions** | **Consistent, dependent** |
| Contradiction row $[0 \cdots 0 \mid c \neq 0]$ | No solution | Inconsistent |

## Key Properties

- **Solution set is a subspace:** The solution set has dimension equal to the number of free variables
- **Parametric representation:** Solutions are expressed using free variable parameters
- **Linear dependence:** Some equations are linear combinations of others
- **Reduced information:** The system doesn't provide enough independent constraints to determine a unique solution

## Relations

- `[[System_of_Linear_Equations]]` - the general algebraic structure that can be dependent
- `[[Augmented_Matrix]]` - representation used to identify free variables through row reduction
- `[[Reduced_Row_Echelon_Form]]` - form where free variable columns are clearly visible
- `[[Gauss_Jordan_Elimination]]` - algorithm that reveals dependent structure systematically
- `[[Inconsistent_System]]` - contrasting case where no solution exists (dependent systems have infinitely many)
