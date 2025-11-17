---
layout: concept
title: Absolute Value Inequalities
topic: General Math
type: Definition
status: stable
importance: high
tags:
- concept/algebra
- concept/inequalities
- chapter-1
- solving-inequalities
sources:
- miller-gerken-2ed
source_refs:
- Miller & Gerken §1.7 p.145-152
relations:
  broader:
  - '[[Inequalities]]'
  - '[[Compound_Inequalities]]'
  narrower:
  - Less Than Type (|x| < k)
  - Greater Than Type (|x| > k)
  depends_on:
  - '[[Absolute_Value]]'
  - '[[Compound_Inequalities]]'
  - '[[Interval_Notation]]'
  related:
  - '[[Linear_Inequalities]]'
  - '[[Distance_Interpretation]]'
  - '[[Solution_Sets]]'
  used_in:
  - '[[Absolute_Value_Functions]]'
  - '[[Error_Bounds]]'
  - '[[Tolerance_Problems]]'
review:
  last: 2025-10-19
  next: 2025-10-26
  interval: 7 days
created: 2025-10-19
updated: 2025-11-16
qa_certified: true
qa_date: 2025-11-16
qa_migration: v2.0
related:
- '[[Absolute_Value]]'
- '[[Compound_Inequalities]]'
- '[[Inequality_Properties]]'
- '[[Number_Line_Graphing]]'
defines:
- '[[Absolute_Value]]'
- '[[Compound_Inequalities]]'
- '[[Interval_Notation]]'
---
# Absolute Value Inequalities

## Definition

**Absolute value inequalities** are inequalities containing absolute value expressions. Unlike equations, they have solution sets that are intervals or unions of intervals, not individual points.

**Standard Forms**:
```
|expression| < k    (less than)
|expression| > k    (greater than)
|expression| ≤ k    (less than or equal)
|expression| ≥ k    (greater than or equal)
```

**Key Principle**: Absolute value represents distance from zero, so inequalities describe ranges of distance.

---

## Core Concept: Distance Interpretation

**Geometric Meaning**:
- |x| = distance from x to 0 on number line
- |x - a| = distance from x to a
- |x| < k means "within k units of origin"
- |x| > k means "more than k units from origin"

**Visual**:
```
|x| < 3:  Distance < 3 from origin
   ←●═════●→
   -3  0  3
   Solution: (-3, 3)

|x| > 3:  Distance > 3 from origin
←══●     ●══→
   -3  0  3
   Solution: (-∞, -3) ∪ (3, ∞)
```

---

## Type 1: "Less Than" Inequalities |x| < k

**Pattern**: Distance less than k

**Rule**: |expression| < k  ⟹  -k < expression < k

**Form**: Compound AND inequality (intersection)

**Process**:
```
1. Recognize |A| < k pattern
2. Rewrite as: -k < A < k
3. Solve compound AND inequality
4. Write in interval notation
```

### Example 1: Basic Less Than
**Solve**: |x| < 5

```
Step 1: Apply rule
-5 < x < 5

Step 2: Already solved

Interval notation: (-5, 5)

Graph: ←●═════●→
       -5  0  5
   (open circles at -5 and 5)
```

### Example 2: Expression Inside
**Solve**: |2x - 3| ≤ 5

```
Step 1: Apply rule
-5 ≤ 2x - 3 ≤ 5

Step 2: Solve compound inequality
-5 + 3 ≤ 2x ≤ 5 + 3
-2 ≤ 2x ≤ 8
-1 ≤ x ≤ 4

Interval notation: [-1, 4]

Graph: ←●═════●→
       -1  0  4
   (closed circles at -1 and 4)

Distance interpretation:
Points on number line within 5 units of 3/2
```

### Example 3: Isolate First
**Solve**: |3x + 1| - 2 < 7

```
Step 1: Isolate absolute value
|3x + 1| < 9

Step 2: Apply rule
-9 < 3x + 1 < 9

Step 3: Solve
-10 < 3x < 8
-10/3 < x < 8/3

Interval notation: (-10/3, 8/3)
```

