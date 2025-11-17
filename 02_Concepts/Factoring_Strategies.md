---
layout: concept
title: Factoring Strategies
topic: Polynomials
type: Method
status: stable
importance: critical
tags:
- concept/algebra
- concept/polynomials
- concept/factoring
- chapter-r
- prerequisites
sources:
- miller-gerken-2ed
source_refs:
- Miller & Gerken §R.5 p.37-45
relations:
  broader:
  - '[[Polynomial_Operations]]'
  - '[[Algebraic_Techniques]]'
  narrower:
  - Greatest Common Factor (GCF)
  - Factoring by Grouping
  - Trinomial Factoring
  - Special Patterns
  depends_on:
  - '[[Distributive_Property]]'
  - '[[Special_Product_Patterns]]'
  - '[[Prime_Factorization]]'
  related:
  - '[[Zero_Product_Property]]'
  - '[[Polynomial_Multiplication]]'
  - '[[Solving_Equations]]'
  used_in:
  - '[[Quadratic_Equations]]'
  - '[[Rational_Expressions]]'
  - '[[Solving_Polynomial_Equations]]'
review:
  last: 2025-10-19
  next: 2025-10-26
  interval: 7 days
created: 2025-10-19
updated: 2025-11-16
qa_certified: true
qa_date: 2025-11-16
qa_migration: v2.0
defines:
- '[[Zero_Product_Property]]'
---
# Factoring Strategies

## Definition

**Factoring strategies** are systematic methods for expressing a polynomial as a product of its factors—reversing the multiplication process. Factoring is essential for solving equations, simplifying expressions, and analyzing polynomial functions.

**Fundamental Principle**: 
```
Factoring is the inverse of multiplication
Multiplication: (x + 3)(x + 2) → x² + 5x + 6
Factoring:       x² + 5x + 6 → (x + 3)(x + 2)
```

**Complete Factorization**: Continue factoring until all factors are prime (cannot be factored further over the set of integers).

---

## The STOP Method: Universal Factoring Strategy

A systematic approach to factor any polynomial:

### **S** - Search for Greatest Common Factor (GCF)
**Always factor out GCF first**

### **T** - Two terms? 
Check for special patterns:
- Difference of squares: a² - b²
- Sum of cubes: a³ + b³
- Difference of cubes: a³ - b³

### **O** - One more term (3 terms total)?
Try trinomial factoring or perfect square patterns:
- Perfect square trinomial: a² ± 2ab + b²
- General trinomial: ax² + bx + c

### **P** - Pairs (4+ terms)?
Try factoring by grouping

---

## Strategy 1: Greatest Common Factor (GCF)

**When to Use**: ALWAYS check first for all polynomials

**Process**:
1. Find GCF of all coefficients
2. Find lowest power of each variable present in ALL terms
3. Factor out the complete GCF
4. Continue factoring the remaining polynomial

### Pattern Recognition
```
Before: All terms share common factors
After: GCF · (simplified polynomial)
```

### Examples

**Example 1: Numerical GCF**
```
Factor: 12x³ + 18x² - 24x

GCF of coefficients: GCF(12, 18, 24) = 6
Lowest power of x: x¹ (all terms have at least x)
Complete GCF: 6x

= 6x(2x² + 3x - 4)

Check: 6x · 2x² = 12x³ ✓
       6x · 3x = 18x² ✓
       6x · (-4) = -24x ✓
```

**Example 2: Variable GCF**
```
Factor: 15x⁵y³ - 25x³y⁴ + 10x²y²

GCF of coefficients: 5
Lowest power of x: x²
Lowest power of y: y²
Complete GCF: 5x²y²

= 5x²y²(3x³y - 5xy² + 2)
```

**Example 3: Negative GCF**
```
Factor: -3x² + 6x - 9

Can factor out -3 to make leading coefficient positive:
= -3(x² - 2x + 3)

This is often preferable for further factoring
```

### Common Mistakes
- Forgetting to factor variable parts
- Not factoring completely (GCF should be largest possible)
- Skipping GCF step before other factoring methods

---

## Strategy 2: Factoring by Grouping

**When to Use**: Four or more terms that share factors in pairs

**Process**:
1. Group terms in pairs (or other strategic groupings)
2. Factor GCF from each group
3. If a common binomial appears, factor it out
4. If no common binomial, try different grouping

### Pattern Recognition
```
Before: ax + ay + bx + by
Group: (ax + ay) + (bx + by)
Factor each: a(x + y) + b(x + y)
Factor out (x + y): (x + y)(a + b)
```

### Examples

**Example 1: Standard Grouping**
```
Factor: x³ + 3x² + 2x + 6

Step 1: Group in pairs
= (x³ + 3x²) + (2x + 6)

Step 2: Factor each group
= x²(x + 3) + 2(x + 3)

Step 3: Factor out common (x + 3)
= (x + 3)(x² + 2)

Check: (x + 3)(x² + 2) = x³ + 2x + 3x² + 6 = x³ + 3x² + 2x + 6 ✓
```

