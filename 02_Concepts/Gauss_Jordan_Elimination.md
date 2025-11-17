---
type: concept
status: active
tags:
  - concept/linear_systems
  - math/algebra
  - math/matrices
  - technique/elimination
  - chapter-5
created: 2025-10-25
updated: 2025-11-16
---

# Gauss-Jordan Elimination

## Definition

**Gauss-Jordan elimination** is an algorithmic extension of Gaussian elimination that continues row operations beyond row echelon form (REF) to produce reduced row echelon form (RREF). The result displays solutions directly without requiring back-substitution.

## Algorithm Steps

### Phase 1: Forward Elimination (to REF)

1. **Form augmented matrix** $[A|b]$ from the system $Ax = b$
2. **Identify pivot position** (leftmost nonzero column)
3. **Swap rows if needed** to place nonzero entry in pivot position
4. **Scale pivot row** to make leading entry equal to 1
5. **Eliminate below** the pivot using row operations
6. **Repeat** for next row until reaching REF

### Phase 2: Backward Elimination (REF to RREF)

1. **Start from bottom pivot** and work upward
2. **Eliminate above each pivot** to create zeros in entire pivot column
3. **Result:** RREF with identity matrix pattern in pivot columns

## Complete Example

Solve the system:
$$
\begin{cases}
x + 2y + z = 4 \\
2x + 3y + 3z = 7 \\
3x + 4y + z = 8
\end{cases}
$$

**Step 1:** Form augmented matrix
$$
\left[\begin{array}{ccc|c}
1 & 2 & 1 & 4 \\
2 & 3 & 3 & 7 \\
3 & 4 & 1 & 8
\end{array}\right]
$$

**Step 2:** Eliminate below first pivot
$$
\xrightarrow{\substack{R_2 - 2R_1 \to R_2 \\ R_3 - 3R_1 \to R_3}}
\left[\begin{array}{ccc|c}
1 & 2 & 1 & 4 \\
0 & -1 & 1 & -1 \\
0 & -2 & -2 & -4
\end{array}\right]
$$

**Step 3:** Scale second pivot and eliminate below
$$
\xrightarrow{-R_2 \to R_2}
\left[\begin{array}{ccc|c}
1 & 2 & 1 & 4 \\
0 & 1 & -1 & 1 \\
0 & -2 & -2 & -4
\end{array}\right]
\xrightarrow{R_3 + 2R_2 \to R_3}
\left[\begin{array}{ccc|c}
1 & 2 & 1 & 4 \\
0 & 1 & -1 & 1 \\
0 & 0 & -4 & -2
\end{array}\right]
$$

**Step 4:** Scale third pivot (REF complete)
$$
\xrightarrow{-\frac{1}{4}R_3 \to R_3}
\left[\begin{array}{ccc|c}
1 & 2 & 1 & 4 \\
0 & 1 & -1 & 1 \\
0 & 0 & 1 & \frac{1}{2}
\end{array}\right]
$$

**Step 5:** Eliminate above third pivot
$$
\xrightarrow{\substack{R_2 + R_3 \to R_2 \\ R_1 - R_3 \to R_1}}
\left[\begin{array}{ccc|c}
1 & 2 & 0 & \frac{7}{2} \\
0 & 1 & 0 & \frac{3}{2} \\
0 & 0 & 1 & \frac{1}{2}
\end{array}\right]
$$

**Step 6:** Eliminate above second pivot (RREF complete)
$$
\xrightarrow{R_1 - 2R_2 \to R_1}
\left[\begin{array}{ccc|c}
1 & 0 & 0 & 2 \\
0 & 1 & 0 & \frac{3}{2} \\
0 & 0 & 1 & \frac{1}{2}
\end{array}\right]
$$

**Solution:** $x = 2$, $y = \frac{3}{2}$, $z = \frac{1}{2}$ (read directly from RREF)

## Solution Types Revealed by RREF

### Unique Solution

Identity matrix in coefficient columns:
$$
\left[\begin{array}{cc|c}
1 & 0 & a \\
0 & 1 & b
\end{array}\right]
$$

### No Solution (Inconsistent)

Row of form $[0 \; 0 \; \cdots \; 0 | c]$ with $c \neq 0$:
$$
\left[\begin{array}{cc|c}
1 & 2 & 3 \\
0 & 0 & 5
\end{array}\right]
$$

### Infinitely Many Solutions (Dependent)

Free variable columns (no pivot):
$$
\left[\begin{array}{ccc|c}
1 & 0 & 3 & 2 \\
0 & 1 & -1 & 4 \\
0 & 0 & 0 & 0
\end{array}\right]
$$
Solution: $x_1 = 2 - 3x_3$, $x_2 = 4 + x_3$, $x_3$ free

## Key Properties

- **RREF uniqueness:** Every matrix has exactly one RREF representation
- **Direct solutions:** No back-substitution needed; read solutions immediately
- **Complete information:** Solution type (unique/none/infinite) is immediately visible
- **More work than Gaussian elimination:** Requires additional row operations beyond REF

## Relations

- `[[Row_Operations]]` - the three elementary operations that drive the algorithm
- `[[Augmented_Matrix]]` - the matrix structure on which the algorithm operates
- `[[Reduced_Row_Echelon_Form]]` - the unique target form produced by the algorithm
- `[[Row_Echelon_Form]]` - intermediate form achieved after forward elimination phase
- `[[System_of_Linear_Equations]]` - the algebraic problem that this algorithm solves systematically
