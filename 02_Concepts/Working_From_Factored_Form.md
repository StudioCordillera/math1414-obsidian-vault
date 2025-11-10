---
title: Working From Factored Form (Polynomials)
type: Method
status: review
importance: high
tags:
  - node/method
  - status/review
  - pedagogy/pattern
  - domain/analysis
relations:
  broader: ["[[Factored_Form]]"]
  narrower: []
  depends_on: ["[[Zero_Product_Property]]", "[[Root_Multiplicity]]", "[[End_Behavior]]"]
  defines: []
  related: ["[[Standard_Form]]", "[[Graphing_Functions]]", "[[Constructing_Polynomials_from_Roots]]"]
  used_in: ["[[Finding_Polynomial_Roots]]", "[[Polynomial_and_Rational_Inequalities]]"]
sources: []
source_refs: []
created: 2025-10-21
updated: 2025-10-21
---

# Working From Factored Form
*When You Start With Factors: A Complete Guide*

---

## 🎯 CORE INSIGHT

**Factored Form is the Most Information-Rich Representation**

When a polynomial is given in factored form, you can instantly read:
- Every root (set each factor = 0)
- The degree (count all factors)
- The multiplicity (count repeated factors)
- The leading coefficient (multiply all leading terms)

**The Pattern:**
```
f(x) = a(x - r₁)ᵐ¹(x - r₂)ᵐ²...(x - rₖ)ᵐᵏ

Immediately visible:
- Roots: r₁, r₂, ..., rₖ
- Multiplicities: m₁, m₂, ..., mₖ
- Degree: m₁ + m₂ + ... + mₖ
- Leading coefficient: a
```

**Why This Matters:**
Factored form is your END GOAL when solving, but it's also a powerful STARTING POINT. You can transform it to any other form or extract any feature.

---

## 📐 READING FACTORED FORM

### Anatomy of Factored Form

**General Structure:**
```
f(x) = a(x - r₁)(x - r₂)...(x - rₙ)
       ↑    ↑      ↑          ↑
       |    |      |          └─ Root n
       |    |      └─ Root 2
       |    └─ Root 1
       └─ Leading coefficient (vertical stretch/compression + reflection)
```

### Extracting Information Directly

**1. Finding Roots (x-intercepts):**
Set each factor = 0:
- From (x - 3): x = 3
- From (x + 2): x = -2
- From (x - 0) or (x): x = 0

**2. Identifying Multiplicity:**
Count exponents on each factor:
- (x - 2)¹ → multiplicity 1 (odd → crosses x-axis)
- (x + 1)² → multiplicity 2 (even → touches x-axis)
- (x - 4)³ → multiplicity 3 (odd → crosses with inflection)

**3. Determining Degree:**
Sum all exponents:
```
f(x) = (x - 1)²(x + 3)(x - 5)³
Degree = 2 + 1 + 3 = 6
```

**4. Finding Y-intercept:**
Substitute x = 0:
```
f(x) = 2(x - 3)(x + 1)
f(0) = 2(0 - 3)(0 + 1) = 2(-3)(1) = -6
Y-intercept: (0, -6)
```

---

## 🔧 TRANSFORMATIONS FROM FACTORED FORM

### Factored → Standard Form

**Method: Expand systematically**

**Step 1:** Multiply first two factors
**Step 2:** Multiply result by next factor
**Step 3:** Repeat until all factors used
**Step 4:** Distribute leading coefficient

**Example:**
```
f(x) = 2(x - 1)(x + 3)(x - 2)

Step 1: (x - 1)(x + 3)
= x² + 3x - x - 3
= x² + 2x - 3

Step 2: (x² + 2x - 3)(x - 2)
= x³ - 2x² + 2x² - 4x - 3x + 6
= x³ - 7x + 6

Step 3: Multiply by 2
f(x) = 2x³ - 14x + 12
```

### Factored → Vertex Form (Quadratics only)

**For f(x) = a(x - r₁)(x - r₂):**

**Step 1:** Find axis of symmetry
```
h = (r₁ + r₂)/2
```

**Step 2:** Evaluate f(h) to get k
```
k = f(h)
```

**Step 3:** Write vertex form
```
f(x) = a(x - h)² + k
```

**Example:**
```
f(x) = 2(x - 1)(x - 5)

Step 1: h = (1 + 5)/2 = 3
Step 2: k = f(3) = 2(3 - 1)(3 - 5) = 2(2)(-2) = -8
Step 3: f(x) = 2(x - 3)² - 8
```

### Factored → Graph

**Direct Graphing Procedure:**

**Step 1:** Plot roots on x-axis
- Mark each x-intercept
- Note multiplicity (cross vs touch)

**Step 2:** Plot y-intercept
- Evaluate f(0)

**Step 3:** Determine end behavior
- Use degree + leading coefficient sign

**Step 4:** Identify turning points
- Between each pair of roots
- Maximum of (degree - 1) turns

