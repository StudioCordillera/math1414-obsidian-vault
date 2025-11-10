# Exam Practice Problem Sets
*Organized by Topic with Solutions*

---

## 🎯 PURPOSE

This is your practice problem bank, organized by exam topic. Each problem includes:
- Full solution with explanation
- Common mistakes to avoid
- Which entry to reference if stuck

**Use this for:**
- Last-minute practice
- Identifying weak areas
- Building confidence

---

## 📚 TOPIC 1: COMPLETING THE SQUARE

### Problem 1.1 (Basic)
**Question:** Complete the square for f(x) = x² + 6x + 2

**Solution:**
```
Step 1: Identify b = 6
Step 2: Calculate (b/2)² = (6/2)² = 9
Step 3: Add and subtract inside
f(x) = x² + 6x + 9 - 9 + 2
Step 4: Factor perfect square
f(x) = (x + 3)² - 7

Vertex: (-3, -7)
```

**Common Mistake:** Forgetting to subtract the 9 you added
**Reference:** [[Completing_the_Square]]

---

### Problem 1.2 (With Leading Coefficient)
**Question:** Complete the square for f(x) = 3x² - 12x + 5

**Solution:**
```
Step 1: Factor out a = 3 from x-terms
f(x) = 3(x² - 4x) + 5

Step 2: Complete square inside parentheses
Half of -4 is -2, squared is 4
f(x) = 3(x² - 4x + 4) + 5 - 3(4)
f(x) = 3(x² - 4x + 4) + 5 - 12

Step 3: Factor and simplify
f(x) = 3(x - 2)² - 7

Vertex: (2, -7)
```

**Common Mistake:** Forgetting to multiply the subtracted term by 'a'
**Check:** 3(4) = 12, not just 4!

---

### Problem 1.3 (Tricky)
**Question:** Complete the square for f(x) = -2x² + 8x - 3

**Solution:**
```
Step 1: Factor out a = -2
f(x) = -2(x² - 4x) - 3

Step 2: Complete square
Half of -4 is -2, squared is 4
f(x) = -2(x² - 4x + 4) - 3 - (-2)(4)
f(x) = -2(x² - 4x + 4) - 3 + 8

Step 3: Simplify
f(x) = -2(x - 2)² + 5

Vertex: (2, 5) [maximum since a < 0]
```

**Common Mistake:** Sign error with negative leading coefficient

---

## 📚 TOPIC 2: DISCRIMINANT

### Problem 2.1 (Classification)
**Question:** Classify roots of 2x² - 5x + 1 = 0

**Solution:**
```
Δ = b² - 4ac = (-5)² - 4(2)(1) = 25 - 8 = 17

Δ = 17 > 0 → Two distinct real roots
Is 17 a perfect square? No
Therefore: Two irrational roots

Roots will involve √17
```

**Reference:** [[The_Discriminant]]

---

### Problem 2.2 (Finding Condition)
**Question:** For what value of k does x² + kx + 9 = 0 have exactly one real root?

**Solution:**
```
One real root means Δ = 0

Δ = k² - 4(1)(9) = 0
k² - 36 = 0
k² = 36
k = ±6

Answer: k = 6 or k = -6
```

**Common Mistake:** Forgetting k can be negative

---

### Problem 2.3 (Complex Prediction)
**Question:** Without solving, determine if x² + 4x + 13 = 0 has real or complex roots

**Solution:**
```
Δ = (4)² - 4(1)(13) = 16 - 52 = -36

Δ < 0 → Two complex conjugate roots

The roots will be: -2 ± 3i
(though we didn't need to calculate them)
```

**Key Insight:** Negative discriminant ALWAYS means complex roots

---

## 📚 TOPIC 3: SYNTHETIC DIVISION

### Problem 3.1 (Basic Division)
**Question:** Divide P(x) = x³ + 2x² - 5x - 6 by (x - 2)

**Solution:**
```
Setup:
    2 | 1   2  -5  -6
      |     2   8   6
      |________________
        1   4   3   0
        
Quotient: x² + 4x + 3
Remainder: 0

Since R = 0, (x - 2) is a factor!
P(x) = (x - 2)(x² + 4x + 3)
     = (x - 2)(x + 1)(x + 3)

All roots: x = 2, -1, -3
```

**Reference:** [[Synthetic_Division]]

---

### Problem 3.2 (Testing for Factor)
**Question:** Is (x + 3) a factor of x³ - 27?

**Solution:**
```
Rewrite: (x + 3) = (x - (-3)), so c = -3
Fill in missing terms: x³ + 0x² + 0x - 27

   -3 | 1   0    0  -27
      |    -3    9  -27
      |__________________
        1  -3    9  -54
        
Remainder: -54 ≠ 0

No, (x + 3) is NOT a factor

Note: x³ - 27 = (x - 3)(x² + 3x + 9)
```

