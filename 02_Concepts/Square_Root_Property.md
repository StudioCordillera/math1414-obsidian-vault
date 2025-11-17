---
layout: concept
title: Square Root Property
topic: Polynomials
type: Claim
status: stable
importance: critical
tags:
- math/properties
- math/quadratic
- math/equations
- concept/method
sources:
- miller-gerken-2ed
source_refs:
- Miller & Gerken §1.4 p.102-103
relations:
  broader:
  - '[[Quadratic_Equations]]'
  narrower: []
  depends_on:
  - '[[Equality_Properties]]'
  - '[[Real_Number_System]]'
  - '[[Complex_Numbers]]'
  - '[[Imaginary_Unit]]'
  defines: []
  used_in:
  - '[[Completing_the_Square]]'
  - '[[Quadratic_Formula]]'
  related:
  - '[[Zero_Product_Property]]'
  - '[[Radical_Equations]]'
review:
  next: 2025-10-26
  cadence: monthly
created: 2025-10-19
updated: 2025-11-16
qa_certified: true
qa_date: 2025-11-16
qa_migration: v2.0
related:
- '[[Quadratic_Formula]]'
---
# Square Root Property

## Definition

The **Square Root Property** states that if $x^2 = k$, then $x = \pm\sqrt{k}$.

### Formal Statement

**Property**: For any real number $k$:
$$\text{If } x^2 = k, \text{ then } x = \pm\sqrt{k}$$

**Symbol Meaning**: The notation $\pm$ (read as "plus or minus") indicates **two solutions**:
- $x = +\sqrt{k}$ (the positive square root)
- $x = -\sqrt{k}$ (the negative square root)

### Why Two Solutions?

**Reasoning**:
```
If x² = k, then x · x = k

Two values when squared give k:
• Positive: √k · √k = k
• Negative: (-√k) · (-√k) = k

Therefore: x = √k or x = -√k
```

**Example**:
```
x² = 16
Then: x = ±√16 = ±4

Check:
• x = 4:  4² = 16 ✓
• x = -4: (-4)² = 16 ✓

Both values satisfy the equation!
```

---

## When to Use

### Ideal Situations

The Square Root Property is most efficient when:

**1. Perfect Square Form**:
```
x² = 25
(x - 3)² = 16
(2x + 1)² = 9
```

**2. No Linear Term**:
```
Equations like: ax² = c (no x term)

Example: 3x² = 48
          x² = 16
          x = ±4
```

**3. After Completing the Square**:
```
x² + 6x + 9 = 25
(x + 3)² = 25    ← Perfect square created
x + 3 = ±5       ← Apply Square Root Property
```

**4. In Geometric Problems**:
```
Area of square = 64 ft²
s² = 64
s = ±8

Context: Side length must be positive → s = 8 ft
```

### When NOT to Use

Avoid Square Root Property when:
- Factoring is easier: $x^2 - 5x + 6 = 0$ → factor instead
- Quadratic formula is needed: $2x^2 + 3x - 5 = 0$ → has linear term
- Expression is not a perfect square

---

## Solution Types by Value of k

### Case 1: k > 0 (Positive)

**Result**: Two distinct real solutions

**Example**: $x^2 = 9$
```
x = ±√9 = ±3

Solutions: x = 3 and x = -3 (both real, distinct)
```

**Number line**:
```
      ×                    ×
  ----|--------------------|----
     -3                    3
     
Two points, symmetric about origin
```

### Case 2: k = 0 (Zero)

**Result**: One repeated solution (or "double root")

**Example**: $x^2 = 0$
```
x = ±√0 = ±0 = 0

Solution: x = 0 (only one value, repeated)
```

**Interpretation**: Both positive and negative roots coincide at zero.

### Case 3: k < 0 (Negative)

**Result**: Two complex conjugate solutions (no real solutions)

**Example**: $x^2 = -4$
```
x = ±√(-4)
x = ±√(4 · -1)
x = ±2√(-1)
x = ±2i

Solutions: x = 2i and x = -2i (complex conjugates)
```

**Key Insight**: Square roots of negative numbers require complex numbers.

### Case 4: k is Not a Perfect Square

**Result**: Two irrational real solutions