### Example 4: No Solution Case
**Solve**: |x - 2| < -3

```
Step 1: Recognize impossibility
Absolute value is ALWAYS ≥ 0
Cannot be less than negative number

Solution: ∅ (no solution)
Empty set
```

---

## Type 2: "Greater Than" Inequalities |x| > k

**Pattern**: Distance greater than k

**Rule**: |expression| > k  ⟹  expression < -k  OR  expression > k

**Form**: Compound OR inequality (union)

**Process**:
```
1. Recognize |A| > k pattern
2. Rewrite as: A < -k  OR  A > k
3. Solve each inequality separately
4. Write as union of intervals
```

### Example 1: Basic Greater Than
**Solve**: |x| > 3

```
Step 1: Apply rule
x < -3  OR  x > 3

Step 2: Already solved

Interval notation: (-∞, -3) ∪ (3, ∞)

Graph: ←══●     ●══→
          -3  0  3
   (solution is shaded regions, not middle)
```

### Example 2: Expression Inside
**Solve**: |2x + 1| ≥ 7

```
Step 1: Apply rule
2x + 1 ≤ -7  OR  2x + 1 ≥ 7

Step 2: Solve each
2x ≤ -8  OR  2x ≥ 6
x ≤ -4   OR  x ≥ 3

Interval notation: (-∞, -4] ∪ [3, ∞)

Graph: ←══●     ●══→
          -4  0  3
   (closed circles at -4 and 3)

Distance interpretation:
Points more than 7/2 units from -1/2
```

### Example 3: Isolate First
**Solve**: |5 - 2x| + 3 > 8

```
Step 1: Isolate absolute value
|5 - 2x| > 5

Step 2: Apply rule
5 - 2x < -5  OR  5 - 2x > 5

Step 3: Solve each
-2x < -10  OR  -2x > 0
x > 5     OR  x < 0
(inequality reverses when dividing by negative)

Interval notation: (-∞, 0) ∪ (5, ∞)
```

### Example 4: All Real Numbers Case
**Solve**: |x + 2| > -1

```
Step 1: Recognize tautology
Absolute value is ALWAYS ≥ 0
Always greater than any negative number

Solution: All real numbers
Interval: (-∞, ∞) or ℝ
```

---

## Summary Table: Type Recognition

| Inequality | Splits Into | Solution Type | Keyword |
|-----------|-------------|---------------|---------|
| \|A\| < k | -k < A < k | AND (intersection) | Between |
| \|A\| ≤ k | -k ≤ A ≤ k | AND (intersection) | Within |
| \|A\| > k | A < -k OR A > k | OR (union) | Outside |
| \|A\| ≥ k | A ≤ -k OR A ≥ k | OR (union) | Beyond |

**Memory Aid**:
- **Less Than** (<, ≤): Sandwiched between → AND
- **Greater Than** (>, ≥): Split apart → OR

---

## Special Cases and Edge Cases

### Case 1: |A| < 0 (Always False)
```
|x - 2| < -5  →  ∅ (no solution)
Absolute value cannot be negative
```

### Case 2: |A| > 0 (Usually True)
```
|x + 3| > 0  →  All x except x = -3
Absolute value is 0 only at one point
Solution: (-∞, -3) ∪ (-3, ∞)
```

### Case 3: |A| < 0 or |A| = 0
```
|x - 5| ≤ 0  →  x = 5 only
Absolute value equals 0 only when expression = 0
```

### Case 4: |A| > -k (k positive)
```
|2x + 1| > -3  →  All real numbers
Absolute value always ≥ 0, so always > negative
```

### Case 5: |A| ≥ 0 (Always True)
```
|x² + 1| ≥ 0  →  All real numbers
Absolute value is always non-negative
```

---

## Complex Examples

### Example 1: Requires Quadratic
**Solve**: |x² - 2x| < 3

