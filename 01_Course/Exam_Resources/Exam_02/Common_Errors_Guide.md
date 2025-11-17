# Common Errors & How to Avoid Them
*Learn From Others' Mistakes Before Making Your Own*

---

## 🎯 PURPOSE

**Why this matters:** Most exam points are lost to repeated, predictable errors—not lack of knowledge. Learn these patterns, avoid these traps, ace the exam.

---

## ❌ ERROR CATEGORY 1: SIGN ERRORS

### Error 1.1: Factor-to-Root Conversion
**WRONG:** (x + 3) = 0 → x = 3  
**RIGHT:** (x + 3) = 0 → x = -3 ✓

**Why it happens:** Brain sees +3 and thinks "positive 3"  
**How to avoid:** Always solve explicitly: x + 3 = 0 → x = -3

**Examples:**
- (x - 5) → x = 5 ✓
- (x + 7) → x = -7 ✓
- (2x - 6) → 2x = 6 → x = 3 ✓

---

### Error 1.2: Synthetic Division Sign
**WRONG:** Divide by (x + 2) using c = 2  
**RIGHT:** Divide by (x + 2) = (x - (-2)) using c = -2 ✓

**Why it happens:** Focusing on the visible number  
**How to avoid:** Rewrite as (x - c) form first

**Practice:**
- (x + 4) → c = -4
- (x - 3) → c = 3
- (x + 1) → c = -1
- (x - 0) → c = 0

---

### Error 1.3: Completing the Square Sign
**WRONG:** x² + 6x → add 9, subtract 9 → x² + 6x + 9 - 9  
**BUT WITH 'a':** 2(x² + 6x + 9) - 9 ❌  
**RIGHT:** 2(x² + 6x + 9) - 2(9) = 2(x² + 6x + 9) - 18 ✓

**Why it happens:** Forgetting to multiply subtracted term by 'a'  
**How to avoid:** Write the subtraction OUTSIDE the parentheses first

**Correct pattern:**
```
3(x² + 4x + 4) + c - 3(4)
     ↑            ↑
  added inside   subtract outside
  multiply by a
```

---

### Error 1.4: Complex Conjugate
**WRONG:** Conjugate of (3 + 4i) is (-3 - 4i)  
**RIGHT:** Conjugate of (3 + 4i) is (3 - 4i) ✓

**Why it happens:** Thinking "opposite" means flip both signs  
**How to avoid:** Only flip the imaginary part sign

**Pattern:**
- (a + bi) ↔ (a - bi)
- REAL part stays same
- IMAGINARY part flips sign

---

## ❌ ERROR CATEGORY 2: ALGEBRAIC MISTAKES

### Error 2.1: Forgetting i² = -1
**WRONG:** (2 + 3i)(2 - 3i) = 4 - 9i² = 4 - 9 = -5  
**RIGHT:** (2 + 3i)(2 - 3i) = 4 - 9i² = 4 - 9(-1) = 4 + 9 = 13 ✓

**Why it happens:** Forgetting to replace i²  
**How to avoid:** Write i² = -1 at start of complex number problems

**Key:** i² always becomes -1, which changes subtraction to addition

---

### Error 2.2: Distributing Leading Coefficient
**WRONG:** Expand 2(x - 1)(x + 3) → x² + 2x - 3  
**RIGHT:** 2(x - 1)(x + 3) → 2(x² + 2x - 3) = 2x² + 4x - 6 ✓

**Why it happens:** Forgetting the 'a' in front after expanding inside  
**How to avoid:** Expand inside first, THEN multiply by 'a' last step

**Checklist:**
1. Expand factors inside → get polynomial
2. Multiply EVERY term by leading coefficient
3. Double-check you didn't skip the 'a'

---

