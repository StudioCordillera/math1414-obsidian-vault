---
layout: concept
title: "Imaginary Unit"
topic: "General Math"
type: Definition
status: stable
importance: critical
tags:
  - concept/number-system
  - concept/algebra
  - chapter1
  - complex-numbers
  - foundation
sources:
  - MillerGerken2023
source_refs:
  - "Miller & Gerken §1.3 p.108-109"
relations:
  broader:
    - "[[Complex_Numbers]]"
  defines:
    - "[[Complex_Numbers]]"
  related:
    - "[[Exponents]]"
    - "[[Square_Roots]]"
  used_in:
    - "[[Complex_Number_Operations]]"
    - "[[Quadratic_Formula]]"
review:
  next: 2025-11-19
  cadence: monthly
created: 2025-10-19
updated: 2025-10-19
---

# Imaginary Unit (i)

## Definition

The **imaginary unit**, denoted **i**, is defined by the property:

```
i² = -1
```

Alternatively expressed as:
```
i = √(-1)
```

**Critical**: i is NOT a real number. It extends the real number system.

## Fundamental Properties

**Core Identity**:
```
i² = -1
```

**Derived from Core**:
```
i³ = i² · i = -1 · i = -i
i⁴ = i² · i² = (-1)(-1) = 1
```

## Powers of i - Cyclic Pattern

Powers of i repeat every 4:

| Power | Value | Calculation |
|-------|-------|-------------|
| i¹ | i | i |
| i² | -1 | -1 |
| i³ | -i | i² · i = -i |
| i⁴ | 1 | i² · i² = 1 |
| i⁵ | i | i⁴ · i = i |
| i⁶ | -1 | i⁴ · i² = -1 |
| ... | ... | Pattern repeats |

**General Pattern**:
```
i⁴ⁿ = 1
i⁴ⁿ⁺¹ = i
i⁴ⁿ⁺² = -1
i⁴ⁿ⁺³ = -i
```

where n is any integer.

## Simplifying Powers of i

**Method**: Reduce exponent modulo 4

**Process**:
1. Divide exponent by 4
2. Use remainder to determine value
3. Apply pattern

**Examples**:

**i⁴⁷**:
```
47 ÷ 4 = 11 remainder 3
Therefore: i⁴⁷ = i³ = -i
```

**i¹⁰⁰**:
```
100 ÷ 4 = 25 remainder 0
Therefore: i¹⁰⁰ = i⁴⁽²⁵⁾ = (i⁴)²⁵ = 1²⁵ = 1
```

**i⁻²**:
```
i⁻² = 1/i² = 1/(-1) = -1
```

## Square Roots of Negative Numbers

Using i, we can express square roots of negative numbers:

```
√(-a) = i√a  (for a > 0)
```

**Examples**:
- √(-1) = i
- √(-4) = i√4 = 2i
- √(-9) = i√9 = 3i
- √(-25) = i√25 = 5i

**CRITICAL RULE**: 
```
√a · √b = √(ab)  ONLY when both a, b ≥ 0
```

This does NOT work with negative numbers:
```
❌ WRONG: √(-4) · √(-9) = √(36) = 6
✓ CORRECT: √(-4) · √(-9) = (2i)(3i) = 6i² = -6
```

## Why "Imaginary"?

**Historical Note**:
- Named "imaginary" by René Descartes (17th century)
- Originally considered "impossible" or "fictitious"
- Despite name, i is as valid mathematically as any number
- Better name might be "lateral unit" (rotates 90° in complex plane)

**Modern Understanding**:
- i is a mathematical tool, like 0 or negative numbers
- Essential in physics, engineering, and mathematics
- Not "imaginary" in sense of being fake or useless

## Geometric Interpretation

In the complex plane:
- Multiplying by i rotates 90° counterclockwise
- Multiplying by i² = -1 rotates 180° (reverses direction)
- Multiplying by i³ = -i rotates 270° (or 90° clockwise)
- Multiplying by i⁴ = 1 rotates 360° (back to start)

This explains why powers cycle every 4!

## Operations with i

**Multiplication**:
```
i · i = i² = -1
i · (-i) = -i² = -(-1) = 1
```

**Division**:
```
1/i = 1/i · i/i = i/i² = i/(-1) = -i
```

**Exponents**:
Use the cyclic pattern or convert to base form

## Key Applications

1. **Quadratic Equations**: Solutions when discriminant < 0
2. **Complex Numbers**: Forms the imaginary component
3. **Electrical Engineering**: AC circuit analysis (j used instead of i)
4. **Quantum Mechanics**: Wave functions
5. **Signal Processing**: Fourier transforms

## Common Mistakes

❌ **Wrong**: Treating i like a variable: i² ≠ i · 2
❌ **Wrong**: i = √(-1) so √(-1) · √(-1) = √(1) = 1 (violates square root rule)
❌ **Wrong**: i is "imaginary" so it doesn't exist (it's a defined mathematical object)
❌ **Wrong**: Forgetting to simplify i² to -1 in calculations

## Key Relationships

**To Complex Numbers**:
```
Every complex number: a + bi
i is the "imaginary basis"
```

**To Quadratic Formula**:
```
When b² - 4ac < 0, solutions involve i:
x = [-b ± i√(4ac - b²)] / (2a)
```

**To Polynomials**:
```
x² + 1 = 0 has solutions x = ±i
x² + k = 0 (k > 0) has solutions x = ±i√k
```

## Practice Examples

**Simplify**:
1. i²⁵ = i⁴⁽⁶⁾⁺¹ = i
2. i⁵⁰ = i⁴⁽¹²⁾⁺² = i² = -1
3. i⁻³ = 1/i³ = 1/(-i) = -i/i² = -i/(-1) = i

**Square Roots**:
1. √(-16) = 4i
2. √(-7) = i√7
3. √(-100) = 10i

**Operations**:
1. (3i)(4i) = 12i² = -12
2. (2i)³ = 8i³ = 8(-i) = -8i
3. i/i³ = i/(-i) = i(-i)/(-i)(-i) = -i²/i² = -(-1)/(-1) = -1

## Summary

> The imaginary unit i, defined by i² = -1, extends the real numbers to create the complex number system. Powers of i follow a repeating cycle of length 4, and i enables solutions to all polynomial equations.

---

**See Also**:
- [[Complex_Numbers]] - Numbers of form a + bi
- [[Complex_Number_Operations]] - Arithmetic with complex numbers
- [[Powers_of_i]] - Detailed pattern analysis (if exists)
- [[The_Discriminant]] - When i appears in quadratic solutions

**Source**: Chapter 1.3 - Miller & Gerken College Algebra & Trigonometry