```
Step 1: Apply rule
-3 < x² - 2x < 3

Step 2: Split into two inequalities
Inequality 1: x² - 2x > -3
              x² - 2x + 3 > 0
              Always true (discriminant < 0)

Inequality 2: x² - 2x < 3
              x² - 2x - 3 < 0
              (x - 3)(x + 1) < 0
              Solution: -1 < x < 3

Step 3: Intersection
All reals AND (-1, 3) = (-1, 3)

Solution: (-1, 3)
```

### Example 2: Multiple Absolute Values
**Solve**: |x - 2| + |x + 1| ≤ 5

```
This requires case analysis based on critical points x = 2, x = -1

Case 1: x < -1
|x - 2| = -(x - 2) = 2 - x
|x + 1| = -(x + 1) = -x - 1
Equation: (2 - x) + (-x - 1) ≤ 5
         1 - 2x ≤ 5
         -2x ≤ 4
         x ≥ -2
Combined with x < -1: -2 ≤ x < -1

Case 2: -1 ≤ x < 2
|x - 2| = 2 - x
|x + 1| = x + 1
Equation: (2 - x) + (x + 1) ≤ 5
         3 ≤ 5  (always true)
All values: -1 ≤ x < 2

Case 3: x ≥ 2
|x - 2| = x - 2
|x + 1| = x + 1
Equation: (x - 2) + (x + 1) ≤ 5
         2x - 1 ≤ 5
         2x ≤ 6
         x ≤ 3
Combined with x ≥ 2: 2 ≤ x ≤ 3

Solution: Union of all cases
[-2, -1) ∪ [-1, 2) ∪ [2, 3] = [-2, 3]
```

---

## Applications

### 1. **Tolerance and Error Bounds**
```
Manufacturing: Part must be 10 cm ± 0.05 cm
|x - 10| ≤ 0.05
Solution: 9.95 ≤ x ≤ 10.05
Acceptable range: [9.95, 10.05]
```

### 2. **Temperature Ranges**
```
Ideal temperature: 72°F ± 3°F
|T - 72| ≤ 3
Solution: 69 ≤ T ≤ 75
Range: [69°F, 75°F]
```

### 3. **Distance Problems**
```
Points more than 5 units from x = 3
|x - 3| > 5
Solution: x < -2 OR x > 8
Intervals: (-∞, -2) ∪ (8, ∞)
```

### 4. **Quality Control**
```
Bottle must contain 500 mL ± 2%
|V - 500| ≤ 0.02(500) = 10
Solution: 490 ≤ V ≤ 510
```

---

## Common Errors and How to Avoid Them

### Error 1: Confusing AND with OR
```
Wrong: |x| < 3 means x < -3 OR x < 3  ✗
Correct: |x| < 3 means -3 < x < 3  ✓
        (AND, not OR for "less than")

Wrong: |x| > 3 means -3 < x < 3  ✗
Correct: |x| > 3 means x < -3 OR x > 3  ✓
        (OR, not AND for "greater than")
```

### Error 2: Sign Errors
```
Wrong: |x| < 3 means x < 3  (missing negative part)  ✗
Correct: |x| < 3 means -3 < x < 3  ✓
```

### Error 3: Not Reversing Inequality
```
Problem: |2x + 1| > 5 gives 2x + 1 < -5
         Then: 2x < -6
         Wrong: x < -3 (when should be x < -3 OR ...)

Correct: Must solve BOTH parts
         2x + 1 < -5 gives x < -3
         2x + 1 > 5 gives x > 2
         Answer: x < -3 OR x > 2
```

### Error 4: Forgetting to Isolate
```
Wrong: |2x - 3| + 5 > 8
       Apply rule directly: |2x - 3| > 8  ✗

Correct: Isolate first
         |2x - 3| > 3
         Then apply rule  ✓
```

### Error 5: Mishandling Special Cases
```
Wrong: |x| > -2 has no solution  ✗
Correct: |x| > -2 is always true (all reals)  ✓

Wrong: |x| < -1 is all real numbers  ✗
Correct: |x| < -1 has no solution  ✓
```

---

## Decision Tree: Solution Strategy