### Error 2.3: Discriminant Arithmetic
**WRONG:** For 3x² - 5x + 1: Δ = 25 - 4(3) = 25 - 12 = 13  
**RIGHT:** Δ = (-5)² - 4(3)(1) = 25 - 12 = 13 ✓  
(This one's actually right, but...)

**Common version:**  
**WRONG:** For -2x² + 3x - 5: Δ = 9 - 4(-2)(-5) = 9 - 40 = -31  
**RIGHT:** Δ = 9 - 4(-2)(-5) = 9 - (-40) = 9 + 40 = 49 ✓

**Why it happens:** Sign errors in multiplication  
**How to avoid:** Use parentheses! Δ = b² - 4(a)(c)

---

### Error 2.4: Synthetic Division Arithmetic
**WRONG:**
```
   2 | 1  -3   5
     |     2  -2  ← ERROR: should be -1
     |_____________
       1  -1   3
```

**RIGHT:**
```
   2 | 1  -3   5
     |     2  -2
     |_____________
       1  -1   3  ✓ (multiply, then add correctly)
```

**Why it happens:** Rushing, not double-checking arithmetic  
**How to avoid:** Double-check each multiplication/addition

---

## ❌ ERROR CATEGORY 3: CONCEPTUAL MISTAKES

### Error 3.1: Multiplicity Interpretation
**WRONG:** (x - 2)² means x = 2 twice (two different roots)  
**RIGHT:** (x - 2)² means ONE root (x = 2) with multiplicity 2 ✓

**Why it happens:** Confusing "squared factor" with "two roots"  
**How to avoid:** Multiplicity = exponent on factor, NOT number of roots

**Degree calculation:**
- f(x) = (x - 1)²(x + 3)¹
- Degree = 2 + 1 = 3 ✓
- Number of distinct roots = 2 (x = 1 and x = -3)
- Total roots counting multiplicity = 3

---

### Error 3.2: End Behavior Confusion
**WRONG:** Polynomial has negative LC → both ends go down  
**RIGHT:** Need to know if degree is even or odd first! ✓

**Why it happens:** Forgetting degree matters  
**How to avoid:** Check BOTH degree (even/odd) AND sign of LC

**Four cases (memorize!):**
- Even + positive → ↑↑
- Even + negative → ↓↓
- Odd + positive → ↓↑
- Odd + negative → ↑↓

---

### Error 3.3: Discriminant Misinterpretation
**WRONG:** Δ = 25 → two roots  
(TRUE but incomplete)  
**RIGHT:** Δ = 25 (perfect square) → two RATIONAL roots ✓

**Why it happens:** Stopping too early in analysis  
**How to avoid:** Always check if positive discriminant is perfect square

**Full classification:**
- Δ > 0 and perfect square → 2 rational roots
- Δ > 0 and not perfect → 2 irrational roots
- Δ = 0 → 1 rational root (repeated)
- Δ < 0 → 2 complex conjugate roots

---

### Error 3.4: Vertex Form Misconception
**WRONG:** Vertex form is a(x + h)² + k  
**RIGHT:** Vertex form is a(x - h)² + k ✓  
**And:** Vertex is at (h, k), not (-h, k)

**Why it happens:** Sign confusion in form  
**How to avoid:** Remember it's (x - h), and vertex is directly (h, k)

**Examples:**
- f(x) = 2(x - 3)² + 5 → vertex (3, 5)
- f(x) = -(x + 2)² - 1 = -(x - (-2))² - 1 → vertex (-2, -1)

---

## ❌ ERROR CATEGORY 4: PROCEDURAL MISTAKES

### Error 4.1: Incomplete Factoring
**WRONG:** x² + 7x + 12 = (x + 3)(x + 4) [DONE]  
**RIGHT BUT MISSING:** Original was 2x² + 14x + 24 = 2(x² + 7x + 12) = 2(x + 3)(x + 4) ✓

**Why it happens:** Forgetting to factor out GCF first  
**How to avoid:** Always check for GCF before factoring quadratic

**Steps:**
1. Look for GCF
2. Factor it out
3. Factor remaining quadratic
4. Don't forget the GCF in final answer!

---

### Error 4.2: Not Using All Given Information
**PROBLEM:** "Quadratic has roots 2 and -5, passes through (0, -10)"  
**WRONG:** f(x) = (x - 2)(x + 5) [INCOMPLETE]  
**RIGHT:** f(x) = a(x - 2)(x + 5), use (0, -10) to find a:  
-10 = a(-2)(5) → -10 = -10a → a = 1  
f(x) = (x - 2)(x + 5) ✓

**Why it happens:** Forgetting the leading coefficient 'a' is unknown  
**How to avoid:** Always include 'a', then use extra condition to solve for it

---

### Error 4.3: Answering Wrong Question
**PROBLEM:** "Find the x-coordinate of the vertex"  
**WRONG:** Vertex is (3, -4) [gave full coordinates]  
**RIGHT:** x-coordinate is 3 ✓

**Why it happens:** Not carefully reading what's asked  
**How to avoid:** Circle/underline what question asks for

**Common variations:**
- "Find the y-intercept" → want (0, c) OR just c?
- "Find the roots" → want just x-values, not y-coordinates
- "Find maximum value" → want y-coordinate of vertex, not both

---

### Error 4.4: Forgetting Domain Restrictions
**PROBLEM:** Simplify (x² - 4)/(x - 2)  
**WRONG:** = x + 2 [INCOMPLETE]  
**RIGHT:** = x + 2, x ≠ 2 ✓

**Why it happens:** Forgetting original denominator restriction  
**How to avoid:** Note restrictions BEFORE canceling

**Key:** Even after simplifying, x cannot equal values that made original denominator zero

---

## ❌ ERROR CATEGORY 5: GRAPH INTERPRETATION

### Error 5.1: Counting Turning Points as Degree
**WRONG:** Graph has 2 turning points → degree 2  
**RIGHT:** Graph has 2 turning points → MINIMUM degree 3 ✓

**Why it happens:** Forgetting the "degree = turns + 1" rule  
**How to avoid:** Degree is ALWAYS one more than turning points (minimum)

---

### Error 5.2: Misreading Multiplicity
**WRONG:** Graph crosses at x = 2 → multiplicity 2  
**RIGHT:** Graph crosses at x = 2 → ODD multiplicity (1, 3, 5...) ✓

**Why it happens:** Associating "2" with "cross"  
**How to avoid:** 
- Touch/bounce → EVEN multiplicity
- Cross → ODD multiplicity

---

### Error 5.3: Ignoring Y-intercept for Finding 'a'
**PROBLEM:** Graph shows zeros at -1, 3 and passes through (0, 6)  
**WRONG:** f(x) = (x + 1)(x - 3) [forgot to use (0, 6)]  
**RIGHT:** f(x) = a(x + 1)(x - 3), use (0, 6):  
6 = a(1)(-3) → a = -2  
f(x) = -2(x + 1)(x - 3) ✓

**Why it happens:** Not using all visible information  
**How to avoid:** After writing general form, use y-intercept to find 'a'

---

## ❌ ERROR CATEGORY 6: OPTIMIZATION MISTAKES

### Error 6.1: Forgetting to Answer in Context
**PROBLEM:** "Maximum area?"  
**WRONG:** "The vertex is at (50, 2500)"  
**RIGHT:** "Maximum area is 2500 square feet" ✓

**Why it happens:** Solving the math, forgetting the real-world question  
**How to avoid:** 
1. Identify what the question is really asking
2. Solve mathematically
3. Translate back to real-world answer with UNITS

---

### Error 6.2: Max vs Min Confusion
**PROBLEM:** "Find minimum cost, C(x) = 3x² - 12x + 20"  
**WRONG:** Opens up (a > 0), so maximum at vertex  
**RIGHT:** Opens up (a > 0), so MINIMUM at vertex ✓

**Why it happens:** Backward thinking  
**How to avoid:**
- Opens up (∪) → vertex is MINIMUM
- Opens down (∩) → vertex is MAXIMUM

---

## 🎯 AVOIDING ERRORS: SYSTEMATIC APPROACH

### Prevention Checklist

**Before starting any problem:**
- [ ] Read entire problem twice
- [ ] Circle what's being asked
- [ ] Note any restrictions or conditions
- [ ] Identify the type of problem

**While solving:**
- [ ] Show every step (even "obvious" ones)
- [ ] Use parentheses liberally
- [ ] Double-check signs
- [ ] Verify arithmetic

**After solving:**
- [ ] Does answer make sense?
- [ ] Did I answer what was asked?
- [ ] Are units included (if needed)?
- [ ] Is work legible?

### Error Recovery

**If you catch an error:**
1. DON'T erase everything
2. Draw single line through error
3. Write correct work clearly
4. Graders give credit for catching/fixing mistakes!

**If you're unsure:**
1. Write what you're thinking
2. Show your reasoning
3. Partial credit > blank page

---

## 💡 ERROR PATTERN RECOGNITION

**Top 10 Most Common Errors (In Order):**

1. Sign error converting (x + a) to root
2. Forgetting i² = -1
3. Not using all given information  
4. Discriminant calculation arithmetic
5. Completing square: forgetting to multiply by 'a'
6. Synthetic division sign error
7. Multiplicity vs number of roots confusion
8. End behavior: forgetting degree matters
9. Answering wrong question
10. Forgetting leading coefficient 'a' in constructions

**Know these, avoid these, succeed!**

---

*Errors are learning opportunities—learn from these NOW so you don't make them on the exam!*
