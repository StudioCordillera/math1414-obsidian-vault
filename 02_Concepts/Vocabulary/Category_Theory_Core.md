# Category Theory Core
**Parent**: [[02_Concepts/Vocabulary_Guide|Vocabulary Guide]]
**Tags**: #category-theory #fundamental #morphism #functor

---

## 🎯 Category

A mathematical structure consisting of:
- **Objects**: Mathematical entities (polynomials, numbers, sets)
- **Morphisms**: Structure-preserving maps between objects
- **Composition**: Ability to chain morphisms
- **Identity**: Each object has an identity morphism to itself

### Laws
- **Associativity**: (f ∘ g) ∘ h = f ∘ (g ∘ h)
- **Identity**: f ∘ id = id ∘ f = f

### In Our Context
Algebraic expressions form categories where solving is morphism composition

### Example
Category of Quadratics with transformations as morphisms

### Related
- [[#Morphism]]
- [[#Functor]]
- [[#Object]]

---

## 🎯 Morphism
**Alternative Names**: Arrow, Map, Transformation

A structure-preserving map between objects in a category.

### Properties
- **Signature**: `f: A → B` (reads as "f maps A to B")
- **Key Property**: Preserves structure (e.g., solutions stay solutions)

### Types
- **[[02_Concepts/Vocabulary/Morphism_Types#Transformation|Transformation morphism]]**: Changes form but preserves solutions
- **[[02_Concepts/Vocabulary/Morphism_Types#Classifier|Classifier morphism]]**: Categorizes objects into types
- **[[02_Concepts/Vocabulary/Morphism_Types#Embedding|Embedding morphism]]**: Places one structure inside another

### Example
`complete_square: ax²+bx+c → a(x-h)²+k`

---

## 🎯 Functor

A map between entire categories that preserves categorical structure.

### Properties
- Maps objects to objects
- Maps morphisms to morphisms
- Preserves composition: F(g ∘ f) = F(g) ∘ F(f)
- Preserves identities: F(idₐ) = id_{F(A)}

### In Our Context
Operations that systematically transform entire problem classes

### Example
`discriminant_classifier` maps all quadratics to root-type categories

### Visual
```
Category A ---[F]---> Category B
(entire structure mapped)
```

---

## 🎯 Object

An entity within a category (can be sets, numbers, expressions, functions).

### Examples in Different Categories
- **Polynomial category**: 3x² + 5x - 2
- **Solution category**: {2, -3}
- **Root-type category**: "Two Real Roots"

### Key Point
Internal structure not required - treated as atomic units

---

## 🎯 Composition

Chaining morphisms together.

### Notation
- Symbol: ∘
- If f: A → B and g: B → C, then g ∘ f: A → C
- Read right to left: (g ∘ f)(x) = g(f(x))

### Example
`solve ∘ complete_square ∘ simplify`

### Requirements
Codomain of f must match domain of g

---

## 🎯 Domain & Codomain

### Domain
The source or input space of a morphism.
- **Traditional**: Input set, pre-image
- **Notation**: For f: A → B, domain is A
- **Example**: Domain of √x is x ≥ 0

### Codomain
The target or output space of a morphism.
- **Traditional**: Range, image
- **Notation**: For f: A → B, codomain is B
- **Example**: Codomain of x² is all non-negative reals

---

## 🎯 Isomorphism

A morphism with an inverse - a "perfect" structure-preserving map.

### Definition
f: A → B is isomorphic if there exists g: B → A where:
- g ∘ f = idₐ
- f ∘ g = id_B

### Meaning
A and B are "the same" structurally

### Example
ax²+bx+c ≅ a(x-h)²+k (equivalent forms)

### Symbol
↔ or ≅

---

## 🎯 Invariant

A property preserved under transformation.

### Core Concept
"What stays the same when things change"

### Examples
- Solutions stay invariant under completing the square
- Degree stays invariant under polynomial addition/subtraction
- Number of roots stays invariant under equivalent transformations

### Symbol
Often denoted I or INV

---

## 🎯 Natural Transformation

A way of transforming one functor into another while preserving structure.

### Advanced Concept
Morphism between functors

### Notation
α: F ⇒ G (double arrow)

### In Our Context
Systematic way to convert between solution methods

---

## 🔗 Navigation

- **Back to**: [[02_Concepts/Vocabulary_Guide|Vocabulary Guide]]
- **Next**: [[02_Concepts/Vocabulary/Morphism_Types|Morphism Types]]
- **Related**: [[02_Concepts/Vocabulary/Algebraic_Structures|Algebraic Structures]]