**Common Mistake:** Using c = 3 instead of c = -3

---

### Problem 3.3 (Using Remainder Theorem)
**Question:** Find P(-2) where P(x) = 2x⁴ - x³ + 3x - 7

**Solution:**
```
Use synthetic division with c = -2

   -2 | 2  -1   0   3  -7
      |   -4  10 -20  34
      |___________________
        2  -5  10 -17  27
        
P(-2) = 27

Verify by direct substitution:
P(-2) = 2(16) - (-8) + 3(-2) - 7
      = 32 + 8 - 6 - 7
      = 27 ✓
```

**Key Insight:** Remainder = function value!

---

## 📚 TOPIC 4: COMPLEX CONJUGATE ROOTS

### Problem 4.1 (Finding Conjugate)
**Question:** If 2 - 5i is a root of a polynomial with real coefficients, what other root must exist?

**Solution:**
```
Complex conjugate: 2 + 5i

These form a quadratic factor:
[x - (2 - 5i)][x - (2 + 5i)]
= [(x - 2) + 5i][(x - 2) - 5i]
= (x - 2)² - (5i)²
= (x - 2)² + 25
= x² - 4x + 4 + 25
= x² - 4x + 29
```

**Reference:** [[Complex_Conjugate_Roots]]

---

### Problem 4.2 (Constructing Polynomial)
**Question:** Write a cubic polynomial with roots: 3, 1 + i, and leading coefficient 2

**Solution:**
```
If 1 + i is a root, then 1 - i is also a root
(conjugate pair requirement)

f(x) = 2(x - 3)[x - (1 + i)][x - (1 - i)]

Complex pair factor:
[x - (1 + i)][x - (1 - i)] = x² - 2x + 2

Therefore:
f(x) = 2(x - 3)(x² - 2x + 2)

Expanded:
= 2[(x)(x² - 2x + 2) - 3(x² - 2x + 2)]
= 2[x³ - 2x² + 2x - 3x² + 6x - 6]
= 2[x³ - 5x² + 8x - 6]
= 2x³ - 10x² + 16x - 12
```

**Common Mistake:** Forgetting to include the conjugate

---

### Problem 4.3 (Finding All Roots)
**Question:** Given P(x) = x⁴ + 2x² + 1, and one root is i, find all roots

**Solution:**
```
If i is a root, -i is also a root (conjugate)

Their quadratic factor:
(x - i)(x + i) = x² + 1

Divide original by x² + 1:
x⁴ + 2x² + 1 = (x² + 1)(x² + 1) = (x² + 1)²

From x² + 1 = 0:
x² = -1
x = ±i (with multiplicity 2 each!)

All roots: i (mult 2), -i (mult 2)
```

**Key Insight:** Complex roots can have multiplicity too!

---

## 📚 TOPIC 5: POLYNOMIAL DEGREE AND SHAPE

### Problem 5.1 (Identifying from Equation)
**Question:** Describe the general shape of f(x) = -3x⁵ + 2x³ - x + 1

**Solution:**
```
Degree: 5 (odd)
Leading coefficient: -3 (negative)

End behavior: Odd degree + negative LC
Left end: UP ↑
Right end: DOWN ↓

Shape: ⟍

Maximum turning points: 5 - 1 = 4
Will have 0, 2, or 4 actual turns

Must cross x-axis at least once (odd degree)
```

**Reference:** [[Polynomial_Degree_and_Shape]]

---

### Problem 5.2 (Determining from Graph)
**Question:** A graph shows 3 turning points and both ends going down. What's the minimum degree?

**Solution:**
```
Turning points = 3
Minimum degree = 3 + 1 = 4

Both ends down → even degree (confirmed!)

Leading coefficient must be negative
(even degree + both down = negative LC)

Minimum function type: 
Quartic (degree 4) with negative LC
```

**Common Mistake:** Saying degree = 3 (from number of turns)

---

## 📚 TOPIC 6: RATIONAL ROOT THEOREM

### Problem 6.1 (Finding Candidates)
**Question:** List all possible rational roots of 2x³ - 5x² + 3x - 6 = 0

**Solution:**
```
p (factors of a₀ = -6): ±1, ±2, ±3, ±6
q (factors of aₙ = 2): ±1, ±2

p/q candidates:
±1, ±2, ±3, ±6 (from q = 1)
±1/2, ±3/2 (from q = 2)

Complete list:
±1, ±2, ±3, ±6, ±1/2, ±3/2

Now test with synthetic division!
```

**Reference:** [[Rational_Root_Theorem]]

---

### Problem 6.2 (Complete Solving)
**Question:** Solve x³ - 4x² + x + 6 = 0 completely

