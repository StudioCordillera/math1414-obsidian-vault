---
layout: concept
title: "Compound Inequalities"
topic: "General Math"
type: Definition
status: stable
importance: high
tags:
  - concept/inequality
  - algebra/inequalities
  - logic/compound-statements
  - set-theory
sources:
  - textbook-ch1
source_refs:
  - "Miller & Gerken §1.7 p.147-152"
relations:
  broader:
    - "[[Inequalities]]"
    - "[[Compound_Statements]]"
  narrower:
    - "[[Conjunction_Inequality]]"
    - "[[Disjunction_Inequality]]"
  depends_on:
    - "[[Linear_Inequalities]]"
    - "[[Interval_Notation]]"
    - "[[Set_Operations]]"
  defines:
    - "[[AND_Logic]]"
    - "[[OR_Logic]]"
  related:
    - "[[Absolute_Value_Inequalities]]"
    - "[[Union_and_Intersection]]"
    - "[[Number_Line_Representation]]"
  used_in:
    - "[[Absolute_Value_Inequalities]]"
    - "[[Domain_Restrictions]]"
    - "[[Piecewise_Functions]]"
    - "[[Optimization_Problems]]"
review:
  last: 2025-10-19
  next: 2025-11-02
  interval: 14
created: 2025-10-19
updated: 2025-10-19
---

# Compound Inequalities

## Definition

A **compound inequality** is formed by joining two inequalities with the word **"and"** or **"or"**. These logical connectors determine whether solutions must satisfy both inequalities simultaneously or just one of them.

### Two Types

**1. Conjunction (AND)**: Both conditions must be true
- Written as: a < x **and** x < b
- Compact form: a < x < b
- Solution: **Intersection** of individual solution sets

**2. Disjunction (OR)**: At least one condition must be true
- Written as: x < a **or** x > b
- Solution: **Union** of individual solution sets

---

## Type 1: AND Compound Inequalities (Conjunction)

### Definition

**x satisfies both inequalities simultaneously**

### Forms

**Expanded form**: a < x **and** x < b

**Compact form**: a < x < b (most common)

**Meaning**: x is between a and b

### Set Theory Interpretation

**Intersection**: Solution set is the overlap of two solution sets

**A ∩ B** (A "and" B)

---

### Graphical Representation

**Inequality**: -2 < x < 5

**Number line**:
```
     o=========o
    -2         5
```

**Interpretation**: All numbers between -2 and 5 (excluding endpoints)

---

### Solution Method

**Step 1**: Isolate variable in the middle by performing same operation on all three parts

**Step 2**: Express solution in interval notation

**Step 3**: Check solution by testing a value from the solution interval

---

### Examples

#### Example 1: Basic AND Inequality

**Solve**: -3 < x < 7

**Solution**: Already solved!

**Interval notation**: (-3, 7)

**Number line**:
```
     o=========o
    -3         7
```

**Meaning**: x is any number between -3 and 7

---

#### Example 2: Isolating Variable

**Solve**: 1 < 2x + 3 < 11

**Solution**:
```
1 < 2x + 3 < 11           [Given]
1 - 3 < 2x + 3 - 3 < 11 - 3   [Subtract 3 from all parts]
-2 < 2x < 8               [Simplify]
-2/2 < 2x/2 < 8/2         [Divide all parts by 2]
-1 < x < 4                [Solution]
```

**Interval notation**: (-1, 4)

**Check**: Test x = 0 (in the interval):
```
1 < 2(0) + 3 < 11
1 < 3 < 11 ✓ (true)
```

---

#### Example 3: With Negative Coefficient

**Solve**: -6 ≤ -2x < 4

**Solution**:
```
-6 ≤ -2x < 4              [Given]
-6/-2 ≥ -2x/-2 > 4/-2     [Divide by -2, REVERSE inequalities]
3 ≥ x > -2                [Simplify]
-2 < x ≤ 3                [Rewrite in standard form]
```

**Interval notation**: (-2, 3]

**CRITICAL**: When multiplying or dividing by a negative, **reverse BOTH inequality signs**!

---

#### Example 4: Breaking Down Complex AND

**Solve**: x + 2 > 5 and x - 3 < 7

**Solution**:
```
Inequality 1: x + 2 > 5
x > 3

Inequality 2: x - 3 < 7
x < 10

Combined (AND): 3 < x < 10
```

**Interval notation**: (3, 10)

**Number line**:
```
     o==========o
     3         10
```

---

## Type 2: OR Compound Inequalities (Disjunction)

### Definition

**x satisfies at least one of the inequalities**

### Form

