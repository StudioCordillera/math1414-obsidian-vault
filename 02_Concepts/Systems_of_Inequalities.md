---
type: concept
status: active
tags:
  - concept/methods
  - concept/algebra
  - math/systems
  - math/inequalities
  - chapter-9
created: 2025-11-17
updated: 2025-11-17
---

# Systems of Inequalities

## Definition

A **system of inequalities** consists of two or more inequalities with the same variables. The solution is the **set of all points** that simultaneously satisfy every inequality in the system. Graphically, the solution is the **region of overlap** (intersection) of the individual solution regions.

**Formal Statement**: For a system:
$$\begin{cases} f_1(x, y) \leq g_1(x, y) \\ f_2(x, y) \leq g_2(x, y) \\ \vdots \end{cases}$$

The solution set is: $\{(x, y) : \text{all inequalities are true}\}$

**Key Difference from Equations**: Solution is a **region** (infinitely many points), not just discrete points.

## Mathematical Expression

**Standard Form for Linear Inequalities**:
$$\begin{cases} ax + by \leq c \\ dx + ey > f \\ gx + hy \geq k \end{cases}$$

**Graphical Solution Process**:
1. **Graph each inequality** as if it were an equation (boundary line)
2. **Determine line type**: Solid line for $\leq$ or $\geq$, dashed for $<$ or $>$
3. **Shade the region** that satisfies each inequality
4. **Find the overlap**: The intersection of all shaded regions is the solution

**Key insight**: The solution to a system of inequalities is where ALL shaded regions overlap.

## Example 1: Two Linear Inequalities

**Problem**: Graph the solution to the system:
$$\begin{cases} y \leq 2x + 1 \\ y > -x + 3 \end{cases}$$

**Step 1**: Graph first inequality $y \leq 2x + 1$
- Boundary line: $y = 2x + 1$ (slope = 2, y-intercept = 1)
- **Solid line** (because $\leq$ includes equality)
- Test point $(0, 0)$: $0 \leq 2(0) + 1 = 1$ ✓ (shade below/on line)

**Step 2**: Graph second inequality $y > -x + 3$
- Boundary line: $y = -x + 3$ (slope = -1, y-intercept = 3)
- **Dashed line** (because $>$ excludes equality)
- Test point $(0, 0)$: $0 > -(0) + 3 = 3$ ✗ (shade above line)

**Step 3**: Identify solution region
- Solution is where BOTH shadings overlap
- Region is **bounded by both lines**
- Includes points on $y = 2x + 1$ but NOT on $y = -x + 3$

**Sample solution point**: $(0, 0)$
- Check: $0 \leq 2(0) + 1 = 1$ ✓
- Check: $0 > -(0) + 3 = 3$ ✗ 
- Actually $(0, 0)$ is NOT in solution region (fails second inequality)

**Correct sample**: $(2, 0)$
- Check: $0 \leq 2(2) + 1 = 5$ ✓
- Check: $0 > -(2) + 3 = 1$ ✗
- Still fails! Try $(3, 0)$:
- Check: $0 \leq 2(3) + 1 = 7$ ✓
- Check: $0 > -(3) + 3 = 0$ ✗ (exactly on boundary)

**Valid point**: $(4, 1)$
- Check: $1 \leq 2(4) + 1 = 9$ ✓
- Check: $1 > -(4) + 3 = -1$ ✓ (BOTH satisfied!)

## Example 2: System with Three Inequalities

**Problem**: Graph the solution to the system:
$$\begin{cases} 
x + y \leq 4 \\
x - y < 2 \\
x \geq 0
\end{cases}$$

**Step 1**: Graph $x + y \leq 4$
- Boundary: $x + y = 4$ (solid line through $(4, 0)$ and $(0, 4)$)
- Test $(0, 0)$: $0 + 0 \leq 4$ ✓ (shade below/left)

**Step 2**: Graph $x - y < 2$
- Boundary: $x - y = 2$ (dashed line through $(2, 0)$ and $(0, -2)$)
- Test $(0, 0)$: $0 - 0 < 2$ ✓ (shade left of line)

**Step 3**: Graph $x \geq 0$
- Boundary: $x = 0$ (solid vertical line, the y-axis)
- Shade to the right (all points with $x \geq 0$)

**Step 4**: Find triple overlap
- Solution is the region satisfying ALL THREE inequalities
- Bounded by three lines, forms a **triangular region**
- Vertices can be found by solving pairs of boundary equations

**Finding vertices** (solve boundary line pairs):
- $x = 0$ and $x + y = 4$: Point $(0, 4)$
- $x = 0$ and $x - y = 2$: Point $(0, -2)$
- $x + y = 4$ and $x - y = 2$: 
  - Add equations: $2x = 6$, so $x = 3$
  - Then $y = 1$
  - Point $(3, 1)$

**Feasible region**: Triangle with vertices near $(0, 4)$, $(0, -2)$, and $(3, 1)$, adjusted for solid/dashed boundaries.

## Key Properties

- **Solution is a region**: Contains infinitely many points (unless system is inconsistent)
- **Boundary inclusion**: Solid line ($\leq$, $\geq$) means boundary is IN solution; dashed ($<$, $>$) means boundary is NOT in solution
- **Bounded vs unbounded**: System may produce bounded region (enclosed) or unbounded (extends to infinity)
- **Vertices are key**: Corner points (vertices) of feasible region are important for optimization problems
- **Test point strategy**: Use $(0, 0)$ when possible to determine which side of boundary to shade

## Solution Process Summary

**Systematic graphing approach:**

1. **Graph each boundary line**
   - Treat inequality as equation
   - Solid line for $\leq$ or $\geq$
   - Dashed line for $<$ or $>$

2. **Shade each inequality**
   - Use test point (often origin if not on line)
   - Shade region where inequality is TRUE

3. **Find intersection**
   - Solution is where ALL shaded regions overlap
   - May be bounded (enclosed) or unbounded

4. **Verify with test point**
   - Choose point from overlapping region
   - Confirm it satisfies EVERY inequality

## Common Errors

**Error 1**: Wrong line type
```
Wrong: Dashed line for y ≤ 2x + 1
Right: SOLID line for y ≤ 2x + 1 (includes boundary)
```

**Error 2**: Shading wrong side
```
Must test a point or use logic:
- y < mx + b → shade BELOW line
- y > mx + b → shade ABOVE line
- x < a → shade LEFT of vertical line
- x > a → shade RIGHT of vertical line
```

**Error 3**: Not finding the overlap
```
Wrong: Shading each inequality but not identifying intersection
Right: Solution is ONLY where ALL regions overlap
```

**Error 4**: Including dashed boundary in solution
```
For y > 2 (dashed line at y = 2):
Point (3, 2) is NOT in solution (exactly on excluded boundary)
Point (3, 2.1) IS in solution
```

## Applications

**Systems of inequalities model:**
- **Linear programming**: Feasible region for optimization (maximize profit, minimize cost)
- **Resource constraints**: Limited materials, time, budget
- **Nutrition planning**: Minimum/maximum intake of nutrients
- **Manufacturing**: Production constraints and capacity limits

## Relations

- `[[Linear_Inequalities]]` - individual inequalities that form the system
- `[[Graphing_Linear_Equations]]` - boundary lines are graphs of related equations
- `[[System_of_Linear_Equations]]` - equations system is related but produces points, not regions
- `[[Linear_Programming]]` - systems of inequalities define feasible regions for optimization
- `[[Absolute_Value_Inequalities]]` - can appear in more complex inequality systems
