---
type: concept
status: active
tags:
  - concept/linear_systems
  - math/algebra
  - math/matrices
  - technique/row_operations
  - chapter-5
created: 2025-10-25
updated: 2025-11-16
---

# Elementary Row Operations

## Definition

**Elementary row operations** are three fundamental transformations that can be applied to the rows of a matrix while preserving the solution set of the corresponding linear system. These operations form the foundation of systematic solution methods like Gaussian elimination.

## The Three Operations

### 1. Row Interchange (Swap)

**Notation:** $R_i \leftrightarrow R_j$

Swap the positions of row $i$ and row $j$.

**Example:**
$$
\left[\begin{array}{cc|c}
2 & 1 & 5 \\
1 & 3 & 8
\end{array}\right]
\xrightarrow{R_1 \leftrightarrow R_2}
\left[\begin{array}{cc|c}
1 & 3 & 8 \\
2 & 1 & 5
\end{array}\right]
$$

### 2. Row Scaling (Multiplication)

**Notation:** $kR_i \to R_i$ where $k \neq 0$

Multiply all entries in row $i$ by nonzero constant $k$.

**Example:**
$$
\left[\begin{array}{cc|c}
2 & 4 & 6 \\
1 & 3 & 8
\end{array}\right]
\xrightarrow{\frac{1}{2}R_1 \to R_1}
\left[\begin{array}{cc|c}
1 & 2 & 3 \\
1 & 3 & 8
\end{array}\right]
$$

### 3. Row Addition (Replacement)

**Notation:** $R_i + kR_j \to R_i$ where $i \neq j$

Add $k$ times row $j$ to row $i$, storing the result in row $i$.

**Example:**
$$
\left[\begin{array}{cc|c}
1 & 2 & 3 \\
2 & 5 & 9
\end{array}\right]
\xrightarrow{R_2 - 2R_1 \to R_2}
\left[\begin{array}{cc|c}
1 & 2 & 3 \\
0 & 1 & 3
\end{array}\right]
$$

## Complete Example

Solve the system using elementary row operations:
$$
\begin{cases}
x + 2y = 5 \\
3x + 7y = 16
\end{cases}
$$

**Step 1:** Form augmented matrix
$$
\left[\begin{array}{cc|c}
1 & 2 & 5 \\
3 & 7 & 16
\end{array}\right]
$$

**Step 2:** Eliminate below pivot (Row Addition)
$$
\xrightarrow{R_2 - 3R_1 \to R_2}
\left[\begin{array}{cc|c}
1 & 2 & 5 \\
0 & 1 & 1
\end{array}\right]
$$

**Step 3:** Back-substitution or continue to RREF
$$
\xrightarrow{R_1 - 2R_2 \to R_1}
\left[\begin{array}{cc|c}
1 & 0 & 3 \\
0 & 1 & 1
\end{array}\right]
$$

**Solution:** $x = 3, y = 1$

## Key Properties

- **Solution preservation:** All three operations produce row-equivalent matrices with identical solution sets
- **Reversibility:** Each operation has an inverse operation that undoes it
- **Basis for algorithms:** Gaussian elimination and Gauss-Jordan elimination are systematic applications of these operations

## Common Mistakes

- **Multiplying by zero:** $0 \cdot R_i$ destroys information and is not an elementary row operation
- **Partial application:** Forgetting to apply the operation to all entries in the row, including the constant term
- **Incorrect notation:** Writing $R_1 + R_2 \to R_1 + R_2$ instead of specifying which row stores the result

## Relations

- `[[Augmented_Matrix]]` - the matrix structure on which row operations are performed
- `[[Row_Echelon_Form]]` - achieved by systematic application of row operations
- `[[Reduced_Row_Echelon_Form]]` - further refined form using additional row operations
- `[[Gauss_Jordan_Elimination]]` - algorithm that applies row operations to reach RREF
- `[[System_of_Linear_Equations]]` - the algebraic system that row operations help solve
