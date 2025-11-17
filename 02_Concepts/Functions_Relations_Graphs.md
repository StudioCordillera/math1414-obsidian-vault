---
layout: concept
title: Functions Relations Graphs
topic: Functions
updated: 2025-11-16
qa_certified: true
qa_date: 2025-11-16
qa_migration: v2.0
narrower:
- '[[Average_Rate_of_Change]]'
- '[[Continuity]]'
- '[[Function_Operations]]'
- '[[Function_Transformations]]'
- '[[Graphing_Functions]]'
- '[[Linear_Functions]]'
- '[[Logarithmic_Functions]]'
- '[[Piecewise_Functions]]'
- '[[Rectangular_Coordinate_System]]'
- '[[Secant_Line]]'
- '[[What_IS_a_Function]]'
---
# Functions, Relations, and Graphs
*The Foundation of Mathematical Relationships*

---

## 🎯 CORE INSIGHT

**Functions Are Special Relations That Pass the "One Output Rule"**

Mathematics is about relationships between quantities. A **relation** connects inputs to outputs, but a **function** is a relation with a crucial restriction: each input maps to EXACTLY ONE output. This seemingly simple requirement unlocks powerful tools for modeling real-world phenomena.

**The Pattern:**
```
Relation: Any pairing of inputs and outputs
Function: Each input → exactly one output (no repeats in x-values)
```

**Why This Matters:**
- Functions model predictable systems (every input has a definite result)
- Graphs visualize relationships instantly
- Function notation provides a compact language for mathematics

**The Vertical Line Test:** If any vertical line crosses a graph more than once, it's NOT a function.

---

## 📐 THE MATHEMATICAL FOUNDATION

### What IS a Relation?

**Definition:**  
@RELATION = a set of ordered pairs (x, y), showing how values are related

**Examples:**
```
{(1, 2), (3, 4), (1, 5)}  ← Relation
{(1, 2), (3, 4), (5, 6)}  ← Also a relation (and a function!)
```

**Domain:** All possible x-values (inputs)  
**Range:** All possible y-values (outputs)

**Representations:**
1. **Set notation:** {(x, y) pairs}
2. **Table:** Two columns (x and y)
3. **Graph:** Points plotted on coordinate plane
4. **Mapping diagram:** Arrows from inputs to outputs

### What IS a Function?

**Definition:**  
@FUNCTION = a relation where each input (x-value) corresponds to EXACTLY ONE output (y-value)

**Formal Statement:**  
f: X → Y means "f is a function from set X to set Y"

**The Crucial Restriction:**
```
If (a, b) and (a, c) are both in the relation, then b MUST equal c
```

**Non-Example:**
```
{(2, 3), (2, 5), (4, 7)}  ← NOT a function!
Why? Input 2 maps to both 3 and 5
```

**Example:**
```
{(2, 3), (3, 5), (4, 7)}  ← IS a function
Each x-value appears only once
```

### Function Notation

**Standard Form:** f(x) = [expression]

**Reading:** "f of x equals..."

**Meaning:**
- f = name of the function
- x = input variable
- f(x) = output value

**Example:**
```
f(x) = 2x + 3

f(5) = 2(5) + 3 = 13    "f of 5 equals 13"
f(-1) = 2(-1) + 3 = 1   "f of negative 1 equals 1"
```

**Why This Notation?**
- Compact: f(3) instead of "the output when x = 3"
- Clear: Shows which variable is the input
- Flexible: Can use any letter (g(x), h(t), etc.)


---

## 🔧 DOMAIN AND RANGE

### Finding Domain

**Definition:** Domain = all possible INPUT values (x-values)

**Default Rule:** All real numbers UNLESS there's a restriction

**Common Restrictions:**

| Issue | Restriction | Example |
|-------|-------------|---------|
| **Division by zero** | Denominator ≠ 0 | f(x) = 1/x → Domain: x ≠ 0 |
| **Square root** | Radicand ≥ 0 | f(x) = √x → Domain: x ≥ 0 |
| **Even root** | Expression ≥ 0 | f(x) = √(x-3) → Domain: x ≥ 3 |
| **Logarithm** | Argument > 0 | f(x) = ln(x) → Domain: x > 0 |

**Procedure for Finding Domain:**
1. Identify restrictions (denominators, radicals, logs)
2. Set up inequalities to avoid restrictions
3. Solve inequalities
4. Express in interval notation or set-builder notation

**Example:** Find domain of f(x) = √(x - 2)/(x + 3)
```
Step 1: Restrictions
- Square root: x - 2 ≥ 0
- Denominator: x + 3 ≠ 0

Step 2: Solve
- x ≥ 2
- x ≠ -3

Step 3: Combine
Domain: x ≥ 2  (the x ≠ -3 is automatically satisfied)
Interval notation: [2, ∞)
```

### Finding Range

**Definition:** Range = all possible OUTPUT values (y-values)

**Methods:**
1. **From graph:** Look at y-values covered
2. **Algebraically:** Solve for x in terms of y, find valid y-values
3. **Analysis:** Consider function behavior (min/max, asymptotes)

