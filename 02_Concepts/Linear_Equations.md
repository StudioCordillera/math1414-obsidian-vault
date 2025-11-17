---
layout: concept
title: Linear Equations
topic: Systems & Matrices
type: Definition
status: stable
importance: critical
tags:
- concept/equations
- concept/algebra
- chapter1
- foundation
- linear
sources:
- MillerGerken2023
source_refs:
- Miller & Gerken §1.1 p.86-92
relations:
  broader:
  - '[[Equations]]'
  narrower:
  - '[[Linear_Equations_Two_Variables]]'
  depends_on:
  - '[[Real_Number_System]]'
  - '[[Equality_Properties]]'
  related:
  - '[[Quadratic_Equations]]'
  - '[[Linear_Functions]]'
  used_in:
  - '[[Systems_of_Equations]]'
  - '[[Linear_Programming]]'
review:
  next: 2025-11-19
  cadence: monthly
created: 2025-10-19
updated: 2025-11-16
qa_certified: true
qa_date: 2025-11-16
qa_migration: v2.0
narrower:
- '[[Equation_Types]]'
- '[[Literal_Equations]]'
defines:
- '[[Inequality_Properties]]'
- '[[Number_Line_Graphing]]'
---
# Linear Equations (One Variable)

## Definition

A **linear equation in one variable** is an equation that can be written in the form:

```
ax + b = 0
```

where:
- **x** is the variable
- **a** and **b** are real number constants
- **a ≠ 0** (if a = 0, equation becomes 0 = -b, which is not linear)

### Key Characteristics

**1. Degree**: The variable has degree (exponent) of 1
- x¹ (or just x) appears
- x² , x³, √x, 1/x, etc. do NOT appear

**2. One Solution**: Linear equations have exactly ONE solution (when a ≠ 0)

**3. Straight Line**: Graph is a straight line (when extended to two variables)

## Standard Form

```
ax + b = 0
```

**Examples in Standard Form**:
- 2x + 7 = 0
- -3x - 5 = 0
- ½x + 4 = 0
- x - 9 = 0

## General Forms

Linear equations appear in many equivalent forms:

**Form 1**: Two expressions equal
```
2x + 5 = 3x - 1
```

**Form 2**: Multiple terms on both sides
```
3(x - 4) + 2 = 5x - 7
```

**Form 3**: Fractions involved
```
(x/3) + 2 = (x-1)/2
```

All can be simplified to standard form ax + b = 0

## Solution

The **solution** (or root) is the value of x that makes the equation true.

**Finding Solution from Standard Form**:
```
ax + b = 0
ax = -b
x = -b/a  (the unique solution)
```

**Example**:
```
3x + 12 = 0
3x = -12
x = -4
```

## Standard Solution Method

**Step-by-Step Process**:

**Step 1**: Clear fractions/decimals (if present)
- Multiply entire equation by LCD or power of 10

**Step 2**: Clear parentheses
- Use distributive property
- Be careful with negative signs

**Step 3**: Combine like terms
- On each side separately
- Simplify expressions

**Step 4**: Collect variable terms on one side
- Usually move to left side
- Move constants to other side

**Step 5**: Isolate variable
- Divide by coefficient of variable

**Step 6**: Check solution
- Substitute back into ORIGINAL equation

### Example: Complete Solution

**Solve**: 3(2x - 4) - 5 = 2x + 7

```
Step 1: No fractions to clear

Step 2: Distribute
6x - 12 - 5 = 2x + 7
6x - 17 = 2x + 7

Step 3: Already combined

Step 4: Collect variables (subtract 2x from both sides)
4x - 17 = 7

Step 5: Isolate x
4x = 24
x = 6

Step 6: Check in original
3(2(6) - 4) - 5 = 2(6) + 7
3(12 - 4) - 5 = 12 + 7
3(8) - 5 = 19
24 - 5 = 19
19 = 19 ✓
```

## Equality Properties (Foundation)

Linear equations are solved using these fundamental properties:

**Addition Property of Equality**:
```
If a = b, then a + c = b + c
```
*Can add (or subtract) same value to both sides*

**Multiplication Property of Equality**:
```
If a = b, then ac = bc  (where c ≠ 0)
```
*Can multiply (or divide) both sides by same nonzero value*

**See**: [[Equality_Properties]] for detailed treatment

## Special Cases

### Case 1: Identity (Infinitely Many Solutions)

An **identity** is true for ALL values of the variable.

**Recognition**: Variables cancel, leaving true statement
```
Example: 2(x + 3) = 2x + 6
         2x + 6 = 2x + 6
         0 = 0 ✓ (always true)

Solution: All real numbers (ℝ or (-∞, ∞))
```

### Case 2: Contradiction (No Solution)

