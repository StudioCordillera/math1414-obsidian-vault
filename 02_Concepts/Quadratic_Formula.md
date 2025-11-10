---
layout: concept
title: "Quadratic Formula"
topic: "Polynomials"
type: Definition
status: stable
importance: critical
tags:
  - concept/algebra
  - chapter-1
  - math/quadratics
  - method/solving
sources:
  - MillerGerken2023
source_refs:
  - Miller & Gerken §1.4 p.124-126
relations:
  broader:
    - "[[Quadratic_Equations]]"
  depends_on:
    - "[[Completing_the_Square]]"
    - "[[The_Discriminant]]"
  related:
    - "[[Complex_Numbers]]"
    - "[[Zero_Product_Property]]"
    - "[[Square_Root_Property]]"
  used_in:
    - "[[Graphing_Quadratic_Functions]]"
    - "[[Quadratic_Optimization]]"
review:
  next: 2025-11-19
  cadence: monthly
created: 2025-10-19
updated: 2025-10-19
---

# Quadratic Formula

## The Formula

For any quadratic equation in standard form:
```
ax² + bx + c = 0  (where a ≠ 0)
```

The solutions are given by:

```
x = [-b ± √(b² - 4ac)] / (2a)
```

**Components**:
- **a** = coefficient of x² term (leading coefficient)
- **b** = coefficient of x term (linear coefficient)
- **c** = constant term
- **±** = gives TWO solutions (one with +, one with -)

## Why It Works

The quadratic formula is derived by completing the square on the general form ax² + bx + c = 0.

**Key Steps in Derivation**:
1. Start with ax² + bx + c = 0
2. Divide by a: x² + (b/a)x + c/a = 0
3. Complete the square on left side
4. Isolate x using square root property
5. Simplify to get formula

Result: A universal solution method for ALL quadratics

## When to Use

**Best Choice When**:
- Equation doesn't factor easily
- Need exact answers (not estimates)
- Discriminant analysis needed
- Variables have fractional coefficients
- Completing the square is tedious

**Alternative Methods** (sometimes better):
- **Factoring**: When factors are obvious (fastest)
- **Square Root Property**: When b = 0 (simpler)
- **Completing the Square**: When deriving formula or need vertex form

**Rule of Thumb**: Quadratic formula is the "universal" method - works for ALL quadratics

## The Discriminant

The expression under the radical, **b² - 4ac**, is called the **discriminant** (Δ or D).

```
Δ = b² - 4ac
```

**Discriminant determines solution types**:

| Discriminant Value | Solutions | Type |
|-------------------|-----------|------|
| Δ > 0 | Two distinct real solutions | Real, unequal |
| Δ = 0 | One repeated real solution | Real, equal (double root) |
| Δ < 0 | Two complex conjugate solutions | Complex (involves i) |

**Examples**:
- x² - 5x + 6 = 0: Δ = 25 - 24 = 1 > 0 → Two real solutions (x = 2, 3)
- x² - 4x + 4 = 0: Δ = 16 - 16 = 0 → One solution (x = 2)
- x² + x + 1 = 0: Δ = 1 - 4 = -3 < 0 → Two complex solutions (x = -½ ± i√3/2)

**See**: [[The_Discriminant]] for detailed analysis

## Step-by-Step Method

**To solve ax² + bx + c = 0**:

**Step 1**: Identify a, b, c from standard form
```
Example: 2x² - 3x - 4 = 0
a = 2, b = -3, c = -4
```

**Step 2**: Calculate discriminant (optional but recommended)
```
Δ = b² - 4ac = (-3)² - 4(2)(-4) = 9 + 32 = 41 > 0
Predicts: Two distinct real solutions
```

**Step 3**: Substitute into formula
```
x = [-(-3) ± √41] / (2·2)
x = [3 ± √41] / 4
```

**Step 4**: Write solutions
```
x = (3 + √41)/4  or  x = (3 - √41)/4
```

**Step 5**: Simplify if possible and check
```
If radical simplifies, reduce it
Check by substitution (recommended)
```

## Common Patterns

**No Linear Term** (b = 0):
```
ax² + c = 0
x = [±√(-4ac)] / (2a) = ±√(-c/a)
(Can use square root property more easily)
```

**No Constant Term** (c = 0):
```
ax² + bx = 0
x(ax + b) = 0
x = 0 or x = -b/a
(Factoring is easier here)
```

**Leading Coefficient is 1** (a = 1):
```
x² + bx + c = 0
x = [-b ± √(b² - 4c)] / 2
(Slightly simpler calculation)
```

