---
layout: concept
title: Radical Equations
topic: Equations & Inequalities
type: Method
status: stable
importance: high
tags:
- concept/algebra
- concept/equations
- chapter-1
- solving-equations
- radicals
sources:
- miller-gerken-2ed
source_refs:
- Miller & Gerken §1.6 p.128-134
relations:
  broader:
  - '[[Equations]]'
  - '[[Solving_Techniques]]'
  narrower:
  - Square Root Method
  - Higher-Order Roots
  depends_on:
  - '[[Radical_Properties]]'
  - '[[Exponent_Properties]]'
  - '[[Quadratic_Equations]]'
  related:
  - '[[Extraneous_Solutions]]'
  - '[[Square_Root_Property]]'
  - '[[Domain_Restrictions]]'
  used_in:
  - '[[Distance_Formula]]'
  - '[[Pythagorean_Theorem]]'
  - '[[Function_Composition]]'
review:
  last: 2025-10-19
  next: 2025-10-26
  interval: 7 days
created: 2025-10-19
updated: 2025-10-19
qa_certified: true
qa_date: 2025-11-16
qa_migration: v2.0
related:
- '[[Equation_Types]]'
defines:
- '[[Radical_Properties]]'
---
# Radical Equations

## Definition

**Radical equations** are equations containing variables under a radical symbol (√, ³√, etc.). Solutions require eliminating radicals by raising both sides to appropriate powers.

**Standard Forms**:
```
√(expression) = value
³√(expression) = value
Expression with multiple radicals
```

**Key Characteristic**: Variable appears inside a radical (under the root symbol)

**Critical Warning**: Raising both sides to a power can introduce extraneous solutions—checking is MANDATORY.

---

## Solution Strategy: Isolate and Eliminate

**Core Process**:
```
1. Isolate radical on one side
2. Raise both sides to power matching radical index
3. Solve resulting equation
4. CHECK all solutions in original equation
5. State solution set (reject extraneous solutions)
```

**Why Check is Essential**: 
- Squaring both sides is NOT reversible
- Can introduce solutions that don't satisfy original
- Example: x = 3 AND x = -3 both give x² = 9, but only one may be valid in original

---

## Type 1: Single Square Root

### Process
```
1. Isolate √(expression)
2. Square both sides
3. Solve resulting equation
4. CHECK in original equation
```

### Example 1: Basic Radical Equation
**Solve**: √(2x + 3) = 5

```
Step 1: Radical already isolated

Step 2: Square both sides
(√(2x + 3))² = 5²
2x + 3 = 25

Step 3: Solve
2x = 22
x = 11

Step 4: CHECK in original
√(2(11) + 3) = √25 = 5 ✓

Solution: x = 11
```

### Example 2: Isolate First
**Solve**: √(x + 7) - 2 = 3

```
Step 1: Isolate radical
√(x + 7) = 5

Step 2: Square both sides
x + 7 = 25

Step 3: Solve
x = 18

Step 4: CHECK
√(18 + 7) - 2 = √25 - 2 = 5 - 2 = 3 ✓

Solution: x = 18
```

### Example 3: Leads to Quadratic
**Solve**: √(x + 5) = x - 1

```
Step 1: Radical isolated

Step 2: Square both sides
(√(x + 5))² = (x - 1)²
x + 5 = x² - 2x + 1

Step 3: Solve quadratic
0 = x² - 3x - 4
0 = (x - 4)(x + 1)
x = 4 or x = -1

Step 4: CHECK both solutions
For x = 4: √(4 + 5) = 4 - 1 → √9 = 3 → 3 = 3 ✓
For x = -1: √(-1 + 5) = -1 - 1 → √4 = -2 → 2 = -2 ✗

Solution: x = 4 only
(x = -1 is EXTRANEOUS)
```

### Example 4: No Solution Case
**Solve**: √(3x - 2) = -4