**Example 2: Grouping with Sign Change**
```
Factor: x³ - 2x² + 5x - 10

Step 1: Group
= (x³ - 2x²) + (5x - 10)

Step 2: Factor each (note: factor out -1 from second group if helpful)
= x²(x - 2) + 5(x - 2)

Step 3: Factor out (x - 2)
= (x - 2)(x² + 5)
```

**Example 3: Non-obvious Grouping**
```
Factor: ax + bx - ay - by

Try 1: (ax + bx) - (ay + by)
     = x(a + b) - y(a + b)
     = (a + b)(x - y) ✓

Try 2: (ax - ay) + (bx - by)
     = a(x - y) + b(x - y)
     = (x - y)(a + b) ✓

Both work! Sometimes reordering helps find grouping
```

### Common Mistakes
- Not factoring out -1 when needed for common factor
- Giving up after first grouping attempt
- Forgetting to check if final factors can be factored further

---

## Strategy 3: Factoring Trinomials

**When to Use**: Three-term polynomials in form ax² + bx + c

### Case A: When a = 1 (x² + bx + c)

**Process**: Find two numbers that:
- **Multiply** to c (constant term)
- **Add** to b (coefficient of x)

**Pattern**: (x + m)(x + n) where m·n = c and m + n = b

### Sign Pattern Guide
| Signs in x² + bx + c | Sign Pattern in Factors |
|---------------------|------------------------|
| + + | Both positive: (x + m)(x + n) |
| - + | Both negative: (x - m)(x - n) |
| - - | Opposite signs, larger absolute value is negative |
| + - | Opposite signs, larger absolute value is positive |

**Example 1: Both Positive**
```
Factor: x² + 7x + 12

Find: m · n = 12 and m + n = 7
Try pairs of 12: (1,12), (2,6), (3,4)
Answer: 3 and 4 (since 3·4 = 12 and 3+4 = 7)

= (x + 3)(x + 4)

Check: (x + 3)(x + 4) = x² + 4x + 3x + 12 = x² + 7x + 12 ✓
```

**Example 2: Both Negative**
```
Factor: x² - 9x + 20

Find: m · n = 20 and m + n = -9
Need negative factors: (-1,-20), (-2,-10), (-4,-5)
Answer: -4 and -5 (since -4·-5 = 20 and -4-5 = -9)

= (x - 4)(x - 5)
```

**Example 3: Opposite Signs**
```
Factor: x² + 3x - 10

Find: m · n = -10 and m + n = 3
Need opposite signs: (-1,10), (1,-10), (-2,5), (2,-5)
Answer: -2 and 5 (since -2·5 = -10 and -2+5 = 3)

= (x - 2)(x + 5)
```

### Case B: When a ≠ 1 (ax² + bx + c)

**Method 1: Trial and Error**
Systematically try combinations of factors

**Method 2: AC Method** (More systematic)
1. Multiply a · c
2. Find two numbers that multiply to ac and add to b
3. Split middle term using these numbers
4. Factor by grouping

**Example: AC Method**
```
Factor: 3x² + 11x + 6

Step 1: Calculate ac
a · c = 3 · 6 = 18

Step 2: Find numbers that multiply to 18 and add to 11
Pairs: (1,18), (2,9), (3,6)
Answer: 2 and 9 (since 2·9 = 18 and 2+9 = 11)

Step 3: Rewrite middle term
3x² + 2x + 9x + 6

Step 4: Factor by grouping
= x(3x + 2) + 3(3x + 2)
= (3x + 2)(x + 3)

Check: (3x + 2)(x + 3) = 3x² + 9x + 2x + 6 = 3x² + 11x + 6 ✓
```

### Common Mistakes
- Wrong sign combination
- Arithmetic errors in finding m and n
- Not checking answer by multiplying
- Forgetting GCF before factoring trinomial

---

## Strategy 4: Special Patterns

**When to Use**: Recognize specific forms immediately

### Pattern 1: Difference of Squares
```
a² - b² = (a + b)(a - b)
```

**Recognition**: 
- Two terms
- Both perfect squares
- Subtraction

**Example**:
```
Factor: 16x² - 49

Identify: (4x)² - (7)²
= (4x + 7)(4x - 7)

Note: Check if factors can be factored further
(4x + 7) and (4x - 7) are prime
```

### Pattern 2: Perfect Square Trinomial
```
a² + 2ab + b² = (a + b)²
a² - 2ab + b² = (a - b)²
```

**Recognition**:
- Three terms
- First and last are perfect squares
- Middle term = ±2√(first·last)

