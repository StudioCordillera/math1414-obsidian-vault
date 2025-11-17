---
layout: concept
title: Rational Equations
topic: Equations & Inequalities
type: Method
status: stable
importance: high
tags:
- concept/algebra
- concept/equations
- chapter-1
- solving-equations
sources:
- miller-gerken-2ed
source_refs:
- Miller & Gerken §1.1 p.87-93
relations:
  broader:
  - '[[Equations]]'
  - '[[Solving_Techniques]]'
  narrower:
  - LCD Method
  - Cross-Multiplication
  depends_on:
  - '[[Rational_Expressions_Operations]]'
  - '[[Linear_Equations]]'
  - '[[Factoring_Strategies]]'
  - '[[Domain_Restrictions]]'
  related:
  - '[[Extraneous_Solutions]]'
  - '[[Rational_Functions]]'
  - '[[Proportion_Problems]]'
  used_in:
  - '[[Work_Problems]]'
  - '[[Rate_Problems]]'
  - '[[Mixture_Problems]]'
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
- '[[Distance_Rate_Time_Problems]]'
- '[[Domain_Restrictions]]'
- '[[Equation_Types]]'
- '[[Literal_Equations]]'
- '[[Mixture_Problems]]'
---
# Rational Equations

## Definition

**Rational equations** are equations containing one or more rational expressions (fractions with polynomials in numerator and/or denominator). Unlike rational expression operations, rational equations can be solved for specific values by eliminating fractions.

**Standard Form**:
```
Equation containing rational expressions: P(x)/Q(x) = R(x)/S(x) or similar
```

**Key Characteristic**: Contains an equals sign (=) with fractions involving variables

**Critical Distinction**:
- **Rational Expression**: (x + 1)/(x - 2) [simplify or operate]
- **Rational Equation**: (x + 1)/(x - 2) = 3 [solve for x]

---

## Solution Strategy: The LCD Method

**Core Principle**: Clear fractions by multiplying by LCD, then solve resulting equation

**Step-by-Step Process**:
```
1. Factor all denominators
2. Identify domain restrictions (denominators ≠ 0)
3. Find LCD of all denominators
4. Multiply ENTIRE equation by LCD
5. Solve resulting equation (usually linear or quadratic)
6. CHECK all solutions against restrictions
7. State solution set (reject extraneous solutions)
```

**Why Check?**: Multiplying by variable expression can introduce extraneous solutions

---

## Examples

### Example 1: Basic Rational Equation
**Solve**: 3/(x - 2) + 4/(x + 1) = 2

```
Step 1: Factor denominators (already factored)
Denominators: (x - 2), (x + 1)

Step 2: Domain restrictions
x ≠ 2, x ≠ -1

Step 3: Find LCD
LCD = (x - 2)(x + 1)

Step 4: Multiply entire equation by LCD
(x - 2)(x + 1)[3/(x - 2) + 4/(x + 1)] = (x - 2)(x + 1)(2)

Distribute:
(x - 2)(x + 1) · 3/(x - 2) + (x - 2)(x + 1) · 4/(x + 1) = 2(x - 2)(x + 1)

Simplify (fractions cancel):
3(x + 1) + 4(x - 2) = 2(x² - x - 2)

Step 5: Solve
3x + 3 + 4x - 8 = 2x² - 2x - 4
7x - 5 = 2x² - 2x - 4
0 = 2x² - 9x + 1

Using quadratic formula:
x = [9 ± √(81 - 8)]/4 = [9 ± √73]/4

x ≈ 4.39 or x ≈ 0.11

Step 6: Check against restrictions
Neither solution is 2 or -1, both valid ✓

Solution set: {(9 + √73)/4, (9 - √73)/4}
```

### Example 2: Solution That Creates Extraneous Root
**Solve**: 2/(x - 3) - 1/(x + 3) = 6/(x² - 9)

