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

# Row Echelon Form

## Definition

A matrix is in **row echelon form (REF)** if it satisfies three conditions:

1. **All nonzero rows are above any rows of all zeros**
2. **Each leading entry (first nonzero entry from the left) of a row is in a column to the right of the leading entry of the row above it**
3. **All entries in a column below a leading entry are zeros**

The leading entry in each nonzero row is called a **pivot**.

## Mathematical Criteria

For a matrix $A$ in REF:

- If row $i$ is nonzero and row $j$ is zero, then $i < j$
- If $a_{ik}$ is the leading entry of row $i$ and $a_{j\ell}$ is the leading entry of row $j$ where $i < j$, then $k < \ell$
- If column $k$ contains a leading entry, all entries below that leading entry are zero

## Examples

### Example 1: Matrix in REF

$$
\left[\begin{array}{cccc|c}
1 & 2 & 3 & 4 & 5 \\
0 & 0 & 2 & 1 & 6 \\
0 & 0 & 0 & 3 & 9 \\
0 & 0 & 0 & 0 & 0
\end{array}\right]
$$

**Pivots:** 1 (row 1, column 1), 2 (row 2, column 3), 3 (row 3, column 4)

This matrix satisfies all three REF conditions.

### Example 2: Not in REF

$$
\left[\begin{array}{ccc|c}
1 & 2 & 3 & 5 \\
0 & 0 & 0 & 0 \\
0 & 0 & 2 & 4
\end{array}\right]
$$

**Violation:** Zero row appears before a nonzero row (condition 1 violated).

### Example 3: Complete System in REF

Original system:
$$
\begin{cases}
2x + 4y - 2z = 2 \\
4x + 9y - 3z = 8 \\
-2x - 3y + 7z = 10
\end{cases}
$$

After row operations:
$$
\left[\begin{array}{ccc|c}
1 & 2 & -1 & 1 \\
0 & 1 & 1 & 4 \\
0 & 0 & 1 & 2
\end{array}\right]
$$

This REF allows **back-substitution**:

- From row 3: $z = 2$
- From row 2: $y + z = 4 \Rightarrow y = 2$
- From row 1: $x + 2y - z = 1 \Rightarrow x = -1$

## Key Properties

- **Non-unique:** A matrix can have multiple valid REF representations
- **Stopping point:** REF is the natural endpoint of forward elimination in Gaussian elimination
- **Back-substitution ready:** Solutions can be found by working upward from the bottom row
- **Pivot positions:** The locations of pivots reveal information about solution structure

## Relations

- `[[Row_Operations]]` - elementary operations used to transform matrices into REF
- `[[Augmented_Matrix]]` - the matrix structure typically transformed to REF
- `[[Reduced_Row_Echelon_Form]]` - unique further simplification of REF
- `[[Gauss_Jordan_Elimination]]` - extends Gaussian elimination to reach RREF
- `[[System_of_Linear_Equations]]` - the algebraic system that REF helps solve