**Example**:
```
Factor: x² + 10x + 25

Check: x² = (x)², 25 = (5)²
Middle: 10x = 2(x)(5) ✓

= (x + 5)²
```

### Pattern 3: Difference of Cubes
```
a³ - b³ = (a - b)(a² + ab + b²)
```

**Example**:
```
Factor: 8x³ - 27

Identify: (2x)³ - (3)³
= (2x - 3)[(2x)² + (2x)(3) + (3)²]
= (2x - 3)(4x² + 6x + 9)

Note: 4x² + 6x + 9 doesn't factor (discriminant < 0)
```

### Pattern 4: Sum of Cubes
```
a³ + b³ = (a + b)(a² - ab + b²)
```

**SOAP Mnemonic**: Same, Opposite, Always Positive

**Example**:
```
Factor: 125x³ + 64

Identify: (5x)³ + (4)³
= (5x + 4)[(5x)² - (5x)(4) + (4)²]
= (5x + 4)(25x² - 20x + 16)
```

---

## Complete Factoring Strategy: Step-by-Step

### Full Process Checklist

**Step 1: Factor out GCF**
- Check all terms for common factors
- Factor out largest GCF
- ✓ Makes remaining polynomial simpler

**Step 2: Count terms**
- 2 terms → Check special patterns (difference of squares, sum/diff of cubes)
- 3 terms → Try trinomial factoring or perfect square pattern
- 4+ terms → Try factoring by grouping

**Step 3: Check each factor**
- Can it be factored further?
- Apply strategies recursively

**Step 4: Verify**
- Multiply factors to check
- Should get original polynomial

### Decision Tree

```
START: Polynomial to factor
  ↓
1. GCF? → Factor out GCF
  ↓
2. How many terms remain?
  ├─ 2 terms
  │   ├─ a² - b²? → (a+b)(a-b)
  │   ├─ a³ + b³? → (a+b)(a²-ab+b²)
  │   └─ a³ - b³? → (a-b)(a²+ab+b²)
  │
  ├─ 3 terms
  │   ├─ Perfect square? → (a±b)²
  │   ├─ a = 1? → Find m,n where m·n=c, m+n=b
  │   └─ a ≠ 1? → Use AC method + grouping
  │
  └─ 4+ terms → Try grouping
  ↓
3. Check each factor → Can it factor more?
  ↓
4. VERIFY → Multiply to confirm
  ↓
DONE: Complete factorization
```

---

## Complex Examples

### Example 1: Multiple Steps
```
Factor completely: 2x⁴ - 32

Step 1: GCF = 2
= 2(x⁴ - 16)

Step 2: Difference of squares (x⁴ - 16)
= 2[(x²)² - (4)²]
= 2(x² + 4)(x² - 4)

Step 3: x² - 4 factors further (difference of squares)
= 2(x² + 4)(x + 2)(x - 2)

Step 4: x² + 4 doesn't factor over reals

Complete: 2(x² + 4)(x + 2)(x - 2)
```

### Example 2: Grouping After GCF
```
Factor: 3x³ + 6x² - 27x - 54

Step 1: GCF = 3
= 3(x³ + 2x² - 9x - 18)

Step 2: Group
= 3[(x³ + 2x²) + (-9x - 18)]
= 3[x²(x + 2) - 9(x + 2)]

Step 3: Factor out (x + 2)
= 3(x + 2)(x² - 9)

Step 4: x² - 9 is difference of squares
= 3(x + 2)(x + 3)(x - 3)
```

### Example 3: Hidden Perfect Square
```
Factor: 4x² + 12xy + 9y²

Step 1: No GCF

Step 2: Check if perfect square trinomial
(2x)² + 2(2x)(3y) + (3y)²? YES!

= (2x + 3y)²
```

---

## Applications

### 1. **Solving Equations (Zero Product Property)**
```
Equation: x² - 5x - 14 = 0
Factor: (x - 7)(x + 2) = 0
Solve: x = 7 or x = -2
```

### 2. **Simplifying Rational Expressions**
```
Simplify: (x² - 4)/(x² + 4x + 4)

Factor: (x + 2)(x - 2)/(x + 2)²
Cancel: (x - 2)/(x + 2)
```

### 3. **Finding Zeros of Functions**
```
Function: f(x) = x³ - 4x
Factor: f(x) = x(x² - 4) = x(x + 2)(x - 2)
Zeros: x = 0, -2, 2
```

### 4. **Domain Restrictions**
```
Expression: 1/(x² - 9)
Factor denominator: 1/[(x + 3)(x - 3)]
Domain: x ≠ -3, x ≠ 3
```

---

## Common Errors and How to Avoid Them