```
Step 1: Factor denominators
Note: x² - 9 = (x + 3)(x - 3)

Equation becomes:
2/(x - 3) - 1/(x + 3) = 6/[(x + 3)(x - 3)]

Step 2: Restrictions
x ≠ 3, x ≠ -3

Step 3: LCD = (x + 3)(x - 3)

Step 4: Multiply by LCD
(x + 3)(x - 3) · 2/(x - 3) - (x + 3)(x - 3) · 1/(x + 3) = 6

Simplify:
2(x + 3) - 1(x - 3) = 6

Step 5: Solve
2x + 6 - x + 3 = 6
x + 9 = 6
x = -3

Step 6: CHECK against restrictions
x = -3 is EXCLUDED from domain (makes denominator = 0)

Solution set: ∅ (no solution)
This is an EXTRANEOUS SOLUTION!
```

### Example 3: Multiple Fractions, Linear Result
**Solve**: 1/x + 2/(x + 1) = 3/(x + 1)

```
Step 1: Denominators: x, (x + 1)

Step 2: Restrictions: x ≠ 0, x ≠ -1

Step 3: LCD = x(x + 1)

Step 4: Multiply by LCD
x(x + 1) · 1/x + x(x + 1) · 2/(x + 1) = x(x + 1) · 3/(x + 1)

Simplify:
(x + 1) + 2x = 3x

Step 5: Solve
x + 1 + 2x = 3x
3x + 1 = 3x
1 = 0  [Contradiction!]

Step 6: Check
Since we get a contradiction, equation has no solution

Solution set: ∅
```

### Example 4: Quadratic Result
**Solve**: x/(x - 1) = (x + 2)/(x + 1)

```
Method 1: Cross-multiplication
x(x + 1) = (x + 2)(x - 1)
x² + x = x² + x - 2
x = x - 2
0 = -2  [Contradiction]

No solution: ∅

Method 2: LCD Method
LCD = (x - 1)(x + 1)
(x - 1)(x + 1) · x/(x - 1) = (x - 1)(x + 1) · (x + 2)/(x + 1)
x(x + 1) = (x + 2)(x - 1)
[Same result]

Restrictions: x ≠ 1, -1
```

### Example 5: Practical Problem
**Solve Work Problem**: 
Pipe A fills pool in 4 hours. Pipe B fills it in 6 hours. How long together?

```
Setup:
Rate of A: 1/4 pool per hour
Rate of B: 1/6 pool per hour
Let t = time to fill together

Equation:
(1/4)t + (1/6)t = 1 pool

Solve:
LCD = 12
12(1/4)t + 12(1/6)t = 12(1)
3t + 2t = 12
5t = 12
t = 12/5 = 2.4 hours

Check: (1/4)(2.4) + (1/6)(2.4) = 0.6 + 0.4 = 1 ✓

Answer: 2.4 hours (or 2 hours 24 minutes)
```

### Example 6: Complex Rational Equation
**Solve**: 3/(x² - 4) + 2/(x - 2) = 1/(x + 2)

```
Step 1: Factor
x² - 4 = (x + 2)(x - 2)

Equation:
3/[(x + 2)(x - 2)] + 2/(x - 2) = 1/(x + 2)

Step 2: Restrictions: x ≠ ±2

Step 3: LCD = (x + 2)(x - 2)

Step 4: Multiply by LCD
3 + 2(x + 2) = (x - 2)

Step 5: Solve
3 + 2x + 4 = x - 2
2x + 7 = x - 2
x = -9

Step 6: Check
x = -9 doesn't violate restrictions ✓

Verify in original:
LHS: 3/(81-4) + 2/(-9-2) = 3/77 - 2/11 = 3/77 - 14/77 = -11/77 = -1/7
RHS: 1/(-9+2) = 1/(-7) = -1/7 ✓

Solution: x = -9
```

---

## Special Technique: Cross-Multiplication

**When Applicable**: Single fraction on each side

**Form**: A/B = C/D

**Process**: A·D = B·C

### Example
**Solve**: (x + 3)/(x - 1) = (2x + 1)/(x + 2)

