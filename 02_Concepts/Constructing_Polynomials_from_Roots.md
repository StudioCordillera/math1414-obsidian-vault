---
layout: concept
title: Constructing Polynomials from Roots
topic: Polynomials
type: Method
status: review
importance: high
tags: '- concept/algebra

  - chapter-3

  - math/polynomials

  - method/construction'
sources:
- Textbook Chapter 3
source_refs:
- Ch.3 — Polynomial functions
relations:
  broader:
  - '[[Polynomial_Equations]]'
  narrower: []
  depends_on:
  - '[[Factor_Theorem]]'
  - '[[Complex_Conjugate_Roots]]'
  - '[[Root_Multiplicity]]'
  - '[[Standard_Form]]'
  - '[[Factored_Form]]'
  defines: []
  related:
  - '[[Finding_Polynomial_Roots]]'
  - '[[Graphing_Functions]]'
  - '[[Graphing_Quadratic_Functions]]'
  used_in:
  - '[[Polynomial_Equations]]'
  - '[[Graph_to_Equation]]'
created: 2025-10-21
updated: 2025-11-16
qa_certified: true
qa_date: 2025-11-16
qa_migration: v2.0
defines:
- '[[End_Behavior]]'
related:
- '[[Factor_Theorem]]'
- '[[Polynomial_Degree_and_Shape]]'
- '[[Rational_Root_Theorem]]'
- '[[Root_Multiplicity]]'
- '[[Standard_Form]]'
- '[[Synthetic_Division]]'
- '[[Working_From_Factored_Form]]'
broader:
- '[[Factored_Form]]'
---
# Constructing Polynomials from Given Roots
*Building the Equation from the Solutions*

---

## 🎯 CORE INSIGHT

**Reverse Engineering: From Solutions Back to Equation**

If you know the roots, you can build the polynomial! Each root r gives you a factor (x - r). Multiply all factors together, and you've reconstructed the equation. This is the reverse of solving—instead of finding roots from an equation, you're finding the equation from roots.

**The Pattern:**
```
Root r → Factor (x - r)
All roots → Multiply all factors
Result → The polynomial!
```

**Why This Matters:**
- Essential exam skill: "Write an equation with roots..."
- Understand the root-factor connection deeply
- Create polynomials with specific properties

**The Power:**
You control the degree, the roots, and even complex/real mixtures. It's like being the architect instead of the archaeologist!

---

## 📐 THE MATHEMATICAL FOUNDATION

### The Factor Theorem (Reverse Direction)

**Forward:** If (x - r) is a factor, then r is a root  
**Reverse:** If r is a root, then (x - r) is a factor

**This is your construction tool!**

### The Basic Construction Formula

**For roots r₁, r₂, r₃, ..., rₙ:**
```
P(x) = a(x - r₁)(x - r₂)(x - r₃)···(x - rₙ)
```

Where:
- a = leading coefficient (scaling factor, any nonzero constant)
- Each (x - rᵢ) is a linear factor
- Product gives polynomial of degree n

**Default Choice:** Set a = 1 for simplest polynomial

### Handling Multiplicity

**When roots repeat:**
```
Root r with multiplicity m → Factor (x - r)ᵐ
```

**Example:** Roots 2, 2, 2, -3
```
P(x) = (x - 2)³(x + 3)
```

---

## 🔧 CONSTRUCTION PROCEDURES

### Method 1: Simple Integer Roots

**For distinct integer roots:**

**Step 1:** Write factor for each root
- Root r → Factor (x - r)
- Watch signs! Root -3 → Factor (x - (-3)) = (x + 3)

**Step 2:** Multiply factors together

**Step 3:** Choose leading coefficient (usually a = 1)

**Example:** Roots: 1, -2, 4
```
Factors: (x - 1)(x + 2)(x - 4)

Multiply first two:
(x - 1)(x + 2) = x² + 2x - x - 2 = x² + x - 2

Multiply by third:
(x² + x - 2)(x - 4)
= x³ - 4x² + x² - 4x - 2x + 8
= x³ - 3x² - 6x + 8

Answer: P(x) = x³ - 3x² - 6x + 8
```

---

### Method 2: Including Multiplicity

**For repeated roots:**

**Step 1:** Write each distinct root with its multiplicity as exponent

**Step 2:** Multiply factors

**Example:** Roots: 3 (multiplicity 2), -1, -1, -1
```
P(x) = (x - 3)²(x + 1)³

Expand (x - 3)²:
(x - 3)² = x² - 6x + 9

Expand (x + 1)³:
(x + 1)³ = x³ + 3x² + 3x + 1

Multiply:
P(x) = (x² - 6x + 9)(x³ + 3x² + 3x + 1)
= x⁵ - 3x⁴ - 8x³ + 12x² + 12x + 9
```

---

### Method 3: Complex Conjugate Roots

**CRITICAL RULE:** Real-coefficient polynomials with complex roots MUST include conjugate pairs!

**Step 1:** For each complex root a + bi, include both a + bi and a - bi

**Step 2:** Form quadratic factor from conjugate pair
```
[x - (a + bi)][x - (a - bi)] = x² - 2ax + (a² + b²)
```

**Step 3:** Multiply with other factors

**Example:** Roots: 2, 1 + i

MUST include conjugate: 1 - i

```
P(x) = (x - 2)[x - (1 + i)][x - (1 - i)]

Conjugate pair:
[x - (1 + i)][x - (1 - i)]
= [(x - 1) - i][(x - 1) + i]
= (x - 1)² - i²
= x² - 2x + 1 + 1
= x² - 2x + 2

Full polynomial:
P(x) = (x - 2)(x² - 2x + 2)
     = x³ - 2x² + 2x - 2x² + 4x - 4
     = x³ - 4x² + 6x - 4
```