**Step 5:** Sketch curve
- Start from left end behavior
- Pass through roots respecting multiplicity
- Connect smoothly through turning points
- End with right end behavior

---

## 📋 WORKED EXAMPLES

### Example 1: Complete Analysis from Factored Form

**Given:** f(x) = -2(x + 3)(x - 1)²(x - 4)

**Analysis:**

**Roots:**
- x = -3 (multiplicity 1, crosses)
- x = 1 (multiplicity 2, touches)
- x = 4 (multiplicity 1, crosses)

**Degree:** 1 + 2 + 1 = 4 (even)

**Leading Coefficient:** -2 (negative)

**End Behavior:**
- Even degree + negative LC → both ends down (∩ shape)

**Y-intercept:**
```
f(0) = -2(0 + 3)(0 - 1)²(0 - 4)
     = -2(3)(1)(-4)
     = 24
Point: (0, 24)
```

**Maximum Turning Points:** 4 - 1 = 3

---

### Example 2: Factored → Standard Form

**Given:** f(x) = 3(x - 2)(x + 1)(x - 5)

**Solution:**
```
Step 1: (x - 2)(x + 1)
= x² + x - 2x - 2
= x² - x - 2

Step 2: (x² - x - 2)(x - 5)
= x³ - 5x² - x² + 5x - 2x + 10
= x³ - 6x² + 3x + 10

Step 3: Multiply by 3
f(x) = 3x³ - 18x² + 9x + 30
```

**Verify y-intercept:**
- From factored: f(0) = 3(-2)(1)(-5) = 30 ✓
- From standard: f(0) = 30 ✓

---

### Example 3: Factored → Vertex Form (Quadratic)

**Given:** f(x) = -3(x - 4)(x + 2)

**Solution:**
```
Step 1: Axis of symmetry
h = (4 + (-2))/2 = 2/2 = 1

Step 2: Find k
k = f(1) = -3(1 - 4)(1 + 2)
         = -3(-3)(3)
         = 27

Step 3: Vertex form
f(x) = -3(x - 1)² + 27
```

**Verify:** Vertex at (1, 27) ✓

---

## 💡 SPECIAL CASES

### Complex Factors

**If complex roots given in factored form:**
```
f(x) = (x - (2 + 3i))(x - (2 - 3i))
```

**Convert to real quadratic factor:**
```
= [(x - 2) - 3i][(x - 2) + 3i]
= (x - 2)² - (3i)²
= (x - 2)² + 9
= x² - 4x + 13
```

### Repeated Linear Factors

**Multiplicity > 1:**
```
f(x) = (x - 3)⁴
```

**To standard form:** Use binomial expansion or repeated multiplication
```
(x - 3)² = x² - 6x + 9
(x - 3)² · (x - 3)² = (x² - 6x + 9)²
```

---

## ⚠️ COMMON PITFALLS

### Mistake 1: Sign Errors in Roots
**Error:** From (x - 3), thinking root is -3  
**Correction:** Set factor = 0 → x - 3 = 0 → x = 3 ✓

### Mistake 2: Forgetting Leading Coefficient
**Error:** Expanding (x - 1)(x + 2) and forgetting the 3 in front  
**Correction:** Always multiply final result by leading coefficient ✓

### Mistake 3: Multiplicity Confusion
**Error:** (x - 2)² means x = 2 twice, so two different roots  
**Correction:** One root (x = 2) with multiplicity 2 ✓

### Mistake 4: Y-intercept Calculation
**Error:** Forgetting to include all factors when evaluating f(0)  
**Correction:** Substitute x = 0 into ENTIRE factored form ✓

---

## 🔗 CONNECTIONS

**Prerequisites:**
- [[Factoring_Polynomials]] - How to GET to factored form
- [[Root_Multiplicity]] - Understanding repeated roots

**Related Concepts:**
- [[Constructing_Polynomials_from_Roots]] - Reverse process
- [[Graphing_Polynomials]] - Using factored form to graph
- [[Standard_Form]] - Converting to standard form

**Applications:**
- [[Finding_Polynomial_Roots]] - Factored form reveals all roots
- [[End_Behavior]] - Degree and LC visible in factored form
- [[Optimization]] - Finding vertex from factored quadratic

---

## 🎓 EXAM STRATEGIES

### Quick Feature Extraction
1. **Need roots?** Read them directly (set factors = 0)
2. **Need degree?** Add up all exponents
3. **Need y-intercept?** Plug in x = 0
4. **Need end behavior?** Check degree (even/odd) and leading coeff (±)

### Conversion Strategy
- **To standard:** Expand methodically, left to right
- **To vertex (quadratic):** Find midpoint of roots
- **To graph:** Plot roots, mark multiplicity, use end behavior

### Verification Checks
- Y-intercept should match in all forms
- Roots should be same in all forms
- Degree should be consistent

---

*Remember: Factored form is information-rich! Extract what you need directly before converting to other forms.*