```
Absolute Value Inequality
│
├─ Is |A| isolated?
│   ├─ NO → Isolate first
│   └─ YES → Continue
│
├─ What type?
│   ├─ |A| < k or |A| ≤ k
│   │   ├─ k < 0? → No solution
│   │   ├─ k = 0? → A = 0 (equation)
│   │   └─ k > 0? → -k < A < k (AND)
│   │
│   └─ |A| > k or |A| ≥ k
│       ├─ k < 0? → All real numbers
│       ├─ k = 0? → All except A = 0
│       └─ k > 0? → A < -k OR A > k (OR)
│
└─ Write solution in interval notation
```

---

## Practice Problems

### Level 1: Basic Less Than
1. Solve: |x| < 7
2. Solve: |x + 3| ≤ 5
3. Solve: |2x - 1| < 9

### Level 2: Basic Greater Than
4. Solve: |x| > 4
5. Solve: |x - 5| ≥ 2
6. Solve: |3x + 2| > 7

### Level 3: Isolate First
7. Solve: |x - 4| + 3 < 8
8. Solve: |2x + 5| - 1 ≥ 6
9. Solve: 2|x + 1| - 3 > 5

### Level 4: Special Cases
10. Solve: |x - 2| < 0
11. Solve: |x + 1| > -3
12. Solve: |x| ≤ 0

### Level 5: Complex
13. Solve: |x² - 4| < 5
14. Solve: |2x - 1| + |x + 3| ≤ 6
15. Solve: |x - 3| < |x + 1|

### Applications
16. A machine produces parts that must be 15 cm ± 0.2 cm. Write and solve absolute value inequality.
17. Temperature must stay within 5°F of 68°F. Write and solve absolute value inequality.

---

## Summary

**Absolute value inequalities** describe ranges of distances on the number line:

**Two Types**:
1. **"Less Than"** (|A| < k): Splits to AND
   - -k < A < k
   - Single interval (between)
   - Compound AND inequality

2. **"Greater Than"** (|A| > k): Splits to OR
   - A < -k OR A > k
   - Two intervals (outside)
   - Compound OR inequality

**Memory Device**:
- "**L**ess than" → Stays **L**ocal (one interval, AND)
- "**G**reater than" → **G**oes far (two intervals, OR)

**Key Steps**:
1. Isolate absolute value
2. Identify type (< or >)
3. Apply appropriate rule
4. Solve resulting inequality/inequalities
5. Write in interval notation

**Special Cases**:
- |A| < negative → No solution
- |A| > negative → All reals (or almost all)
- |A| ≤ 0 → Only where A = 0
- |A| ≥ 0 → All reals

**Distance Interpretation**:
- |x - a| < k: Within k units of a
- |x - a| > k: More than k units from a

**Foundation For**: Error analysis, tolerance specifications, function analysis, optimization with constraints

---

*Absolute value inequalities extend the distance concept to ranges. Understanding the geometric meaning (distance from a point) clarifies why "less than" creates an interval and "greater than" creates a union.*
---
type: Definition
status: stable
importance: high
tags:
  - concept/definition
  - math/algebra
  - chapter-1/inequalities
  - absolute-value
  - solution-sets
sources:
  - miller-gerken-2025
source_refs:
  - "Miller & Gerken §1.7 p.140-144"
relations:
  broader:
    - "[[Inequalities]]"
  narrower:
    - "[[Less_Than_Absolute_Value]]"
    - "[[Greater_Than_Absolute_Value]]"
  depends_on:
    - "[[Absolute_Value]]"
    - "[[Compound_Inequalities]]"
    - "[[Interval_Notation]]"
  related:
    - "[[Absolute_Value_Equations]]"
    - "[[Linear_Inequalities]]"
  used_in:
    - "[[Tolerance_Problems]]"
    - "[[Error_Bounds]]"
    - "[[Distance_Problems]]"
review:
  last: 2025-10-19
  next: 2025-10-26
  interval: 7
created: 2025-10-19
updated: 2025-10-19
---

# Absolute Value Inequalities

## Definition