**Example**: $x^2 = 7$
```
x = ±√7

Solutions: x = √7 ≈ 2.646 and x = -√7 ≈ -2.646

These are exact (irrational) values, not approximations
```

**Note**: Leave in radical form unless asked to approximate.

---

## Step-by-Step Method

### Standard Process

**Given**: Equation in form $(expression)^2 = k$

**Steps**:
```
1. Verify equation is in form u² = k
2. Apply Square Root Property: u = ±√k
3. Simplify the radical if possible
4. Solve for the variable
5. Check both solutions (if required)
```

### Example 1: Basic Application

**Solve**: $x^2 = 25$

```
Step 1: Already in form x² = k, where k = 25

Step 2: Apply Square Root Property
        x = ±√25

Step 3: Simplify
        x = ±5

Step 4: Write solutions
        x = 5 or x = -5

Check:
• For x = 5:  5² = 25 ✓
• For x = -5: (-5)² = 25 ✓

Solutions: x = ±5
```

### Example 2: With a Binomial Square

**Solve**: $(x - 3)^2 = 16$

```
Step 1: Form (x - 3)² = k, where k = 16

Step 2: Apply Square Root Property
        x - 3 = ±√16

Step 3: Simplify
        x - 3 = ±4

Step 4: Solve for x (add 3 to both sides)
        x = 3 ± 4

Step 5: Expand ± notation
        x = 3 + 4 = 7  or  x = 3 - 4 = -1

Solutions: x = 7 and x = -1
```

### Example 3: Irrational Solutions

**Solve**: $(x + 2)^2 = 10$

```
Step 1: Form (x + 2)² = 10

Step 2: Apply Square Root Property
        x + 2 = ±√10

Step 3: Radical is already simplified

Step 4: Solve for x
        x = -2 ± √10

Step 5: Write as two solutions
        x = -2 + √10  or  x = -2 - √10

Solutions: x = -2 ± √10

Approximate: x ≈ 1.162 or x ≈ -5.162
```

### Example 4: Complex Solutions

**Solve**: $x^2 + 9 = 0$

```
Step 1: Isolate x²
        x² = -9

Step 2: Apply Square Root Property
        x = ±√(-9)

Step 3: Express using imaginary unit
        x = ±√(9 · -1)
        x = ±3√(-1)
        x = ±3i

Solutions: x = 3i and x = -3i (complex conjugates)
```

---

## Relationship to Completing the Square

### The Connection

The Square Root Property is the **final step** in completing the square:

**Process**:
```
Start:    x² + 6x = 7           (Not in perfect square form)
Add (6/2)²: x² + 6x + 9 = 7 + 9  (Complete the square)
Factor:   (x + 3)² = 16         (Perfect square form)
Apply SRP: x + 3 = ±4           (Square Root Property!)
Solve:    x = -3 ± 4
          x = 1 or x = -7
```

**Key Insight**: Completing the square transforms ANY quadratic into a form where Square Root Property applies.

### Derivation of Quadratic Formula

The quadratic formula is derived using Square Root Property:

**Start**: $ax^2 + bx + c = 0$ (divide by $a$)

$$x^2 + \frac{b}{a}x + \frac{c}{a} = 0$$

**Complete the square**: (add $(\frac{b}{2a})^2$ to both sides)

$$x^2 + \frac{b}{a}x + \frac{b^2}{4a^2} = -\frac{c}{a} + \frac{b^2}{4a^2}$$

**Factor left side**:

$$\left(x + \frac{b}{2a}\right)^2 = \frac{b^2 - 4ac}{4a^2}$$

**Apply Square Root Property**:

$$x + \frac{b}{2a} = \pm\frac{\sqrt{b^2 - 4ac}}{2a}$$

**Solve for x**:

$$x = -\frac{b}{2a} \pm \frac{\sqrt{b^2 - 4ac}}{2a} = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}$$

**This is the quadratic formula!**

---

## Common Errors and Misconceptions

### Error 1: Forgetting the ± Sign

**Incorrect**:
```
x² = 16
x = √16 = 4    ✗ (Missing the negative solution!)
```

**Correct**:
```
x² = 16
x = ±√16 = ±4
x = 4 or x = -4 ✓
```