```
Cross-multiply:
(x + 3)(x + 2) = (2x + 1)(x - 1)

Expand:
x² + 5x + 6 = 2x² - x - 1

Rearrange:
0 = x² - 6x - 7

Factor:
0 = (x - 7)(x + 1)

Solutions: x = 7 or x = -1

Check restrictions (x ≠ 1, -2):
Both values valid ✓

Check in original:
For x = 7: (10/6) = (15/9) → 5/3 = 5/3 ✓
For x = -1: (2/-2) = (-1/1) → -1 = -1 ✓

Solution set: {-1, 7}
```

---

## Extraneous Solutions

**Definition**: Values that satisfy the transformed equation but NOT the original equation

**Causes**:
1. Value makes original denominator zero
2. Introduced when multiplying by variable expression
3. Result of algebraic operations that aren't reversible

**Why They Occur**:
- Multiplying both sides by (x - a) when x = a makes denominators zero
- This operation is valid only when (x - a) ≠ 0
- Solution must be checked against original domain restrictions

### Example Showing Why Checking is Essential
```
Original: 2/x + 3 = (2 + 3x)/x

Multiply by x:
2 + 3x = 2 + 3x

Result: 0 = 0 (identity!)

Seems like all real numbers work...
BUT x = 0 makes original equation undefined

Solution: All real numbers EXCEPT x = 0
Written as: (-∞, 0) ∪ (0, ∞) or ℝ \ {0}
```

---

## Common Types and Applications

### Type 1: Proportion Problems
```
Form: a/b = c/d
Technique: Cross-multiply
Example: If 3 cups flour makes 24 cookies, how many cups for 40 cookies?
3/24 = x/40 → 24x = 120 → x = 5 cups
```

### Type 2: Work Problems
```
Form: (rate₁)t + (rate₂)t = 1 job
Key: Combined rates add
Example: A does job in 5 hr, B in 3 hr. Together?
(1/5)t + (1/3)t = 1 → t = 15/8 hr
```

### Type 3: Distance-Rate-Time Problems
```
Form: d = rt, so t = d/r
Example: Upstream vs downstream with current
d/(r - c) + d/(r + c) = total time
```

### Type 4: Mixture/Concentration Problems
```
Form: (conc₁)(vol₁) + (conc₂)(vol₂) = (conc_final)(vol_total)
Often leads to rational equation after setup
```

---

## Common Errors and How to Avoid Them

### Error 1: Not Checking Solutions
```
Problem: Accept x = 2 when (x - 2) is in denominator
Fix: ALWAYS check against domain restrictions from step 2
```

### Error 2: Forgetting to Distribute LCD
```
Wrong: LCD(A/B + C/D) = LCD·A/B + C/D  ✗
Correct: LCD(A/B + C/D) = LCD·A/B + LCD·C/D  ✓
Must distribute to EVERY term
```

### Error 3: Algebraic Errors After Clearing Fractions
```
Problem: Errors in solving resulting linear/quadratic equation
Fix: Work carefully, check algebra
```

### Error 4: Incomplete Factoring
```
Problem: Missing factors in LCD
Wrong LCD: x(x - 2) when should be x(x - 2)(x + 2)
Fix: Factor ALL denominators completely
```

### Error 5: Sign Errors
```
Problem: 2/(x-3) = 2/(3-x)?  NO!
Correct: 2/(x-3) = -2/(3-x)  ✓
Remember: (a - b) = -(b - a)
```

---

## Decision Tree: Solving Strategy

```
Is it a rational EQUATION?
│
├─ YES: Continue
│
├─ Only one fraction each side?
│   ├─ YES → Use cross-multiplication
│   └─ NO → Use LCD method
│
└─ LCD Method Steps:
    ├─ 1. Factor all denominators
    ├─ 2. Note restrictions
    ├─ 3. Find LCD
    ├─ 4. Multiply by LCD
    ├─ 5. Solve resulting equation
    └─ 6. CHECK and state solution set
```

---

## Practice Problems

### Level 1: Basic Equations
1. Solve: x/3 + x/4 = 7
2. Solve: 2/x = 5/(x + 3)
3. Solve: (x + 1)/2 = (x - 1)/3

### Level 2: Intermediate
4. Solve: 3/(x - 2) + 2/(x + 1) = 1
5. Solve: x/(x - 3) = 4/(x - 3) + 1
6. Solve: 2/x - 3/(x + 2) = 1/(x² + 2x)