**Common Ranges:**

| Function Type | Range |
|---------------|-------|
| Linear: f(x) = mx + b | All real numbers (−∞, ∞) |
| Quadratic (opens up): f(x) = x² + k | [k, ∞) |
| Quadratic (opens down): f(x) = -x² + k | (−∞, k] |
| Square root: f(x) = √x | [0, ∞) |
| Absolute value: f(x) = \|x\| | [0, ∞) |
| Rational: f(x) = 1/x | All reals except 0 |

---

## 🎯 TESTING FOR FUNCTIONS

### The Vertical Line Test (VLT)

**Rule:** A graph represents a function IF AND ONLY IF every vertical line crosses it at most once.

**Why It Works:**
- Vertical line at x = a represents all points with that x-value
- If it crosses twice, that x-value has two y-values → NOT a function

**Examples:**
```
Circle: x² + y² = 1
VLT: FAILS (vertical line crosses twice)
Conclusion: NOT a function

Parabola: y = x²
VLT: PASSES (every vertical line crosses once)
Conclusion: IS a function
```

### The Horizontal Line Test (HLT)

**Purpose:** Determines if a function is ONE-TO-ONE (injective)

**Rule:** A function is one-to-one IF every horizontal line crosses its graph at most once.

**Meaning:**
- One-to-one: Different inputs → different outputs
- If f(a) = f(b), then a = b

**Why It Matters:** One-to-one functions have inverses that are also functions.

**Example:**
```
f(x) = x² 
HLT: FAILS (horizontal line y = 4 crosses at x = ±2)
Conclusion: NOT one-to-one

g(x) = x³
HLT: PASSES (every horizontal line crosses once)
Conclusion: IS one-to-one
```

---

## 📋 FUNCTION EVALUATION

### Direct Substitution

**Process:** Replace every instance of the variable with the given value.

**Example:** f(x) = 3x² - 2x + 1, find f(4)
```
f(4) = 3(4)² - 2(4) + 1
     = 3(16) - 8 + 1
     = 48 - 8 + 1
     = 41
```

### Composite Evaluation

**For expressions like f(a + h):**

**Example:** f(x) = x² + 2x, find f(x + h)
```
f(x + h) = (x + h)² + 2(x + h)
         = x² + 2xh + h² + 2x + 2h
         = x² + 2xh + h² + 2x + 2h
```

### The Difference Quotient

**Formula:** [f(x + h) - f(x)]/h

**Purpose:** Foundation of calculus (represents average rate of change)

**Example:** f(x) = x², find difference quotient
```
[f(x + h) - f(x)]/h = [(x + h)² - x²]/h
                     = [x² + 2xh + h² - x²]/h
                     = [2xh + h²]/h
                     = h(2x + h)/h
                     = 2x + h
```


---

## 🔧 SPECIAL FUNCTION TYPES

### Piecewise Functions

**Definition:** Function defined by different formulas on different intervals

**General Form:**
```
f(x) = { expression₁,  if condition₁
       { expression₂,  if condition₂
       { expression₃,  if condition₃
```

**Example:**
```
f(x) = { x + 2,    if x < 0
       { x²,       if 0 ≤ x < 3
       { 2x - 1,   if x ≥ 3
```

**Evaluation:**
```
f(-2) = -2 + 2 = 0         (use first piece, since -2 < 0)
f(1) = 1² = 1              (use second piece, since 0 ≤ 1 < 3)
f(5) = 2(5) - 1 = 9        (use third piece, since 5 ≥ 3)
```

**Common Piecewise Function:** Absolute Value
```
|x| = { x,   if x ≥ 0
      { -x,  if x < 0
```

### Even and Odd Functions

**Even Function:** f(-x) = f(x) for all x
- **Symmetry:** Reflects across y-axis
- **Example:** f(x) = x², f(x) = cos(x), f(x) = |x|

**Odd Function:** f(-x) = -f(x) for all x
- **Symmetry:** Rotates 180° around origin
- **Example:** f(x) = x³, f(x) = sin(x), f(x) = 1/x

**Test:**
```
For f(x) = x²:
f(-x) = (-x)² = x² = f(x) → EVEN

For f(x) = x³:
f(-x) = (-x)³ = -x³ = -f(x) → ODD
```

---

## 📊 GRAPHING FUNDAMENTALS

### Key Points to Plot

**Intercepts:**
- **x-intercept:** Where graph crosses x-axis (set y = 0)
- **y-intercept:** Where graph crosses y-axis (set x = 0)

**Example:** y = 2x - 4
```
x-intercept: 0 = 2x - 4 → x = 2  →  (2, 0)
y-intercept: y = 2(0) - 4 → y = -4  →  (0, -4)
```

### Function Transformations

**Vertical Shifts:** f(x) + k
- k > 0: Shift UP k units
- k < 0: Shift DOWN |k| units

**Horizontal Shifts:** f(x - h)
- h > 0: Shift RIGHT h units
- h < 0: Shift LEFT |h| units

**Vertical Stretch/Compression:** a·f(x)
- |a| > 1: Stretch (taller)
- 0 < |a| < 1: Compression (shorter)
- a < 0: Reflection across x-axis