### Error 1: Stopping Too Early
**Wrong**: x⁴ - 16 = (x² + 4)(x² - 4) [INCOMPLETE] ✗
**Correct**: x⁴ - 16 = (x² + 4)(x + 2)(x - 2) ✓
**Lesson**: Always check if factors can factor further

### Error 2: Skipping GCF
**Wrong**: 2x² + 8x + 6 = (2x + 2)(x + 3) ✗
**Correct**: 2x² + 8x + 6 = 2(x² + 4x + 3) = 2(x + 1)(x + 3) ✓
**Lesson**: ALWAYS factor GCF first

### Error 3: Sign Errors in Trinomials
**Wrong**: x² - 5x + 6 = (x + 2)(x + 3) ✗
**Correct**: x² - 5x + 6 = (x - 2)(x - 3) ✓
**Lesson**: Check signs carefully: need -2 - 3 = -5 ✓

### Error 4: Not Checking Answer
**Problem**: Factoring errors go unnoticed
**Solution**: ALWAYS multiply factors to verify

### Error 5: Giving Up on Grouping
**Problem**: First grouping attempt doesn't work
**Solution**: Try different groupings or reorder terms

---

## Practice Problems

### Level 1: GCF Only
1. Factor: 12x³ - 18x² + 24x
2. Factor: -5x⁴y + 15x²y² - 10xy³

### Level 2: Two-Term Patterns
3. Factor: x² - 100
4. Factor: 8x³ + 125
5. Factor: 27x³ - 64

### Level 3: Trinomials (a = 1)
6. Factor: x² + 9x + 20
7. Factor: x² - 11x + 28
8. Factor: x² + 2x - 35

### Level 4: Trinomials (a ≠ 1)
9. Factor: 2x² + 7x + 3
10. Factor: 6x² - 13x - 5

### Level 5: Grouping
11. Factor: x³ + 2x² + 3x + 6
12. Factor: 2x³ - x² - 18x + 9

### Level 6: Complete Factorization
13. Factor completely: 3x⁴ - 48
14. Factor completely: 2x³ + 4x² - 30x
15. Factor completely: x⁴ - 81

### Challenge
16. Factor: x⁶ - 64
17. Factor: 4x² - 12xy + 9y²
18. Factor: x⁴ + 4

---

## Summary

**Factoring strategies** provide systematic methods to express polynomials as products of simpler factors:

**Universal Strategy - STOP Method**:
1. **S**earch for GCF (always first!)
2. **T**wo terms → special patterns
3. **O**ne more term → trinomial factoring
4. **P**airs → grouping

**Key Principles**:
- Factor GCF first, always
- Check every factor for further factoring
- Verify by multiplying
- Complete factorization = all factors prime

**Essential Patterns**:
- Difference of squares: a² - b²
- Perfect square trinomials: a² ± 2ab + b²
- Sum/difference of cubes: a³ ± b³

**Critical Skill**: Pattern recognition speeds up factoring dramatically

**Foundation For**: Solving equations, simplifying rational expressions, finding zeros, analyzing functions

---

*Factoring is reverse engineering of multiplication—a fundamental skill throughout algebra, precalculus, and calculus. Mastery requires pattern recognition, systematic approach, and persistent practice.*
---
type: Method
status: stable
importance: critical
tags:
  - concept/method
  - math/algebra
  - chapter-r/prerequisites
  - factoring
  - polynomials
sources:
  - miller-gerken-2025
source_refs:
  - "Miller & Gerken §R.5 p.51-58"
relations:
  broader:
    - "[[Polynomial_Operations]]"
  narrower:
    - "[[GCF_Factoring]]"
    - "[[Factoring_Trinomials]]"
    - "[[Factoring_by_Grouping]]"
  depends_on:
    - "[[Special_Product_Patterns]]"
    - "[[Zero_Product_Property]]"
    - "[[Distributive_Property]]"
  defines:
    - "[[Prime_Polynomial]]"
  related:
    - "[[Quadratic_Equations]]"
    - "[[Rational_Expressions_Operations]]"
  used_in:
    - "[[Solving_Polynomial_Equations]]"
    - "[[Simplifying_Rational_Expressions]]"
    - "[[Finding_Zeros_of_Functions]]"
review:
  last: 2025-10-19
  next: 2025-10-26
  interval: 7
created: 2025-10-19
updated: 2025-10-19
---

# Factoring Strategies

## Definition

**Factoring** is the process of expressing a polynomial as a product of two or more simpler polynomial factors. Effective factoring requires systematic application of multiple strategies in a specific order to completely factor any factorable polynomial.

### Complete Factoring

A polynomial is **completely factored** when:
1. It is expressed as a product of prime factors
2. No factor can be factored further
3. All common factors have been removed
4. All factoring patterns have been applied

**Prime polynomial**: A polynomial that cannot be factored using integer coefficients (over the integers).

---

## The Six Core Factoring Strategies