**Why it matters**: Missing a solution is a complete error in mathematics.

### Error 2: Taking Square Root of Both Sides Incorrectly

**Incorrect approach**:
```
x² = 16
√(x²) = √16
x = 4    ✗ (This reasoning is flawed)
```

**Why it's wrong**: $\sqrt{x^2} = |x|$ (absolute value), not just $x$!

**Correct reasoning**:
```
x² = 16 means x · x = 16
Both 4 · 4 = 16 and (-4) · (-4) = 16
Therefore: x = ±4
```

### Error 3: Applying to Equations Not in Correct Form

**Incorrect**:
```
x² + 5x = 14
x + 5 = ±√14    ✗ (Can't apply SRP directly!)
```

**Why it's wrong**: Square Root Property requires form $u^2 = k$, not $u^2 + \text{something} = k$.

**Correct**: Must rearrange to standard form or complete the square first.

### Error 4: Simplifying √(negative) Incorrectly

**Incorrect**:
```
x² = -16
x = ±√(-16) = ±4    ✗ (Forgot about imaginary unit!)
```

**Correct**:
```
x² = -16
x = ±√(-16) = ±√(16 · -1) = ±4i
```

**Key**: Negative under radical requires imaginary unit $i = \sqrt{-1}$.

### Error 5: Rejecting Negative Solutions Prematurely

**Context matters**:
```
"What is the side length of a square with area 64 ft²?"

Math: s² = 64 → s = ±8
Context: Side length must be positive → s = 8 ft (reject s = -8)

BUT in pure equation solving:
x² = 64 has TWO solutions: x = ±8 (both valid mathematically)
```

**Guideline**: Keep both solutions unless the context requires rejection.

---

## Applications

### Application 1: Geometry - Pythagorean Theorem

**Problem**: Find the length of the diagonal of a square with side length 5 cm.

```
Using Pythagorean theorem: d² = 5² + 5²
                           d² = 25 + 25 = 50

Apply Square Root Property:
d = ±√50 = ±√(25 · 2) = ±5√2

Context: Length must be positive
Answer: d = 5√2 ≈ 7.07 cm
```

### Application 2: Physics - Free Fall

**Problem**: An object is dropped from 64 feet. The height equation is $h(t) = -16t^2 + 64$. When does it hit the ground?

```
At ground level: h(t) = 0
0 = -16t² + 64
16t² = 64
t² = 4

Apply Square Root Property:
t = ±√4 = ±2

Context: Time must be positive
Answer: t = 2 seconds
```

### Application 3: Area Problems

**Problem**: A square has area 20 square inches. Find the side length.

```
Area formula: s² = 20

Apply Square Root Property:
s = ±√20 = ±√(4 · 5) = ±2√5

Context: Side length must be positive
Answer: s = 2√5 ≈ 4.47 inches
```

### Application 4: Complex Numbers

**Problem**: Solve $4x^2 + 25 = 0$ for complex solutions.

```
4x² + 25 = 0
4x² = -25
x² = -25/4

Apply Square Root Property:
x = ±√(-25/4) = ±√(25/4 · -1)
x = ±(5/2)i
x = ±(5/2)i = ±2.5i

Solutions: x = 2.5i and x = -2.5i (complex conjugates)
```

---

## Theoretical Foundation

### Why Does This Property Work?

**Mathematical Proof**:

**Given**: $x^2 = k$

**To prove**: $x = \pm\sqrt{k}$

**Proof**:
```
1. Start with x² = k
2. By definition of square root: (√k)² = k
3. Therefore: x² = (√k)²
4. This means: x² - (√k)² = 0
5. Factor as difference of squares: (x - √k)(x + √k) = 0
6. By Zero Product Property: x - √k = 0 or x + √k = 0
7. Solving each: x = √k or x = -√k
8. Written compactly: x = ±√k ∎
```

### Connection to Quadratic Formula

When $b = 0$ in the quadratic formula:

$$x = \frac{-0 \pm \sqrt{0^2 - 4ac}}{2a} = \frac{\pm\sqrt{-4ac}}{2a}$$

For $ax^2 = c$ (when $b = 0$):
$$x^2 = \frac{c}{a}$$

