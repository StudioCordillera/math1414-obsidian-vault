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

# Reduced Row Echelon Form

## Definition

A matrix is in **reduced row echelon form (RREF)** if it satisfies all conditions for row echelon form (REF) plus two additional conditions:

**REF Conditions:**

1. All nonzero rows are above any rows of all zeros
2. Each leading entry is to the right of the leading entry in the row above
3. All entries below a leading entry are zeros

**Additional RREF Conditions:**
4. **Every leading entry is 1** (called a **leading 1** or **pivot 1**)
5. **Each leading 1 is the only nonzero entry in its column** (zeros above and below)

RREF is the **unique** canonical form for any matrix—unlike REF, there is only one RREF for a given matrix.

## Mathematical Criteria

For a matrix $A$ in RREF:

- All conditions for REF hold
- If $a_{ik}$ is a leading entry in row $i$, then $a_{ik} = 1$
- If column $k$ contains a leading 1, then all other entries in column $k$ are zero

## Examples

### Example 1: Matrix in RREF

$$
\left[\begin{array}{cccc|c}
1 & 0 & 0 & 3 & 4 \\
0 & 1 & 0 & 2 & -1 \\
0 & 0 & 1 & -5 & 7 \\
0 & 0 & 0 & 0 & 0
\end{array}\right]
$$

**Pivot columns:** 1, 2, 3 (each contains exactly one 1, rest zeros)  
**Free variable:** Column 4 (no pivot)

This directly reveals: $x_1 = 4 - 3x_4$, $x_2 = -1 - 2x_4$, $x_3 = 7 + 5x_4$ where $x_4$ is free.

### Example 2: REF but Not RREF

$$
\left[\begin{array}{ccc|c}
2 & 4 & -2 & 6 \\
0 & 1 & 3 & 5 \\
0 & 0 & 1 & 2
\end{array}\right]
$$

**Violations:**

- Leading entry in row 1 is 2, not 1 (condition 4)
- Column 2 has nonzero entry above the leading 1 (condition 5)
- Column 3 has nonzero entry above the leading 1 (condition 5)

### Example 3: Converting REF to RREF

Start with REF:
$$
\left[\begin{array}{ccc|c}
1 & 2 & -1 & 1 \\
0 & 1 & 1 & 4 \\
0 & 0 & 1 & 2
\end{array}\right]
$$

**Step 1:** Eliminate above pivot in column 3
$$
\xrightarrow{R_2 - R_3 \to R_2}
\left[\begin{array}{ccc|c}
1 & 2 & -1 & 1 \\
0 & 1 & 0 & 2 \\
0 & 0 & 1 & 2
\end{array}\right]
$$

**Step 2:** Eliminate above pivot in column 2 and remaining in column 3
$$
\xrightarrow{R_1 - 2R_2 + R_3 \to R_1}
\left[\begin{array}{ccc|c}
1 & 0 & 0 & -1 \\
0 & 1 & 0 & 2 \\
0 & 0 & 1 & 2
\end{array}\right]
$$

**Solution:** $x = -1$, $y = 2$, $z = 2$ (read directly from RREF)

## Key Properties

- **Uniqueness:** Every matrix has exactly one RREF (unlike REF which is non-unique)
- **Solution visibility:** Solutions can be read directly without back-substitution
- **Pivot identification:** Pivot columns and free variables are immediately apparent
- **Canonical form:** RREF serves as the standard representative for row-equivalent matrices

## Computational Notes

- RREF requires more row operations than REF
- Gauss-Jordan elimination produces RREF
- Standard Gaussian elimination stops at REF, then uses back-substitution

## Relations

- `[[Row_Echelon_Form]]` - the intermediate form that RREF extends and refines
- `[[Row_Operations]]` - elementary operations used to transform REF into RREF
- `[[Gauss_Jordan_Elimination]]` - algorithm that systematically produces RREF
- `[[Augmented_Matrix]]` - the matrix structure transformed to RREF to solve systems
- `[[System_of_Linear_Equations]]` - algebraic system whose solutions are revealed in RREF