**x < a or x > b**

**Meaning**: x is less than a OR greater than b (two separate regions)

### Set Theory Interpretation

**Union**: Solution set combines both solution sets

**A ∪ B** (A "or" B)

---

### Graphical Representation

**Inequality**: x < -2 or x > 5

**Number line**:
```
<====o         o====>
    -2         5
```

**Interpretation**: All numbers less than -2 OR all numbers greater than 5

---

### Solution Method

**Step 1**: Solve each inequality separately

**Step 2**: Express each solution in interval notation

**Step 3**: Combine using union (∪) symbol

**Step 4**: Check solutions by testing values from each region

---

### Examples

#### Example 5: Basic OR Inequality

**Solve**: x < -1 or x > 4

**Solution**: Already solved!

**Interval notation**: (-∞, -1) ∪ (4, ∞)

**Number line**:
```
<====o         o====>
    -1         4
```

**Meaning**: x is less than -1 OR greater than 4

---

#### Example 6: Solving OR Inequality

**Solve**: 2x + 1 < -5 or 3x - 2 > 10

**Solution**:

**Inequality 1**: 2x + 1 < -5
```
2x < -6        [Subtract 1]
x < -3         [Divide by 2]
```

**Inequality 2**: 3x - 2 > 10
```
3x > 12        [Add 2]
x > 4          [Divide by 3]
```

**Combined (OR)**: x < -3 or x > 4

**Interval notation**: (-∞, -3) ∪ (4, ∞)

**Number line**:
```
<====o         o====>
    -3         4
```

---

#### Example 7: OR with ≤ and ≥

**Solve**: x ≤ 2 or x ≥ 5

**Solution**: Already solved!

**Interval notation**: (-∞, 2] ∪ [5, ∞)

**Number line**:
```
<====•         •====>
     2         5
```

**Note**: Endpoints included (solid dots) because of ≤ and ≥

---

## AND vs OR: Visual Comparison

### AND Inequality: Intersection (Overlap)

**-2 < x < 5**

```
Solution set:     o=========o
                 -2         5

Interpretation: Values between -2 and 5 (middle region)
```

**Compact notation**: One continuous interval

---

### OR Inequality: Union (Separate Regions)

**x < -2 or x > 5**

```
Solution set: <===o         o===>
                 -2         5

Interpretation: Values less than -2 OR greater than 5 (two outer regions)
```

**Requires union symbol (∪)**: Two separate intervals

---

## Interval Notation Summary

| Inequality Type | Example | Interval Notation | Number Line |
|----------------|---------|-------------------|-------------|
| **AND (between)** | -2 < x < 5 | (-2, 5) | o====o |
| **AND (inclusive)** | -2 ≤ x ≤ 5 | [-2, 5] | •====• |
| **AND (mixed)** | -2 ≤ x < 5 | [-2, 5) | •====o |
| **OR (outside)** | x < -2 or x > 5 | (-∞, -2) ∪ (5, ∞) | <===o  o===> |
| **OR (inclusive)** | x ≤ -2 or x ≥ 5 | (-∞, -2] ∪ [5, ∞) | <===•  •===> |

---

## Special Cases

### Case 1: AND Results in Empty Set

**Example**: x > 5 and x < 3

**Analysis**: No number can be simultaneously greater than 5 and less than 3

**Solution**: ∅ (empty set) or "No solution"

**Number line**:
```
     <=o         o=>
       3         5
       (no overlap!)
```

---

### Case 2: OR Results in All Real Numbers

**Example**: x < 5 or x > 3

**Analysis**: Every real number is either less than 5 or greater than 3 (or both)

**Solution**: (-∞, ∞) or ℝ (all real numbers)

**Number line**:
```
<=====•===•=====>
      3   5
   (complete coverage)
```

---

### Case 3: Redundant AND

**Example**: x > 2 and x > 5

**Analysis**: If x > 5, then automatically x > 2. The stricter condition (x > 5) dominates.

**Solution**: (5, ∞)

**Simplification**: x > 2 is redundant; solution is just x > 5

---

### Case 4: Redundant OR

**Example**: x < 8 or x < 5

**Analysis**: If x < 5, then automatically x < 8. The less strict condition (x < 8) covers everything.

**Solution**: (-∞, 8)

**Simplification**: x < 5 is included in x < 8; solution is just x < 8

---

## Connection to Absolute Value Inequalities

### |x| < a translates to AND

**|x| < 3** means "distance from 0 less than 3"

**Translation**: -3 < x < 3 (AND inequality)

**Interval**: (-3, 3)

