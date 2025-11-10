---
layout: concept
title: "Interval Notation"
topic: "General Math"
type: Definition
status: stable
importance: high
tags:
  - concept/notation
  - algebra/foundations
  - algebra/inequalities
  - set-theory
sources:
  - textbook-chR
  - textbook-ch1
source_refs:
  - "Miller & Gerken §R.1 p.5-8"
  - "Miller & Gerken §1.7 p.147-152"
relations:
  broader:
    - "[[Set_Notation]]"
  narrower:
    - "[[Open_Interval]]"
    - "[[Closed_Interval]]"
    - "[[Half_Open_Interval]]"
  depends_on:
    - "[[Real_Number_System]]"
    - "[[Inequality_Notation]]"
  defines:
    - "[[Domain_and_Range]]"
    - "[[Solution_Sets]]"
  related:
    - "[[Set_Builder_Notation]]"
    - "[[Number_Line_Representation]]"
    - "[[Inequalities]]"
  used_in:
    - "[[Linear_Inequalities]]"
    - "[[Compound_Inequalities]]"
    - "[[Absolute_Value_Inequalities]]"
    - "[[Function_Domain]]"
    - "[[Function_Range]]"
review:
  last: 2025-10-19
  next: 2025-11-02
  interval: 14
created: 2025-10-19
updated: 2025-10-19
---

# Interval Notation

## Definition

**Interval notation** is a mathematical shorthand for describing sets of real numbers using brackets and parentheses. It provides a compact way to represent continuous ranges of values on the real number line.

### Basic Syntax

**Interval notation uses:**
- **Parentheses ( )**: Exclude the endpoint (open boundary)
- **Brackets [ ]**: Include the endpoint (closed boundary)
- **Infinity symbols ∞, -∞**: Always use parentheses (infinity is a concept, not a number)

### General Form

```
(a, b)  or  [a, b]  or  (a, b]  or  [a, b)
```

Where `a` is the **left endpoint** and `b` is the **right endpoint** with `a < b`.

---

## Types of Intervals

### 1. Open Interval: (a, b)

**Definition**: All real numbers strictly between a and b, **excluding** both endpoints.

**Set-builder notation**: `{x | a < x < b}`

**Number line**:
```
     o=========o
     a         b
```
(Open circles indicate excluded endpoints)

**Example**: `(2, 5)` means all real numbers between 2 and 5
- Includes: 2.1, 3, 4.999, π
- Excludes: 2, 5

---

### 2. Closed Interval: [a, b]

**Definition**: All real numbers between a and b, **including** both endpoints.

**Set-builder notation**: `{x | a ≤ x ≤ b}`

**Number line**:
```
     •=========•
     a         b
```
(Solid dots indicate included endpoints)

**Example**: `[2, 5]` means all real numbers from 2 to 5, inclusive
- Includes: 2, 2.1, 3, 4.999, 5
- Excludes: 1.999, 5.001

---

### 3. Half-Open (or Half-Closed) Intervals

**Left-closed, right-open: [a, b)**

**Set-builder**: `{x | a ≤ x < b}`

**Number line**:
```
     •=========o
     a         b
```

**Example**: `[2, 5)` includes 2 but excludes 5

---

**Left-open, right-closed: (a, b]**

**Set-builder**: `{x | a < x ≤ b}`

**Number line**:
```
     o=========•
     a         b
```

**Example**: `(2, 5]` excludes 2 but includes 5

---

### 4. Unbounded Intervals (Infinite Intervals)

**Left-unbounded: (-∞, b]** or **(-∞, b)**

**Set-builder**: `{x | x ≤ b}` or `{x | x < b}`

**Number line**:
```
<============•
            b
```

**Example**: `(-∞, 5]` means all real numbers less than or equal to 5

---

**Right-unbounded: [a, ∞)** or **(a, ∞)**

**Set-builder**: `{x | x ≥ a}` or `{x | x > a}`

**Number line**:
```
     •===========>
     a
```

**Example**: `[3, ∞)` means all real numbers greater than or equal to 3

---

**All real numbers: (-∞, ∞)**

**Set-builder**: `{x | x ∈ ℝ}` or simply `ℝ`

**Number line**:
```
<===============>
```

**Example**: `(-∞, ∞)` represents the entire real number line

---

## Critical Rules

