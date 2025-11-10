---
layout: concept
title: "Absolute Value"
topic: "General Math"
type: Definition
status: stable
importance: critical
tags:
  - concept/function
  - algebra/foundations
  - algebra/inequalities
  - geometry/distance
sources:
  - textbook-chR
  - textbook-ch1
source_refs:
  - "Miller & Gerken §R.1 p.8-10"
  - "Miller & Gerken §1.7 p.152-157"
relations:
  broader:
    - "[[Piecewise_Functions]]"
    - "[[Distance_Functions]]"
  narrower:
    - "[[Absolute_Value_of_Real_Numbers]]"
    - "[[Absolute_Value_of_Expressions]]"
  depends_on:
    - "[[Real_Number_System]]"
    - "[[Number_Line_Representation]]"
  defines:
    - "[[Distance_on_Number_Line]]"
    - "[[Magnitude]]"
  related:
    - "[[Absolute_Value_Equations]]"
    - "[[Absolute_Value_Inequalities]]"
    - "[[Piecewise_Functions]]"
  used_in:
    - "[[Absolute_Value_Equations]]"
    - "[[Absolute_Value_Inequalities]]"
    - "[[Distance_Formula]]"
    - "[[Modulus_Complex_Numbers]]"
review:
  last: 2025-10-19
  next: 2025-11-02
  interval: 14
created: 2025-10-19
updated: 2025-10-19
---

# Absolute Value

## Definition

The **absolute value** of a real number is its distance from zero on the number line, regardless of direction. It represents the magnitude or size of a number without regard to its sign.

### Formal Definition

For any real number x:

**|x| = {  x    if x ≥ 0**
**      { -x    if x < 0**

This piecewise definition means:
- If the number is positive or zero, absolute value equals the number itself
- If the number is negative, absolute value equals the opposite (making it positive)

### Standard Notation

- **Symbol**: | x | (vertical bars around the expression)
- **Read as**: "the absolute value of x" or "absolute x"
- **Alternative names**: Magnitude, modulus, norm (in different contexts)

---

## Geometric Interpretation

### Distance from Zero

**Key insight**: |x| measures how far x is from 0 on the number line.

**Number line visualization**:
```
         |----5 units----|
    <----•-------•-------•------•---->
        -5       0       3      5
         
         |-5| = 5       |3| = 3       |5| = 5
```

**Examples**:
- |5| = 5 because 5 is 5 units from 0
- |-5| = 5 because -5 is 5 units from 0
- |0| = 0 because 0 is 0 units from itself

**Important**: Distance is always non-negative!

---

### Distance Between Two Points

**Extended definition**: The distance between two numbers a and b is |a - b| or equivalently |b - a|

**Formula**: distance(a, b) = |a - b| = |b - a|

**Example**: Distance between -3 and 5
```
|-3 - 5| = |-8| = 8
or
|5 - (-3)| = |5 + 3| = |8| = 8
```

Both give the same result because distance is independent of direction.

---

## Key Properties

### Property 1: Always Non-Negative

**|x| ≥ 0 for all real numbers x**

- Absolute value cannot be negative
- |x| = 0 if and only if x = 0
- |x| > 0 if and only if x ≠ 0

---

### Property 2: Symmetric Property

**|x| = |-x| for all real numbers x**

**Meaning**: Opposite numbers have the same absolute value

**Examples**:
- |7| = |-7| = 7
- |π| = |-π| = π
- |√2| = |-√2| = √2

**Visual**: Numbers equidistant from 0 (on opposite sides) have equal absolute values

---

### Property 3: Product Property

**|xy| = |x| · |y| for all real numbers x, y**

**Example**:
- |(-3)(4)| = |-12| = 12
- |-3| · |4| = 3 · 4 = 12 ✓

**Application**: Absolute value of a product equals the product of absolute values

---

### Property 4: Quotient Property

**|x/y| = |x| / |y| for all real numbers x, y with y ≠ 0**

**Example**:
- |-12/4| = |-3| = 3
- |-12| / |4| = 12 / 4 = 3 ✓

---

### Property 5: Triangle Inequality

**|x + y| ≤ |x| + |y| for all real numbers x, y**

**Meaning**: The absolute value of a sum is less than or equal to the sum of absolute values

**Example where inequality is strict**:
- |3 + (-5)| = |-2| = 2
- |3| + |-5| = 3 + 5 = 8
- 2 < 8 ✓

**Example where equality holds** (same sign):
- |3 + 5| = |8| = 8
- |3| + |5| = 3 + 5 = 8 ✓

**Name origin**: In geometry, this states that one side of a triangle cannot exceed the sum of the other two sides.

---

### Property 6: Reverse Triangle Inequality

**|x - y| ≥ ||x| - |y|| for all real numbers x, y**

**Meaning**: The distance between two numbers is at least as large as the difference of their distances from zero

---

## Examples

### Example 1: Basic Evaluations

Evaluate each absolute value:

a) |8| = 8 (positive number stays positive)

b) |-8| = 8 (negative becomes positive)