Square Root Property gives:
$$x = \pm\sqrt{\frac{c}{a}}$$

**Both methods agree** when there's no linear term!

---

## Practice Problems

### Level 1: Basic

**1.** Solve: $x^2 = 49$
<details><summary>Solution</summary>

```
x = ±√49 = ±7
Solutions: x = 7 or x = -7
```
</details>

**2.** Solve: $x^2 = 100$
<details><summary>Solution</summary>

```
x = ±√100 = ±10
Solutions: x = 10 or x = -10
```
</details>

### Level 2: Binomial Squares

**3.** Solve: $(x - 5)^2 = 36$
<details><summary>Solution</summary>

```
x - 5 = ±√36 = ±6
x = 5 ± 6
x = 11 or x = -1
```
</details>

**4.** Solve: $(x + 3)^2 = 25$
<details><summary>Solution</summary>

```
x + 3 = ±5
x = -3 ± 5
x = 2 or x = -8
```
</details>

### Level 3: Irrational Solutions

**5.** Solve: $x^2 = 12$
<details><summary>Solution</summary>

```
x = ±√12 = ±√(4 · 3) = ±2√3
Solutions: x = 2√3 or x = -2√3

Approximate: x ≈ ±3.46
```
</details>

**6.** Solve: $(x - 1)^2 = 18$
<details><summary>Solution</summary>

```
x - 1 = ±√18 = ±√(9 · 2) = ±3√2
x = 1 ± 3√2

Solutions: x = 1 + 3√2 ≈ 5.24 or x = 1 - 3√2 ≈ -3.24
```
</details>

### Level 4: Complex Solutions

**7.** Solve: $x^2 = -25$
<details><summary>Solution</summary>

```
x = ±√(-25) = ±√(25 · -1) = ±5i
Solutions: x = 5i or x = -5i
```
</details>

**8.** Solve: $3x^2 + 48 = 0$
<details><summary>Solution</summary>

```
3x² = -48
x² = -16
x = ±√(-16) = ±4i

Solutions: x = 4i or x = -4i
```
</details>

### Level 5: Applications

**9.** A square has area 75 cm². Find its side length (exact and approximate).
<details><summary>Solution</summary>

```
s² = 75
s = ±√75 = ±√(25 · 3) = ±5√3

Context: Side length must be positive
s = 5√3 cm ≈ 8.66 cm
```
</details>

**10.** Solve: $(2x + 3)^2 = 20$
<details><summary>Solution</summary>

```
2x + 3 = ±√20 = ±2√5
2x = -3 ± 2√5
x = (-3 ± 2√5)/2

Solutions: x = (-3 + 2√5)/2 ≈ 0.736 or x = (-3 - 2√5)/2 ≈ -3.736
```
</details>

---

## Summary

The **Square Root Property** is a fundamental tool for solving quadratic equations:

**Property**: If $x^2 = k$, then $x = \pm\sqrt{k}$

**Key Points**:
- Always gives TWO solutions (except when $k = 0$)
- The $\pm$ symbol is mandatory (represents both positive and negative roots)
- Solutions can be real, irrational, or complex depending on $k$
- Most efficient for equations in perfect square form
- Essential step in completing the square method
- Foundation of the quadratic formula derivation

**When to Use**:
- Perfect square form: $(expression)^2 = k$
- No linear term: $ax^2 = c$
- After completing the square
- Geometric problems involving squares

**Common Errors to Avoid**:
- Forgetting the $\pm$ sign
- Mishandling negative values under radicals
- Applying to equations not in correct form

**Connection**: The Square Root Property bridges elementary algebra (solving $x^2 = k$) to advanced techniques (completing the square, quadratic formula) and extends to complex numbers.

---

**References**:
- Miller & Gerken, *College Algebra & Trigonometry*, 2nd Ed., §1.4, pp.102-103
- Related concepts: [[Quadratic_Equations]], [[Completing_the_Square]], [[Complex_Numbers]], [[Zero_Product_Property]]
---
type: Claim
status: stable
importance: high
tags:
  - concept/property
  - concept/method
  - algebra/equations
  - algebra/quadratics
sources:
  - textbook-ch1