```
Step 1: Recognize impossibility
Principal square root is ALWAYS ≥ 0
Cannot equal negative number

Solution: ∅ (no solution)

Even if we continued:
3x - 2 = 16 → x = 6
CHECK: √(3(6) - 2) = √16 = 4 ≠ -4 ✗
```

---

## Type 2: Multiple Radicals on Same Side

### Process
```
1. Isolate one radical
2. Square both sides
3. If radical remains, isolate it and square again
4. Solve resulting equation
5. CHECK all solutions
```

### Example 1: Two Radicals
**Solve**: √(x + 4) + √(x - 1) = 5

```
Step 1: Isolate one radical
√(x + 4) = 5 - √(x - 1)

Step 2: Square both sides
(√(x + 4))² = (5 - √(x - 1))²
x + 4 = 25 - 10√(x - 1) + (x - 1)

Simplify:
x + 4 = 24 + x - 10√(x - 1)
4 = 24 - 10√(x - 1)
-20 = -10√(x - 1)
2 = √(x - 1)

Step 3: Square again
4 = x - 1
x = 5

Step 4: CHECK
√(5 + 4) + √(5 - 1) = √9 + √4 = 3 + 2 = 5 ✓

Solution: x = 5
```

### Example 2: Radicals on Both Sides
**Solve**: √(3x + 1) = √(x + 5)

```
Step 1: Square both sides (equal radicals)
3x + 1 = x + 5

Step 2: Solve
2x = 4
x = 2

Step 3: CHECK
√(3(2) + 1) = √(2 + 5)
√7 = √7 ✓

Solution: x = 2
```

---

## Type 3: Higher-Order Roots (Cube Roots, etc.)

### Process
```
1. Isolate radical
2. Raise both sides to power matching index
3. Solve resulting equation
4. CHECK in original (less likely to have extraneous, but still check)
```

### Example 1: Cube Root
**Solve**: ³√(2x - 1) = 3

```
Step 1: Radical isolated

Step 2: Cube both sides
(³√(2x - 1))³ = 3³
2x - 1 = 27

Step 3: Solve
2x = 28
x = 14

Step 4: CHECK
³√(2(14) - 1) = ³√27 = 3 ✓

Solution: x = 14
```

### Example 2: Fourth Root
**Solve**: ⁴√(3x + 5) + 2 = 5

```
Step 1: Isolate
⁴√(3x + 5) = 3

Step 2: Raise to 4th power
3x + 5 = 81

Step 3: Solve
3x = 76
x = 76/3

Step 4: CHECK
⁴√(3(76/3) + 5) + 2 = ⁴√81 + 2 = 3 + 2 = 5 ✓

Solution: x = 76/3
```

---

## Type 4: Radical Equations with Other Terms

### Example 1: Variable on Both Sides
**Solve**: √(x + 12) = x

```
Step 1: Isolate (already done)

Step 2: Square
x + 12 = x²

Step 3: Rearrange and solve
0 = x² - x - 12
0 = (x - 4)(x + 3)
x = 4 or x = -3

Step 4: CHECK both
For x = 4: √(4 + 12) = 4 → √16 = 4 → 4 = 4 ✓
For x = -3: √(-3 + 12) = -3 → √9 = -3 → 3 = -3 ✗

Solution: x = 4
```

### Example 2: Complex Isolation
**Solve**: √(2x + 3) = x - 3

```
Step 1: Already isolated

Step 2: Square
2x + 3 = (x - 3)²
2x + 3 = x² - 6x + 9

Step 3: Solve
0 = x² - 8x + 6

Using quadratic formula:
x = [8 ± √(64 - 24)]/2 = [8 ± √40]/2 = [8 ± 2√10]/2 = 4 ± √10

x ≈ 7.162 or x ≈ 0.838

Step 4: CHECK both
For x = 4 + √10 ≈ 7.162:
√(2(7.162) + 3) ≈ √17.324 ≈ 4.162
x - 3 ≈ 4.162 ✓

For x = 4 - √10 ≈ 0.838:
√(2(0.838) + 3) ≈ √4.676 ≈ 2.162
x - 3 ≈ -2.162 ✗ (different sign!)

Solution: x = 4 + √10 only
```