An **absolute value inequality** is an inequality involving the absolute value of a variable expression. These inequalities describe solution sets that are either **intervals centered at a point** ("less than" inequalities) or **two rays extending from a point** ("greater than" inequalities).

### Standard Forms

**Type 1 - "Less Than"**: $|x| < a$ or $|x| \leq a$

**Type 2 - "Greater Than"**: $|x| > a$ or $|x| \geq a$

**General form**: $|f(x)| < a$, $|f(x)| \leq a$, $|f(x)| > a$, or $|f(x)| \geq a$

---

## The Two Fundamental Patterns

### Pattern 1: |x| < a (Distance Within)

**Interpretation**: Distance from 0 is less than $a$

**Equivalent compound inequality**:
$$|x| < a \quad \Leftrightarrow \quad -a < x < a$$

**Solution set**: Single interval centered at 0

**Graph**: 
```
      ←————•————————————•————→
         -a       0       a
```

**Example**: $|x| < 3$ means $-3 < x < 3$, or $(-3, 3)$

---

### Pattern 2: |x| > a (Distance Beyond)

**Interpretation**: Distance from 0 is greater than $a$

**Equivalent compound inequality**:
$$|x| > a \quad \Leftrightarrow \quad x < -a \text{ OR } x > a$$

**Solution set**: Two separate rays (union)

**Graph**:
```
   ←————•                 •————→
       -a       0        a
```

**Example**: $|x| > 3$ means $x < -3$ OR $x > 3$, or $(-\infty, -3) \cup (3, \infty)$

---

## Solution Method

### Universal Process

#### Step 1: Isolate Absolute Value Expression
Get $|expression|$ by itself on one side of inequality.

#### Step 2: Identify Type and Convert
- **If |expression| < a**: Write as compound AND inequality: $-a < expression < a$
- **If |expression| > a**: Write as compound OR inequality: $expression < -a$ OR $expression > a$

#### Step 3: Solve Compound Inequality
Apply appropriate technique for AND or OR form.

#### Step 4: Express Solution
Write in interval notation and/or graph.

---

## Key Theorem: Distance Interpretation

### For any real number $a > 0$:

**Less Than Form**:
$$|x - c| < a \quad \Leftrightarrow \quad c - a < x < c + a$$

**Interpretation**: $x$ is within distance $a$ from center point $c$

---

**Greater Than Form**:
$$|x - c| > a \quad \Leftrightarrow \quad x < c - a \text{ OR } x > c + a$$

**Interpretation**: $x$ is more than distance $a$ away from center point $c$

---

## Examples

### Example 1: Basic "Less Than" Inequality

**Solve**: $|x| < 5$

**Step 1** - Already isolated.

**Step 2** - "Less than" type, write compound AND:
$$-5 < x < 5$$

**Step 3** - Already solved.

**Step 4** - Solution: $(-5, 5)$

**Graph**:
```
   ←————o===================o————→
       -5         0         5
```

---

### Example 2: Basic "Greater Than" Inequality

**Solve**: $|x| \geq 4$

**Step 1** - Already isolated.

**Step 2** - "Greater than" type, write compound OR:
$$x \leq -4 \quad \text{OR} \quad x \geq 4$$

**Step 3** - Already solved.

**Step 4** - Solution: $(-\infty, -4] \cup [4, \infty)$

**Graph**:
```
   ←====•                    •=====→
       -4         0          4
```

---

### Example 3: Expression Inside Absolute Value

**Solve**: $|2x - 3| < 7$

**Step 1** - Already isolated.

**Step 2** - "Less than" type:
$$-7 < 2x - 3 < 7$$

**Step 3** - Solve compound inequality:
$$-7 + 3 < 2x < 7 + 3$$
$$-4 < 2x < 10$$
$$-2 < x < 5$$

**Step 4** - Solution: $(-2, 5)$

---

### Example 4: "Greater Than" with Expression

**Solve**: $|3x + 2| > 8$

**Step 1** - Already isolated.

**Step 2** - "Greater than" type:
$$3x + 2 < -8 \quad \text{OR} \quad 3x + 2 > 8$$