source_refs:
  - "Miller & Gerken §1.4 p.115-117"
relations:
  broader:
    - "[[Quadratic_Equations]]"
    - "[[Root_Extraction_Methods]]"
  narrower:
    - "[[Square_Root_Property_Simple_Form]]"
    - "[[Square_Root_Property_General_Form]]"
  depends_on:
    - "[[Square_Roots]]"
    - "[[Real_Number_System]]"
    - "[[Complex_Numbers]]"
  defines:
    - "[[Quadratic_Solution_Method]]"
  related:
    - "[[Completing_the_Square]]"
    - "[[Quadratic_Formula]]"
    - "[[Plus_Minus_Notation]]"
  used_in:
    - "[[Quadratic_Equations]]"
    - "[[Completing_the_Square]]"
    - "[[Circle_Equations]]"
    - "[[Pythagorean_Theorem]]"
review:
  last: 2025-10-19
  next: 2025-11-02
  interval: 14
created: 2025-10-19
updated: 2025-10-19
---

# Square Root Property

## Definition

The **Square Root Property** states that if an expression squared equals a constant, then the expression equals the positive or negative square root of that constant.

### Formal Statement

**If u² = k, then u = ±√k**

Where:
- **u**: Any algebraic expression
- **k**: A real constant (can be positive, negative, or zero)
- **±**: Plus-or-minus symbol (indicates two solutions)

### Alternative Notation

**u² = k ⟺ u = √k or u = -√k**

Both forms express the same idea: squaring creates two solutions (one positive, one negative).

---

## Why This Property Works

### Understanding Through Squaring

Consider what happens when we square both positive and negative numbers:

```
(+3)² = 9
(-3)² = 9
```

**Both +3 and -3 square to give 9**

Therefore, if x² = 9, then x could be either +3 or -3.

**Key insight**: Squaring "loses" information about the sign. Taking the square root must "recover" both possibilities.

---

### Geometric Interpretation

If x² = k, we're asking: **"What number, when squared, gives k?"**

On the number line, two numbers equidistant from zero will have the same square:

```
        |----|----|----|
       -√k   0   +√k
       
Both -√k and +√k square to k
```

---

## Three Cases of the Square Root Property

### Case 1: k > 0 (Positive)

**If u² = k where k > 0, then u = ±√k**

**Two distinct real solutions**

**Example**: x² = 16
```
x = ±√16
x = ±4
x = 4  or  x = -4
```

**Check**:
- (4)² = 16 ✓
- (-4)² = 16 ✓

---

### Case 2: k = 0 (Zero)

**If u² = 0, then u = 0**

**One solution (repeated root)**

**Example**: x² = 0
```
x = ±√0
x = 0
```

Only one solution because √0 = 0 and -√0 = 0.

---

### Case 3: k < 0 (Negative)

**If u² = k where k < 0, then u = ±i√|k|**

**Two complex conjugate solutions**

**Example**: x² = -9
```
x = ±√(-9)
x = ±√(9 · (-1))
x = ±√9 · √(-1)
x = ±3i
```

**Solutions**: x = 3i or x = -3i (complex numbers)

See [[Complex_Numbers]] and [[Imaginary_Unit]]

---

## The ± Symbol (Plus-or-Minus)

### Notation

**x = ±a** means **x = a or x = -a**

**Compact way to write two solutions simultaneously**

### Examples

- x = ±5 means x = 5 or x = -5
- x = ±√7 means x = √7 or x = -√7
- x = ±2i means x = 2i or x = -2i

### Common Error

**❌ Don't write**: x = ± both answers

**✓ Write**: x = ±5, which means two separate solutions: x = 5 and x = -5

---

## Step-by-Step Method

### For Simple Form: x² = k

**Step 1**: Ensure equation is in form u² = k (expression squared equals constant)

**Step 2**: Apply square root property: u = ±√k

**Step 3**: Simplify radicals if possible

**Step 4**: Write two solutions explicitly

**Step 5**: Check both solutions in original equation

---

### For General Form: (x - h)² = k

**Step 1**: Isolate the squared expression: (x - h)² = k

**Step 2**: Apply square root property: x - h = ±√k

**Step 3**: Solve for x: x = h ± √k