### Level 3: Extraneous Solutions
7. Solve: 3/(x - 2) = 2/(x - 2) + 1 [Check carefully!]
8. Solve: 2x/(x - 1) = 2 + 2/(x - 1)
9. Solve: 1/(x - 3) + 1/(x + 3) = 6/(x² - 9)

### Level 4: Applications
10. One pipe fills tank in 6 hours, another in 4 hours. How long together?
11. Cyclist rides 15 miles with wind (faster), 15 miles against (slower). Wind adds/subtracts 3 mph. Total time 2 hours. Find speed in still air.
12. Solution is 20% acid. How much pure acid to add to 10 L to make 30%?

### Challenge
13. Solve: 1/x + 1/(x + 1) = 1/((x)(x + 1))
14. Solve: (x + 2)/(x - 1) - (x - 2)/(x + 1) = 4/(x² - 1)

---

## Summary

**Rational equations** are solved by clearing fractions using the LCD:

**Key Steps**:
1. Factor all denominators
2. Note domain restrictions (x ≠ values making denominators zero)
3. Find LCD
4. Multiply entire equation by LCD
5. Solve resulting equation (often linear or quadratic)
6. **CHECK** solutions against restrictions

**Critical Awareness**:
- **Checking is MANDATORY**, not optional
- Extraneous solutions occur when values violate original domain
- Domain from ORIGINAL equation, not transformed version

**Special Cases**:
- Cross-multiplication when single fraction each side
- Work problems: rates add when working together
- Proportion problems: set up as a/b = c/d

**Common Results**:
- One solution (most common)
- Two solutions (from quadratic)
- No solution (contradiction or all solutions extraneous)
- Infinitely many (rare, usually identity)

**Essential Skill**: Recognizing when solution is extraneous—must check every solution!

**Foundation For**: Rational functions, related rates (calculus), optimization problems, real-world modeling

---

*Rational equations combine fraction operations with equation-solving techniques. The LCD method transforms complex rational equations into simpler polynomial equations, but careful checking ensures only valid solutions are accepted.*
---
type: Definition
status: stable
importance: high
tags:
  - concept/definition
  - math/algebra
  - chapter-1/equations
  - rational-expressions
  - equation-solving
sources:
  - miller-gerken-2025
source_refs:
  - "Miller & Gerken §1.1 p.92-96"
relations:
  broader:
    - "[[Equations]]"
  narrower:
    - "[[Proportion_Equations]]"
  depends_on:
    - "[[Linear_Equations]]"
    - "[[Rational_Expressions_Operations]]"
    - "[[Domain_Restrictions]]"
    - "[[LCD_Technique]]"
  defines:
    - "[[Extraneous_Solutions]]"
  related:
    - "[[Radical_Equations]]"
    - "[[Factoring_Strategies]]"
  used_in:
    - "[[Work_Rate_Problems]]"
    - "[[Mixture_Problems]]"
    - "[[Distance_Rate_Time_Problems]]"
review:
  last: 2025-10-19
  next: 2025-10-26
  interval: 7
created: 2025-10-19
updated: 2025-10-19
---

# Rational Equations

## Definition

A **rational equation** is an equation containing one or more **rational expressions** (fractions with polynomial numerators and denominators). Solving rational equations requires eliminating fractions by multiplying through by the LCD (Least Common Denominator), then solving the resulting polynomial equation.

### Standard Form

$$\frac{P_1(x)}{Q_1(x)} = \frac{P_2(x)}{Q_2(x)}$$

or more generally:

$$\frac{P_1(x)}{Q_1(x)} \pm \frac{P_2(x)}{Q_2(x)} \pm \cdots = k$$

where $P_i(x)$ and $Q_i(x)$ are polynomials, $Q_i(x) \neq 0$.

### Critical Concepts

**Domain restrictions**: Values that make any denominator zero are excluded from the solution set.

**Extraneous solutions**: Values that emerge during solving but violate domain restrictions. Must be checked and rejected.

**LCD (Least Common Denominator)**: The smallest expression that all denominators divide into evenly.

---

## Solution Method