A **contradiction** is never true for any value.

**Recognition**: Variables cancel, leaving false statement
```
Example: x + 5 = x + 3
         5 = 3 ✗ (never true)

Solution: Empty set (∅ or { })
```

### Case 3: Conditional Equation (One Solution)

A **conditional equation** is true for specific value(s) only.

**Recognition**: Can isolate variable to get one value
```
Example: 2x + 1 = 7
         x = 3 (true only when x = 3)

Solution: {3}
```

**Most linear equations are conditional**

## Common Patterns

**Pattern 1**: No constant term
```
ax = 0
Solution: x = 0
```

**Pattern 2**: No variable term (contradiction or identity)
```
0·x + b = 0
If b = 0: Identity (all real numbers)
If b ≠ 0: Contradiction (no solution)
```

**Pattern 3**: Fractions with LCD
```
x/2 + x/3 = 5
LCD = 6: 3x + 2x = 30
         5x = 30
         x = 6
```

## Applications

Linear equations model countless real-world situations:

**1. Simple Interest**: A = P(1 + rt)

**2. Distance-Rate-Time**: d = rt

**3. Mixture Problems**: Concentration equations

**4. Consecutive Integers**: n, n+1, n+2

**5. Geometry**: Perimeter, area with unknowns

**6. Finance**: Cost, revenue, profit relationships

**See**: [[01_Course/Textbook/Chapter1_Equations_Inequalities|Chapter 1.2]] for applications

## Visual Representation

**Number Line Solution**:
- Single point where x = solution value
- Contrasts with inequalities (intervals)

**Graph (in xy-plane)**:
- Linear equation in two variables (ax + by = c) graphs as line
- One-variable solution is x-intercept when y = 0

## Common Student Errors

**Error 1**: Distribution mistakes
```
❌ 2(x - 3) = 2x - 3  (forgot to distribute to -3)
✓ 2(x - 3) = 2x - 6
```

**Error 2**: Sign errors when moving terms
```
❌ 3x + 5 = 11, so 3x = 11 + 5 (wrong sign)
✓ 3x + 5 = 11, so 3x = 11 - 5 = 6
```

**Error 3**: Dividing only one term
```
❌ (2x + 4)/2 = x + 4 (only divided 2x)
✓ (2x + 4)/2 = x + 2 (divide both terms)
```

**Error 4**: Not checking solution
```
Missing errors from previous steps
```

**Error 5**: Confusing identity with single solution
```
❌ Thinking "0 = 0" means "x = 0"
✓ "0 = 0" means all real numbers are solutions
```

## Comparison with Other Equation Types

| Type | Form | Solutions | Difficulty |
|------|------|-----------|------------|
| Linear | ax + b = 0 | Exactly 1 | Easiest |
| Quadratic | ax² + bx + c = 0 | 0, 1, or 2 | Medium |
| Cubic | ax³ + bx² + cx + d = 0 | 1, 2, or 3 | Harder |
| Radical | √(ax + b) = c | Check for extraneous | Medium |
| Rational | P(x)/Q(x) = c | Check domain | Medium |

**Linear equations are the foundation** - other types often reduce to linear equations

## Why "Linear"?

**Origin of Name**: From Latin *linearis* ("of a line")

**Geometric Meaning**: 
- In two variables (ax + by = c), graphs as straight line
- In one variable, solution is single point (0-dimensional line)
- Degree 1 → no curves, just straight

## Historical Context

- Ancient Babylonians (~2000 BCE) solved linear equations
- Egyptian Rhind Papyrus (~1650 BCE) contains linear problems
- Al-Khwarizmi (~820 CE) systematized algebraic solution methods
- Modern notation developed in 16th-17th century Europe

## Key Properties Summary

**1. Closure**: Linear equation + linear equation = linear equation

**2. Uniqueness**: Exactly one solution (unless identity or contradiction)

**3. Simplicity**: Solvable by elementary operations

**4. Universality**: Appears everywhere in mathematics and applications

## Summary

> A linear equation in one variable has the form ax + b = 0 (a ≠ 0) and is solved by isolating the variable using equality properties. Linear equations have exactly one solution (conditional), infinitely many solutions (identity), or no solution (contradiction). They are the foundation for all equation solving in algebra.

---

**See Also**:
- [[Equality_Properties]] - Foundation for solving
- [[Quadratic_Equations]] - Next level complexity
- [[Linear_Functions]] - Functional perspective
- [[Systems_of_Equations]] - Multiple linear equations
- [[Linear_Equations_Two_Variables]] - Extended to 2D

**Practice**: [[01_Course/Textbook/Chapter1_Equations_Inequalities]] - Section 1.1

**Source**: Chapter 1.1 - Miller & Gerken College Algebra & Trigonometry