### Strategy 1: Factor Out Greatest Common Factor (GCF)

**Always the first step in any factoring problem.**

#### Process:
1. Identify GCF of all terms (numerical and variable parts)
2. Factor GCF out using distributive property
3. Verify: $\text{GCF} \times \text{(remaining polynomial)} = \text{original}$

#### Example:
$$6x^3 + 9x^2 - 15x$$

**GCF**: $3x$ (appears in all terms)

$$= 3x(2x^2 + 3x - 5)$$

**Critical**: Continue factoring the parenthetical expression if possible.

---

### Strategy 2: Factoring by Grouping (4-Term Polynomials)

**Use when**: Polynomial has 4 terms and no common factor for all terms.

#### Process:
1. Group terms in pairs: $(term_1 + term_2) + (term_3 + term_4)$
2. Factor GCF from each group
3. Factor out common binomial factor
4. If no common binomial appears, try different grouping

#### Example:
$$x^3 + 3x^2 + 2x + 6$$

**Step 1** - Group:
$$(x^3 + 3x^2) + (2x + 6)$$

**Step 2** - Factor each group:
$$x^2(x + 3) + 2(x + 3)$$

**Step 3** - Factor common binomial $(x + 3)$:
$$(x + 3)(x^2 + 2)$$

---

### Strategy 3: Factoring Trinomials of Form $x^2 + bx + c$

**Pattern**: Find two numbers that multiply to $c$ and add to $b$.

#### Process:
1. List factor pairs of $c$
2. Identify pair that sums to $b$
3. Express as $(x + m)(x + n)$ where $m \cdot n = c$ and $m + n = b$

#### Example 1: $x^2 + 7x + 12$

**Need**: Two numbers that multiply to 12 and add to 7

| Factors of 12 | Sum |
|---------------|-----|
| 1, 12 | 13 |
| 2, 6 | 8 |
| 3, 4 | **7** ✓ |

**Result**: $x^2 + 7x + 12 = (x + 3)(x + 4)$

#### Example 2: $x^2 - 5x + 6$

**Need**: Two numbers that multiply to 6 and add to -5

**Factors**: $-2$ and $-3$ (both negative since product positive, sum negative)

**Result**: $x^2 - 5x + 6 = (x - 2)(x - 3)$

---

### Strategy 4: Factoring Trinomials of Form $ax^2 + bx + c$ (a ≠ 1)

**Two approaches**: Trial-and-error OR AC method

#### AC Method (Systematic):
1. Multiply: $a \times c = AC$
2. Find two numbers that multiply to $AC$ and add to $b$
3. Rewrite middle term using these numbers
4. Factor by grouping

#### Example: $3x^2 + 10x + 8$

**Step 1**: $AC = 3 \times 8 = 24$

**Step 2**: Find factors of 24 that add to 10:
- $4 \times 6 = 24$ and $4 + 6 = 10$ ✓

**Step 3**: Rewrite:
$$3x^2 + 10x + 8 = 3x^2 + 4x + 6x + 8$$

**Step 4**: Factor by grouping:
$$= x(3x + 4) + 2(3x + 4)$$
$$= (3x + 4)(x + 2)$$

---

### Strategy 5: Special Product Patterns

**Recognize and apply**: Reverse of multiplication patterns.

#### Pattern 5a: Difference of Squares
$$a^2 - b^2 = (a + b)(a - b)$$

**Example**: $16x^2 - 25 = (4x)^2 - 5^2 = (4x + 5)(4x - 5)$

#### Pattern 5b: Perfect Square Trinomials
$$a^2 + 2ab + b^2 = (a + b)^2$$
$$a^2 - 2ab + b^2 = (a - b)^2$$

**Recognition test**: 
- First and last terms are perfect squares
- Middle term = $\pm 2 \times \sqrt{\text{first}} \times \sqrt{\text{last}}$

**Example**: $9x^2 + 12x + 4 = (3x)^2 + 2(3x)(2) + 2^2 = (3x + 2)^2$

#### Pattern 5c: Sum/Difference of Cubes
$$a^3 + b^3 = (a + b)(a^2 - ab + b^2)$$
$$a^3 - b^3 = (a - b)(a^2 + ab + b^2)$$

**Example**: $x^3 - 8 = x^3 - 2^3 = (x - 2)(x^2 + 2x + 4)$

---

### Strategy 6: Combination Techniques

**Real-world problems** often require multiple strategies in sequence.

#### Example: $2x^3 - 18x$

**Step 1** - GCF first: $2x(x^2 - 9)$

**Step 2** - Recognize difference of squares: $x^2 - 9 = (x + 3)(x - 3)$

**Complete factorization**: $2x(x + 3)(x - 3)$

---

## The Complete Factoring Algorithm

### Universal Process (Apply in Order):