**Solution:**
```
Step 1: Rational Root Theorem
p/q candidates: ±1, ±2, ±3, ±6

Step 2: Test with synthetic division
Try x = 1:
   1 | 1  -4   1   6
     |     1  -3  -2
     |_______________
       1  -3  -2   4  → R ≠ 0

Try x = 2:
   2 | 1  -4   1   6
     |     2  -4  -6
     |_______________
       1  -2  -3   0  → R = 0 ✓

Step 3: Factor using quotient
P(x) = (x - 2)(x² - 2x - 3)
     = (x - 2)(x - 3)(x + 1)

Step 4: All roots
x = 2, 3, -1
```

**Strategy:** Start with ±1, ±2 (easiest to test)

---

## 📚 TOPIC 7: GRAPHING QUADRATICS

### Problem 7.1 (Complete Graph from Standard)
**Question:** Graph f(x) = -x² + 4x - 3 showing all key features

**Solution:**
```
Step 1: Find vertex (complete square)
f(x) = -(x² - 4x) - 3
     = -(x² - 4x + 4) - 3 + 4
     = -(x - 2)² + 1
Vertex: (2, 1)

Step 2: Direction
a = -1 < 0 → Opens down (∩)

Step 3: Y-intercept
f(0) = -3
Point: (0, -3)

Step 4: X-intercepts (solve = 0)
-(x - 2)² + 1 = 0
(x - 2)² = 1
x - 2 = ±1
x = 3 or x = 1
Points: (1, 0), (3, 0)

Step 5: Axis of symmetry
x = 2 (vertical line through vertex)

Step 6: Additional point (use symmetry)
Since (0, -3) is 2 units left of axis,
(4, -3) is 2 units right

Now plot and connect smoothly!
```

**Reference:** [[Graphing_Quadratic_Functions]]

---

## 📚 TOPIC 8: WORKING FROM FACTORED FORM

### Problem 8.1 (Complete Analysis)
**Question:** Given f(x) = 2(x + 1)²(x - 3), find all features

**Solution:**
```
Roots:
x = -1 (multiplicity 2, touches)
x = 3 (multiplicity 1, crosses)

Degree: 2 + 1 = 3 (odd)

Leading coefficient: 2 (positive)

End behavior: Odd + positive
Left: DOWN ↓
Right: UP ↑

Y-intercept:
f(0) = 2(1)²(-3) = -6
Point: (0, -6)

Turning points: Max 3 - 1 = 2

Standard form (if needed):
f(x) = 2(x² + 2x + 1)(x - 3)
     = 2(x³ + 2x² + x - 3x² - 6x - 3)
     = 2(x³ - x² - 5x - 3)
     = 2x³ - 2x² - 10x - 6
```

**Reference:** [[Working_From_Factored_Form]]

---

## 📚 TOPIC 9: OPTIMIZATION PROBLEMS

### Problem 9.1 (Rectangle Area)
**Question:** A farmer has 200 feet of fence to enclose a rectangular garden. What dimensions maximize the area?

**Solution:**
```
Let x = width, y = length

Constraint: 2x + 2y = 200
Simplify: x + y = 100
          y = 100 - x

Area function:
A(x) = x · y = x(100 - x) = 100x - x²

This is a downward parabola!
Maximum at vertex.

Find vertex: A(x) = -x² + 100x
Complete square or use h = -b/(2a)

h = -100/(2(-1)) = 50

When x = 50: y = 100 - 50 = 50

Maximum area: 50 × 50 = 2500 sq ft

Answer: 50 ft × 50 ft (a square!)
```

**Key Insight:** Maximum area of rectangle with fixed perimeter is always a square

**Reference:** [[Quadratic_Optimization]]

---

### Problem 9.2 (Projectile Motion)
**Question:** A ball is thrown with height h(t) = -16t² + 64t + 5 feet. Find maximum height and when it hits the ground.

**Solution:**
```
Maximum height (vertex):
h(t) = -16(t² - 4t) + 5

Complete square:
h(t) = -16(t² - 4t + 4) + 5 + 64
     = -16(t - 2)² + 69

Maximum height: 69 feet at t = 2 seconds

Ground level (h = 0):
-16(t - 2)² + 69 = 0
(t - 2)² = 69/16
t - 2 = ±√(69/16)
t = 2 ± √69/4

Taking positive: t = 2 + √69/4 ≈ 4.08 seconds
```

**Common Mistake:** Forgetting to reject negative time

---

## 🎯 USING THIS PROBLEM BANK

### Practice Strategy

**For Each Problem:**
1. Try solving WITHOUT looking at solution
2. Check your answer
3. If wrong, identify where you made mistake
4. Reference the relevant entry
5. Try a similar problem

**Before Exam:**
- Do one problem from each topic
- Focus on topics where you make mistakes
- Time yourself (2-4 min per problem)

### Confidence Builders

**As you solve these:**
- ✅ Check off problems you get right
- ⭐ Star problems to retry later
- 📝 Note which concepts need review

---

*More problems being added continuously...*