### Universal Process for Rational Equations

#### Step 1: Identify Domain Restrictions
Set each denominator ≠ 0 and solve for excluded values.

**Example**: For $\frac{1}{x-3} = \frac{2}{x+1}$, exclude $x = 3$ and $x = -1$.

#### Step 2: Find the LCD
Factor all denominators, then construct LCD using highest power of each factor.

**Example**: 
- Denominators: $x-3$, $x+1$
- LCD: $(x-3)(x+1)$

#### Step 3: Multiply Both Sides by LCD
This eliminates all fractions, creating a polynomial equation.

**Critical**: Multiply EVERY term, including stand-alone numbers.

#### Step 4: Solve the Resulting Equation
Use appropriate technique (linear, quadratic, factoring).

#### Step 5: Check Solutions
**Mandatory**: Verify solutions don't create zero denominators (extraneous solutions).

---

## Examples

### Example 1: Simple Rational Equation

**Solve**: $\frac{1}{x} + \frac{2}{3x} = \frac{5}{6}$

**Step 1** - Domain: $x \neq 0$

**Step 2** - LCD: $6x$

**Step 3** - Multiply by LCD:
$$6x \cdot \frac{1}{x} + 6x \cdot \frac{2}{3x} = 6x \cdot \frac{5}{6}$$
$$6 + 4 = 5x$$
$$10 = 5x$$

**Step 4** - Solve:
$$x = 2$$

**Step 5** - Check: $x = 2$ doesn't make any denominator zero ✓

**Verification**:
$$\frac{1}{2} + \frac{2}{6} = \frac{1}{2} + \frac{1}{3} = \frac{5}{6}$$ ✓

---

### Example 2: Equation with Variable in Numerator

**Solve**: $\frac{x}{x-2} = \frac{4}{x-2} + 2$

**Step 1** - Domain: $x \neq 2$

**Step 2** - LCD: $x - 2$

**Step 3** - Multiply by LCD:
$$(x-2) \cdot \frac{x}{x-2} = (x-2) \cdot \frac{4}{x-2} + (x-2) \cdot 2$$
$$x = 4 + 2(x-2)$$
$$x = 4 + 2x - 4$$
$$x = 2x$$

**Step 4** - Solve:
$$x = 2x$$
$$0 = x$$

**Wait!** We got $x = 0$, but let's check...

**Step 5** - Check: $x = 0$ in original equation:
$$\frac{0}{0-2} = \frac{4}{0-2} + 2$$
$$0 = -2 + 2$$
$$0 = 0$$ ✓

**Solution**: $x = 0$ (not extraneous even though it emerged oddly)

---

### Example 3: Equation Leading to Extraneous Solution

**Solve**: $\frac{x}{x-3} - \frac{3}{x-3} = \frac{9}{x^2-9}$

**Step 1** - Domain: 
- $x - 3 \neq 0 \Rightarrow x \neq 3$
- $x^2 - 9 = (x+3)(x-3) \neq 0 \Rightarrow x \neq \pm 3$

**Excluded**: $x = 3, -3$

**Step 2** - LCD: $(x+3)(x-3)$

**Step 3** - Multiply by LCD:
$$(x+3)(x-3) \cdot \frac{x}{x-3} - (x+3)(x-3) \cdot \frac{3}{x-3} = (x+3)(x-3) \cdot \frac{9}{(x+3)(x-3)}$$

Simplify:
$$(x+3) \cdot x - (x+3) \cdot 3 = 9$$
$$x^2 + 3x - 3x - 9 = 9$$
$$x^2 - 9 = 9$$
$$x^2 = 18$$
$$x = \pm 3\sqrt{2}$$

**Step 5** - Check:
- $x = 3\sqrt{2} \approx 4.24$: Not in excluded set ✓
- $x = -3\sqrt{2} \approx -4.24$: Not in excluded set ✓

**Solutions**: $x = \pm 3\sqrt{2}$

---

### Example 4: Equation with Extraneous Solution

**Solve**: $\frac{x+2}{x-2} = \frac{4}{x-2} + 1$

**Step 1** - Domain: $x \neq 2$