```
1. ALWAYS factor out GCF first
   ↓
2. Count terms remaining
   ↓
3. BRANCH:
   
   TWO TERMS?
   ├─ Difference of squares? → Factor
   ├─ Sum/difference of cubes? → Factor
   └─ Otherwise → Prime (cannot factor)
   
   THREE TERMS (Trinomial)?
   ├─ Perfect square trinomial? → Factor as (a ± b)²
   ├─ Form x² + bx + c? → Find factors of c that sum to b
   └─ Form ax² + bx + c (a≠1)? → Use AC method or trial-and-error
   
   FOUR TERMS?
   └─ Factor by grouping
   
   MORE THAN FOUR TERMS?
   └─ Look for patterns or try creative grouping

4. Check each factor
   ↓
5. Factor further if possible
   ↓
6. Verify by multiplication
```

---

## Examples

### Example 1: Complete Factoring with Multiple Steps

**Factor completely**: $5x^3 - 45x$

**Step 1** - GCF: $5x(x^2 - 9)$

**Step 2** - Difference of squares: $x^2 - 9 = (x + 3)(x - 3)$

**Final answer**: $5x(x + 3)(x - 3)$

**Verification**: $5x(x + 3)(x - 3) = 5x(x^2 - 9) = 5x^3 - 45x$ ✓

---

### Example 2: Trinomial with Leading Coefficient ≠ 1

**Factor**: $6x^2 - 13x - 5$

**AC Method**:
- $AC = 6 \times (-5) = -30$
- Need factors of -30 that add to -13: $-15$ and $2$

**Rewrite**:
$$6x^2 - 15x + 2x - 5$$

**Group**:
$$3x(2x - 5) + 1(2x - 5)$$

**Factor**:
$$(2x - 5)(3x + 1)$$

---

### Example 3: Four-Term Grouping

**Factor**: $x^3 - 2x^2 - 9x + 18$

**Group**:
$$(x^3 - 2x^2) + (-9x + 18)$$

**Factor each**:
$$x^2(x - 2) - 9(x - 2)$$

**Common binomial**:
$$(x - 2)(x^2 - 9)$$

**Continue factoring** (difference of squares):
$$(x - 2)(x + 3)(x - 3)$$

---

### Example 4: Perfect Square Trinomial

**Factor**: $25x^2 - 40x + 16$

**Check pattern** $a^2 - 2ab + b^2$:
- $a^2 = (5x)^2$ ✓
- $b^2 = 4^2$ ✓
- $2ab = 2(5x)(4) = 40x$ ✓

**Result**: $(5x - 4)^2$

---

### Example 5: Sum of Cubes

**Factor**: $27x^3 + 64$

**Recognize**: $(3x)^3 + 4^3$

**Apply pattern** $a^3 + b^3 = (a + b)(a^2 - ab + b^2)$:
$$= (3x + 4)((3x)^2 - (3x)(4) + 4^2)$$
$$= (3x + 4)(9x^2 - 12x + 16)$$

**Note**: Trinomial does not factor further.

---

### Example 6: Nested Factoring

**Factor**: $x^4 - 16$

**Method 1** - Difference of squares twice:
$$x^4 - 16 = (x^2)^2 - 4^2 = (x^2 + 4)(x^2 - 4)$$
$$= (x^2 + 4)(x + 2)(x - 2)$$

**Note**: $x^2 + 4$ is prime (sum of squares, no real factorization).

---

### Example 7: Trinomial with Negative Leading Coefficient

**Factor**: $-3x^2 + 14x + 5$

**Step 1** - Factor out -1 (or -3) to make leading coefficient positive:
$$= -1(3x^2 - 14x - 5)$$

**Step 2** - Factor trinomial:
- $AC = 3 \times (-5) = -15$
- Factors of -15 that add to -14: $-15$ and $1$

$$3x^2 - 15x + x - 5$$
$$= 3x(x - 5) + 1(x - 5)$$
$$= (x - 5)(3x + 1)$$

**Final**: $-1(x - 5)(3x + 1)$ or $-(x - 5)(3x + 1)$

---

### Example 8: No Common Factor, Use Grouping Strategy

**Factor**: $ax + ay + bx + by$

**Group**:
$$(ax + ay) + (bx + by)$$

**Factor each**:
$$a(x + y) + b(x + y)$$

**Common binomial**:
$$(x + y)(a + b)$$

---

## Applications

### 1. Solving Polynomial Equations

**Equation**: $x^2 + 5x - 14 = 0$

**Factor**: $(x + 7)(x - 2) = 0$

**Zero Product Property**: $x = -7$ or $x = 2$

**Critical**: Factoring converts polynomial equation to product form, enabling ZPP.

---

### 2. Simplifying Rational Expressions

**Simplify**: $\frac{x^2 - 4}{x^2 + 4x + 4}$