**Step 3** - Solve each:

**Left inequality**:
$$3x < -10$$
$$x < -\frac{10}{3}$$

**Right inequality**:
$$3x > 6$$
$$x > 2$$

**Step 4** - Solution: $\left(-\infty, -\frac{10}{3}\right) \cup (2, \infty)$

---

### Example 5: Coefficient on Absolute Value

**Solve**: $3|x - 1| \leq 12$

**Step 1** - Isolate absolute value (divide by 3):
$$|x - 1| \leq 4$$

**Step 2** - "Less than" type:
$$-4 \leq x - 1 \leq 4$$

**Step 3** - Solve (add 1 throughout):
$$-3 \leq x \leq 5$$

**Step 4** - Solution: $[-3, 5]$

**Distance interpretation**: $x$ is within distance 4 from center point 1.

---

### Example 6: Absolute Value Shifted from Origin

**Solve**: $|x - 5| < 3$

**Interpretation**: Distance from 5 is less than 3.

**Method 1** - Distance interpretation:
Center: 5, radius: 3
$$5 - 3 < x < 5 + 3$$
$$2 < x < 8$$

**Method 2** - Standard conversion:
$$-3 < x - 5 < 3$$
$$2 < x < 8$$

**Solution**: $(2, 8)$

---

### Example 7: "Greater Than" Shifted

**Solve**: $|x + 2| \geq 5$

**Rewrite**: $|x - (-2)| \geq 5$

**Interpretation**: Distance from -2 is at least 5.

**Method 1** - Distance:
$$x \leq -2 - 5 \quad \text{OR} \quad x \geq -2 + 5$$
$$x \leq -7 \quad \text{OR} \quad x \geq 3$$

**Method 2** - Standard:
$$x + 2 \leq -5 \quad \text{OR} \quad x + 2 \geq 5$$
$$x \leq -7 \quad \text{OR} \quad x \geq 3$$

**Solution**: $(-\infty, -7] \cup [3, \infty)$

---

### Example 8: All Real Numbers Solution

**Solve**: $|x| > -2$

**Analysis**: Absolute value is **always non-negative**.

Since $|x| \geq 0$ for all $x$, and $0 > -2$, this inequality is **always true**.

**Solution**: All real numbers, $(-\infty, \infty)$ or $\mathbb{R}$

---

### Example 9: No Solution

**Solve**: $|x| < -3$

**Analysis**: Absolute value **cannot be negative**.

Since $|x| \geq 0$ for all $x$, and we need $|x| < -3$, this is **impossible**.

**Solution**: No solution, $\emptyset$ or $\{\}$

---

### Example 10: Complex Expression

**Solve**: $\left|\frac{2x - 1}{3}\right| \leq 2$

**Step 1** - Already isolated.

**Step 2** - "Less than" type:
$$-2 \leq \frac{2x - 1}{3} \leq 2$$

**Step 3** - Multiply by 3:
$$-6 \leq 2x - 1 \leq 6$$

Add 1:
$$-5 \leq 2x \leq 7$$

Divide by 2:
$$-\frac{5}{2} \leq x \leq \frac{7}{2}$$

**Step 4** - Solution: $\left[-\frac{5}{2}, \frac{7}{2}\right]$ or $[-2.5, 3.5]$

---

### Example 11: Quadratic Inside Absolute Value

**Solve**: $|x^2 - 4| < 5$

**Step 1** - Already isolated.

**Step 2** - "Less than" type:
$$-5 < x^2 - 4 < 5$$

**Step 3** - Solve compound:

**Left inequality**:
$$-5 < x^2 - 4$$
$$-1 < x^2$$

This is always true (since $x^2 \geq 0 > -1$).

**Right inequality**:
$$x^2 - 4 < 5$$
$$x^2 < 9$$
$$-3 < x < 3$$

**Step 4** - Intersection: $(-3, 3)$

---

### Example 12: Application - Tolerance

**Manufacturing**: A machine produces bolts with target diameter 5.00 cm. The tolerance is ±0.02 cm.