### Rule 1: Infinity Always Gets Parentheses

**✓ CORRECT**: `[3, ∞)`, `(-∞, 5]`, `(-∞, ∞)`

**✗ INCORRECT**: `[3, ∞]`, `[-∞, 5]`

**Reason**: Infinity (∞) is not a real number—it's a concept representing unboundedness. We can never "reach" or "include" infinity.

---

### Rule 2: Left Endpoint Must Be Less Than Right Endpoint

**✓ CORRECT**: `[2, 5]` (since 2 < 5)

**✗ INCORRECT**: `[5, 2]` (since 5 > 2)

**Exception**: For union of intervals, order doesn't matter
- `[2, 5] ∪ [7, 10]` is same as `[7, 10] ∪ [2, 5]`

---

### Rule 3: Empty Interval Has No Standard Notation

If a ≥ b in (a, b), the interval is **empty** (contains no real numbers)

**Example**: `(5, 5)` is empty because there are no numbers strictly between 5 and itself
- Typically written as: `∅` or `{ }` (empty set)

---

## Conversion Between Notations

### From Set-Builder to Interval

| Set-Builder Notation | Interval Notation | Description |
|---------------------|-------------------|-------------|
| `{x \| x < 3}` | `(-∞, 3)` | Less than 3 |
| `{x \| x ≤ 3}` | `(-∞, 3]` | Less than or equal to 3 |
| `{x \| x > 3}` | `(3, ∞)` | Greater than 3 |
| `{x \| x ≥ 3}` | `[3, ∞)` | Greater than or equal to 3 |
| `{x \| 2 < x < 5}` | `(2, 5)` | Between 2 and 5 (exclusive) |
| `{x \| 2 ≤ x ≤ 5}` | `[2, 5]` | Between 2 and 5 (inclusive) |
| `{x \| 2 ≤ x < 5}` | `[2, 5)` | 2 inclusive, 5 exclusive |
| `{x \| 2 < x ≤ 5}` | `(2, 5]` | 2 exclusive, 5 inclusive |

---

### From Interval to Set-Builder

**Process**:
1. Identify endpoints a and b
2. Determine inclusion (brackets) vs exclusion (parentheses)
3. Write appropriate inequalities

**Example 1**: `[3, 7)` → `{x | 3 ≤ x < 7}`
- Left bracket → ≤ on left side
- Right parenthesis → < on right side

**Example 2**: `(-∞, 4]` → `{x | x ≤ 4}`
- Negative infinity → no lower bound
- Right bracket → ≤

**Example 3**: `(2, ∞)` → `{x | x > 2}`
- Left parenthesis → > (not ≥)
- Positive infinity → no upper bound

---

## Examples

### Example 1: Describing Solution Sets

**Problem**: Solve 2x + 3 < 11 and express in interval notation

**Solution**:
```
2x + 3 < 11
2x < 8
x < 4
```

**Interval notation**: `(-∞, 4)`

**Meaning**: All real numbers less than 4

---

### Example 2: Domain of a Function

**Problem**: Find the domain of f(x) = √(x - 3) in interval notation

**Solution**:
- Square root requires: x - 3 ≥ 0
- Therefore: x ≥ 3

**Interval notation**: `[3, ∞)`

**Meaning**: All real numbers greater than or equal to 3

---

### Example 3: Compound Inequality

**Problem**: Express -2 ≤ x < 5 in interval notation

**Solution**: `[-2, 5)`

**Number line**:
```
     •=========o
    -2         5
```

**Meaning**: 
- Includes -2 (bracket)
- Excludes 5 (parenthesis)
- All values in between

---

### Example 4: Union of Intervals

**Problem**: Graph x < -1 or x ≥ 3 using interval notation

**Solution**: 
- x < -1 is `(-∞, -1)`
- x ≥ 3 is `[3, ∞)`
- Union: `(-∞, -1) ∪ [3, ∞)`

**Number line**:
```
<====o         •======>
    -1         3
```

**Meaning**: All numbers less than -1 OR greater than or equal to 3

---

### Example 5: Intersection of Intervals

**Problem**: Find `[1, 5) ∩ (3, 7]`

**Solution**: 
- Overlap occurs from 3 to 5 (excluding both 3 and 5)
- Answer: `(3, 5)`

**Visualization**:
```
[1, 5):      •=======o
                (3, 7]:      o=========•
Intersection:       o===o
                   3   5
```