---

## Type 5: Equations with Radical Expressions

### Example: Radical in Denominator
**Solve**: 6/√x = √x

```
Step 1: Clear fraction
6/√x · √x = √x · √x
6 = (√x)²
6 = x

Step 2: CHECK
6/√6 = √6
6/√6 = 6/√6 ✓

Or: 6/√6 = 6√6/6 = √6 ✓

Solution: x = 6
```

---

## Extraneous Solutions in Detail

**Why They Occur**:
1. **Squaring creates symmetry**: x = 3 and x = -3 both give x² = 9
2. **Original may be one-directional**: √x = 3 only accepts x = 3
3. **Direction matters**: √x = -3 has no solution (principal root ≥ 0)

### Example Demonstrating Why
```
Original: √x = -2
This has NO solution (√x ≥ 0 always)

But if we square: x = 4
And "check" algebraically: √4 = 2, not -2

The squaring operation lost the sign information!
```

### Pattern Recognition for Extraneous
**Likely extraneous when:**
- Solution makes radicand negative (for even index)
- Solution gives negative where principal root needed
- Sign mismatch after substitution

---

## Domain Considerations

**Before Solving**:
- Even roots: radicand must be ≥ 0
- Odd roots: radicand can be any real number

**Example: Find Domain First**:
```
Equation: √(x - 3) = 5

Domain of √(x - 3): x - 3 ≥ 0, so x ≥ 3

Solution: x = 28 (after squaring and solving)

Check domain: 28 ≥ 3 ✓
```

---

## Common Errors and How to Avoid Them

### Error 1: Not Isolating Radical First
```
Wrong approach: √(x + 1) + 2 = 5
             Square: x + 1 + 4 = 25  ✗

Correct: Isolate first
         √(x + 1) = 3
         Then square: x + 1 = 9  ✓
```

### Error 2: Squaring Incorrectly
```
Wrong: (a + √b)² = a² + b  ✗

Correct: (a + √b)² = a² + 2a√b + b  ✓
Must use (a + b)² = a² + 2ab + b² pattern
```

### Error 3: Not Checking Solutions
```
Problem: Accept all solutions from squared equation
Fix: ALWAYS substitute back into ORIGINAL equation
```

### Error 4: Checking Algebraically Instead of Numerically
```
Problem: Algebraic manipulation might preserve the error
Fix: Substitute actual numbers, evaluate both sides
```

### Error 5: Forgetting Principal Root
```
Problem: √9 = ±3  ✗
Correct: √9 = 3 only (principal root)
         x² = 9 gives x = ±3, but √9 = 3
```

---

## Special Cases and Patterns

### Case 1: Both Sides Have Same Radical
```
If √A = √B, then A = B (square both sides)
Example: √(2x + 1) = √(x + 5)
         2x + 1 = x + 5
         x = 4
```

### Case 2: Radical Equals Itself
```
√(expression) = √(expression) is identity
Example: √(x² + 1) = √(x² + 1)
         All values where x² + 1 ≥ 0
         Domain: all real numbers
```

### Case 3: Radical Equals Zero
```
√A = 0 means A = 0
Example: √(x - 5) = 0 → x = 5
```

---

## Applications

### 1. **Distance Problems**
```
Distance formula: d = √[(x₂ - x₁)² + (y₂ - y₁)²]

If distance is known, solve radical equation:
√[(x - 2)² + (y - 3)²] = 5
```

### 2. **Pythagorean Theorem**
```
c = √(a² + b²)

Given c and one leg, find other:
10 = √(6² + b²)
100 = 36 + b²
b = 8
```

### 3. **Velocity Problems**
```
Escape velocity: v = √(2gR)
Given v, solve for R
```