c) |0| = 0 (zero stays zero)

d) |-3.7| = 3.7 (negative decimal becomes positive)

e) |5 - 9| = |-4| = 4 (evaluate inside first, then absolute value)

f) |9 - 5| = |4| = 4 (different order, same distance)

---

### Example 2: Absolute Value with Expressions

Evaluate: |2x - 5| when x = 1

**Solution**:
```
|2x - 5|
= |2(1) - 5|      [Substitute x = 1]
= |2 - 5|         [Multiply]
= |-3|            [Subtract]
= 3               [Absolute value]
```

**Answer**: 3

---

### Example 3: Absolute Value of Opposite

Show that |x| = |-x| using x = 6 and x = -6

**For x = 6**:
```
|6| = 6
|-6| = 6
Therefore: |6| = |-6| ✓
```

**For x = -6**:
```
|-6| = 6
|-(-6)| = |6| = 6
Therefore: |-6| = |-(-6)| ✓
```

Property confirmed!

---

### Example 4: Product Property

Verify |xy| = |x| · |y| for x = -5, y = 3

**Left side**:
```
|xy| = |(-5)(3)| = |-15| = 15
```

**Right side**:
```
|x| · |y| = |-5| · |3| = 5 · 3 = 15
```

**Conclusion**: 15 = 15 ✓

---

### Example 5: Triangle Inequality

Verify |x + y| ≤ |x| + |y| for x = 4, y = -7

**Left side**:
```
|x + y| = |4 + (-7)| = |-3| = 3
```

**Right side**:
```
|x| + |y| = |4| + |-7| = 4 + 7 = 11
```

**Conclusion**: 3 ≤ 11 ✓ (strict inequality)

---

### Example 6: Distance Between Points

Find the distance between -8 and 3 on the number line.

**Solution**:
```
distance = |-8 - 3| = |-11| = 11
or
distance = |3 - (-8)| = |3 + 8| = |11| = 11
```

**Answer**: 11 units

**Number line check**:
```
      <----•-------•-------•---->
          -8       0       3
           |------11------|
```
From -8 to 3 is indeed 11 units.

---

## Applications

### 1. Solving Absolute Value Equations

**Basic equation**: |x| = a (where a ≥ 0)

**Solution**: x = a or x = -a

**Why**: Both a and -a are distance a from zero

**Example**: |x| = 5 means x = 5 or x = -5

See [[Absolute_Value_Equations]] for detailed methods

---

### 2. Solving Absolute Value Inequalities

**Type 1**: |x| < a means -a < x < a
- Numbers within distance a from zero
- Interval: (-a, a)

**Type 2**: |x| > a means x < -a or x > a
- Numbers farther than distance a from zero
- Interval: (-∞, -a) ∪ (a, ∞)

See [[Absolute_Value_Inequalities]]

---

### 3. Distance Formula

In the coordinate plane, distance between points (x₁, y₁) and (x₂, y₂):

**d = √[(x₂ - x₁)² + (y₂ - y₁)²]**

This uses the fact that √(a²) = |a|, so:
- Horizontal distance: |x₂ - x₁|
- Vertical distance: |y₂ - y₁|
- Total distance via Pythagorean theorem

See [[Distance_Formula]]

---

### 4. Error Analysis and Tolerance

In science and engineering, |actual - expected| represents error or deviation:

**Example**: If a part should be 10 cm with tolerance ±0.5 cm:
- Acceptable if: |length - 10| ≤ 0.5
- This means: 9.5 ≤ length ≤ 10.5

---

### 5. Piecewise Function Representation

Absolute value can be written as a piecewise function:

