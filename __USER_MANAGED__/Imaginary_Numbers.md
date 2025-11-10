
# Imaginary Numbers
*Understanding i and the Complex Number System*

---

## 🎯 CORE INSIGHT

**Imaginary Numbers Complete the Number System**

When mathematicians tried to solve x² = -1, they discovered that no real number works. Instead of abandoning the problem, they INVENTED a new number: **i = √(-1)**. This isn't just mathematical fiction—it's a fundamental extension that makes algebra complete.

**The Pattern:**
```
Real numbers can't solve: x² + 1 = 0
Solution requires: x² = -1
Define: i = √(-1), so i² = -1
Result: x = ±i
```

**Why This Matters:**
- Every polynomial equation now has solutions (Fundamental Theorem of Algebra)
- Engineering applications: AC circuits, signal processing, quantum mechanics
- Geometric interpretation: rotation in the complex plane

**The Building Block:**
All imaginary and complex numbers are built from one simple definition: **i² = -1**

---

## 📐 THE MATHEMATICAL FOUNDATION

### What IS i?

**Definition:**  
@IMAGINARY_UNIT: i = √(-1), with the fundamental property **i² = -1**

**Powers of i (The Cycle):**
```
i¹ = i
i² = -1
i³ = i² · i = -1 · i = -i
i⁴ = i² · i² = (-1)(-1) = 1
i⁵ = i⁴ · i = 1 · i = i  ← Back to start!
```

**The Pattern:** Powers of i repeat every 4 steps: i, -1, -i, 1, i, -1, -i, 1, ...

**Quick Trick:** To find iⁿ, divide n by 4 and use the remainder:
- Remainder 0 → i⁴ = 1
- Remainder 1 → i¹ = i
- Remainder 2 → i² = -1
- Remainder 3 → i³ = -i

### Complex Numbers

**Definition:**  
@COMPLEX_NUMBER: z = a + bi, where:
- a = real part (Re(z))
- b = imaginary part (Im(z))
- a, b ∈ ℝ (real numbers)

**Types:**
- **Pure Imaginary:** a = 0, so z = bi (Example: 3i, -5i)
- **Real Number:** b = 0, so z = a (Example: 5, -2)
- **Complex:** both a ≠ 0 and b ≠ 0 (Example: 3 + 4i)

**Number System Hierarchy:**
```
Complex Numbers (ℂ)
    ├── Real Numbers (ℝ)
    │       ├── Rational (ℚ)
    │       └── Irrational
    └── Pure Imaginary (bi)
```


---

## 🔧 OPERATIONS WITH IMAGINARY AND COMPLEX NUMBERS

### Addition and Subtraction

**Rule:** Combine like terms (real with real, imaginary with imaginary)

**Format:**
```
(a + bi) + (c + di) = (a + c) + (b + d)i
(a + bi) - (c + di) = (a - c) + (b - d)i
```

**Example:**
```
(3 + 2i) + (1 - 4i) = (3 + 1) + (2 - 4)i = 4 - 2i
(5 - i) - (2 + 3i) = (5 - 2) + (-1 - 3)i = 3 - 4i
```

### Multiplication

**Rule:** Use FOIL and remember i² = -1

**Format:**
```
(a + bi)(c + di) = ac + adi + bci + bdi²
                 = ac + adi + bci - bd
                 = (ac - bd) + (ad + bc)i
```

**Example:**
```
(2 + 3i)(1 + 4i) = 2(1) + 2(4i) + 3i(1) + 3i(4i)
                 = 2 + 8i + 3i + 12i²
                 = 2 + 11i + 12(-1)
                 = 2 + 11i - 12
                 = -10 + 11i
```

**Special Case - Squaring:**
```
(a + bi)² = a² + 2abi + (bi)²
          = a² + 2abi - b²
          = (a² - b²) + 2abi
```

### Division (Using Complex Conjugates)

**Rule:** Multiply numerator and denominator by the conjugate of the denominator