### 4. **Pendulum Period**
```
T = 2π√(L/g)
Given T, solve for length L
```

---

## Practice Problems

### Level 1: Basic Square Roots
1. Solve: √(x + 5) = 4
2. Solve: √(3x - 2) = 7
3. Solve: √(x - 1) + 3 = 8

### Level 2: Leads to Quadratic
4. Solve: √(x + 3) = x - 3
5. Solve: √(2x + 1) = x - 1
6. Solve: √(x + 12) = x

### Level 3: Multiple Radicals
7. Solve: √x + √(x - 5) = 5
8. Solve: √(x + 7) = √(2x + 1)
9. Solve: √(2x + 3) - √(x + 1) = 1

### Level 4: Higher-Order Roots
10. Solve: ³√(2x + 5) = 3
11. Solve: ⁴√(x + 1) = 2
12. Solve: ³√(x - 1) + 2 = 5

### Level 5: Complex
13. Solve: √(x + √x) = 2
14. Solve: x - 3√x - 4 = 0 [Hint: Let u = √x]
15. Solve: √(x + 2) - √(x - 3) = 1

### Challenge
16. Solve: √(x + 4) = x + 2
17. Solve for positive solution only: √(2x + 9) - √(x + 4) = 1
18. Solve: √(x + 6) + √(x + 1) = √(7x + 6)

---

## Summary

**Radical equations** are solved by eliminating radicals through raising to appropriate powers:

**Universal Strategy**:
1. **Isolate** one radical
2. **Raise** both sides to matching power
3. **Repeat** if radicals remain
4. **Solve** resulting equation
5. **CHECK** all solutions (MANDATORY)

**Critical Principles**:
- Squaring is NOT reversible → creates extraneous solutions
- Principal square root is always ≥ 0
- Odd roots allow negative radicands
- Check in ORIGINAL equation, not transformed

**Common Patterns**:
- Single radical → isolate, square, solve
- Multiple radicals → isolate one, square, repeat
- Higher-order roots → raise to matching index

**Extraneous Solutions**:
- Introduced by squaring operation
- MUST check every solution
- Reject those that don't satisfy original

**Key Insight**: The price of eliminating radicals (squaring) is possible extraneous solutions—checking is not optional, it's essential.

**Foundation For**: Distance formula applications, Pythagorean theorem problems, function analysis, calculus (derivatives of radical functions)

---

*Radical equations combine algebraic manipulation with careful verification. The power to eliminate radicals through exponentiation comes with the responsibility to verify that solutions are genuine, not artifacts of the transformation process.*
---
type: Definition
status: stable
importance: high
tags:
  - concept/definition
  - math/algebra
  - chapter-1/equations
  - radicals
  - equation-solving
sources:
  - miller-gerken-2025
source_refs:
  - "Miller & Gerken §1.6 p.128-132"
relations:
  broader:
    - "[[Equations]]"
  narrower:
    - "[[Square_Root_Equations]]"
    - "[[Cube_Root_Equations]]"
  depends_on:
    - "[[Radical_Properties]]"
    - "[[Power_Property_of_Equality]]"
    - "[[Domain_Restrictions]]"
  defines:
    - "[[Extraneous_Solutions]]"
  related:
    - "[[Rational_Equations]]"
    - "[[Quadratic_Equations]]"
  used_in:
    - "[[Pythagorean_Theorem_Applications]]"
    - "[[Distance_Formula_Problems]]"
review:
  last: 2025-10-19
  next: 2025-10-26
  interval: 7
created: 2025-10-19
updated: 2025-10-19
---

# Radical Equations

## Definition

A **radical equation** is an equation in which the variable appears inside a radical (under a root symbol). Solving radical equations requires isolating the radical and then raising both sides to the appropriate power to eliminate the radical, followed by checking for extraneous solutions.

### Standard Forms

**Square root equation**:
$$\sqrt{f(x)} = g(x)$$