**Horizontal Stretch/Compression:** f(bx)
- |b| > 1: Compression (narrower)
- 0 < |b| < 1: Stretch (wider)
- b < 0: Reflection across y-axis

**Combined:** f(x) = a·f(b(x - h)) + k
1. Horizontal shift by h
2. Horizontal stretch/compress by 1/b
3. Vertical stretch/compress by a
4. Vertical shift by k

---

## 📋 WORKED EXAMPLES

### Example 1: Identifying Functions

**Problem:** Which are functions?
A) {(1,2), (2,3), (1,4)}
B) {(1,2), (2,3), (3,4)}

**Solution:**
```
A) Input 1 appears twice with different outputs (2 and 4)
   NOT a function ✗

B) Each input appears exactly once
   IS a function ✓
```

---

### Example 2: Finding Domain and Range

**Problem:** Find domain and range of f(x) = √(x + 3)

**Solution:**
```
Domain:
Square root requires: x + 3 ≥ 0
                      x ≥ -3
Domain: [-3, ∞)

Range:
Square root outputs are ≥ 0
As x increases from -3, f(x) increases from 0
Range: [0, ∞)
```

---

### Example 3: Function Evaluation

**Problem:** f(x) = 2x² - 3x + 1, find f(-2) and f(a+1)

**Solution:**
```
f(-2) = 2(-2)² - 3(-2) + 1
      = 2(4) + 6 + 1
      = 8 + 6 + 1
      = 15

f(a+1) = 2(a+1)² - 3(a+1) + 1
       = 2(a² + 2a + 1) - 3a - 3 + 1
       = 2a² + 4a + 2 - 3a - 3 + 1
       = 2a² + a
```

---

### Example 4: Piecewise Function Evaluation

**Problem:** 
```
f(x) = { 2x + 1,    if x < 0
       { x² - 1,    if x ≥ 0
```
Find f(-3), f(0), f(4)

**Solution:**
```
f(-3): Use first piece (since -3 < 0)
     = 2(-3) + 1 = -6 + 1 = -5

f(0): Use second piece (since 0 ≥ 0)
    = 0² - 1 = -1

f(4): Use second piece (since 4 ≥ 0)
    = 4² - 1 = 16 - 1 = 15
```

---

### Example 5: Vertical Line Test

**Problem:** Does the circle x² + y² = 25 represent a function?

**Solution:**
```
Test a vertical line, say x = 0:
0² + y² = 25
y² = 25
y = ±5

The line x = 0 crosses at (0, 5) and (0, -5) → TWO points

Conclusion: FAILS vertical line test → NOT a function
```

---

## ⚠️ COMMON PITFALLS

### Mistake 1: Confusing Domain Restrictions
**Error:** "√(x-2) has domain x > 2"  
**Correction:** Domain is x ≥ 2 (can equal 2, gives √0 = 0) ✓

### Mistake 2: Wrong Horizontal Shift Direction
**Error:** f(x - 3) shifts left 3  
**Correction:** f(x - 3) shifts RIGHT 3 (opposite of sign) ✓

### Mistake 3: Mixing Up Intercepts
**Error:** "x-intercept is where x = 0"  
**Correction:** x-intercept is where y = 0 (crosses x-axis) ✓

### Mistake 4: Function Notation Confusion
**Error:** f(x + 2) = f(x) + 2  
**Correction:** Must substitute: f(x+2) = entire formula with (x+2) replacing x ✓

### Mistake 5: Assuming All Relations Are Functions
**Error:** "Every graph is a function"  
**Correction:** Only graphs that pass vertical line test are functions ✓

---

## 🔗 CONNECTIONS

**Prerequisites:**
- [[Coordinate_Plane]] - Plotting points
- [[Ordered_Pairs]] - Understanding (x, y)
- [[Set_Notation]] - Expressing domains/ranges

**Related Concepts:**
- [[Linear_Functions]] - Simplest function type
- [[Quadratic_Functions]] - Parabolas
- [[Inverse_Functions]] - Reversing input/output
- [[Composition_of_Functions]] - Combining functions

**Applications:**
- [[Modeling_Real_World]] - Functions represent relationships
- [[Graphing_Techniques]] - Visual representation
- [[Calculus_Foundations]] - Limits, derivatives built on functions

---

## 🎓 EXAM STRATEGIES

### Quick Identification
- **Function test:** Check for repeated x-values
- **Domain:** Look for denominators, radicals, logs
- **Range:** Analyze graph or function behavior

### Common Question Types
1. "Is this a function?" → VLT or check ordered pairs
2. "Find domain" → Identify restrictions
3. "Evaluate f(a)" → Direct substitution
4. "Graph transformation" → Apply shift/stretch rules

### Time-Savers
- **VLT:** Faster than checking all ordered pairs
- **Domain patterns:** Memorize common restrictions
- **Piecewise:** Check which piece applies first

---

*Remember: Functions are the backbone of mathematics. Master the "one output per input" rule, and everything else—from graphing to calculus—builds naturally on this foundation!*
