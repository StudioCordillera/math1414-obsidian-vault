---
layout: concept
title: Root Multiplicity
topic: Polynomials
type: Topic
status: review
importance: high
tags:
- concept/algebra
- chapter-3
- math/polynomials
- method/analyzing
relations:
  broader:
  - '[[Polynomial_Degree_and_Shape]]'
  narrower: []
  depends_on:
  - '[[What_IS_a_Polynomial]]'
  - '[[Factored_Form]]'
  related:
  - '[[End_Behavior]]'
  - '[[Finding_Polynomial_Roots]]'
  - '[[Constructing_Polynomials_from_Roots]]'
  used_in:
  - '[[Graphing_Functions]]'
review:
  next: 2025-11-21
updated: 2025-11-16
qa_certified: true
qa_date: 2025-11-16
qa_migration: v2.0
related:
- '[[Factored_Form]]'
---
# Root Multiplicity
*When Roots Repeat: Understanding Double, Triple, and Higher Multiplicities*

---

## 🎯 CORE INSIGHT

**Multiplicity Determines How Graphs Touch the X-Axis**

When a root appears multiple times in a polynomial, its multiplicity completely changes how the graph behaves at that x-intercept. A simple root crosses through, a double root bounces off, a triple root crosses with a flat point.

**The Pattern:**
```
(x - r)¹ → Cross through (multiplicity 1)
(x - r)² → Bounce/touch (multiplicity 2)
(x - r)³ → Flat cross (multiplicity 3)
(x - r)⁴ → Flat bounce (multiplicity 4)
```

**Why This Matters:**
- Predict graph behavior without plotting
- Understand why some roots "don't look like roots"
- Count total roots including repetitions

**Visual Connection:**
The higher the multiplicity, the "flatter" the graph becomes at that root. Even multiplicities bounce, odd multiplicities cross.

---

## 📐 THE MATHEMATICAL FOUNDATION

### What IS Multiplicity?

**Definition:**  
@MULTIPLICITY = the number of times a particular root appears as a factor

**In Factored Form:**
```
P(x) = (x - 2)³(x + 1)²(x - 5)

Root x = 2 has multiplicity 3
Root x = -1 has multiplicity 2
Root x = 5 has multiplicity 1 (simple root)
```

**Total Degree:** Sum of all multiplicities = 3 + 2 + 1 = 6

### The Fundamental Counting Principle

**Fundamental Theorem of Algebra (Counting Version):**
A polynomial of degree n has EXACTLY n roots when counted with multiplicity.

**Example:** P(x) = (x - 3)²(x + 2)
- Degree: 2 + 1 = 3
- Roots: 3, 3, -2 (three roots total, but only two distinct values)
- Root 3 has multiplicity 2
- Root -2 has multiplicity 1

---

## 🔧 IDENTIFYING MULTIPLICITY

### Method 1: From Factored Form

**Direct Reading:**

Count the exponent on each factor!

**Example:** P(x) = 2(x - 1)⁴(x + 3)²(x - 5)
```
Root x = 1: multiplicity 4
Root x = -3: multiplicity 2
Root x = 5: multiplicity 1
```

**Total degree:** 4 + 2 + 1 = 7 ✓

### Method 2: From Repeated Synthetic Division

**When roots repeat, you can divide again!**

**Example:** Find multiplicity of root x = 2 in P(x) = x³ - 6x² + 12x - 8

```
First division by (x - 2):
     2 |  1   -6   12   -8
       |      2   -8    8
       |__________________
         1   -4    4    0  ← R = 0, so x = 2 is a root!

Quotient: x² - 4x + 4

Second division by (x - 2):
     2 |  1   -4    4
       |      2   -4
       |______________
         1   -2    0  ← R = 0 again!

Quotient: x - 2

Third division by (x - 2):
     2 |  1   -2
       |      2
       |________
         1    0  ← R = 0 again!

Quotient: 1 (constant)
```

**Result:** (x - 2) divides out 3 times → multiplicity 3

P(x) = (x - 2)³

### Method 3: From the Graph

**Visual Inspection:**
- **Crosses x-axis** (passes through): Odd multiplicity (1, 3, 5, ...)
- **Touches and bounces** (tangent): Even multiplicity (2, 4, 6, ...)

**Flatness Indicator:**
- Sharp crossing: multiplicity 1
- Flat crossing: multiplicity 3, 5, 7, ...
- Gentle bounce: multiplicity 2
- Flat bounce: multiplicity 4, 6, 8, ...

---

## 📋 WORKED EXAMPLES

[... retained existing examples ...]

---

## 🔗 CONNECTIONS

**Prerequisites:**
- [[Factored_Form]]
- [[Fundamental_Theorem_of_Algebra]]

**Related Concepts:**
- [[End_Behavior]]
- [[Graphing_Functions]]
- [[Finding_Polynomial_Roots]]

**Applications:**
- [[Constructing_Polynomials_from_Roots]]
- [[Optimization_Problems]]

---

*Remember: Multiplicity isn't just counting—it's the graph's personality at each root.*