**General radical equation**:
$$\sqrt[n]{f(x)} = g(x)$$

**Multiple radicals**:
$$\sqrt{f(x)} + \sqrt{g(x)} = k$$

### Critical Principle

**Power Property of Equality**: If $a = b$, then $a^n = b^n$ for any positive integer $n$.

**Danger**: Squaring (or raising to even powers) can introduce extraneous solutions, so **checking is mandatory**.

---

## Solution Method

### Universal Process for Radical Equations

#### Step 1: Isolate a Radical
Move one radical to one side of equation, everything else to the other side.

#### Step 2: Raise Both Sides to Appropriate Power
- Square root → square both sides
- Cube root → cube both sides
- nth root → raise to nth power

**Critical**: $(a + b)^2 \neq a^2 + b^2$ — must expand properly!

#### Step 3: Simplify and Solve
The radical should be eliminated. Solve resulting equation.

#### Step 4: If Radicals Remain, Repeat
For equations with multiple radicals, may need to repeat Steps 1-3.

#### Step 5: Check ALL Solutions (MANDATORY)
Substitute each solution into **original equation** to verify. Reject any that produce:
- Negative values under even roots
- False statements

---

## Examples

### Example 1: Basic Square Root Equation

**Solve**: $\sqrt{x + 7} = 4$

**Step 1** - Already isolated.

**Step 2** - Square both sides:
$$(\sqrt{x + 7})^2 = 4^2$$
$$x + 7 = 16$$

**Step 3** - Solve:
$$x = 9$$

**Step 4** - Check in original:
$$\sqrt{9 + 7} = \sqrt{16} = 4$$ ✓

**Solution**: $x = 9$

---

### Example 2: Variable on Both Sides

**Solve**: $\sqrt{3x + 1} = x - 1$

**Step 1** - Already isolated.

**Step 2** - Square both sides:
$$(\sqrt{3x + 1})^2 = (x - 1)^2$$
$$3x + 1 = x^2 - 2x + 1$$

**Step 3** - Rearrange to standard form:
$$0 = x^2 - 2x - 3x + 1 - 1$$
$$0 = x^2 - 5x$$
$$0 = x(x - 5)$$

**Solutions**: $x = 0$ or $x = 5$

**Step 5** - Check both:

**Check $x = 0$**:
$$\sqrt{3(0) + 1} = 0 - 1$$
$$\sqrt{1} = -1$$
$$1 = -1$$ ❌ **Extraneous!**

**Check $x = 5$**:
$$\sqrt{3(5) + 1} = 5 - 1$$
$$\sqrt{16} = 4$$
$$4 = 4$$ ✓

**Solution**: $x = 5$ only

---

### Example 3: Radical with Coefficient

**Solve**: $3\sqrt{x - 2} = 12$

**Step 1** - Isolate radical (divide by 3):
$$\sqrt{x - 2} = 4$$

**Step 2** - Square:
$$x - 2 = 16$$

**Step 3** - Solve:
$$x = 18$$

**Step 5** - Check:
$$3\sqrt{18 - 2} = 3\sqrt{16} = 3(4) = 12$$ ✓

**Solution**: $x = 18$

---

### Example 4: Two Radicals (Same Side)

**Solve**: $\sqrt{x + 5} + \sqrt{x} = 5$

**Step 1** - Isolate one radical:
$$\sqrt{x + 5} = 5 - \sqrt{x}$$

**Step 2** - Square both sides:
$$(\sqrt{x + 5})^2 = (5 - \sqrt{x})^2$$
$$x + 5 = 25 - 10\sqrt{x} + x$$

**Step 3** - Simplify (radical remains!):
$$5 = 25 - 10\sqrt{x}$$
$$10\sqrt{x} = 20$$
$$\sqrt{x} = 2$$

**Step 4** - Square again:
$$x = 4$$

**Step 5** - Check in original:
$$\sqrt{4 + 5} + \sqrt{4} = \sqrt{9} + 2 = 3 + 2 = 5$$ ✓