**Step 4**: Write two solutions: x = h + √k and x = h - √k

**Step 5**: Check solutions

---

## Examples

### Example 1: Simple Positive Constant

**Solve**: x² = 25

**Solution**:
```
x² = 25                [Given]
x = ±√25               [Square Root Property]
x = ±5                 [Simplify]
```

**Two solutions**: x = 5 or x = -5

**Check**:
- (5)² = 25 ✓
- (-5)² = 25 ✓

---

### Example 2: Non-Perfect Square

**Solve**: x² = 7

**Solution**:
```
x² = 7                 [Given]
x = ±√7                [Square Root Property]
```

**Two solutions**: x = √7 or x = -√7 (exact form)

**Approximate values**: x ≈ 2.646 or x ≈ -2.646

---

### Example 3: Negative Constant (Complex Solutions)

**Solve**: x² = -16

**Solution**:
```
x² = -16               [Given]
x = ±√(-16)            [Square Root Property]
x = ±√(16 · (-1))      [Factor]
x = ±√16 · √(-1)       [Product property]
x = ±4i                [Since √(-1) = i]
```

**Two complex solutions**: x = 4i or x = -4i

---

### Example 4: Equation with Binomial Squared

**Solve**: (x - 3)² = 16

**Solution**:
```
(x - 3)² = 16          [Given]
x - 3 = ±√16           [Square Root Property]
x - 3 = ±4             [Simplify]
x = 3 ± 4              [Add 3 to both sides]
```

**Two solutions**:
```
x = 3 + 4 = 7
x = 3 - 4 = -1
```

**Answer**: x = 7 or x = -1

**Check**:
- (7 - 3)² = 4² = 16 ✓
- (-1 - 3)² = (-4)² = 16 ✓

---

### Example 5: Coefficient Before x²

**Solve**: 3x² = 27

**Solution**:
```
3x² = 27               [Given]
x² = 9                 [Divide both sides by 3]
x = ±√9                [Square Root Property]
x = ±3                 [Simplify]
```

**Two solutions**: x = 3 or x = -3

**Note**: Must isolate x² before applying the property!

---

### Example 6: Fractional Constant

**Solve**: x² = 1/4

**Solution**:
```
x² = 1/4               [Given]
x = ±√(1/4)            [Square Root Property]
x = ±(√1/√4)           [Quotient property of radicals]
x = ±(1/2)             [Simplify]
```

**Two solutions**: x = 1/2 or x = -1/2

---

### Example 7: Requires Algebraic Manipulation First

**Solve**: (2x + 1)² = 9

**Solution**:
```
(2x + 1)² = 9          [Given]
2x + 1 = ±√9           [Square Root Property]
2x + 1 = ±3            [Simplify]
2x = -1 ± 3            [Subtract 1]
```

**Case 1**: 
```
2x = -1 + 3 = 2
x = 1
```

**Case 2**:
```
2x = -1 - 3 = -4
x = -2
```

**Two solutions**: x = 1 or x = -2

---

### Example 8: Zero Result

**Solve**: (x + 5)² = 0

**Solution**:
```
(x + 5)² = 0           [Given]
x + 5 = ±√0            [Square Root Property]
x + 5 = 0              [Since ±0 = 0]
x = -5                 [Subtract 5]
```

**One solution**: x = -5 (repeated root)

---

## Relationship to Other Methods

### vs. Factoring Method

**Square Root Property**:
- Best when equation is already in form u² = k
- Works for non-perfect squares
- Direct and fast

**Factoring**:
- Best when polynomial factors easily
- Requires Zero Product Property
- May not work if not factorable

**Example**: x² = 11
- Square Root Method: x = ±√11 ✓ (immediate)
- Factoring: x² - 11 = 0 cannot be factored over integers ✗

---

### vs. Quadratic Formula

**Square Root Property**:
- Limited to equations in form u² = k
- Simpler and faster when applicable
- No formula to memorize (just take ± square root)

**Quadratic Formula**:
- Works for ALL quadratic equations
- More complex to use
- Universally applicable

**Hierarchy**:
1. Try Square Root Property first (if in form u² = k)
2. Try factoring (if easily factorable)
3. Use Quadratic Formula (always works)

