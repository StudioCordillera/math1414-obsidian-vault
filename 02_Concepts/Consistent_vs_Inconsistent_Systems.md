---
type: concept
status: active
tags:
  - concept/linear_systems
  - math/algebra
  - math/systems
  - chapter-5
created: 2025-10-25
updated: 2025-11-16
---

# Inconsistent System

## Definition

An **inconsistent system** of linear equations is a system that has **no solution**. Algebraically, the equations represent constraints that cannot simultaneously be satisfied—there exists no assignment of values to the variables that makes all equations true.

In contrast, a **consistent system** has at least one solution (either unique or infinitely many).

## Matrix Diagnostic

After applying row operations to the augmented matrix, an inconsistent system reveals itself through a **contradiction row**:

$$
[0 \; 0 \; \cdots \; 0 \mid c] \quad \text{where } c \neq 0
$$

This row translates to the equation $0 = c$, which is impossible.

## Examples

### Example 1: Inconsistent Two-Variable System

$$
\begin{cases}
x + 2y = 3 \\
2x + 4y = 10
\end{cases}
$$

**Augmented matrix:**
$$
\left[\begin{array}{cc|c}
1 & 2 & 3 \\
2 & 4 & 10
\end{array}\right]
$$

**Row reduction:**
$$
\xrightarrow{R_2 - 2R_1 \to R_2}
\left[\begin{array}{cc|c}
1 & 2 & 3 \\
0 & 0 & 4
\end{array}\right]
$$

**Interpretation:** The second row says $0 = 4$, which is impossible. **No solution.**

### Example 2: Inconsistent Three-Variable System

$$
\begin{cases}
x + y + z = 1 \\
2x + 2y + 2z = 3 \\
3x - y + z = 0
\end{cases}
$$

**Augmented matrix:**
$$
\left[\begin{array}{ccc|c}
1 & 1 & 1 & 1 \\
2 & 2 & 2 & 3 \\
3 & -1 & 1 & 0
\end{array}\right]
$$

**After row operations:**
$$
\left[\begin{array}{ccc|c}
1 & 1 & 1 & 1 \\
0 & 0 & 0 & 1 \\
0 & -4 & -2 & -3
\end{array}\right]
$$

**Row 2** produces the contradiction $0 = 1$. **No solution.**

### Example 3: Consistent System (For Contrast)

$$
\begin{cases}
x + 2y = 5 \\
3x + 6y = 15
\end{cases}
$$

**After reduction:**
$$
\left[\begin{array}{cc|c}
1 & 2 & 5 \\
0 & 0 & 0
\end{array}\right]
$$

**Row 2** is $0 = 0$ (true), so the system is **consistent** with infinitely many solutions.

## Geometric Interpretation

### In $\mathbb{R}^2$

Two equations in two variables represent lines:

- **Consistent unique:** Lines intersect at one point
- **Consistent infinite:** Lines coincide (same line)
- **Inconsistent:** Lines are parallel and distinct (never meet)

**Example:** $x + y = 1$ and $x + y = 2$ are parallel lines ($y = 1 - x$ vs $y = 2 - x$).

### In $\mathbb{R}^3$

Three equations represent planes:

- **Inconsistent:** Planes arranged so there is no common intersection point (e.g., parallel planes, planes forming a "triangular prism")

## Classification Summary

| **Condition After REF** | **Solution Type** | **Name** |
|---|---|---|
| No contradiction row; all columns have pivots | Unique solution | Consistent, independent |
| No contradiction row; at least one free variable | Infinitely many solutions | Consistent, dependent |
| At least one row $[0 \cdots 0 \mid c]$ with $c \neq 0$ | No solution | **Inconsistent** |

## Relations

- `[[System_of_Linear_Equations]]` - the general structure that can be consistent or inconsistent
- `[[Augmented_Matrix]]` - the representation used to detect inconsistency through row operations
- `[[Row_Echelon_Form]]` - the form where contradiction rows become visible
- `[[Gauss_Jordan_Elimination]]` - algorithm that reveals inconsistency systematically
- `[[Dependent_System]]` - another classification (consistent with infinitely many solutions)