## Critical Tips

**Sign Awareness**:
- Be EXTRA careful with negative b values
- Remember: -(-b) = +b in formula
- Example: If b = -5, then -b = 5 (positive)

**Simplifying Radicals**:
- Always check if √(b² - 4ac) can be simplified
- Factor perfect squares from radicand
- Example: √48 = √(16·3) = 4√3

**Denominator**:
- It's 2a, not just a
- Common error: forgetting the 2
- Can't cancel term by term: (3 ± √5)/4 ≠ 3/4 ± √5/4 separately

**Complex Solutions**:
- When Δ < 0, use i = √(-1)
- Example: √(-12) = i√12 = 2i√3

## Examples

**Example 1**: Standard Application
```
Solve: 3x² - 7x + 2 = 0

a = 3, b = -7, c = 2

x = [-(-7) ± √(49 - 24)] / 6
x = [7 ± √25] / 6
x = [7 ± 5] / 6

x = 12/6 = 2  or  x = 2/6 = 1/3
```

**Example 2**: Complex Solutions
```
Solve: x² + 2x + 5 = 0

a = 1, b = 2, c = 5

Δ = 4 - 20 = -16 < 0 (complex solutions)

x = [-2 ± √(-16)] / 2
x = [-2 ± 4i] / 2
x = -1 ± 2i
```

**Example 3**: One Solution (Perfect Square)
```
Solve: 4x² - 12x + 9 = 0

a = 4, b = -12, c = 9

Δ = 144 - 144 = 0 (one solution)

x = [12 ± 0] / 8
x = 12/8 = 3/2
```

## Common Mistakes

❌ **Sign Error**: Forgetting -b when b is negative
```
Wrong: x² - 6x + 5 = 0 gives x = [-6 ± ...] / 2
Right: x = [6 ± ...] / 2  (because -(-6) = 6)
```

❌ **Denominator Error**: Using a instead of 2a
```
Wrong: x = [-b ± √Δ] / a
Right: x = [-b ± √Δ] / (2a)
```

❌ **Premature Simplification**: Canceling incorrectly
```
Wrong: (6 ± 4√2) / 2 = 6 ± 2√2
Right: (6 ± 4√2) / 2 = 3 ± 2√2
(Divide EACH term in numerator by 2)
```

❌ **Not Simplifying**: Leaving radical unsimplified
```
Wrong: x = [3 ± √12] / 2 (final answer)
Right: x = [3 ± 2√3] / 2 = (3 ± 2√3)/2
```

❌ **Wrong Form**: Not writing in standard form first
```
Wrong: Using formula on 2x² = 5x - 3
Right: First rewrite as 2x² - 5x + 3 = 0, then apply formula
```

## Advantages

1. **Universal**: Works for ALL quadratic equations
2. **Reliable**: No guessing required (unlike factoring)
3. **Exact**: Gives precise answers (not estimates)
4. **Predictive**: Discriminant tells solution type before solving
5. **Efficient**: Direct path to answer

## Historical Note

- Known to ancient Babylonians (~2000 BCE) in geometric form
- Algebraic formula developed by Indian mathematician Brahmagupta (~628 CE)
- Completed by Persian mathematician Al-Khwarizmi (~820 CE)
- Modern notation established in 16th century Europe
- One of the most important formulas in algebra

## Memorization Tip

**Mnemonic**: "negative b, plus or minus, square root, b squared minus four a c, all over two a"

**Rhythm Method**: Say it to a beat:
"x equals negative b / plus or minus square root / b squared minus four a c / all over two a"

**Visual**: Draw the formula large and label each part

## Summary

> The Quadratic Formula provides solutions to any quadratic equation ax² + bx + c = 0. The discriminant b² - 4ac predicts the nature of solutions: two real (Δ > 0), one real (Δ = 0), or two complex (Δ < 0).

---

**See Also**:
- [[Quadratic_Equations]] - Types and solving methods
- [[The_Discriminant]] - Solution type prediction
- [[Completing_the_Square]] - Derivation method
- [[Complex_Numbers]] - For when Δ < 0
- [[Zero_Product_Property]] - Alternative solving method
- [[Graphing_Quadratic_Functions]] - Geometric interpretation

**Practice**: [[01_Course/Textbook/Chapter1_Equations_Inequalities]] - Section 1.4

**Source**: Chapter 1.4 - Miller & Gerken College Algebra & Trigonometry
