---
type: concept
status: active
tags:
  - concept/methods
  - concept/algebra
  - math/systems
  - math/equations
  - chapter-9
created: 2025-11-17
updated: 2025-11-17
---

# Three Variable Systems

## Definition

A **three-variable system** (also called a **3×3 system**) consists of three equations with three unknowns, typically $x$, $y$, and $z$. The goal is to find values for all three variables that simultaneously satisfy all three equations.

**Formal Statement**: A system of three linear equations in three variables:
$$\begin{cases} a_1x + b_1y + c_1z = d_1 \\ a_2x + b_2y + c_2z = d_2 \\ a_3x + b_3y + c_3z = d_3 \end{cases}$$

**Solution**: An ordered triple $(x, y, z)$ that satisfies all three equations.

**Key Strategy**: Reduce the 3×3 system to a 2×2 system by eliminating one variable from two pairs of equations, then solve the 2×2 system.

## Mathematical Expression

**General Solution Process**:

1. **Eliminate one variable** (choose $z$ if convenient) from equations (1) and (2)
2. **Eliminate the same variable** from equations (1) and (3) or (2) and (3)
3. **Solve the resulting 2×2 system** for two variables
4. **Back-substitute** to find the third variable
5. **Verify** solution in all three original equations

**Key insight**: The 3-variable problem reduces to a familiar 2-variable problem through systematic elimination.

## Example: Complete 3×3 Solution

**Problem**: Solve the system:
$$\begin{cases} 
x + y + z = 6 \quad \text{(1)}\\
2x - y + 3z = 14 \quad \text{(2)}\\
-x + 2y + z = 1 \quad \text{(3)}
\end{cases}$$

**Step 1**: Eliminate $z$ from equations (1) and (2)

Multiply equation (1) by -3:
$$-3x - 3y - 3z = -18$$

Add to equation (2):
$$2x - y + 3z = 14$$
$$\underline{-3x - 3y - 3z = -18}$$
$$-x - 4y = -4 \quad \text{(4)}$$

**Step 2**: Eliminate $z$ from equations (1) and (3)

Subtract equation (3) from equation (1):
$$(x + y + z) - (-x + 2y + z) = 6 - 1$$
$$2x - y = 5 \quad \text{(5)}$$

**Step 3**: Solve the 2×2 system of equations (4) and (5)

We have:
$$\begin{cases} 
-x - 4y = -4 \quad \text{(4)}\\
2x - y = 5 \quad \text{(5)}
\end{cases}$$

Multiply equation (4) by 2:
$$-2x - 8y = -8$$

Add to equation (5):
$$2x - y = 5$$
$$\underline{-2x - 8y = -8}$$
$$-9y = -3$$
$$y = \frac{1}{3}$$

**Step 4**: Back-substitute $y = \frac{1}{3}$ into equation (5)
$$2x - \frac{1}{3} = 5$$
$$2x = 5 + \frac{1}{3} = \frac{16}{3}$$
$$x = \frac{8}{3}$$

**Step 5**: Back-substitute $x = \frac{8}{3}$ and $y = \frac{1}{3}$ into equation (1)
$$\frac{8}{3} + \frac{1}{3} + z = 6$$
$$3 + z = 6$$
$$z = 3$$

**Solution**: $\left(\frac{8}{3}, \frac{1}{3}, 3\right)$ or approximately $(2.67, 0.33, 3)$

**Verification**:

- Equation (1): $\frac{8}{3} + \frac{1}{3} + 3 = \frac{9}{3} + 3 = 3 + 3 = 6$ ✓
- Equation (2): $2 \cdot \frac{8}{3} - \frac{1}{3} + 3 \cdot 3 = \frac{16}{3} - \frac{1}{3} + 9 = \frac{15}{3} + 9 = 5 + 9 = 14$ ✓
- Equation (3): $-\frac{8}{3} + 2 \cdot \frac{1}{3} + 3 = -\frac{8}{3} + \frac{2}{3} + 3 = -\frac{6}{3} + 3 = -2 + 3 = 1$ ✓

## Key Properties

- **Three-dimensional geometry**: Solution represents intersection point of three planes in 3D space
- **Systematic reduction**: Always reduces 3×3 to 2×2, then 2×2 to single equation
- **Variable choice**: Strategically choose which variable to eliminate first (look for coefficients of 1 or simple relationships)
- **Solution types**: 
  - One solution (planes intersect at a point)
  - No solution (planes have no common intersection)
  - Infinitely many solutions (planes intersect along a line or coincide)

## Strategic Approach

**Choose which variable to eliminate:**
- Look for coefficients of **1** or **-1** (easiest to eliminate)
- Look for a variable **missing** from one equation (use that pair first)
- Choose variable with **simplest coefficient relationships**

**Which equations to pair:**
- Combine equations that make elimination easiest
- Typically: (1)+(2), then (1)+(3) or (2)+(3)

## Common Errors

**Error 1**: Forgetting to eliminate the **same** variable twice
```
Wrong: Eliminate x from (1)+(2), then eliminate y from (2)+(3)
Right: Eliminate x from (1)+(2), then eliminate x from (1)+(3)
```

**Error 2**: Arithmetic errors in multiple steps compound
```
Strategy: Work carefully, check intermediate steps
Verify 2×2 system before solving
```

**Error 3**: Not verifying in all three original equations
```
Must check solution in ALL THREE equations
Don't stop after checking just one or two
```

## Relations

- `[[Elimination_Method]]` - core technique extended to three variables
- `[[Substitution_Method]]` - alternative approach, though elimination is typically more efficient for 3×3
- `[[System_of_Linear_Equations]]` - general category (3×3 is specific case)
- `[[Augmented_Matrix]]` - 3×3 systems can also be solved using matrix methods (Gauss-Jordan)
- `[[Consistent_vs_Inconsistent_Systems]]` - 3×3 systems can also be inconsistent or dependent