**Step 2** - LCD: $x - 2$

**Step 3** - Multiply:
$$(x-2) \cdot \frac{x+2}{x-2} = (x-2) \cdot \frac{4}{x-2} + (x-2) \cdot 1$$
$$x + 2 = 4 + x - 2$$
$$x + 2 = x + 2$$

**Step 4** - Simplify:
$$x + 2 = x + 2$$
$$0 = 0$$

**This is an identity!** True for all $x$ in the domain.

**Step 5** - Apply domain restriction:

**Solution**: All real numbers **except** $x = 2$

**In interval notation**: $(-\infty, 2) \cup (2, \infty)$

---

### Example 5: Proportion Equation

**Solve**: $\frac{x-1}{3} = \frac{5}{x+2}$

**Cross-multiply** (special LCD technique for proportions):
$$(x-1)(x+2) = 3 \cdot 5$$
$$x^2 + 2x - x - 2 = 15$$
$$x^2 + x - 2 = 15$$
$$x^2 + x - 17 = 0$$

**Quadratic formula**:
$$x = \frac{-1 \pm \sqrt{1 + 68}}{2} = \frac{-1 \pm \sqrt{69}}{2}$$

**Solutions**: $x = \frac{-1 + \sqrt{69}}{2}$ or $x = \frac{-1 - \sqrt{69}}{2}$

**Check**: Neither solution makes denominator zero ✓

---

### Example 6: Work Rate Problem Application

**Problem**: Sarah can paint a room in 6 hours. Tom can paint the same room in 9 hours. How long to paint together?

**Setup**: 
- Sarah's rate: $\frac{1}{6}$ room/hour
- Tom's rate: $\frac{1}{9}$ room/hour
- Combined rate: $\frac{1}{6} + \frac{1}{9}$ room/hour

**Equation**: If time together is $t$ hours:
$$\frac{1}{6}t + \frac{1}{9}t = 1$$

**LCD**: 18

**Solve**:
$$18 \cdot \frac{1}{6}t + 18 \cdot \frac{1}{9}t = 18$$
$$3t + 2t = 18$$
$$5t = 18$$
$$t = \frac{18}{5} = 3.6 \text{ hours}$$

**Answer**: $3.6$ hours or $3$ hours $36$ minutes

---

### Example 7: Multiple Fractions

**Solve**: $\frac{2}{x+1} + \frac{3}{x-1} = \frac{4}{x^2-1}$

**Step 1** - Factor: $x^2 - 1 = (x+1)(x-1)$

**Domain**: $x \neq \pm 1$

**Step 2** - LCD: $(x+1)(x-1)$

**Step 3** - Multiply:
$$(x+1)(x-1) \cdot \frac{2}{x+1} + (x+1)(x-1) \cdot \frac{3}{x-1} = (x+1)(x-1) \cdot \frac{4}{(x+1)(x-1)}$$

Simplify:
$$2(x-1) + 3(x+1) = 4$$
$$2x - 2 + 3x + 3 = 4$$
$$5x + 1 = 4$$
$$5x = 3$$
$$x = \frac{3}{5}$$

**Step 5** - Check: $x = \frac{3}{5}$ doesn't make denominator zero ✓

**Solution**: $x = \frac{3}{5}$

---

### Example 8: Equation Leading to "No Solution"

**Solve**: $\frac{1}{x-3} + \frac{2}{x-3} = \frac{3x-9}{x-3}$

**Step 1** - Domain: $x \neq 3$

**Step 2** - LCD: $x - 3$

**Step 3** - Multiply:
$$(x-3) \cdot \frac{1}{x-3} + (x-3) \cdot \frac{2}{x-3} = (x-3) \cdot \frac{3x-9}{x-3}$$
$$1 + 2 = 3x - 9$$
$$3 = 3x - 9$$
$$12 = 3x$$
$$x = 4$$

**Wait, that's odd...** Let me reconsider the right side:
$$\frac{3x-9}{x-3} = \frac{3(x-3)}{x-3} = 3$$ (when $x \neq 3$)