**Solution**: $x = 4$

---

### Example 5: Cube Root Equation

**Solve**: $\sqrt[3]{2x + 3} = 3$

**Step 1** - Already isolated.

**Step 2** - Cube both sides:
$$(\sqrt[3]{2x + 3})^3 = 3^3$$
$$2x + 3 = 27$$

**Step 3** - Solve:
$$2x = 24$$
$$x = 12$$

**Step 5** - Check:
$$\sqrt[3]{2(12) + 3} = \sqrt[3]{27} = 3$$ ✓

**Solution**: $x = 12$

**Note**: Odd roots typically don't produce extraneous solutions (can take odd roots of negative numbers).

---

### Example 6: Radical Equation Leading to Quadratic

**Solve**: $\sqrt{x^2 - 5} = x - 1$

**Step 1** - Already isolated.

**Step 2** - Square:
$$x^2 - 5 = (x - 1)^2$$
$$x^2 - 5 = x^2 - 2x + 1$$

**Step 3** - Simplify:
$$-5 = -2x + 1$$
$$-6 = -2x$$
$$x = 3$$

**Step 5** - Check:
$$\sqrt{3^2 - 5} = 3 - 1$$
$$\sqrt{4} = 2$$
$$2 = 2$$ ✓

**Solution**: $x = 3$

---

### Example 7: No Real Solution

**Solve**: $\sqrt{x - 5} = -3$

**Analysis**: Square root produces **non-negative** values only.

**Right side is negative**, so no real solution exists.

**Alternative verification**: Square both sides anyway:
$$x - 5 = 9$$
$$x = 14$$

**Check**: $\sqrt{14 - 5} = \sqrt{9} = 3 \neq -3$ ❌

**Solution**: No real solution (or $\emptyset$)

---

### Example 8: Two Radicals (Opposite Sides)

**Solve**: $\sqrt{2x + 5} = \sqrt{x + 7}$

**Step 1** - Radicals already on opposite sides.

**Step 2** - Square both sides:
$$2x + 5 = x + 7$$

**Step 3** - Solve:
$$x = 2$$

**Step 5** - Check:
$$\sqrt{2(2) + 5} = \sqrt{2 + 7}$$
$$\sqrt{9} = \sqrt{9}$$
$$3 = 3$$ ✓

**Solution**: $x = 2$

---

### Example 9: Radical with Absolute Value Result

**Solve**: $\sqrt{x^2} = 5$

**Method 1** - Recognize $\sqrt{x^2} = |x|$:
$$|x| = 5$$
$$x = \pm 5$$

**Method 2** - Square both sides:
$$x^2 = 25$$
$$x = \pm 5$$

**Check both**:
- $\sqrt{5^2} = \sqrt{25} = 5$ ✓
- $\sqrt{(-5)^2} = \sqrt{25} = 5$ ✓

**Solutions**: $x = 5$ or $x = -5$

---

### Example 10: Application - Pythagorean Theorem

**Problem**: A ladder 13 ft long leans against a wall. The base is 5 ft from the wall. How high up the wall does it reach?

**Setup**: $a^2 + b^2 = c^2$
$$5^2 + h^2 = 13^2$$
$$25 + h^2 = 169$$
$$h^2 = 144$$

**Solve**:
$$h = \sqrt{144} = 12$$

**Note**: Reject $h = -12$ (negative height meaningless in context).

**Answer**: 12 feet

---

## Applications

### 1. Distance Formula

**Distance between points** $(x_1, y_1)$ and $(x_2, y_2)$:
$$d = \sqrt{(x_2 - x_1)^2 + (y_2 - y_1)^2}$$

Often requires solving for coordinate when distance is known.

---

### 2. Pythagorean Theorem

$$a^2 + b^2 = c^2$$

Solving for a side: $a = \sqrt{c^2 - b^2}$

---

### 3. Free Fall