**Number line**:
```
     o=========o
    -3         3
```

See [[Absolute_Value_Inequalities]]

---

### |x| > a translates to OR

**|x| > 3** means "distance from 0 greater than 3"

**Translation**: x < -3 or x > 3 (OR inequality)

**Interval**: (-∞, -3) ∪ (3, ∞)

**Number line**:
```
<====o         o====>
    -3         3
```

---

## Applications

### 1. Domain Restrictions

**Function**: f(x) = 1/[(x - 2)(x + 3)]

**Domain**: x ≠ 2 and x ≠ -3

**In interval form**: (-∞, -3) ∪ (-3, 2) ∪ (2, ∞)

---

### 2. Range Constraints

**Find x such that 0 < x² < 25**

**Solution**:
```
0 < x² < 25
√0 < |x| < √25      [Take square root]
0 < |x| < 5

This means: -5 < x < 0 or 0 < x < 5
Interval: (-5, 0) ∪ (0, 5)
```

---

### 3. Quality Control (Tolerance)

**A part must be 10 ± 0.2 cm**

**Acceptable range**: 9.8 ≤ length ≤ 10.2

**Interval notation**: [9.8, 10.2]

**Compound form**: length ≥ 9.8 AND length ≤ 10.2

---

### 4. Temperature Ranges

**Safe storage**: Temperature between 2°C and 8°C

**Inequality**: 2 ≤ T ≤ 8

**Interval**: [2, 8]

---

## Common Misconceptions

### ❌ Misconception 1: "OR means both conditions"

**Wrong thinking**: x < 3 or x > 7 means x is between 3 and 7

**Reality**: OR means **at least one** condition is true
- x < 3 or x > 7 means x is OUTSIDE the interval [3, 7]
- x is less than 3 OR greater than 7 (not between)

**Remember**: 
- **AND** = intersection (middle, overlap)
- **OR** = union (outer regions, combination)

---

### ❌ Misconception 2: "Can write OR in compact form"

**Wrong**: x < -2 or x > 5 as -2 < x < 5 (or similar compact form)

**Reality**: OR inequalities CANNOT be written in compact form
- AND: a < x < b ✓ (compact form exists)
- OR: must use union: (-∞, a) ∪ (b, ∞) ✓

**Why**: OR represents two separate regions, not one continuous interval

---

### ❌ Misconception 3: "Forgetting to reverse inequality with negatives"

**Wrong**: 
```
-4 < -2x < 6
-4/-2 < x < 6/-2    [Divide by -2]
2 < x < -3          [Wrong! Did not reverse]
```

**Right**:
```
-4 < -2x < 6
-4/-2 > x > 6/-2    [Divide by -2, REVERSE both signs]
2 > x > -3
-3 < x < 2          [Rewrite in standard order]
```

**Remember**: When multiplying/dividing by negative, **flip BOTH inequality signs**

---

### ❌ Misconception 4: "OR means 'exclusive or'"

**Wrong**: x < 3 or x > 7 means x cannot equal 3 or 7

