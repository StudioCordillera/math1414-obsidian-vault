---
layout: concept
title: "Concept Library"
topic: "General Math"
---

# Concept Library v1.0
## Compressed Knowledge Base with @Reference System
**Version**: 1.0 | **Date**: October 15, 2025  
**Purpose**: Single-source-of-truth for all mathematical concepts, referenced by methods

---

## 🎯 METHODOLOGY

Based on Lawvere's compression principles from "Conceptual Mathematics":
1. **Define once**: Each concept has ONE authoritative entry
2. **Reference everywhere**: Methods use @CONCEPT_ID instead of repeating
3. **Three-level detail**: Symbolic, Structural, Full explanation
4. **Preserve relations**: Show how concepts connect

---

## 📐 Algebraic Structures

### @POLYNOMIAL_FUNCTION
**Formal Definition**: `f(x) = aₙxⁿ + aₙ₋₁xⁿ⁻¹ + ... + a₁x + a₀` where aₙ ≠ 0
**Properties**:
- Coefficients: Real numbers
- Exponents: Whole numbers (0, 1, 2, ...)
- Domain: All real numbers
- Graph: Continuous and smooth

**Related**: [[#@DEGREE]], [[#@LEADING_TERM]], [[#@ZEROS]]

---

### @QUADRATIC_FUNCTION
**Formal Definition**: `f(x) = ax² + bx + c` where a ≠ 0
**Special Case**: Polynomial of degree 2
**Forms**:
- Standard: `ax² + bx + c`
- Vertex: `a(x - h)² + k`
- Factored: `a(x - r₁)(x - r₂)`

**Graph**: Parabola  
**Related**: [[#@VERTEX]], [[#@DISCRIMINANT]], [[#@PARABOLA]]

---

## 🎯 Zeros and Roots

### @ZERO
**Definition**: Value c where f(c) = 0
**Aliases**: Root, solution, x-intercept
**Notation**: If f(r) = 0, then r is a zero
**Types**: 
- [[#@REAL_ZERO]]
- [[#@COMPLEX_ZERO]]
- [[#@REPEATED_ZERO]]

**Graph**: x-intercept at (r, 0)

---

### @MULTIPLICITY
**Definition**: Number of times (x - c) appears as factor
**Notation**: (x - c)ᵏ means multiplicity k
**Impact on Graph**:
- Odd multiplicity → [[#@CROSS_POINT]]
- Even multiplicity → [[#@TOUCH_POINT]]

**Related**: [[#@REPEATED_ROOT]]

---

### @DISCRIMINANT
**Formula**: `Δ = b² - 4ac` (for ax² + bx + c = 0)
**Purpose**: Classifies root types without solving
**Classification**:
- Δ > 0: Two distinct real roots
- Δ = 0: One repeated real root
- Δ < 0: Two complex conjugate roots

**Related**: [[#@QUADRATIC_FORMULA]], [[#@COMPLEX_CONJUGATE]]

---

## 📊 Graph Features

### @VERTEX
**Definition**: Turning point of parabola
**Coordinates**: (h, k) in vertex form
**Formulas**:
- x-coordinate: `h = -b/(2a)`
- y-coordinate: `k = f(h)`

**Significance**: [[#@MAXIMUM]] or [[#@MINIMUM]] value

---

### @END_BEHAVIOR
**Definition**: Graph behavior as x → ±∞
**Determined by**: [[#@LEADING_TERM]] (aₙxⁿ)
**Patterns**:
- Even degree, aₙ > 0: ∪ (up both ends)
- Even degree, aₙ < 0: ∩ (down both ends)
- Odd degree, aₙ > 0: / (down-left, up-right)
- Odd degree, aₙ < 0: \ (up-left, down-right)

---

## 🔄 Transformations

### @COMPLETE_SQUARE
**Purpose**: Transform [[#@STANDARD_FORM]] to [[#@VERTEX_FORM]]
**Algorithm**:
1. Factor out 'a' from x-terms
2. Add/subtract `[½(b/a)]²` inside parentheses
3. Distribute 'a' through subtracted term
4. Simplify to `a(x - h)² + k`

**Preserves**: [[#@SOLUTIONS]], [[#@ZEROS]]  
**Reveals**: [[#@VERTEX]] location

---

## 🧮 Solving Methods

### @QUADRATIC_FORMULA
**Formula**: 
```
x = [-b ± √(b² - 4ac)] / (2a)
```
**Input**: Coefficients from ax² + bx + c = 0  
**Output**: Exact solutions (may be complex)  
**Components**:
- [[#@DISCRIMINANT]]: Under the radical
- Axis value: -b/(2a)
- Distance from axis: ±√Δ/(2a)

---

## 🔗 Method Signatures

These are the computational function names used in our framework:

### Transformation Morphisms
- `complete_square_transform()`: [[#@STANDARD_FORM]] → [[#@VERTEX_FORM]]
- `factor_polynomial()`: Standard → [[#@FACTORED_FORM]]
- `expand_product()`: Factored → Standard

### Classifier Morphisms
- `discriminant_classifier()`: Quadratic → Root Type
- `degree_classifier()`: Polynomial → Shape Category
- `end_behavior_classifier()`: Leading Term → Behavior Pattern

### Solution Morphisms
- `quadratic_solver()`: Quadratic → Solution Set
- `rational_root_finder()`: Polynomial → Potential Rational Roots
- `synthetic_division()`: Polynomial ÷ (x-c) → Quotient + Remainder

---

## 📈 Concept Relationships

### Morphism Chains
```mermaid
graph LR
    A[@STANDARD_FORM] -->|complete_square| B[@VERTEX_FORM]
    B -->|extract| C[@VERTEX]
    C -->|evaluate| D[@MAX/MIN]
```

### Equivalences
- @ZERO ≡ @ROOT ≡ @X_INTERCEPT (as real number)
- @FACTORED_FORM reveals @ZEROS directly
- @VERTEX_FORM reveals @VERTEX directly
- @STANDARD_FORM requires formulas to extract features

---

## 🏷️ Tags

#concept-library #reference-system #compression #algebraic-structure #polynomial #quadratic #transformation #morphism #solving-method

---

**Navigation**: [[00_Index/Master_Index|← Master Index]] | [[03_Methods/Method_Templates|Method Templates →]]


---

## 📚 FOUNDATIONAL THEOREMS

### @FUNDAMENTAL_THEOREM_OF_ALGEBRA
**Statement**: Every polynomial of degree n ≥ 1 has exactly n roots in ℂ (counting multiplicity)
**Significance**: 
- Guarantees roots exist
- Justifies complex numbers
- Enables complete factorization
- ℂ is algebraically closed

**Key Consequences**:
- All polynomials factor completely over ℂ
- Complex roots of real polynomials come in conjugate pairs
- Degree determines exact number of roots

**Related**: [[#@COMPLEX_ZERO]], [[#@FACTORED_FORM]], [[Fundamental_Theorem_of_Algebra]]

---

### @DIVISION_ALGORITHM
**Statement**: For polynomials f(x) and d(x) ≠ 0, there exist unique q(x) and r(x) such that:
```
f(x) = d(x)·q(x) + r(x)
where deg(r) < deg(d) or r = 0
```

**Significance**:
- Foundation for all polynomial division
- Guarantees division always works and terminates
- Ensures quotient and remainder are unique

**Special Cases**:
- When d(x) = (x - c): remainder is constant → [[#@REMAINDER_THEOREM]]
- When r = 0: d(x) is a factor → [[#@FACTOR_THEOREM]]

**Related**: [[Division_Algorithm]], [[Remainder_Theorem]], [[Factor_Theorem]]

---

### @FACTOR_THEOREM
**Statement**: (x - c) is a factor of f(x) ⟺ f(c) = 0

**Bidirectional Connection**:
- Root → Factor: If f(c) = 0, then (x - c) divides f(x)
- Factor → Root: If (x - c) divides f(x), then f(c) = 0

**Use Cases**:
- Testing if (x - c) is a factor: just evaluate f(c)
- Building polynomials from roots
- Reducing degree after finding one root

**Related**: [[Factor_Theorem]], [[#@REMAINDER_THEOREM]], [[#@ZERO]]

---

### @REMAINDER_THEOREM  
**Statement**: When f(x) is divided by (x - c), the remainder is f(c)

**Quick Application**: 
No need to perform division to find remainder—just evaluate!

**Connection to Division Algorithm**:
```
f(x) = (x - c)·q(x) + r
Evaluate at x = c:
f(c) = 0·q(c) + r
f(c) = r
```

**Special Case**: When f(c) = 0, remainder is 0 → [[#@FACTOR_THEOREM]]

**Related**: [[Remainder_Theorem]], [[#@DIVISION_ALGORITHM]]

---

## 🔄 FUNCTION OPERATIONS

### @FUNCTION_COMPOSITION
**Notation**: (g ∘ f)(x) = g(f(x))
**Read**: "g after f" or "g composed with f"

**Visual Flow**:
```
x → f → f(x) → g → g(f(x))
```

**Key Properties**:
- **Associative**: (h ∘ g) ∘ f = h ∘ (g ∘ f)
- **Has Identity**: f ∘ I = I ∘ f = f where I(x) = x
- **NOT Commutative**: g ∘ f ≠ f ∘ g (usually)

**Applications**:
- Building [[#@TRANSFORMATIONS]] chains
- Creating complex functions from simple ones
- Foundation for inverse functions: f ∘ f⁻¹ = I

**Category Theory**: Composition is THE fundamental operation in category theory—morphisms compose!

**Related**: [[Function_Composition]], [[#@TRANSFORMATION]], [[#@INVERSE_FUNCTION]]



---

## 🧬 NEW: Foundational Concepts (Oct 2025)

### @FUNCTION
**Formal Definition**: A rule f: A → B that assigns to each element x ∈ A exactly one element f(x) ∈ B
**Components**:
- Domain: Set of allowed inputs (A)
- Codomain: Set of possible outputs (B)
- Rule: The transformation x ↦ f(x)

**Critical Property**: Each input → exactly ONE output

**Types**:
- Injective (one-to-one): Different inputs → different outputs
- Surjective (onto): Every output is hit
- Bijective: Both injective and surjective (has inverse)

**Composition**: (g ∘ f)(x) = g(f(x))

**Related**: [[What_IS_a_Function]], [[Composition]], [[Inverse_Functions]]

---

### @POLYNOMIAL  
**Formal Definition**: `f(x) = aₙxⁿ + aₙ₋₁xⁿ⁻¹ + ... + a₁x + a₀` where n ∈ ℕ₀, aₙ ≠ 0
**Structure**:
- Terms: aᵢxⁱ (coefficient times power)
- Degree: Highest exponent (n)
- Leading term: aₙxⁿ
- Leading coefficient: aₙ  
- Constant term: a₀

**Properties**:
- Domain: All ℝ (or all ℂ)
- Continuous everywhere (no breaks/jumps)
- Smooth (infinitely differentiable)
- At most n real roots
- Exactly n complex roots (counting multiplicity)

**Related**: [[What_IS_a_Polynomial]], [[Polynomial_Degree_and_Shape]], [[Standard_Form]]

---

### @FACTOR_THEOREM (Bidirectional)
**Statement**: (x - c) is a factor of f(x) ⟺ f(c) = 0

**Direction 1 (Factor → Root)**:
If (x - c) | f(x), then f(c) = 0

**Direction 2 (Root → Factor)**:
If f(c) = 0, then (x - c) | f(x)

**Usage**:
- Testing factors: Evaluate f(c) instead of dividing
- Building from roots: Roots → factors → polynomial
- Finding structure: One root reveals one factor

**Foundation**: Special case of [[Remainder_Theorem|@REMAINDER_THEOREM]] where r = 0

**Related**: [[Factor_Theorem]], [[Constructing_Polynomials_from_Roots]]

---

### @REMAINDER_THEOREM
**Statement**: When f(x) ÷ (x - c), remainder = f(c)

**Power**: Skip division! Just plug in c.

**Why it works**: From [[Division_Algorithm|@DIVISION_ALGORITHM]]:
- f(x) = (x - c)·q(x) + r
- Evaluate at x = c: f(c) = (c - c)·q(c) + r = 0 + r = r

**Special cases**:
- r = f(c) = 0 → (x - c) is a factor
- r = f(c) ≠ 0 → (x - c) is NOT a factor

**Extended**: For (ax - b), remainder = f(b/a)

**Related**: [[Remainder_Theorem]], [[Factor_Theorem]], [[Synthetic_Division]]

---

### @DIVISION_ALGORITHM (Foundation of All Division)
**Statement**: For f(x) and d(x) ≠ 0, ∃! unique q(x), r(x) such that:
```
f(x) = d(x)·q(x) + r(x)
where deg(r) < deg(d) or r = 0
```

**The Three Guarantees**:
1. **Existence**: Can always divide
2. **Uniqueness**: Only one answer
3. **Degree bound**: Remainder is smaller than divisor

**Components**:
- Dividend: f(x) (what you're dividing)
- Divisor: d(x) (what you're dividing by)
- Quotient: q(x) (how many times)
- Remainder: r(x) (what's left)

**This enables**: [[Remainder_Theorem]], [[Factor_Theorem]], [[Synthetic_Division]], [[Euclidean_Algorithm]]

**Related**: [[Division_Algorithm]], [[Polynomial_Long_Division]]

---

## 📝 UPDATE LOG

**October 16, 2025 - Foundation Expansion**
- ✅ Added Factor_Theorem.md (complete bidirectional treatment)
- ✅ Added Remainder_Theorem.md (complete with applications)
- ✅ Added What_IS_a_Function.md (morphism perspective)
- ✅ Added What_IS_a_Polynomial.md (complete formal treatment)
- ✅ Updated Build_Roadmap.md with progress assessment
- 🎯 Next: What_IS_a_Variable, Standard_Form_Deep_Dive, Function_Composition