**Write inequality**: Let $d$ = actual diameter.
$$|d - 5.00| \leq 0.02$$

**Solve**:
$$-0.02 \leq d - 5.00 \leq 0.02$$
$$4.98 \leq d \leq 5.02$$

**Interpretation**: Acceptable diameters are between 4.98 and 5.02 cm.

---

## Applications

### 1. Manufacturing Tolerance

**Quality control**: $|actual - target| \leq tolerance$

**Example**: Target weight 100g, tolerance ±2g:
$$|w - 100| \leq 2 \quad \Rightarrow \quad 98 \leq w \leq 102$$

---

### 2. Temperature Ranges

**Acceptable range**: $|T - optimal| \leq variation$

**Example**: Vaccine storage: optimal 5°C, variation ±2°C:
$$|T - 5| \leq 2 \quad \Rightarrow \quad 3 \leq T \leq 7$$

---

### 3. Error Bounds

**Measurement error**: $|measured - actual| < error$

**Example**: Distance measured as 100m ± 0.5m:
$$|d - 100| < 0.5 \quad \Rightarrow \quad 99.5 < d < 100.5$$

---

### 4. Distance Problems

**Within range**: $|position - center| < radius$

**Outside range**: $|position - center| > radius$

---

### 5. Statistical Outliers

**Data point $x$ is outlier** if:
$$|x - \bar{x}| > k \cdot s$$

where $\bar{x}$ = mean, $s$ = standard deviation, $k$ = threshold (often 2 or 3)

---

### 6. Physics - Displacement

**Oscillating motion** within bounds:
$$|x(t) - equilibrium| < amplitude$$

---

## Common Misconceptions

### ❌ Misconception 1: Incorrect Compound Form

**Incorrect**: $|x| < 3$ means $x < -3$ OR $x < 3$

**Correct**: $|x| < 3$ means $-3 < x < 3$ (compound AND)

**Key**: "Less than" uses AND; "greater than" uses OR.

---

### ❌ Misconception 2: Wrong Direction for "Greater Than"

**Incorrect**: $|x| > 3$ means $-3 > x > 3$

**Correct**: $|x| > 3$ means $x < -3$ OR $x > 3$

**Why**: Solution set is **outside** the interval, not inside.

---

### ❌ Misconception 3: Forgetting to Isolate First

**Problem**: $2|x| + 3 < 7$

**Incorrect approach**: Convert directly to compound inequality.

**Correct**: 
1. Isolate: $2|x| < 4$, then $|x| < 2$
2. Then convert: $-2 < x < 2$

---

### ❌ Misconception 4: Misapplying Operations to Compound Inequality

**Incorrect**:
$$-3 < 2x - 1 < 3$$

Subtract 1 from first term only: $-4 < 2x < 3$ ❌

**Correct**: Perform operation on ALL three parts:
$$-3 - 1 < 2x - 1 - 1 < 3 - 1$$
$$-4 < 2x < 2$$

---

### ❌ Misconception 5: Accepting Impossible Solutions

**Problem**: $|x| < -5$

**Incorrect**: $-5 < x < 5$

**Correct**: No solution (absolute value cannot be negative)

---

### ❌ Misconception 6: Interval Notation Error

**Problem**: $|x| > 3$

**Incorrect**: $(-\infty, -3) \cap (3, \infty)$ (using intersection)

**Correct**: $(-\infty, -3) \cup (3, \infty)$ (using union)

**Key**: "OR" means union (∪); "AND" means intersection (∩)

---

### ❌ Misconception 7: Sign Errors in Compound Inequality

**Problem**: $|x - 2| < 5$

**Incorrect**: $-5 < x - 2 > 5$ (mixing inequality directions)

**Correct**: $-5 < x - 2 < 5$ (consistent direction)

---

## Related Concepts

### Prerequisites
- [[Absolute_Value]] - Understanding distance interpretation
- [[Compound_Inequalities]] - AND vs OR logic
- [[Interval_Notation]] - Expressing solution sets
- [[Linear_Inequalities]] - Basic inequality solving