**f(x) = |x| = { x if x ≥ 0**
**               { -x if x < 0**

**Graph**: V-shaped graph with vertex at origin

```
    y
    |    /
    |   /
    |  /
    | /
----•----x
   /|
  / |
 /  |
```

See [[Piecewise_Functions]]

---

### 6. Modulus of Complex Numbers

For complex number z = a + bi:

**|z| = √(a² + b²)**

This extends the real number absolute value to complex plane as distance from origin.

See [[Modulus_Complex_Numbers]]

---

## Common Misconceptions

### ❌ Misconception 1: "Absolute value removes negative signs"

**Wrong thinking**: |x - 3| = x - 3 (just remove the bars)

**Reality**: Depends on whether x - 3 is positive or negative!
- If x = 5: |5 - 3| = |2| = 2 ✓
- If x = 1: |1 - 3| = |-2| = 2 ✗ (not 1 - 3 = -2)

**Correct approach**: Evaluate the expression inside first, THEN apply absolute value

---

### ❌ Misconception 2: "Absolute value always makes the answer positive"

**More precise statement**: Absolute value makes the **result** non-negative, but the **expression inside** can be any sign

**Example**: 
- |-5| = 5 (result is positive)
- |5| = 5 (input was already positive, result is positive)
- |0| = 0 (result is zero, which is non-negative but not positive)

**Key**: The *output* is non-negative (≥ 0), not necessarily positive (> 0)

---

### ❌ Misconception 3: "|x| = -x means x is negative"

**Wrong thinking**: The negative sign means x must be negative

**Reality**: -x represents the **opposite** of x
- If x = 5, then -x = -5 (negative)
- If x = -5, then -x = 5 (positive!)

**For |x| = -x to be true**: x must be ≤ 0 (zero or negative)
- Example: x = -3: |-3| = 3 and -(-3) = 3 ✓
- Example: x = 0: |0| = 0 and -0 = 0 ✓

---

### ❌ Misconception 4: "Can distribute absolute value over addition"

**Wrong**: |a + b| = |a| + |b|

**Reality**: This is only true when a and b have the same sign

**Counterexample**: 
```
|3 + (-5)| = |-2| = 2
|3| + |-5| = 3 + 5 = 8
2 ≠ 8 ✗
```

**Correct relationship**: |a + b| ≤ |a| + |b| (Triangle Inequality)

---

### ❌ Misconception 5: "Squaring is the same as absolute value"

**Wrong**: |x| = x²

**Reality**: |x| = √(x²)

**Difference**:
- |x| always gives a **positive number or zero**
- x² gives a positive number or zero, but loses information about the sign
- √(x²) = |x| (not just x!)

**Example**: 
- x = -3: |x| = 3, but x² = 9 (not the same!)
- x = -3: √((-3)²) = √9 = 3 = |x| ✓

---

### ❌ Misconception 6: "Absolute value equations always have two solutions"

**Wrong**: |x| = a always gives x = ±a

**Reality**: Depends on the value of a
- If a > 0: Two solutions (x = a or x = -a)
- If a = 0: One solution (x = 0)
- If a < 0: No solution (absolute value cannot be negative!)

**Example**: |x| = -3 has **no solution** because absolute values are never negative

---

## Piecewise Definition in Detail

### Understanding the Cases

**Case 1: When x ≥ 0** (x is zero or positive)
```
|x| = x
```
The number is already non-negative, so absolute value doesn't change it.

**Examples**:
- |5| = 5
- |0.3| = 0.3
- |0| = 0

---

**Case 2: When x < 0** (x is negative)
```
|x| = -x
```
The number is negative, so we negate it (take its opposite) to make it positive.

**Examples**:
- |-5| = -(-5) = 5
- |-0.3| = -(-0.3) = 0.3
- |-π| = -(-π) = π

---

### Evaluating Absolute Value of Expressions

**Process**:
1. Evaluate the expression inside the absolute value
2. Determine if result is positive, negative, or zero
3. Apply appropriate case of piecewise definition

**Example**: Evaluate |3 - 7|
```
Step 1: 3 - 7 = -4
Step 2: -4 < 0 (negative)
Step 3: Since negative, use |x| = -x
        |-4| = -(-4) = 4
```

---

## Connection to Other Concepts

### Builds Upon
- [[Real_Number_System]] - Defined for real numbers
- [[Number_Line_Representation]] - Geometric interpretation
- [[Distance_Concepts]] - Measures distance from zero

### Supports
- [[Absolute_Value_Equations]] - Primary application
- [[Absolute_Value_Inequalities]] - Distance inequalities
- [[Distance_Formula]] - Extends to 2D and 3D
- [[Piecewise_Functions]] - Example of piecewise definition

### Related To
- [[Modulus_Complex_Numbers]] - Extension to complex plane
- [[Norm_Vectors]] - Generalization to vectors
- [[Magnitude]] - General concept of size
- [[Sign_Function]] - Related piecewise function

### Used In
- [[Tolerance_Intervals]] - Engineering applications
- [[Error_Bounds]] - Numerical analysis
- [[Limits]] - ε-δ definitions in calculus
- [[Metric_Spaces]] - Distance functions in analysis

---

## Graphing Absolute Value Functions

### Basic Absolute Value Function: f(x) = |x|

**Table of values**:
| x | f(x) = \|x\| |
|---|------------|
| -3 | 3 |
| -2 | 2 |
| -1 | 1 |
| 0 | 0 |
| 1 | 1 |
| 2 | 2 |
| 3 | 3 |

**Graph**: V-shape with vertex at origin (0, 0)
- Opens upward
- Slope is -1 for x < 0
- Slope is +1 for x > 0
- Not differentiable at x = 0 (sharp corner)

---

### Transformations

**f(x) = |x - h| + k**: Translates the V-shape
- h units horizontally (right if h > 0)
- k units vertically (up if k > 0)
- Vertex at (h, k)

**f(x) = a|x|**: Vertical stretch/compression and reflection
- If |a| > 1: Vertical stretch (narrower V)
- If 0 < |a| < 1: Vertical compression (wider V)
- If a < 0: Reflection over x-axis (opens downward)

---

## Historical Note

The absolute value symbol |x| was introduced by German mathematician **Karl Weierstrass** in the 1840s. The notation gained widespread acceptance by the early 20th century.

Earlier notations included:
- mod(x) for "modulus"
- abs(x) for "absolute value"
- Occasionally √(x²) to represent the same concept

The vertical bar notation |x| is now universal in mathematics.

---

## Practice Problems

### Problem 1
Evaluate: |-7 + 3|

**Solution**:
```
|-7 + 3| = |-4| = 4
```

---

### Problem 2
Solve: |x| = 9

**Solution**: x = 9 or x = -9

**Explanation**: Both 9 and -9 are distance 9 from zero.

---

### Problem 3
True or False: |x - y| = |y - x|

**Answer**: True

**Explanation**: Distance between two points is the same regardless of order.
- |x - y| = distance from x to y
- |y - x| = distance from y to x
- These are the same distance!

---

### Problem 4
Which is larger: |5 + (-8)| or |5| + |-8|?

**Solution**:
```
|5 + (-8)| = |-3| = 3

|5| + |-8| = 5 + 8 = 13

13 > 3
```

**Answer**: |5| + |-8| is larger (Triangle Inequality)

---

### Problem 5
If |2x - 3| = 7, what are the possible values of x?

**Solution**:
```
2x - 3 = 7  or  2x - 3 = -7
2x = 10  or  2x = -4
x = 5  or  x = -2
```

**Answer**: x = 5 or x = -2

---

## Summary

**Absolute value** |x| represents the **distance from zero** on the number line—the magnitude of a number without regard to sign.

**Key properties**:
1. ✅ Always non-negative: |x| ≥ 0
2. ✅ Symmetric: |x| = |-x|
3. ✅ Product rule: |xy| = |x| · |y|
4. ✅ Quotient rule: |x/y| = |x| / |y|
5. ✅ Triangle inequality: |x + y| ≤ |x| + |y|

**Piecewise definition**:
```
|x| = { x    if x ≥ 0
      { -x   if x < 0
```

**Remember**:
- Absolute value measures **distance** (always positive or zero)
- |x| = a has solutions x = ±a (if a ≥ 0)
- Cannot distribute over addition: |a + b| ≠ |a| + |b| in general
- Graph is V-shaped with vertex at origin

**Applications**: Everywhere in mathematics—equations, inequalities, distance, tolerance, error analysis, and beyond!

---

## References

- Miller & Gerken, *College Algebra*, Section R.1: "Sets and the Real Number Line"
- Miller & Gerken, *College Algebra*, Section 1.7: "Absolute Value Inequalities"
- [[Absolute_Value_Equations]] - Solving equations
- [[Absolute_Value_Inequalities]] - Solving inequalities
- [[Distance_Formula]] - Applications to geometry

---

*Last updated: 2025-10-19*
*Status: Stable ✓*
*Review: Every 2 weeks*