**Reality**: "OR" in mathematics is **inclusive** by default
- At least one condition must be true
- Both conditions CAN be true (though not in this example's case)

**Example where both true**: x > 2 or x > 0
- If x = 5, BOTH conditions are satisfied ✓

---

### ❌ Misconception 5: "Can solve compound inequality by solving separately and combining at end"

**Partially correct**: Works for OR, NOT for AND (compact form)

**OR inequalities**: ✓ Solve each separately, then combine
```
x + 2 < 0  or  x - 3 > 5
x < -2  or  x > 8
Solution: (-∞, -2) ∪ (8, ∞) ✓
```

**AND inequalities (compact form)**: ✗ Must keep compound structure
```
Wrong approach:
1 < 2x + 3 < 11
Solve 1 < 2x + 3: x > -1
Solve 2x + 3 < 11: x < 4
Then combine? x > -1 and x < 4 is -1 < x < 4 ✓ (works, but inefficient)

Right approach:
1 < 2x + 3 < 11
-2 < 2x < 8          [Operate on all three parts at once]
-1 < x < 4           [More direct!]
```

---

## Decision Tree: AND vs OR

### How to Identify Type

**Ask**: "Does x need to satisfy both conditions simultaneously?"

**YES** → AND inequality (intersection)
- Often written in compact form: a < x < b
- Single continuous interval
- Example: 2 < x < 7

**NO** → OR inequality (union)
- Separate regions
- Use union symbol: ∪
- Example: x < 2 or x > 7

---

### Keywords in Word Problems

**AND indicators**:
- "between"
- "within range"
- "at least ___ and at most ___"
- "from ___ to ___"

**OR indicators**:
- "less than ___ or greater than ___"
- "outside the range"
- "not between"
- "either"

---

## Solving Strategy

### For AND Inequalities (Compact Form)

**Step 1**: Ensure all inequality signs point the same direction

**Step 2**: Perform same operation on all three parts

**Step 3**: If multiplying/dividing by negative, reverse ALL signs

**Step 4**: Express in interval notation (single interval)

---

### For OR Inequalities

**Step 1**: Solve each inequality independently

**Step 2**: Express each solution in interval notation

**Step 3**: Combine using union symbol (∪)

**Step 4**: Simplify if possible (check for redundancies)

---

## Connection to Other Concepts

### Builds Upon
- [[Linear_Inequalities]] - Single inequality solving
- [[Interval_Notation]] - Solution set notation
- [[Set_Operations]] - Union and intersection

### Supports
- [[Absolute_Value_Inequalities]] - Translates to compound form
- [[Domain_and_Range]] - Expressing restrictions
- [[Piecewise_Functions]] - Multiple condition definitions
- [[Systems_of_Inequalities]] - Extension to two variables

### Related To
- [[Logic_Statements]] - AND/OR logical connectors
- [[Set_Theory]] - Intersection (∩) and union (∪)
- [[Number_Line_Representation]] - Visual model

### Used In
- **Function domains**: Where function is defined
- **Optimization**: Feasible regions
- **Word problems**: Range constraints
- **Real-world applications**: Temperature ranges, tolerance intervals, safety limits

---

## Practice Problems

### Problem 1
Solve: -5 < x < 3

**Solution**: Already solved!
**Interval notation**: (-5, 3)

---

### Problem 2
Solve: -8 ≤ 2x - 4 < 6

**Solution**:
```
-8 ≤ 2x - 4 < 6
-4 ≤ 2x < 10        [Add 4 to all parts]
-2 ≤ x < 5          [Divide by 2]
```
**Interval notation**: [-2, 5)

---

### Problem 3
Solve: x - 1 < -3 or x + 2 > 7

**Solution**:
```
x - 1 < -3  →  x < -2
x + 2 > 7  →  x > 5
```
**Combined**: x < -2 or x > 5
**Interval notation**: (-∞, -2) ∪ (5, ∞)

---

### Problem 4
Solve: -12 < -3x ≤ 9

**Solution**:
```
-12 < -3x ≤ 9
-12/-3 > x ≥ 9/-3   [Divide by -3, reverse signs]
4 > x ≥ -3
-3 ≤ x < 4          [Rewrite in standard form]
```
**Interval notation**: [-3, 4)

---

### Problem 5
Which type (AND or OR): x < -1 or x > 4

**Answer**: OR inequality (disjunction)
**Interval notation**: (-∞, -1) ∪ (4, ∞)

---

### Problem 6
Which type (AND or OR): -2 ≤ x ≤ 5

**Answer**: AND inequality (conjunction)
**Interval notation**: [-2, 5]

---

## Summary

**Compound inequalities** join two inequalities using **AND** or **OR**:

### AND (Conjunction)
- **Form**: a < x < b (compact) or (x > a and x < b)
- **Meaning**: Both conditions simultaneously
- **Set operation**: Intersection (∩)
- **Result**: Single continuous interval
- **Example**: -3 < x < 7 → (-3, 7)

### OR (Disjunction)
- **Form**: x < a or x > b (no compact form)
- **Meaning**: At least one condition true
- **Set operation**: Union (∪)
- **Result**: Two separate regions
- **Example**: x < -2 or x > 5 → (-∞, -2) ∪ (5, ∞)

**Key differences**:
- **AND** = middle region (between endpoints)
- **OR** = outer regions (outside endpoints)

**Critical rules**:
- ✅ When dividing by negative: reverse BOTH inequality signs (AND)
- ✅ Can write AND in compact form: a < x < b
- ✅ Cannot write OR in compact form: must use ∪
- ✅ Check for redundancies in OR (which condition is less strict?)

**Master compound inequalities**—they're essential for absolute value inequalities and function domains!

---

## References

- Miller & Gerken, *College Algebra*, Section 1.7: "Linear, Compound, and Absolute Value Inequalities"
- [[Linear_Inequalities]] - Foundation
- [[Absolute_Value_Inequalities]] - Primary application
- [[Interval_Notation]] - Solution notation
- [[Set_Operations]] - Union and intersection

---

*Last updated: 2025-10-19*
*Status: Stable ✓*
*Review: Every 2 weeks*