### Related Concepts
- [[Absolute_Value_Equations]] - Solving equations with absolute value
- [[Number_Line_Graphs]] - Visualizing solution sets

### Applications
- [[Tolerance_Problems]] - Manufacturing and engineering
- [[Error_Bounds]] - Measurement and statistics
- [[Distance_Problems]] - Position and range problems

### Advanced Topics
- [[Absolute_Value_Functions]] - Graphing and analysis
- [[Piecewise_Functions]] - Alternative representation

---

## Visual Summary

### Pattern Recognition Chart

| Inequality | Compound Form | Solution Type | Interval |
|------------|---------------|---------------|----------|
| $\|x\| < a$ | $-a < x < a$ | Single interval (AND) | $(−a, a)$ |
| $\|x\| \leq a$ | $-a \leq x \leq a$ | Single interval (AND) | $[−a, a]$ |
| $\|x\| > a$ | $x < -a$ OR $x > a$ | Two rays (OR) | $(−\infty,−a) \cup (a,\infty)$ |
| $\|x\| \geq a$ | $x \leq -a$ OR $x \geq a$ | Two rays (OR) | $(−\infty,−a] \cup [a,\infty)$ |

### Special Cases

| Inequality | Solution | Reason |
|------------|----------|--------|
| $\|x\| < 0$ | $\emptyset$ | Absolute value is never negative |
| $\|x\| \leq 0$ | $\{0\}$ | Only zero has absolute value zero |
| $\|x\| > 0$ | All reals except 0 | $(-\infty, 0) \cup (0, \infty)$ |
| $\|x\| \geq 0$ | All reals $\mathbb{R}$ | Always true |
| $\|x\| < -k$ (k>0) | $\emptyset$ | Impossible |
| $\|x\| > -k$ (k>0) | All reals $\mathbb{R}$ | Always true |

---

## Practice Problems

### Basic Recognition
1. Solve: $|x| < 7$ → **Answer**: $(-7, 7)$

2. Solve: $|x| \geq 3$ → **Answer**: $(-\infty, -3] \cup [3, \infty)$

3. Solve: $|x| < 0$ → **Answer**: No solution, $\emptyset$

### With Expressions
4. Solve: $|x - 4| \leq 2$ → **Answer**: $[2, 6]$

5. Solve: $|2x + 1| > 5$ → **Answer**: $(-\infty, -3) \cup (2, \infty)$

6. Solve: $|3x - 2| < 7$ → **Answer**: $\left(-\frac{5}{3}, 3\right)$

### Requires Isolation
7. Solve: $2|x + 3| - 4 \leq 6$ → **Answer**: $[-8, 2]$

8. Solve: $3|2x - 1| + 5 > 14$ → **Answer**: $(-\infty, -1) \cup (2, \infty)$

### Application
9. A thermometer measures temperature with error ±1.5°F. If it reads 72°F, what is the range of actual temperatures? → **Answer**: $[70.5, 73.5]$

10. Solve: $|x + 1| \leq |x - 3|$ → **Advanced** (requires case analysis)

---

## Summary

**Absolute value inequalities** describe distance relationships and have two fundamental patterns:

**"Less than" form** ($|x| < a$): 
- Converts to compound **AND** inequality: $-a < x < a$
- Solution is **single interval** (within distance $a$ from center)

**"Greater than" form** ($|x| > a$):
- Converts to compound **OR** inequality: $x < -a$ OR $x > a$
- Solution is **two separate rays** (beyond distance $a$ from center)

**Critical distinctions**:
- AND form (less than) → intersection, single interval
- OR form (greater than) → union, two rays

**Distance interpretation**: $|x - c| < a$ means "$x$ is within distance $a$ from point $c$"

**Applications**: Manufacturing tolerances, error bounds, temperature ranges, and quality control all use absolute value inequalities to describe acceptable ranges.

**Mastery key**: Instant recognition of type (less than → AND vs. greater than → OR) and correct compound inequality formation.