**Time to fall** from height $h$ (feet):
$$t = \sqrt{\frac{h}{16}}$$

**Solving for height**: $h = 16t^2$

---

### 4. Pendulum Period

**Period** of simple pendulum:
$$T = 2\pi\sqrt{\frac{L}{g}}$$

Solving for length $L$ requires squaring and rearranging.

---

### 5. Standard Deviation

$$s = \sqrt{\frac{\sum(x_i - \bar{x})^2}{n-1}}$$

Solving statistical problems may require radical equations.

---

### 6. Electric Current and Resistance

**Power formula**: $P = I^2R$

Solving for current: $I = \sqrt{\frac{P}{R}}$

---

## Common Misconceptions

### ❌ Misconception 1: Not Checking for Extraneous Solutions

**Error**: Accepting all algebraic solutions without verification.

**Example**: $\sqrt{x} = x - 2$ yields $x = 1, 4$, but $x = 1$ is extraneous.

**Correct**: **Always** check solutions in original equation. Squaring introduces invalid solutions.

---

### ❌ Misconception 2: Squaring Incorrectly

**Incorrect**: $(\sqrt{x} + 3)^2 = x + 9$

**Correct**: $(\sqrt{x} + 3)^2 = (\sqrt{x})^2 + 2(3)(\sqrt{x}) + 3^2 = x + 6\sqrt{x} + 9$

**Must expand** using $(a + b)^2 = a^2 + 2ab + b^2$!

---

### ❌ Misconception 3: Forgetting Absolute Value

**Incorrect**: $\sqrt{x^2} = x$

**Correct**: $\sqrt{x^2} = |x|$

**Example**: $\sqrt{(-3)^2} = \sqrt{9} = 3 = |-3|$, not $-3$

---

### ❌ Misconception 4: Assuming All Even Roots Have Two Solutions

**Problem**: $\sqrt{x} = 4$

**Incorrect**: $x = \pm 16$

**Correct**: $x = 16$ only

**Why**: The radical symbol $\sqrt{\ }$ denotes **principal (positive) square root**. Only when squaring an equation do both solutions emerge.

**Compare**:
- Solving $\sqrt{x} = 4$: Only $x = 16$
- Solving $x^2 = 16$: Both $x = \pm 4$

---

### ❌ Misconception 5: Isolating Incorrectly

**Incorrect approach**: $\sqrt{x} + 3 = 7$

Square immediately: $x + 9 = 49$ ❌

**Correct**: Isolate radical first:
$$\sqrt{x} = 4$$
Then square: $x = 16$ ✓

---

### ❌ Misconception 6: Negative Under Even Root

**Error**: Accepting solution that produces negative radicand.

**Example**: $\sqrt{x - 5} = 3$ giving $x = 14$ is valid.
But $\sqrt{x - 5} = 3$ giving $x = -4$ would be **invalid** (negative under square root).

**Check domain**: Radicand must be non-negative for even roots.

---

### ❌ Misconception 7: Not Repeating Process for Multiple Radicals

**Equation**: $\sqrt{x + 2} - \sqrt{x} = 1$

**Error**: Squaring once and expecting no radicals to remain.

**Correct**: 
1. Isolate one radical
2. Square
3. If radical remains, isolate again and square again
4. Check solutions

---

## Related Concepts

### Prerequisites
- [[Radical_Properties]] - Understanding radical operations
- [[Power_Property_of_Equality]] - Foundation for solving method
- [[Domain_Restrictions]] - Identifying valid solutions
- [[Quadratic_Equations]] - Often result after squaring

### Defined Concepts
- [[Extraneous_Solutions]] - Invalid solutions from squaring
- [[Principal_Square_Root]] - Positive root convention

### Related Equation Types
- [[Rational_Equations]] - Also require checking for extraneous solutions
- [[Absolute_Value_Equations]] - Similar squaring techniques

