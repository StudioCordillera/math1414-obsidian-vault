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

# Substitution Method

## Definition

The **substitution method** is a technique for solving systems of equations by solving one equation for one variable in terms of the other, then substituting that expression into the other equation. This reduces a system of two variables to a single equation in one variable.

**Formal Statement**: For a system of two equations in two variables:
$$\begin{cases} f(x, y) = 0 \\ g(x, y) = 0 \end{cases}$$

Solve one equation for one variable (e.g., $y = h(x)$), then substitute into the other equation to get $f(x, h(x)) = 0$, which can be solved for $x$.

**When to Use**: Most efficient when one equation is already solved for a variable, or can be easily solved for a variable (coefficient of 1).

## Mathematical Expression

**General Process**:
1. Solve one equation for one variable: $y = h(x)$ or $x = k(y)$
2. Substitute into the other equation: Replace the variable everywhere it appears
3. Solve the resulting single-variable equation
4. Back-substitute to find the other variable
5. Check solution in both original equations

**Key insight**: Substitution transforms a 2-variable system into a 1-variable equation by expressing one variable in terms of the other.

## Example 1: Linear System

**Problem**: Solve the system using substitution:
$$\begin{cases} y = 2x - 1 \\ 3x + 2y = 16 \end{cases}$$

**Step 1**: First equation already solved for $y$
$$y = 2x - 1$$

**Step 2**: Substitute into second equation
$$3x + 2(2x - 1) = 16$$

**Step 3**: Solve for $x$
$$3x + 4x - 2 = 16$$
$$7x = 18$$
$$x = \frac{18}{7}$$

**Step 4**: Back-substitute into $y = 2x - 1$
$$y = 2\left(\frac{18}{7}\right) - 1 = \frac{36}{7} - \frac{7}{7} = \frac{29}{7}$$

**Solution**: $\left(\frac{18}{7}, \frac{29}{7}\right)$ or approximately $(2.57, 4.14)$

**Verification**:
- First equation: $\frac{29}{7} = 2 \cdot \frac{18}{7} - 1 = \frac{36}{7} - \frac{7}{7} = \frac{29}{7}$ ✓
- Second equation: $3 \cdot \frac{18}{7} + 2 \cdot \frac{29}{7} = \frac{54 + 58}{7} = \frac{112}{7} = 16$ ✓

## Example 2: System Requiring Initial Solving

**Problem**: Solve using substitution:
$$\begin{cases} x + 3y = 11 \\ 2x - y = 3 \end{cases}$$

**Step 1**: Solve first equation for $x$ (coefficient is 1)
$$x = 11 - 3y$$

**Step 2**: Substitute into second equation
$$2(11 - 3y) - y = 3$$

**Step 3**: Solve for $y$
$$22 - 6y - y = 3$$
$$-7y = -19$$
$$y = \frac{19}{7}$$

**Step 4**: Back-substitute into $x = 11 - 3y$
$$x = 11 - 3\left(\frac{19}{7}\right) = \frac{77 - 57}{7} = \frac{20}{7}$$

**Solution**: $\left(\frac{20}{7}, \frac{19}{7}\right)$ or approximately $(2.86, 2.71)$

**Verification**:
- $\frac{20}{7} + 3 \cdot \frac{19}{7} = \frac{20 + 57}{7} = \frac{77}{7} = 11$ ✓
- $2 \cdot \frac{20}{7} - \frac{19}{7} = \frac{40 - 19}{7} = \frac{21}{7} = 3$ ✓

## Key Properties

- **Best for**: Systems where one variable has coefficient 1 or -1
- **Single-variable reduction**: Converts 2-variable system to 1-variable equation
- **Exact solutions**: Maintains exact fractional answers (no rounding until final answer)
- **Fraction handling**: Can lead to more complex fractions than elimination method
- **Universal applicability**: Works for linear and nonlinear systems

## Strategic Considerations

**Choose substitution when:**
- One equation is already solved for a variable
- A variable has coefficient 1 (easy to isolate)
- System includes nonlinear equations (substitution often required)

**Avoid substitution when:**
- All coefficients are large integers (elimination may be cleaner)
- Both equations would require complex solving for a variable

## Common Errors

**Error 1**: Forgetting to substitute everywhere
```
Wrong: 3x + 2y = 16 with y = 2x - 1
       3x + y = 16  [only substituted once!]
Right: 3x + 2(2x - 1) = 16
```

**Error 2**: Sign errors in distribution
```
Wrong: 2(11 - 3y) - y = 22 - 3y - y
Right: 2(11 - 3y) - y = 22 - 6y - y
```

**Error 3**: Forgetting to back-substitute
```
Finding x = 3 and stopping
Must find y by substituting x = 3 back into one equation
```

## Relations

- `[[Elimination_Method]]` - alternative technique for solving systems by adding/subtracting equations
- `[[System_of_Linear_Equations]]` - the type of problem substitution solves
- `[[Nonlinear_Systems]]` - substitution is primary method for systems with quadratics or other nonlinear equations
- `[[Solving_Equations]]` - substitution uses single-variable equation solving as key step
- `[[Consistent_vs_Inconsistent_Systems]]` - substitution reveals whether system has solutions (0 = contradiction means inconsistent)