**Conjugate:** If z = a + bi, then z̄ = a - bi

**Why this works:** (a + bi)(a - bi) = a² + b² (real number!)

**Procedure:**
```
(a + bi)/(c + di) × (c - di)/(c - di) = [(a + bi)(c - di)] / [c² + d²]
```

**Example:**
```
(3 + 2i)/(1 - i)

Step 1: Identify conjugate of denominator: 1 + i

Step 2: Multiply:
= (3 + 2i)(1 + i) / [(1 - i)(1 + i)]
= (3 + 3i + 2i + 2i²) / (1 - i²)
= (3 + 5i - 2) / (1 + 1)
= (1 + 5i) / 2
= 1/2 + (5/2)i
```

### Powers of i (Shortcut Method)

**For iⁿ where n is large:**

**Method:** n mod 4 (remainder when dividing by 4)

**Examples:**
- i¹⁵ = i^(4×3 + 3) = (i⁴)³ · i³ = 1³ · (-i) = -i
- i³⁸ = i^(4×9 + 2) = (i⁴)⁹ · i² = 1⁹ · (-1) = -1
- i¹⁰⁰ = i^(4×25) = (i⁴)²⁵ = 1

---

## 🎯 SIMPLIFYING SQUARE ROOTS OF NEGATIVE NUMBERS

### The Fundamental Rule

**For negative radicands:**
```
√(-a) = √(-1 · a) = √(-1) · √a = i√a
```

Where a > 0

**Examples:**
```
√(-16) = √(-1 · 16) = i√16 = 4i
√(-7) = √(-1 · 7) = i√7
√(-50) = i√50 = i√(25 · 2) = 5i√2
```

### Operations with Radicals Involving i

**Multiplication:**
```
√(-4) · √(-9) = (2i)(3i) = 6i² = -6
```

**CRITICAL WARNING:** √(-a) · √(-b) ≠ √(ab) when a, b > 0!
```
Wrong: √(-4) · √(-9) = √[(-4)(-9)] = √36 = 6 ✗
Right: √(-4) · √(-9) = (2i)(3i) = 6i² = -6 ✓
```

**Always convert to i form FIRST before multiplying!**


---

## 📋 WORKED EXAMPLES

### Example 1: Simplifying Powers of i

**Problem:** Simplify i⁴⁷

**Solution:**
```
Step 1: Divide exponent by 4
47 ÷ 4 = 11 remainder 3

Step 2: Use remainder
i⁴⁷ = i³ = -i
```

**Alternative method:**
```
i⁴⁷ = i^(44 + 3) = i^44 · i³ = (i⁴)^11 · i³ = 1^11 · (-i) = -i
```

---

### Example 2: Complex Number Arithmetic

**Problem:** Simplify (2 - 3i) - (4 + i) + (1 - 2i)

**Solution:**
```
Step 1: Remove parentheses (watch signs!)
= 2 - 3i - 4 - i + 1 - 2i

Step 2: Combine real parts
= (2 - 4 + 1) + (-3i - i - 2i)

Step 3: Simplify
= -1 - 6i
```

---

### Example 3: Multiplication with i

**Problem:** Multiply (3 + 5i)(2 - i)

**Solution:**
```
Step 1: FOIL
= 3(2) + 3(-i) + 5i(2) + 5i(-i)
= 6 - 3i + 10i - 5i²

Step 2: Replace i² with -1
= 6 - 3i + 10i - 5(-1)
= 6 - 3i + 10i + 5

Step 3: Combine like terms
= 11 + 7i
```

---

### Example 4: Division (Conjugate Method)

**Problem:** Simplify (4 + 3i)/(2 + i)

**Solution:**
```
Step 1: Identify conjugate of denominator
Conjugate of (2 + i) is (2 - i)

Step 2: Multiply numerator and denominator
= (4 + 3i)(2 - i) / [(2 + i)(2 - i)]

Step 3: Expand numerator
= (8 - 4i + 6i - 3i²) / (4 - i²)
= (8 + 2i + 3) / (4 + 1)
= (11 + 2i) / 5

Step 4: Separate into standard form
= 11/5 + (2/5)i
```