---

### Method 4: Rational Roots

**For roots as fractions p/q:**

**Option A:** Use factors (x - p/q) and multiply
**Option B:** Clear denominators first: (qx - p)

**Example:** Roots: 1/2, -3/4, 2

**Option A:**
```
P(x) = (x - 1/2)(x + 3/4)(x - 2)
Then clear fractions by multiplying by 4:
P(x) = 4(x - 1/2)(x + 3/4)(x - 2)
     = (2x - 1)(4x + 3)(x - 2) / 1
     = 1/4 · (2x - 1)(4x + 3)(x - 2)

Choosing to clear fractions at start:
P(x) = (2x - 1)(4x + 3)(x - 2)
```

---

## 📋 WORKED EXAMPLES

### Example 1: Basic Construction

**Problem:** Write a polynomial with roots -2, 1, and 5.

**Solution:**
```
P(x) = (x - (-2))(x - 1)(x - 5)
     = (x + 2)(x - 1)(x - 5)

Multiply (x + 2)(x - 1):
= x² - x + 2x - 2 = x² + x - 2

Multiply by (x - 5):
= (x² + x - 2)(x - 5)
= x³ - 5x² + x² - 5x - 2x + 10
= x³ - 4x² - 7x + 10

Answer: P(x) = x³ - 4x² - 7x + 10
```

---

### Example 2: With Multiplicity

**Problem:** Construct a degree 4 polynomial with:
- Root 0 (multiplicity 2)
- Roots ±3

**Solution:**
```
P(x) = x²(x - 3)(x + 3)
     = x²(x² - 9)
     = x⁴ - 9x²

Answer: P(x) = x⁴ - 9x²

Check degree: 2 + 1 + 1 = 4 ✓
```

---

### Example 3: Complex Roots

**Problem:** Write a cubic with roots 2 and 1 - i, passing through (0, 10).

**Solution:**
```
Step 1: Include conjugate
Roots: 2, 1 - i, 1 + i

Step 2: Build factors
P(x) = a(x - 2)[x - (1 - i)][x - (1 + i)]

Step 3: Simplify conjugate pair
[x - (1 - i)][x - (1 + i)]
= [(x - 1) + i][(x - 1) - i]
= (x - 1)² + 1
= x² - 2x + 2

Step 4: Multiply
P(x) = a(x - 2)(x² - 2x + 2)
     = a(x³ - 2x² + 2x - 2x² + 4x - 4)
     = a(x³ - 4x² + 6x - 4)

Step 5: Use point (0, 10) to find a
P(0) = 10
a(0 - 0 + 0 - 4) = 10
-4a = 10
a = -5/2

Answer: P(x) = -5/2(x³ - 4x² + 6x - 4)
       = -5x³/2 + 10x² - 15x + 10
```

---

## 💡 SPECIAL TECHNIQUES

### Creating Polynomials with Specific Properties

**Problem Type:** "Write a quartic that bounces at x = 2 and crosses at x = -3"

**Translation:**
- "Bounces at x = 2" → even multiplicity at 2 → (x - 2)²
- "Crosses at x = -3" → odd multiplicity at 3 → (x + 3)¹
- Degree 4: 2 + 1 = 3, need one more root

**Solution:** P(x) = (x - 2)²(x + 3)(x - r) where r is any value

### Using Y-Intercept to Find Leading Coefficient

**Strategy:**
1. Build P(x) = a(factors) with unknown a
2. Use P(0) = y-intercept to solve for a

**Example:** Roots 1, -2; y-intercept = 6
```
P(x) = a(x - 1)(x + 2)
P(0) = a(-1)(2) = -2a = 6
a = -3

P(x) = -3(x - 1)(x + 2)
     = -3(x² + x - 2)
     = -3x² - 3x + 6
```

---

## ⚠️ COMMON PITFALLS

### Mistake 1: Wrong Sign in Factor
**Error:** Root 5 → Factor (x + 5)  
**Correction:** Root 5 → Factor (x - 5) ✓  
Remember: Factor is (x - root), not (x + root)!

### Mistake 2: Forgetting Conjugate Pairs
**Error:** "Roots: 3, 2 + i" → P(x) = (x - 3)(x - 2 - i)  
**Correction:** MUST include 2 - i for real coefficients ✓

### Mistake 3: Ignoring Multiplicity
**Error:** "Double root at 4" → Factor (x - 4)  
**Correction:** Double root → Factor (x - 4)² ✓

### Mistake 4: Wrong Degree Count
**Error:** "Need degree 5 with roots 1, 2, 3" → (x-1)(x-2)(x-3)  
**Correction:** That's degree 3! Need 2 more roots or multiplicities ✓

---

## 🔗 CONNECTIONS

**Prerequisites:**
- [[Factor_Theorem]] - The root-factor connection
- [[Complex_Conjugate_Roots]] - Why pairs are necessary
- [[Polynomial_Multiplication]] - Expanding factors

**Related Concepts:**
- [[Root_Multiplicity]] - Repeated roots create powers
- [[Finding_Polynomial_Roots]] - The reverse process
- [[Graphing_Polynomials]] - Visualizing your construction

**Applications:**
- [[Modeling_with_Polynomials]] - Creating functions from data points
- [[Interpolation]] - Fitting curves through points
- [[Optimization]] - Designing functions with specific extrema

---

## ✅ Summary
Constructing a polynomial from roots is the reverse of solving: translate each root into a factor, multiply, and apply constraints like leading coefficient or points to determine the scale. Watch for conjugate pairs and multiplicities, verify degree and given conditions, and you’re done.