---

## Special Cases and Edge Cases

### Case 1: Single Point Intervals

**Question**: Can an interval contain just one point?

**Answer**: Yes! `[5, 5]` = `{5}` (just the number 5)

**But**: `(5, 5)` = `∅` (empty set - no numbers strictly between 5 and itself)

---

### Case 2: Discrete vs Continuous

**Interval notation represents continuous sets only**

- ✓ CORRECT for: All real numbers from 1 to 10: `[1, 10]`
- ✗ INCORRECT for: All integers from 1 to 10: `[1, 10]` would include 1.5, π, etc.

**For discrete sets**, use roster notation: `{1, 2, 3, ..., 10}` or set-builder: `{n | n ∈ ℤ, 1 ≤ n ≤ 10}`

---

### Case 3: Rational vs Real Numbers

Interval notation `[1, 2]` includes **all real numbers** between 1 and 2, including:
- Rational numbers: 1.5, 1.25, 7/4
- Irrational numbers: √2, √(1.5), π/2

If you want **only rationals**, specify: `{x | x ∈ ℚ, 1 ≤ x ≤ 2}`

---

## Applications

### 1. Solving Linear Inequalities

**Example**: 3x - 5 ≥ 4
```
3x ≥ 9
x ≥ 3
```
**Answer**: `[3, ∞)`

See [[Linear_Inequalities]]

---

### 2. Function Domains and Ranges

**Domain of f(x) = 1/(x - 2)**:
- Cannot divide by zero: x ≠ 2
- Domain: `(-∞, 2) ∪ (2, ∞)`

See [[Domain_and_Range]], [[Function_Domain]]

---

### 3. Absolute Value Inequalities

**Example**: |x| < 3 means -3 < x < 3
- **Interval notation**: `(-3, 3)`

See [[Absolute_Value_Inequalities]]

---

### 4. Describing Bounded Regions

In multivariable calculus and real analysis:
- Open interval (a, b): Open set
- Closed interval [a, b]: Closed and bounded (compact)
- Half-open intervals: Neither open nor closed

---

### 5. Calculus Applications

- **Increasing/decreasing intervals**: f(x) increasing on `[2, 5]`
- **Continuity intervals**: f(x) continuous on `(-∞, 3) ∪ (3, ∞)`
- **Integration bounds**: ∫[a,b] f(x)dx

---

## Common Misconceptions

### ❌ Misconception 1: "Infinity can be included"

**Wrong**: `[0, ∞]` (infinity with bracket)

**Right**: `[0, ∞)` (infinity with parenthesis)

**Why**: ∞ is not a real number and cannot be an element of an interval

---

### ❌ Misconception 2: "Parentheses and brackets are interchangeable"

**Wrong**: `[3, 5]` same as `(3, 5)`

**Right**: They represent different sets!
- `[3, 5]` includes endpoints: 3 and 5 are in the set
- `(3, 5)` excludes endpoints: 3 and 5 are NOT in the set

**Example**: Does 3 satisfy x ∈ (3, 5)? **NO**
Does 3 satisfy x ∈ [3, 5]? **YES**

---

### ❌ Misconception 3: "Intervals always describe solutions"

**Wrong**: Only solutions go in interval notation

**Right**: Intervals describe any continuous set of real numbers
- Solutions to inequalities
- Domains of functions
- Ranges of functions
- Intervals of increase/decrease
- Any continuous subset of ℝ

---

### ❌ Misconception 4: "Order doesn't matter"

**Context matters**:
- **Single interval**: Must have left < right: `[2, 5]` ✓, `[5, 2]` ✗
- **Union of intervals**: Order doesn't matter: `(1,3) ∪ (5,7)` = `(5,7) ∪ (1,3)` ✓

---

### ❌ Misconception 5: "Closed intervals are 'better' than open intervals"

**Wrong**: Using brackets when you should use parentheses (or vice versa)

**Right**: The notation must match the mathematics
- If x < 5, use `(-∞, 5)` NOT `(-∞, 5]`
- If x ≤ 5, use `(-∞, 5]` NOT `(-∞, 5)`

The difference of one point matters!

---

## Connection to Other Concepts

### Builds Upon
- [[Real_Number_System]] - Intervals are subsets of ℝ
- [[Inequality_Notation]] - Converts to interval notation
- [[Number_Line_Representation]] - Visual model

