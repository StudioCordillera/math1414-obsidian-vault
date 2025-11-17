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

# Elimination Method

## Definition

The **elimination method** (also called the **addition method**) is a technique for solving systems of equations by adding or subtracting the equations to eliminate one variable. The resulting equation contains only one variable and can be solved directly.

**Formal Statement**: For a system of two linear equations in two variables:
$$\begin{cases} a_1x + b_1y = c_1 \\ a_2x + b_2y = c_2 \end{cases}$$

Multiply one or both equations by constants so that the coefficients of one variable are opposites, then add the equations to eliminate that variable.

**When to Use**: Most efficient when coefficients of a variable are the same, opposites, or simple multiples of each other.

## Mathematical Expression

**General Process**:
1. **Align** equations in standard form: $ax + by = c$
2. **Multiply** one or both equations to create opposite coefficients for one variable
3. **Add** equations to eliminate that variable
4. **Solve** the resulting single-variable equation
5. **Back-substitute** to find the other variable
6. **Check** solution in both original equations

**Key insight**: Adding equations with opposite coefficients ($3x$ and $-3x$) causes cancellation, leaving an equation in only one variable.

## Example 1: Ready-to-Eliminate

**Problem**: Solve using elimination:
$$\begin{cases} 2x + 3y = 13 \\ 2x - y = 5 \end{cases}$$

**Step 1**: Coefficients of $x$ are already the same (both 2)

**Step 2**: Subtract second equation from first to eliminate $x$
$$(2x + 3y) - (2x - y) = 13 - 5$$
$$4y = 8$$
$$y = 2$$

**Step 3**: Back-substitute $y = 2$ into first equation
$$2x + 3(2) = 13$$
$$2x + 6 = 13$$
$$2x = 7$$
$$x = \frac{7}{2}$$

**Solution**: $\left(\frac{7}{2}, 2\right)$ or $(3.5, 2)$

**Verification**:
- First: $2(3.5) + 3(2) = 7 + 6 = 13$ ✓
- Second: $2(3.5) - 2 = 7 - 2 = 5$ ✓

## Example 2: Multiply to Create Opposites

**Problem**: Solve using elimination:
$$\begin{cases} 3x + 4y = 10 \\ 5x - 2y = 8 \end{cases}$$

**Step 1**: Choose to eliminate $y$ (coefficients 4 and -2)

**Step 2**: Multiply second equation by 2 to get $-4y$
$$\begin{cases} 3x + 4y = 10 \\ 10x - 4y = 16 \end{cases}$$

**Step 3**: Add equations to eliminate $y$
$$(3x + 4y) + (10x - 4y) = 10 + 16$$
$$13x = 26$$
$$x = 2$$

**Step 4**: Back-substitute $x = 2$ into first equation
$$3(2) + 4y = 10$$
$$6 + 4y = 10$$
$$4y = 4$$
$$y = 1$$

**Solution**: $(2, 1)$

**Verification**:
- First: $3(2) + 4(1) = 6 + 4 = 10$ ✓
- Second: $5(2) - 2(1) = 10 - 2 = 8$ ✓

## Example 3: Multiply Both Equations

**Problem**: Solve using elimination:
$$\begin{cases} 2x + 3y = 7 \\ 3x + 5y = 12 \end{cases}$$

**Step 1**: Eliminate $x$ by finding LCM of coefficients (2 and 3) = 6

**Step 2**: Multiply first equation by 3, second by -2
$$\begin{cases} 6x + 9y = 21 \\ -6x - 10y = -24 \end{cases}$$

**Step 3**: Add equations
$$(6x + 9y) + (-6x - 10y) = 21 - 24$$
$$-y = -3$$
$$y = 3$$

**Step 4**: Back-substitute $y = 3$ into first original equation
$$2x + 3(3) = 7$$
$$2x + 9 = 7$$
$$2x = -2$$
$$x = -1$$

**Solution**: $(-1, 3)$

**Verification**:
- First: $2(-1) + 3(3) = -2 + 9 = 7$ ✓
- Second: $3(-1) + 5(3) = -3 + 15 = 12$ ✓

## Key Properties

- **Best for**: Systems with integer coefficients or when variables have same/opposite coefficients
- **Variable cancellation**: Direct elimination leaves one equation in one variable
- **Fewer fractions**: Often avoids complex fractions compared to substitution
- **Symmetric approach**: Either variable can be eliminated first (your choice)
- **Reveals inconsistency**: If elimination gives $0 = k$ (where $k \neq 0$), system is inconsistent

## Strategic Considerations

**Choose elimination when:**
- Coefficients are aligned (same, opposite, or simple multiples)
- Both equations are in standard form
- You want to avoid fractions early in the process

**Multiplication strategy:**
- Choose variable with simplest coefficient relationship
- Multiply to create **opposite** coefficients (one positive, one negative)
- Use LCM of coefficients for smallest multipliers

## Common Errors

**Error 1**: Forgetting to distribute multiplier
```
Wrong: 2 × (3x + 4y = 10) → 6x + 4y = 20
Right: 2 × (3x + 4y = 10) → 6x + 8y = 20
```

**Error 2**: Sign errors when subtracting
```
Wrong: (2x + 3y) - (2x - y) = 2x + 3y - 2x - y
Right: (2x + 3y) - (2x - y) = 2x + 3y - 2x + y = 4y
```

**Error 3**: Multiplying only one side of equation
```
Wrong: 2 × (3x + 4y) = 10 → 6x + 8y = 10
Right: 2 × (3x + 4y = 10) → 6x + 8y = 20
```

## Relations

- `[[Substitution_Method]]` - alternative technique using variable replacement
- `[[System_of_Linear_Equations]]` - the type of problem elimination solves
- `[[Three_Variable_Systems]]` - elimination extends to 3×3 systems
- `[[Linear_Combinations]]` - elimination is based on adding scalar multiples of equations
- `[[Inconsistent_System]]` - elimination reveals inconsistency when $0 = k$ with $k \neq 0$
