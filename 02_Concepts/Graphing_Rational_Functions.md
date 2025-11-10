---
layout: concept
title: "Graphing Rational Functions"
topic: "Functions"
---

# Graphing Rational Functions
*Understanding Asymptotes, Holes, and Discontinuities*

---

## 🎯 CORE INSIGHT

**Rational Functions are Fractions with Personality Disorders**

A rational function is just P(x)/Q(x), but this simple division creates dramatic behavior: vertical lines the graph can never cross, horizontal lines it approaches but never quite reaches, and mysterious holes where points vanish.

**The Pattern:**
```
f(x) = P(x)/Q(x) where P and Q are polynomials, Q(x) ≠ 0

Key features:
- Vertical asymptotes where Q(x) = 0 (denominator blows up)
- Horizontal/oblique asymptotes (end behavior)
- Holes where factors cancel
- X-intercepts where P(x) = 0 (numerator = 0)
```

**Why This Matters:**
Division by zero creates infinity. Understanding where and how this happens reveals the entire structure of rational function graphs.

---

## 📐 THE FOUNDATIONAL CONCEPTS

### What Causes What

**Vertical Asymptotes (VA):**  
Occur where denominator = 0 but numerator ≠ 0  
**Cause:** Division by zero → function value → ±∞  
**Graph:** Vertical line x = a that graph approaches but never touches

**Horizontal Asymptotes (HA):**  
Determined by degrees of numerator and denominator  
**Cause:** End behavior as x → ±∞  
**Graph:** Horizontal line y = b that graph approaches at edges

**Holes (Removable Discontinuities):**  
Occur where BOTH numerator and denominator = 0  
**Cause:** Common factor cancels, leaves gap  
**Graph:** Open circle—function undefined at that point

**X-Intercepts:**  
Where numerator = 0 and denominator ≠ 0  
**Cause:** Zero divided by nonzero = 0  
**Graph:** Function crosses x-axis

**Y-Intercept:**  
Value at x = 0 (if defined)  
**Cause:** Substitute x = 0  
**Graph:** Where function crosses y-axis

---

## 🔧 FINDING VERTICAL ASYMPTOTES

**Algorithm:**

**Step 1:** Factor numerator and denominator completely  
**Step 2:** Cancel any common factors (these create holes)  
**Step 3:** Set remaining denominator = 0  
**Step 4:** Solve for x  
**Step 5:** These x-values are vertical asymptotes

**Example:**
```
f(x) = (x² - 4)/(x² - x - 6)

Step 1: Factor
= (x - 2)(x + 2) / (x - 3)(x + 2)

Step 2: Cancel (x + 2)
= (x - 2)/(x - 3), with hole at x = -2

Step 3: Remaining denominator
x - 3 = 0

Step 4: Vertical asymptote at x = 3
```

**Behavior near VA:**
- As x → 3⁻ (from left): f(x) → +∞ or -∞
- As x → 3⁺ (from right): f(x) → -∞ or +∞
- Signs opposite on each side

---

## 🔧 FINDING HORIZONTAL ASYMPTOTES

**Three Cases Based on Degrees:**

Let n = degree of numerator, m = degree of denominator

### Case 1: n < m (bottom heavier)
**HA:** y = 0 (x-axis)  
**Reason:** Denominator grows faster, fraction → 0

### Case 2: n = m (same degree)
**HA:** y = ratio of leading coefficients  
**Formula:** y = aₙ/bₘ

### Case 3: n > m (top heavier)
**HA:** None (oblique asymptote possible if n = m + 1)  
**Reason:** Numerator grows faster, no horizontal limit

**Example:**
```
f(x) = (3x² - 5x + 1)/(x² + 2x - 3)

Degree of num = 2
Degree of denom = 2

Case 2: Same degree
HA: y = 3/1 = 3
```

---

## 🔧 FINDING HOLES

**Algorithm:**

**Step 1:** Factor numerator and denominator  
**Step 2:** Identify common factors  
**Step 3:** Cancel common factors  
**Step 4:** Set cancelled factor = 0 to find x-coordinate  
**Step 5:** Substitute into reduced function to find y-coordinate  
**Step 6:** Hole is at (x, y)

**Example:**
```
f(x) = (x² - x - 6)/(x² - 9)

Step 1: Factor
= (x - 3)(x + 2) / (x - 3)(x + 3)

Step 2: Common factor: (x - 3)

Step 3: Cancel
= (x + 2)/(x + 3), x ≠ 3

Step 4: x-coordinate of hole
x - 3 = 0 → x = 3

Step 5: Substitute x = 3 into reduced function
y = (3 + 2)/(3 + 3) = 5/6

Step 6: Hole at (3, 5/6)
```

---