See [[Quadratic_Formula]]

---

### Leads to Completing the Square

The Square Root Property is the KEY STEP in completing the square:

**Example**: x² + 6x = 7
```
x² + 6x + 9 = 7 + 9        [Complete the square]
(x + 3)² = 16               [Factor left side]
x + 3 = ±√16                [Square Root Property - THIS STEP!]
x + 3 = ±4
x = -3 ± 4
x = 1 or x = -7
```

See [[Completing_the_Square]]

---

## Applications

### 1. Geometric Problems

**Area of Square**: If area = 50 cm², find side length
```
s² = 50
s = ±√50
s = ±5√2

Physical answer: s = 5√2 cm (reject negative)
```

---

### 2. Pythagorean Theorem

**Right triangle**: If a² + b² = c², solve for unknown side
```
Given: a = 3, c = 5, find b
3² + b² = 5²
9 + b² = 25
b² = 16
b = ±4
Physical answer: b = 4 (reject negative)
```

See [[Pythagorean_Theorem]]

---

### 3. Circle Equations

**Standard form**: (x - h)² + (y - k)² = r²

**Find x-intercepts**: Set y = 0
```
(x - h)² = r²
x - h = ±r            [Square Root Property]
x = h ± r
```

See [[Circle_Equations]]

---

### 4. Projectile Motion

**Height equation**: h(t) = -16t² + v₀t + h₀

**When does object hit ground?** (h = 0)
```
-16t² + v₀t + h₀ = 0
```
If simplified to form t² = k, use Square Root Property

---

## Common Misconceptions

### ❌ Misconception 1: "Forgetting the ± symbol"

**Wrong**: If x² = 9, then x = 3

**Right**: If x² = 9, then x = ±3 (two solutions: x = 3 and x = -3)

**Why it matters**: You're missing half the solutions!

**Example**:
```
x² - 9 = 0
x² = 9
x = 3 only ✗ INCOMPLETE!
x = ±3 ✓ COMPLETE (two solutions: 3 and -3)
```

---

### ❌ Misconception 2: "Square root of negative number is impossible"

**Wrong**: √(-9) has no solution

**Right**: √(-9) = 3i (complex solution)

**Reality**: 
- No **real** solution when k < 0
- Two **complex** solutions: ±i√|k|

**Example**: x² = -25
```
x = ±√(-25)
x = ±5i         [Complex solutions exist!]
```

---

### ❌ Misconception 3: "Can apply property to both sides"

**Wrong**: If x² = y², can I conclude x = ±y?

**Partially right**: This gives x = y or x = -y

**Better approach**: Move everything to one side first
```
x² = y²
x² - y² = 0
(x - y)(x + y) = 0    [Factor]
x = y  or  x = -y     [Zero Product Property]
```

---

### ❌ Misconception 4: "The property works in reverse"

**Wrong**: If x = ±3, then x² = 9

**Right**: This IS correct! But be careful...

**Issue**: When you square both sides of an equation, you might introduce extraneous solutions

**Example**:
```
x = 3              [Original]
x² = 9             [Square both sides - VALID]

But if we started with x² = 9:
x = ±3             [Two solutions]
```

Squaring is **not** perfectly reversible—it loses sign information.

---

### ❌ Misconception 5: "Must have x² on left side"

**Wrong**: Only works if it's exactly x² = k

**Right**: Can be ANY expression squared equals constant
- (x - 3)² = 16 ✓
- (2x + 5)² = 7 ✓
- (x² + 1)² = 4 ✓

**Flexibility**: u² = k where u is any expression

---

### ❌ Misconception 6: "The ± means add or subtract both"

**Wrong**: x = 5 ± 3 means x = 5 + 3 and x = 5 - 3 simultaneously

**Right**: x = 5 ± 3 means two separate values:
- x = 5 + 3 = 8 (one solution)
- x = 5 - 3 = 2 (other solution)

**Not**: x = 5 plus or minus both values at once

---

## Special Considerations

### When Physical Context Restricts Solutions

**Mathematical solutions**: Both ± values

**Physical context**: May reject negative or complex solutions

**Example**: Area of a square = 49 ft²
```
s² = 49
s = ±7

Mathematical: s = 7 or s = -7
Physical: s = 7 only (length cannot be negative)
```

