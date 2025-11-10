---
layout: concept
title: "Complex Numbers"
topic: "General Math"
type: Definition
status: stable
importance: high
tags:
  - concept/number-system
  - concept/algebra
  - chapter1
  - complex-numbers
sources:
  - MillerGerken2023
source_refs:
  - "Miller & Gerken §1.3 p.108-115"
relations:
  broader:
    - "[[Real_Number_System]]"
  narrower:
    - "[[Imaginary_Unit]]"
    - "[[Complex_Conjugates]]"
  depends_on:
    - "[[Real_Number_System]]"
    - "[[Imaginary_Unit]]"
  related:
    - "[[Quadratic_Formula]]"
    - "[[The_Discriminant]]"
review:
  next: 2025-11-19
  cadence: monthly
created: 2025-10-19
updated: 2025-10-19
---

# Complex Numbers

## Definition

A **complex number** is a number of the form:
```
z = a + bi
```

where:
- **a** is the **real part** (a ∈ ℝ)
- **b** is the **imaginary part** (b ∈ ℝ, note: NOT bi!)
- **i** is the imaginary unit where i² = -1

### Standard Form
```
a + bi
```
- Real part written first
- Imaginary part written second with i
- Can be positive or negative

## Special Cases

**Pure Imaginary Number**: When a = 0
```
z = bi (examples: 3i, -2i, i)
```

**Real Number**: When b = 0
```
z = a (examples: 5, -3, π)
```

**Important**: All real numbers are complex numbers with imaginary part = 0

## Set Notation

**ℂ** = Set of all complex numbers
```
ℂ = {a + bi | a, b ∈ ℝ}
```

**Relationship to Real Numbers**:
```
ℝ ⊂ ℂ
(Real numbers are a subset of complex numbers)
```

## Why Complex Numbers?

**Motivation**: To solve equations like x² = -1

- No real number satisfies x² = -1
- Introduced i = √(-1) to extend number system
- Allows ALL quadratic equations to have solutions
- Fundamental in mathematics, physics, engineering

## Equality of Complex Numbers

Two complex numbers are equal if and only if both real and imaginary parts are equal:

```
a + bi = c + di  ⟺  a = c AND b = d
```

## Visual Representation

**Complex Plane** (Argand Diagram):
- Horizontal axis: Real part (real axis)
- Vertical axis: Imaginary part (imaginary axis)
- Point (a, b) represents a + bi

## Historical Context

- Introduced in 16th century to solve cubic equations
- Name "complex" from Latin *complexus* (embraced/encompassed)
- Initially called "impossible" or "imaginary" numbers
- Now recognized as fundamental extension of number system

## Connection to Other Concepts

**Prerequisites**:
- [[Real_Number_System]] - Foundation
- [[Imaginary_Unit]] - Core component

**Applications**:
- Solving quadratic equations (discriminant < 0)
- Electrical engineering (AC circuits)
- Quantum mechanics
- Signal processing
- Fractals and chaos theory

**Related Operations**:
- [[Complex_Number_Operations]] - Addition, subtraction, multiplication
- [[Complex_Conjugates]] - Division and simplification
- Powers of i - Simplification techniques

## Key Properties

1. **Closure**: Sum, difference, product, and quotient (divisor ≠ 0) of complex numbers is complex
2. **Field**: Complex numbers form a complete field
3. **Algebraically Closed**: Every polynomial has a root in ℂ (Fundamental Theorem of Algebra)

## Common Misconceptions

❌ **Wrong**: "Complex numbers aren't real" (they're as real as any mathematical object)
❌ **Wrong**: "i = √(-1)" is always safe (technically i² = -1 is the definition)
❌ **Wrong**: Imaginary part is "bi" (it's just b, the coefficient)
❌ **Wrong**: Complex numbers have no practical use (extensively used in science/engineering)

## Examples

**Standard Complex Numbers**:
- 3 + 4i
- -2 + 7i  
- 5 - i
- -6 - 2i

**Special Cases**:
- 5 (real: a = 5, b = 0)
- 3i (pure imaginary: a = 0, b = 3)
- 0 (zero: a = 0, b = 0)

**From Quadratic Equations**:
- x² + 1 = 0 gives x = ±i
- x² + 4 = 0 gives x = ±2i
- x² - 2x + 2 = 0 gives x = 1 ± i

## Summary

> Complex numbers extend the real number system to provide solutions to ALL polynomial equations. Every complex number has a real part and an imaginary part, written in standard form a + bi where i² = -1.

---

**See Also**:
- [[Imaginary_Unit]] - Definition of i
- [[Complex_Number_Operations]] - Arithmetic operations
- [[Complex_Conjugates]] - Conjugate pairs and division
- [[The_Discriminant]] - When complex solutions arise
- [[Fundamental_Theorem_of_Algebra]] - Guarantees complex roots exist

**Source**: Chapter 1.3 - Miller & Gerken College Algebra & Trigonometry
