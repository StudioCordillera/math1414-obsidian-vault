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

# Nonlinear Systems

## Definition

A **nonlinear system of equations** contains at least one equation that is not linear. Common types include systems with quadratic equations, equations with rational expressions, or equations involving radicals. Unlike linear systems that represent lines or planes, nonlinear systems involve curves like parabolas, circles, hyperbolas, or ellipses.

**Formal Statement**: A system where at least one equation contains:
- Variables raised to powers other than 1 (e.g., $x^2$, $y^3$)
- Products of variables (e.g., $xy$)
- Variables in denominators or under radicals

**Solution**: Ordered pair(s) $(x, y)$ representing intersection points of the curves.

**Key Difference from Linear**: Nonlinear systems can have **0, 1, 2, or more** solutions (linear systems have 0, 1, or infinitely many).

## Mathematical Expression

**Common Forms**:

1. **Quadratic + Linear**: Circle/parabola intersecting with line
   $$\begin{cases} x^2 + y^2 = 25 \\ y = x + 1 \end{cases}$$

2. **Two Quadratics**: Two parabolas, circle + parabola, etc.
   $$\begin{cases} x^2 + y^2 = 9 \\ x^2 - y = 3 \end{cases}$$

3. **Rational Equations**: Hyperbola intersecting with line
   $$\begin{cases} xy = 6 \\ 2x + y = 7 \end{cases}$$

**Primary Solution Method**: **Substitution** (solve one equation for a variable, substitute into other)

## Example 1: Parabola and Line

**Problem**: Solve the system:
$$\begin{cases} y = x^2 - 2 \\ y = x + 4 \end{cases}$$

**Step 1**: Both equations solved for $y$, set them equal
$$x^2 - 2 = x + 4$$

**Step 2**: Rearrange and solve quadratic
$$x^2 - x - 6 = 0$$
$$(x - 3)(x + 2) = 0$$
$$x = 3 \text{ or } x = -2$$

**Step 3**: Find corresponding $y$-values using $y = x + 4$

For $x = 3$: $y = 3 + 4 = 7$
For $x = -2$: $y = -2 + 4 = 2$

**Solutions**: $(3, 7)$ and $(-2, 2)$

**Verification**:

For $(3, 7)$:
- $y = x^2 - 2$: $7 = 9 - 2 = 7$ ✓
- $y = x + 4$: $7 = 3 + 4 = 7$ ✓

For $(-2, 2)$:
- $y = x^2 - 2$: $2 = 4 - 2 = 2$ ✓
- $y = x + 4$: $2 = -2 + 4 = 2$ ✓

**Geometric interpretation**: A line intersects a parabola at two points.

## Example 2: Circle and Line

**Problem**: Solve the system:
$$\begin{cases} x^2 + y^2 = 25 \\ y = x - 1 \end{cases}$$

**Step 1**: Substitute $y = x - 1$ into circle equation
$$x^2 + (x - 1)^2 = 25$$

**Step 2**: Expand and simplify
$$x^2 + x^2 - 2x + 1 = 25$$
$$2x^2 - 2x + 1 = 25$$
$$2x^2 - 2x - 24 = 0$$
$$x^2 - x - 12 = 0$$

**Step 3**: Factor
$$(x - 4)(x + 3) = 0$$
$$x = 4 \text{ or } x = -3$$

**Step 4**: Find $y$-values using $y = x - 1$

For $x = 4$: $y = 4 - 1 = 3$
For $x = -3$: $y = -3 - 1 = -4$

**Solutions**: $(4, 3)$ and $(-3, -4)$

**Verification**:

For $(4, 3)$:
- $x^2 + y^2 = 16 + 9 = 25$ ✓
- $y = 4 - 1 = 3$ ✓

For $(-3, -4)$:
- $x^2 + y^2 = 9 + 16 = 25$ ✓
- $y = -3 - 1 = -4$ ✓

**Geometric interpretation**: A line intersects a circle at two points (secant line).

## Example 3: Hyperbola (xy = k form)

**Problem**: Solve the system:
$$\begin{cases} xy = 12 \\ x + y = 7 \end{cases}$$

**Step 1**: Solve second equation for $y$
$$y = 7 - x$$

**Step 2**: Substitute into first equation
$$x(7 - x) = 12$$
$$7x - x^2 = 12$$
$$-x^2 + 7x - 12 = 0$$
$$x^2 - 7x + 12 = 0$$

**Step 3**: Factor
$$(x - 3)(x - 4) = 0$$
$$x = 3 \text{ or } x = 4$$

**Step 4**: Find $y$-values using $y = 7 - x$

For $x = 3$: $y = 7 - 3 = 4$
For $x = 4$: $y = 7 - 4 = 3$

**Solutions**: $(3, 4)$ and $(4, 3)$

**Verification**:
- For $(3, 4)$: $3 \cdot 4 = 12$ ✓ and $3 + 4 = 7$ ✓
- For $(4, 3)$: $4 \cdot 3 = 12$ ✓ and $4 + 3 = 7$ ✓

## Key Properties

- **Multiple solutions common**: Can have 0, 1, 2, 3, 4, or more solutions
- **Substitution preferred**: Generally more effective than elimination for nonlinear systems
- **Higher-degree equations**: Solving often produces quadratics (2 solutions) or higher polynomials
- **Geometric interpretation**: Solutions are intersection points of curves
- **Complex solutions**: Some algebraic solutions may be complex (not real intersections)

## Solution Scenarios

**Number of solutions depends on geometry:**
- **Line and parabola**: 0, 1, or 2 solutions
- **Line and circle**: 0 (miss), 1 (tangent), or 2 (secant) solutions
- **Two circles**: 0, 1, 2, or infinitely many (coincident circles)
- **Two conics**: Can have up to 4 real solutions

## Strategic Approach

**Step-by-step strategy:**
1. **Identify** which equation is easier to solve for a variable (usually the linear one)
2. **Solve** that equation for one variable
3. **Substitute** into the nonlinear equation
4. **Solve resulting** single-variable equation (often quadratic)
5. **Back-substitute** to find corresponding values for other variable
6. **Verify** all solutions in both original equations

## Common Errors

**Error 1**: Forgetting the second solution from quadratic
```
Wrong: Finding x = 3 from (x-3)(x+2)=0 and stopping
Right: x = 3 OR x = -2, find y for both
```

**Error 2**: Sign errors when expanding $(x - a)^2$
```
Wrong: (x - 1)² = x² - 1
Right: (x - 1)² = x² - 2x + 1
```

**Error 3**: Not checking solutions (may be extraneous)
```
Always verify in BOTH original equations
Especially important when squaring occurred
```

## Relations

- `[[Substitution_Method]]` - primary technique for solving nonlinear systems
- `[[Quadratic_Equations]]` - substitution often reduces to solving quadratics
- `[[System_of_Linear_Equations]]` - linear systems are special case with different solution patterns
- `[[Conic_Sections]]` - circles, ellipses, parabolas, hyperbolas appear in nonlinear systems
- `[[Extraneous_Solutions]]` - can arise when solving radical or rational equations in systems