### Applications
- [[Pythagorean_Theorem_Applications]] - Right triangle problems
- [[Distance_Formula_Problems]] - Coordinate geometry
- [[Free_Fall_Problems]] - Physics applications

### Advanced Connections
- [[Complex_Numbers]] - Extends to even roots of negatives
- [[Rational_Exponents]] - Alternative representation

---

## Solution Strategy Summary

### When to Check Solutions

**Always check** in these situations:
1. Any equation involving even-index radicals (square roots, 4th roots, etc.)
2. After squaring (or raising to even power) both sides
3. When obtaining multiple solutions
4. Application problems (verify physical reasonability)

**Odd-index radicals** (cube roots, 5th roots) rarely produce extraneous solutions but checking is still good practice.

### Extraneous Solution Indicators

A solution is extraneous if:
- It produces negative value under even root
- It yields false statement in original equation
- It violates stated domain restrictions
- It's physically meaningless in application context

---

## Practice Problems

### Basic
1. Solve: $\sqrt{x} = 7$ → **Answer**: $x = 49$

2. Solve: $\sqrt{x + 3} = 5$ → **Answer**: $x = 22$

3. Solve: $\sqrt{2x - 1} = 3$ → **Answer**: $x = 5$

### Intermediate
4. Solve: $\sqrt{x + 7} = x - 5$ → **Answer**: $x = 9$ (check: $x = 2$ is extraneous)

5. Solve: $\sqrt{x} + 3 = x$ → **Answer**: $x = 4$ (check: $x = 1$ is extraneous... wait, let me recalculate)

Actually for $\sqrt{x} + 3 = x$:
- Isolate: $\sqrt{x} = x - 3$
- Square: $x = x^2 - 6x + 9$
- Rearrange: $x^2 - 7x + 9 = 0$
- Quadratic formula: $x = \frac{7 \pm \sqrt{49-36}}{2} = \frac{7 \pm \sqrt{13}}{2}$

Wait, that doesn't match. Let me redo:

For #5, if we have $\sqrt{x} + 3 = x$:
- $\sqrt{x} = x - 3$
- $x = (x-3)^2 = x^2 - 6x + 9$
- $0 = x^2 - 7x + 9$

This doesn't factor nicely. Let me use a simpler problem:

5. Solve: $\sqrt{x + 4} - x = -2$ → **Answer**: $x = 5$ (check: $x = 0$ extraneous)

6. Solve: $\sqrt{2x + 3} = \sqrt{x + 7}$ → **Answer**: $x = 4$

### Advanced
7. Solve: $\sqrt{x + 1} + \sqrt{x} = 2$ → **Answer**: $x = \frac{3}{4}$

8. Solve: $\sqrt[3]{3x - 2} = 4$ → **Answer**: $x = 22$

### Application
9. The diagonal of a rectangle is 10 cm, and one side is 6 cm. Find the other side. → **Answer**: 8 cm

10. Solve: $\sqrt{x^2 - 5x} = 6$ → **Answer**: $x = 9$ or $x = -4$

---

## Summary

**Radical equations** require eliminating radicals by raising both sides to appropriate powers, followed by **mandatory checking** for extraneous solutions. Squaring both sides can introduce invalid solutions that satisfy the squared equation but not the original.

**Critical steps**:
1. **Isolate** a radical
2. **Raise to power** (square for square root, cube for cube root, etc.)
3. **Solve** resulting equation
4. **Repeat** if radicals remain
5. **CHECK** all solutions in original equation

**Extraneous solutions** occur because:
- Squaring is not reversible: $a = b \Rightarrow a^2 = b^2$, but $a^2 = b^2 \not\Rightarrow a = b$
- Domain of radical function restricts valid inputs

**Application mastery**: Many geometry problems (Pythagorean Theorem, distance formula) and physics problems (free fall, pendulum) require solving radical equations.

**Key insight**: Checking is NOT optional—it's essential. Extraneous solutions are algebraically valid but violate the original equation's constraints.