**Factor numerator**: $x^2 - 4 = (x + 2)(x - 2)$

**Factor denominator**: $x^2 + 4x + 4 = (x + 2)^2$

**Simplify**: $\frac{(x + 2)(x - 2)}{(x + 2)^2} = \frac{x - 2}{x + 2}, \quad x \neq -2$

---

### 3. Finding Zeros of Functions

**Function**: $f(x) = 2x^3 - 8x$

**Factor**: $2x(x^2 - 4) = 2x(x + 2)(x - 2)$

**Zeros**: Set each factor to zero:
- $2x = 0 \Rightarrow x = 0$
- $x + 2 = 0 \Rightarrow x = -2$
- $x - 2 = 0 \Rightarrow x = 2$

**Zeros**: $x = 0, -2, 2$

---

### 4. Graphing Polynomials

**Key feature identification**:
- **x-intercepts**: Zeros found by factoring
- **Behavior at intercepts**: Multiplicity determined by repeated factors

**Example**: $f(x) = (x - 1)^2(x + 3)$
- Zero at $x = 1$ with multiplicity 2 (touches x-axis, doesn't cross)
- Zero at $x = -3$ with multiplicity 1 (crosses x-axis)

---

### 5. Partial Fraction Decomposition (Advanced)

**Precalculus/Calculus**: Factoring denominators enables decomposition.

**Example**: $\frac{2x + 1}{x^2 - 1} = \frac{2x + 1}{(x + 1)(x - 1)}$

Enables decomposition into simpler fractions.

---

### 6. Optimization Problems

**Geometry**: Factoring area/volume expressions.

**Example**: Box volume $V = x(10 - 2x)(8 - 2x)$

Factoring reveals how dimensions relate to optimal volume.

---

## Common Misconceptions

### ❌ Misconception 1: Skipping GCF Step

**Incorrect approach**: Factor $6x^2 + 18x + 12$ directly as trinomial.

**Correct approach**: 
1. GCF first: $6(x^2 + 3x + 2)$
2. Then factor trinomial: $6(x + 1)(x + 2)$

**Why important**: Missing GCF means incomplete factorization.

---

### ❌ Misconception 2: Attempting to Factor Sum of Squares

**Incorrect**: $x^2 + 9 = (x + 3)(x + 3)$

**Check**: $(x + 3)^2 = x^2 + 6x + 9 \neq x^2 + 9$

**Correct**: $x^2 + 9$ is prime over real numbers (cannot factor).

**Note**: Difference of squares factors; sum of squares does not (over reals).

---

### ❌ Misconception 3: Wrong Signs in Factoring

**Problem**: Factor $x^2 - 5x + 6$

**Incorrect**: $(x - 2)(x + 3)$ (gives $x^2 + x - 6$)

**Correct**: $(x - 2)(x - 3)$ (gives $x^2 - 5x + 6$)

**Check method**: FOIL the result to verify.

---

### ❌ Misconception 4: Incomplete Factoring

**Problem**: Factor $x^4 - 16$

**Incomplete**: $x^4 - 16 = (x^2 + 4)(x^2 - 4)$ **STOP**

**Complete**: $(x^2 + 4)(x^2 - 4) = (x^2 + 4)(x + 2)(x - 2)$

**Always check**: Can any factor be factored further?

---

### ❌ Misconception 5: Incorrect AC Method Application

**Problem**: Factor $2x^2 + 7x + 3$

**Incorrect**: Find factors of 3 that add to 7 (doesn't work for $a \neq 1$)

**Correct**: 
- $AC = 2 \times 3 = 6$
- Find factors of 6 that add to 7: $6$ and $1$
- Rewrite: $2x^2 + 6x + x + 3$
- Group: $(2x^2 + 6x) + (x + 3) = 2x(x + 3) + 1(x + 3) = (x + 3)(2x + 1)$

---

### ❌ Misconception 6: Forgetting to Factor Out Negative

**Problem**: Factor $-x^2 + 4$

**Better approach**: Factor out $-1$ first:
$$-x^2 + 4 = -(x^2 - 4) = -(x + 2)(x - 2)$$

**Rationale**: Leading coefficient positive is easier to work with.

---

### ❌ Misconception 7: Confusing Factoring with Solving

**Factoring**: $x^2 - 5x + 6 = (x - 2)(x - 3)$ (expression manipulation)

**Solving**: $(x - 2)(x - 3) = 0 \Rightarrow x = 2$ or $x = 3$ (finding values)

**These are different processes!** Factoring is often a step in solving, but not the same thing.

---

## Related Concepts

### Prerequisites
- [[Distributive_Property]] - Foundation for factoring (reverse distribution)
- [[Special_Product_Patterns]] - Patterns used in reverse for factoring
- [[Combining_Like_Terms]] - Verifying factorization results

### Direct Dependencies
- [[Zero_Product_Property]] - Primary application of factoring in equations
- [[GCF_Factoring]] - Essential first step
- [[Prime_Polynomial]] - Recognizing when factoring is complete

### Applications
- [[Quadratic_Equations]] - Factoring method for solving
- [[Rational_Expressions_Operations]] - Simplification requires factoring
- [[Polynomial_Functions]] - Finding zeros and graphing features

### Advanced Topics
- [[Polynomial_Division]] - Alternative to factoring in some cases
- [[Rational_Root_Theorem]] - Finding possible rational zeros
- [[Complex_Factorization]] - Factoring over complex numbers

---

## Factoring Decision Tree

```mermaid
graph TD
    A[Start: Polynomial to Factor] --> B[Factor out GCF]
    B --> C{How many terms?}
    C -->|2 terms| D{What type?}
    C -->|3 terms| E{Perfect square?}
    C -->|4 terms| F[Try grouping]
    C -->|More| G[Look for patterns/creative grouping]
    
    D -->|a² - b²| H[Difference of Squares]
    D -->|a³ ± b³| I[Sum/Diff of Cubes]
    D -->|Other| J[Prime - cannot factor]
    
    E -->|Yes| K[Factor as (a±b)²]
    E -->|No| L{Form x² + bx + c?}
    
    L -->|Yes| M[Find factors of c that sum to b]
    L -->|No a≠1| N[Use AC method or trial-and-error]
    
    F --> O{Common binomial?}
    O -->|Yes| P[Factor it out]
    O -->|No| Q[Try different grouping]
    
    H --> R[Check each factor]
    I --> R
    K --> R
    M --> R
    N --> R
    P --> R
    
    R --> S{Can factor further?}
    S -->|Yes| B
    S -->|No| T[Complete - Verify by multiplying]
```

---

## Practice Problems

### Basic Factoring
1. Factor: $3x^2 - 12$ → **Answer**: $3(x + 2)(x - 2)$
2. Factor: $x^2 + 9x + 20$ → **Answer**: $(x + 4)(x + 5)$
3. Factor: $x^2 - 16$ → **Answer**: $(x + 4)(x - 4)$

### Intermediate
4. Factor: $2x^2 + 7x + 3$ → **Answer**: $(2x + 1)(x + 3)$
5. Factor: $x^3 + 2x^2 - 3x - 6$ → **Answer**: $(x + 2)(x + \sqrt{3})(x - \sqrt{3})$ or $(x + 2)(x^2 - 3)$
6. Factor: $9x^2 - 12x + 4$ → **Answer**: $(3x - 2)^2$

### Advanced
7. Factor completely: $x^4 - 81$ → **Answer**: $(x^2 + 9)(x + 3)(x - 3)$
8. Factor: $8x^3 - 27$ → **Answer**: $(2x - 3)(4x^2 + 6x + 9)$
9. Factor: $-5x^3 + 20x$ → **Answer**: $-5x(x + 2)(x - 2)$

### Application
10. Solve by factoring: $x^2 - 3x - 10 = 0$ → **Answer**: $x = 5$ or $x = -2$

---

## Summary

**Factoring strategies** provide systematic methods for expressing polynomials as products. The six core strategies—GCF, grouping, trinomial factoring (two types), and special patterns—combine to handle virtually all elementary factoring problems.

**Universal principle**: **ALWAYS factor out GCF first**, then apply appropriate strategy based on number of terms and pattern recognition.

**Complete factorization** requires:
1. Systematic strategy application
2. Checking each factor for further factorization
3. Verification by multiplication

**Primary application**: Converting polynomial equations to product form enables [[Zero_Product_Property]], transforming difficult equations into solvable systems.

**Mastery indicator**: Instant pattern recognition and efficient strategy selection without trial-and-error.

---

## Strategic Notes

### Factoring Efficiency Tips

1. **GCF first, always** - Reduces coefficients, simplifies remaining work
2. **Pattern recognition** - Train yourself to instantly see:
   - Difference of squares: Two terms, both perfect squares, subtraction
   - Perfect square trinomials: First/last are squares, middle = $2\sqrt{first}\sqrt{last}$
   - Cubes: Recognize perfect cube values (8, 27, 64, 125, ...)

3. **AC Method advantages** - Systematic (no guessing), works every time for factorable trinomials

4. **Verification habit** - Always multiply factors back to confirm correctness

5. **Prime recognition** - Know when to stop:
   - Sum of squares (over reals)
   - Trinomials with no integer factors meeting requirements
   - After applying all strategies with no result

### Common Factor Patterns to Memorize

**Perfect squares**: 1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, ...

**Perfect cubes**: 1, 8, 27, 64, 125, 216, ...

These enable rapid pattern recognition.