---

### Example 5: Simplifying Radicals with Negatives

**Problem:** Simplify √(-48)

**Solution:**
```
Step 1: Factor out -1
= √(-1 · 48)

Step 2: Separate into i and real radical
= √(-1) · √48
= i√48

Step 3: Simplify the real radical
= i√(16 · 3)
= 4i√3
```

---

## ⚠️ COMMON PITFALLS

### Mistake 1: Wrong Radical Multiplication
**Error:** √(-4) · √(-9) = √36 = 6  
**Correction:** Convert FIRST: (2i)(3i) = 6i² = -6 ✓

### Mistake 2: Forgetting i² = -1
**Error:** 3i² = 3i · 2 = 6i  
**Correction:** 3i² = 3(-1) = -3 ✓

### Mistake 3: Wrong Power of i
**Error:** i⁸ = i² = -1  
**Correction:** i⁸ = (i⁴)² = 1² = 1 ✓

### Mistake 4: Not Simplifying After Division
**Error:** Leaving answer as (2 + 4i)/2  
**Correction:** Simplify to 1 + 2i ✓

### Mistake 5: Confusing Real and Imaginary Parts
**Error:** "The imaginary part of 3 + 4i is 4i"  
**Correction:** Imaginary part is just the coefficient: 4 (not 4i) ✓

---

## 💡 GEOMETRIC INTERPRETATION

### The Complex Plane

**Cartesian Mapping:**
- Horizontal axis (x) = Real part
- Vertical axis (y) = Imaginary part
- Point (a, b) represents a + bi

**Example:** 3 + 2i is plotted at coordinates (3, 2)

### Operations as Transformations

**Addition:** Vector addition (tip-to-tail)

**Multiplication by i:** Rotation by 90° counterclockwise
```
1 → i → -1 → -i → 1 (full 360°)
```

**Complex Conjugate:** Reflection across real axis
```
3 + 2i ↔ 3 - 2i
```

---

## 🔗 CONNECTIONS

**Prerequisites:**
- [[Real_Numbers]] - Foundation for complex numbers
- [[Exponent_Rules]] - For simplifying powers of i
- [[Radical_Properties]] - For √(-a) expressions

**Related Concepts:**
- [[Complex_Conjugate_Roots]] - Application to polynomials
- [[The_Discriminant]] - When complex roots appear
- [[Quadratic_Formula]] - Computing complex solutions

**Applications:**
- [[Solving_Quadratic_Equations]] - When Δ < 0
- [[Euler's_Formula]] - e^(iθ) connection
- [[Polar_Form_of_Complex_Numbers]] - Alternative representation

---

## 🎓 EXAM STRATEGIES

### Quick Simplification
1. **Powers of i:** Use n mod 4 trick
2. **Radicals with negatives:** Extract i FIRST
3. **Division:** Always use conjugate method

### Standard Form Requirement
Always express final answers as **a + bi** where a, b are real numbers:
- Good: 3 + 2i, 5 - i, -1 + 0i (= -1)
- Bad: 2 + i + 3i, (4 + i)/2 (not simplified)

### Verification Checks
- **Multiplication:** Final result should have ONE i term
- **Division:** Denominator should be real (no i)
- **Powers:** Result must be one of: 1, i, -1, -i

### Common Exam Patterns
- "Simplify i^n" → Use mod 4 method
- "Write in standard form" → Ensure a + bi format
- "Rationalize the denominator" → Use complex conjugate
- "Solve x² + k = 0 where k > 0" → x = ±i√k

---

*Remember: Imaginary numbers aren't imaginary in the sense of "fake"—they're a legitimate mathematical extension that completes algebra. Master i² = -1, and everything else follows!*