**So equation becomes**:
$$\frac{1}{x-3} + \frac{2}{x-3} = 3$$
$$\frac{3}{x-3} = 3$$
$$3 = 3(x-3)$$
$$3 = 3x - 9$$
$$x = 4$$ ✓

**Solution**: $x = 4$

---

## Applications

### 1. Work Rate Problems

**General form**: $\frac{t}{a} + \frac{t}{b} = 1$

Where:
- $a$ = time for worker A alone
- $b$ = time for worker B alone
- $t$ = time working together

**Interpretation**: (fraction of job by A) + (fraction of job by B) = 1 complete job

---

### 2. Mixture Problems

**Combining solutions** of different concentrations:

$$\frac{\text{amount of substance in solution 1}}{\text{total volume}} + \frac{\text{amount of substance in solution 2}}{\text{total volume}} = \text{final concentration}$$

---

### 3. Distance-Rate-Time

**Opposite directions**:
$$\frac{d_1}{r_1} + \frac{d_2}{r_2} = t$$

**Same direction**:
$$\frac{d_1}{r_1} - \frac{d_2}{r_2} = t$$

**River current problems**: Involves rational expressions for effective speed.

---

### 4. Electrical Resistance (Parallel)

**Total resistance** for parallel circuits:
$$\frac{1}{R_{total}} = \frac{1}{R_1} + \frac{1}{R_2}$$

---

### 5. Lens Equation (Physics)

$$\frac{1}{f} = \frac{1}{d_o} + \frac{1}{d_i}$$

Where:
- $f$ = focal length
- $d_o$ = object distance
- $d_i$ = image distance

---

### 6. Average Rate Problems

**Average speed** for round trip with different speeds:
$$\text{Average speed} = \frac{2d}{\frac{d}{r_1} + \frac{d}{r_2}}$$

Not simply $\frac{r_1 + r_2}{2}$!

---

## Common Misconceptions

### ❌ Misconception 1: Forgetting to Check for Extraneous Solutions

**Error**: Accepting all algebraic solutions without verification.

**Example**: Solving $\frac{x}{x-2} = \frac{2}{x-2}$ gives $x = 2$, but this is **extraneous** (makes denominator zero).

**Correct**: **Always** check solutions against domain restrictions.

---

### ❌ Misconception 2: Not Multiplying ALL Terms by LCD

**Incorrect**:
$$\frac{x}{2} + 3 = \frac{5}{4}$$

Multiply only fractions: $x + 3 = \frac{5}{2}$ ❌

**Correct**: Multiply EVERY term by LCD = 4:
$$4 \cdot \frac{x}{2} + 4 \cdot 3 = 4 \cdot \frac{5}{4}$$
$$2x + 12 = 5$$

---

### ❌ Misconception 3: Cross-Multiplying When More Than Two Fractions

**Cannot use**: Cross-multiplication for $\frac{a}{b} + \frac{c}{d} = \frac{e}{f}$

**Must use**: LCD method for more than one fraction per side.

**Exception**: Cross-multiplication works ONLY for $\frac{a}{b} = \frac{c}{d}$ (proportion form).

---

### ❌ Misconception 4: Incorrectly Identifying LCD

**Error**: Using product of denominators when simpler LCD exists.

**Example**: For $\frac{1}{x}$ and $\frac{1}{x^2}$:
- **Incorrect LCD**: $x \cdot x^2 = x^3$
- **Correct LCD**: $x^2$ (since $x$ divides into $x^2$)

---

### ❌ Misconception 5: Treating Rational Equation Like Rational Expression

**Rational equation**: Contains equals sign; solve for $x$
$$\frac{x}{2} = \frac{3}{4} \quad \text{(solve: } x = \frac{3}{2}\text{)}$$

**Rational expression**: No equals sign; simplify
$$\frac{x}{2} \cdot \frac{3}{4} = \frac{3x}{8} \quad \text{(simplify)}$$

**Different processes entirely!**

---

### ❌ Misconception 6: Canceling Before Multiplying by LCD

**Incorrect approach**:
$$\frac{x+2}{x-1} = \frac{3}{x-1}$$

"Cancel $(x-1)$": $x + 2 = 3$ ❌