**Always**: 
1. Find all mathematical solutions
2. Check which make sense in context
3. State restrictions clearly

---

### Exact vs. Approximate Form

**Exact form** (preferred in algebra): x = ±√7

**Approximate form** (used in applications): x ≈ ±2.646

**When to use each**:
- **Exact**: When doing further algebra, theoretical work
- **Approximate**: When needing numerical answer for real-world application

---

## Connection to Other Concepts

### Builds Upon
- [[Square_Roots]] - Definition and properties
- [[Real_Number_System]] - For real solutions
- [[Complex_Numbers]] - For complex solutions
- [[Plus_Minus_Notation]] - Understanding ± symbol

### Supports
- [[Quadratic_Equations]] - One of four solution methods
- [[Completing_the_Square]] - Essential step in the process
- [[Quadratic_Formula_Derivation]] - Used to derive the formula
- [[Circle_Equations]] - Finding intercepts

### Related Methods
- [[Factoring_Method]] - Alternative for some quadratics
- [[Quadratic_Formula]] - Universal method
- [[Graphing_Method]] - Visual approach

### Used In
- [[Pythagorean_Theorem]] - Solving for unknown sides
- [[Distance_Formula]] - Isolating coordinates
- [[Projectile_Motion]] - Time calculations
- [[Optimization_Problems]] - Finding extrema

---

## Comparison: All Quadratic Solution Methods

| Method | Best When | Advantages | Limitations |
|--------|-----------|------------|-------------|
| **Square Root Property** | u² = k form | Fast, direct | Only works for this form |
| **Factoring** | Easily factorable | Quick, builds number sense | Doesn't work for all equations |
| **Completing Square** | Teaching derivations | Shows structure | More steps required |
| **Quadratic Formula** | Any quadratic | Always works | Formula to memorize |

---

## Practice Problems

### Problem 1
Solve: x² = 81

**Solution**:
```
x = ±√81
x = ±9
```
**Answer**: x = 9 or x = -9

---

### Problem 2
Solve: (x - 7)² = 25

**Solution**:
```
x - 7 = ±√25
x - 7 = ±5
x = 7 ± 5
x = 12 or x = 2
```

---

### Problem 3
Solve: 2x² = 50

**Solution**:
```
x² = 25        [Divide by 2]
x = ±5
```

---

### Problem 4
Solve: x² = -36

**Solution**:
```
x = ±√(-36)
x = ±6i
```
**Answer**: x = 6i or x = -6i (complex solutions)

---

### Problem 5
Solve: (3x + 2)² = 49

**Solution**:
```
3x + 2 = ±7
3x = -2 ± 7

Case 1: 3x = -2 + 7 = 5, so x = 5/3
Case 2: 3x = -2 - 7 = -9, so x = -3
```
**Answer**: x = 5/3 or x = -3

---

## Summary

The **Square Root Property** states: **If u² = k, then u = ±√k**

**Key points**:
1. ✅ Always include ± symbol (two solutions for k > 0)
2. ✅ Three cases: k > 0 (two real), k = 0 (one real), k < 0 (two complex)
3. ✅ Works for ANY expression squared: (x - h)², (ax + b)², etc.
4. ✅ Fastest method when equation is in form u² = k

**When to use**:
- Equation already in form u² = k
- After completing the square
- Geometric problems (area, Pythagorean theorem)
- Circle equations

**Remember**:
- **Don't forget ±**: Most common error!
- **Check context**: Physical problems may reject negative solutions
- **Complex numbers**: Negative constants give imaginary solutions
- **Simple and powerful**: Often overlooked in favor of quadratic formula

**The Square Root Property is the heart of solving quadratic equations**—master it early!

---

## References

- Miller & Gerken, *College Algebra*, Section 1.4: "Quadratic Equations"
- [[Quadratic_Equations]] - Context for this method
- [[Completing_the_Square]] - Uses this as essential step
- [[Complex_Numbers]] - For k < 0 solutions
- [[Pythagorean_Theorem]] - Common application

---

*Last updated: 2025-10-19*
*Status: Stable ✓*
*Review: Every 2 weeks*