### Supports
- [[Linear_Inequalities]] - Solution set notation
- [[Compound_Inequalities]] - Union and intersection of intervals
- [[Absolute_Value_Inequalities]] - Translates to intervals
- [[Domain_and_Range]] - Standard notation for domains/ranges
- [[Function_Notation]] - Specifying input restrictions

### Related To
- [[Set_Builder_Notation]] - Alternative representation
- [[Set_Operations]] - Union, intersection of intervals
- [[Number_Line_Representation]] - Graphical equivalent

### Used In
- All of College Algebra
- Precalculus
- Calculus (limits, continuity, integration)
- Real Analysis (open/closed sets)

---

## Quick Reference Table

| Inequality | Set-Builder | Interval | Includes Endpoint? |
|------------|-------------|----------|-------------------|
| x < a | {x \| x < a} | (-∞, a) | No |
| x ≤ a | {x \| x ≤ a} | (-∞, a] | Yes (right) |
| x > a | {x \| x > a} | (a, ∞) | No |
| x ≥ a | {x \| x ≥ a} | [a, ∞) | Yes (left) |
| a < x < b | {x \| a < x < b} | (a, b) | Neither |
| a ≤ x ≤ b | {x \| a ≤ x ≤ b} | [a, b] | Both |
| a ≤ x < b | {x \| a ≤ x < b} | [a, b) | Left only |
| a < x ≤ b | {x \| a < x ≤ b} | (a, b] | Right only |
| All reals | {x \| x ∈ ℝ} | (-∞, ∞) | N/A |

---

## Memory Aids

### Mnemonic: "Parentheses Push away, Brackets Bring in"
- **(** pushes the endpoint away (excludes)
- **[** brings the endpoint in (includes)

### Visual Trick: "Open mouth eats the number"
- Open circle o or parenthesis ( = "open mouth" doesn't eat the number (excludes)
- Closed dot • or bracket [ = "closed mouth" has eaten the number (includes)

### Infinity Rule: "Infinity is forever OUT of reach"
- Always use parentheses with ∞ because you can never reach it

---

## Practice Problems

### Problem 1
Convert to interval notation: {x | -3 ≤ x < 7}

**Answer**: `[-3, 7)`

---

### Problem 2
Convert to set-builder notation: `(2, ∞)`

**Answer**: `{x | x > 2}` or `{x | x ∈ ℝ, x > 2}`

---

### Problem 3
Which numbers are in `[−2, 3)`?
- a) -2
- b) 0
- c) 3
- d) -2.5

**Answers**: 
- a) Yes (bracket includes -2)
- b) Yes (between endpoints)
- c) No (parenthesis excludes 3)
- d) No (less than left endpoint)

---

### Problem 4
Express the union: x < -1 or x ≥ 2

**Answer**: `(-∞, -1) ∪ [2, ∞)`

---

### Problem 5
True or False: `[3, ∞]` is correct interval notation.

**Answer**: False. Should be `[3, ∞)` because infinity cannot be included (no brackets with infinity).

---

## Summary

**Interval notation** is a compact, standardized way to express continuous sets of real numbers using parentheses and brackets:

- **Parentheses ( )**: Exclude endpoints
- **Brackets [ ]**: Include endpoints
- **Infinity ∞**: Always gets parentheses

**Key advantages**:
- ✅ Concise (shorter than set-builder notation)
- ✅ Clear visual representation
- ✅ Standard across mathematics
- ✅ Easy to read and write

**Remember**:
1. Infinity always gets parentheses: `(−∞, ∞)`
2. Left endpoint < right endpoint: `[a, b]` requires a < b
3. Match brackets/parentheses to your inequalities: < uses ( ), ≤ uses [ ]

**Master this notation early**—it appears throughout College Algebra, Precalculus, and Calculus!

---

## References

- Miller & Gerken, *College Algebra*, Section R.1: "Sets and the Real Number Line"
- Miller & Gerken, *College Algebra*, Section 1.7: "Inequalities"
- [[Set_Builder_Notation]] - Alternative representation
- [[Linear_Inequalities]] - Primary application
- [[Domain_and_Range]] - Function applications

---

*Last updated: 2025-10-19*
*Status: Stable ✓*
*Review: Every 2 weeks*