**Problem**: Loses domain restriction $x \neq 1$.

**Correct**: 
1. Note domain: $x \neq 1$
2. Multiply by LCD: $(x-1)(x+2) = (x-1) \cdot 3$
3. Simplify: $x + 2 = 3$
4. Solve: $x = 1$
5. Check: **Extraneous** (violates $x \neq 1$)

**Answer**: No solution

---

### ❌ Misconception 7: Distributing LCD Incorrectly

**Incorrect**:
$$\text{LCD}(x-2) \cdot \left[\frac{x}{x-2} + 1\right] = (x-2) \cdot \frac{x}{x-2} + 1$$

**Correct**: Distribute to ALL terms:
$$= (x-2) \cdot \frac{x}{x-2} + (x-2) \cdot 1$$
$$= x + (x-2)$$

---

## Related Concepts

### Prerequisites
- [[Linear_Equations]] - Foundation for solving after clearing fractions
- [[Rational_Expressions_Operations]] - Understanding fraction operations
- [[Domain_Restrictions]] - Identifying excluded values
- [[LCD_Technique]] - Finding least common denominator

### Defined Concepts
- [[Extraneous_Solutions]] - Solutions that violate domain restrictions

### Related Equation Types
- [[Radical_Equations]] - Also produce extraneous solutions
- [[Proportion_Equations]] - Special case of rational equations

### Applications
- [[Work_Rate_Problems]] - Primary application type
- [[Mixture_Problems]] - Solution concentration applications
- [[Distance_Rate_Time_Problems]] - Motion problems with rational expressions

### Connected Topics
- [[Factoring_Strategies]] - Used to find LCD
- [[Quadratic_Equations]] - May result after clearing fractions

---

## Solution Strategy Summary

### Decision Tree

```
Start: Rational Equation
    ↓
Identify domain restrictions (set denominators ≠ 0)
    ↓
Determine LCD (factor denominators, take highest powers)
    ↓
Multiply ALL terms by LCD
    ↓
Simplify (fractions should cancel)
    ↓
Solve resulting polynomial equation
    ↓
CHECK each solution against domain restrictions
    ↓
Reject extraneous solutions
    ↓
State final solution set
```

---

## Practice Problems

### Basic
1. Solve: $\frac{x}{3} + \frac{x}{6} = 5$ → **Answer**: $x = 10$

2. Solve: $\frac{2}{x} = \frac{1}{4}$ → **Answer**: $x = 8$

3. Solve: $\frac{x+1}{2} = \frac{x-1}{3}$ → **Answer**: $x = 5$

### Intermediate
4. Solve: $\frac{1}{x-1} + \frac{2}{x+1} = \frac{4}{x^2-1}$ → **Answer**: $x = \frac{5}{3}$

5. Solve: $\frac{x}{x-3} = \frac{3}{x-3} + 2$ → **Answer**: No solution (extraneous)

6. Solve: $\frac{5}{x+2} - \frac{3}{x} = \frac{1}{x}$ → **Answer**: $x = 2$ or $x = -5$

### Application
7. Working together, pumps A and B can fill a pool in 4 hours. Pump A alone takes 6 hours. How long for pump B alone? → **Answer**: 12 hours

8. Solve: $\frac{x+3}{x-2} - \frac{x-3}{x+2} = \frac{8}{x^2-4}$ → **Answer**: $x = 1$

---

## Summary

**Rational equations** require systematic elimination of fractions by multiplying through by the LCD, followed by solving the resulting polynomial equation. The critical step is **checking for extraneous solutions**—algebraic solutions that violate domain restrictions must be rejected.

**Key principles**:
1. **Always** identify domain restrictions first (set denominators ≠ 0)
2. Find LCD by factoring all denominators
3. Multiply EVERY term by LCD
4. Solve resulting equation
5. **Mandatory**: Check solutions against domain restrictions

**Extraneous solutions** occur when algebraic manipulation introduces values excluded from the original equation's domain. Checking is not optional—it's essential.

**Applications**: Work rate problems, mixture problems, and distance-rate-time scenarios frequently produce rational equations, making this technique essential for applied problem-solving.