## 🔧 FINDING INTERCEPTS

### X-Intercepts

**Step 1:** Set numerator = 0  
**Step 2:** Solve for x  
**Step 3:** Verify denominator ≠ 0 at those x-values  
**Step 4:** X-intercepts at those points

**Example:**
```
f(x) = (x² - 4)/(x - 1)

Numerator: x² - 4 = 0
x = ±2

Check denominator:
At x = 2: 2 - 1 = 1 ≠ 0 ✓
At x = -2: -2 - 1 = -3 ≠ 0 ✓

X-intercepts: (2, 0) and (-2, 0)
```

### Y-Intercept

**Step 1:** Substitute x = 0  
**Step 2:** Simplify

**Example:**
```
f(x) = (x² - 4)/(x - 1)

f(0) = (0 - 4)/(0 - 1) = -4/-1 = 4

Y-intercept: (0, 4)
```

---

## 📋 COMPLETE GRAPHING PROCEDURE

**Step-by-Step Workflow:**

```
1. FACTOR COMPLETELY
   Numerator and denominator

2. CANCEL COMMON FACTORS
   → Note holes

3. FIND VERTICAL ASYMPTOTES
   Set reduced denominator = 0

4. FIND HORIZONTAL ASYMPTOTE
   Compare degrees

5. FIND INTERCEPTS
   • X-intercepts: numerator = 0
   • Y-intercept: f(0)

6. TEST SIGNS IN EACH REGION
   Pick test points between asymptotes

7. PLOT KEY FEATURES
   Asymptotes (dashed lines)
   Holes (open circles)
   Intercepts (solid points)

8. SKETCH CURVE
   Approach asymptotes properly
   Connect through regions
```

---

## 🎓 WORKED EXAMPLE

**Problem:** Graph f(x) = (x² - x - 2)/(x² - 4)

**Solution:**

```
Step 1: Factor
f(x) = (x - 2)(x + 1) / (x - 2)(x + 2)

Step 2: Cancel common factor
f(x) = (x + 1)/(x + 2), x ≠ 2
Hole at x = 2

Step 3: Find y-coordinate of hole
f(2) = (2 + 1)/(2 + 2) = 3/4
Hole at (2, 3/4)

Step 4: Vertical asymptote
x + 2 = 0 → x = -2

Step 5: Horizontal asymptote
Degrees equal (both 1 after canceling)
HA: y = 1/1 = 1

Step 6: X-intercept
x + 1 = 0 → x = -1
X-intercept: (-1, 0)

Step 7: Y-intercept
f(0) = (0 + 1)/(0 + 2) = 1/2
Y-intercept: (0, 1/2)

Step 8: Test regions
Region x < -2: Try x = -3
f(-3) = -2/-1 = 2 (positive, above HA)

Region -2 < x < -1: Try x = -1.5
f(-1.5) = -0.5/0.5 = -1 (negative)

Region x > -1: Try x = 0
f(0) = 1/2 (positive)
```

**Final Graph Features:**
- VA: x = -2 (dashed vertical line)
- HA: y = 1 (dashed horizontal line)
- Hole: (2, 3/4) open circle
- X-int: (-1, 0)
- Y-int: (0, 1/2)

---

## ⚠️ COMMON PITFALLS

### Mistake 1: Forgetting to Factor Before Finding Asymptotes
**Error:** Setting x² - 4 = 0 without factoring  
**Correction:** Factor first, cancel, THEN find asymptotes ✓

### Mistake 2: Confusing Holes with Asymptotes
**Error:** Treating a cancelled factor as a vertical asymptote  
**Correction:** Cancelled factors = holes, remaining zeros = VAs ✓

### Mistake 3: Wrong Horizontal Asymptote
**Error:** Always thinking HA is y = 0  
**Correction:** Check degrees! Equal degrees → ratio of leading coefficients ✓

### Mistake 4: Drawing Through Asymptotes
**Error:** Graph crosses vertical asymptote  
**Correction:** Graph APPROACHES but NEVER touches VA ✓

---

## 🔗 CONNECTIONS

**Prerequisites:**
- [[Polynomial_Division]] - For reducing fractions
- [[Factoring]] - Essential for finding features
- [[End_Behavior]] - For understanding horizontal asymptotes

**Related Concepts:**
- [[Limits]] - Formal definition of asymptotic behavior
- [[Discontinuities]] - Types of breaks in functions
- [[Domain_and_Range]] - Restricted by asymptotes

**Applications:**
- [[Optimization]] - Many real-world ratios
- [[Partial_Fractions]] - Decomposition technique

---

*Remember: Rational functions are all about division by zero. Find where it happens (VAs), where it almost happens (holes), and what happens at infinity (HAs)!*
