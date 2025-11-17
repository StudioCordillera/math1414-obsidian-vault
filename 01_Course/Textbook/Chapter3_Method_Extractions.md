# Chapter 3 Method Extractions
**Source**: College Algebra & Trigonometry 2nd Edition - Miller/Gerken  
**Target**: Exam 2 Learning Objectives  
**Tags**: #textbook #extraction #method #example

---

## 📚 EXTRACTION METHODOLOGY

Following the Universal Knowledge Framework approach, this document extracts:
1. **Explicit Knowledge**: Stated definitions, formulas, procedures
2. **Implicit Knowledge**: Assumed prerequisites, unstated steps
3. **Common Errors**: What NOT to do
4. **Relational Connections**: How concepts relate

---

## 📐 SECTION 3.1: QUADRATIC FUNCTIONS

> See [[Graphing_Quadratic_Functions]] for complete graphing procedures.

### Example 1: Analyzing and Graphing a Quadratic Function
**Page**: 303  
**Given**: f(x) = -2(x - 1)² + 8

#### Step-by-Step Solution

1. **Identify Form**: [[Vertex_Form|f(x) = a(x - h)² + k]] where a = -2, h = 1, k = 8
   - Since a < 0, parabola opens **DOWNWARD** ∩

2. **Extract Vertex**: (h, k) = (1, 8)

3. **Find x-intercepts**: Solve f(x) = 0
   ```
   0 = -2(x - 1)² + 8
   -8 = -2(x - 1)²
   4 = (x - 1)²
   ±2 = x - 1
   x = 3 or x = -1
   ```
   **x-intercepts**: (3, 0) and (-1, 0)

4. **Find y-intercept**: f(0) = -2(1) + 8 = 6
   **y-intercept**: (0, 6)

5. **Axis of Symmetry**: x = 1 (vertical through vertex)

6. **Max/Min**: Vertex is **MAXIMUM** at y = 8

7. **[[Domain_and_Range|Domain & Range]]**:
   - Domain: (-∞, ∞)
   - Range: (-∞, 8]

#### 🧠 Implicit Knowledge Required
- Understanding [[Vertex_Form|vertex form]] vs [[Standard_Form|standard form]]
- [[Square_Root_Property]] for solving quadratics
- Concept of parabola symmetry
- Relationship between 'a' coefficient and opening direction

#### ⚠️ Common Errors
- Forgetting ± when taking square roots
- Confusing vertex form a(x-h)² + k with standard form
- Not recognizing max/min occurs at vertex

#### 🔗 Relational Connections
- Vertex form reveals transformations from parent function y = x²
- Method **preserves** solutions when transforming forms
- Alternative: [[#Complete the Square]], vertex formula

---

### Example 2: Writing Quadratic in Vertex Form
**Page**: 304  
**Given**: f(x) = 3x² + 12x + 5

> See [[Completing_the_Square]] for comprehensive method coverage.

#### Complete the Square Method

1. **Factor out leading coefficient**:
   ```
   f(x) = 3(x² + 4x) + 5
   ```

2. **Complete the square inside parentheses**:
   Add/subtract [½ · 4]² = 4
   ```
   = 3(x² + 4x + 4 - 4) + 5
   = 3(x² + 4x + 4) - 12 + 5
   ```

3. **Factor and simplify**:
   ```
   = 3(x + 2)² - 7
   ```

**Result**: Vertex form f(x) = 3(x + 2)² - 7  
**Vertex**: (-2, -7)

#### 🧠 Critical Insights
- **Why factor 'a' first**: Makes completing square easier
- **The [½b]² pattern**: Creates perfect square trinomial
- **Sign handling**: h = -2 means vertex x-coordinate is -2

#### 📊 Finding x-intercepts
Using [[Quadratic_Formula|quadratic formula]]:
```
x = (-12 ± √(144 - 60)) / 6
x = (-12 ± √84) / 6
x = (-6 ± √21) / 3
```
**Key**: Not all quadratics factor nicely! [[The_Discriminant|Δ]] = 84 > 0 → two real roots

---

## 🔄 MORPHISM ANALYSIS

### Transformation Chain
```mermaid
graph LR
    A[Standard Form] -->|complete_square| B[Vertex Form]
    B -->|extract| C[Vertex Point]
    C -->|analyze| D[Graph Features]
    D -->|optimize| E[Max/Min Value]
```

### Preserved Properties
- [[02_Concepts/Concept_Library#@ZERO|Zeros/Solutions]] remain unchanged
- Area under curve preserved
- Discriminant value preserved

### Changed Properties
- Visual representation simplified
- Vertex immediately visible
- Transformations from parent clear

---

## 📝 Method Templates

### Complete Square Transform
```yaml
name: complete_square_transform
signature: ax² + bx + c → a(x - h)² + k
algorithm:
  1. Factor out 'a' from x-terms
  2. Add/subtract [b/(2a)]² inside
  3. Distribute 'a' through subtraction
  4. Simplify to vertex form
preserves: [@ZEROS, @DISCRIMINANT]
reveals: [@VERTEX, @AXIS_SYMMETRY]
common_errors:
  - Forgetting to multiply subtracted term by 'a'
  - Sign errors in final form
```

---

## 🎯 Learning Objective Mapping

This section addresses:
- **Obj. 1**: Solve quadratics by completing the square ✅
- **Obj. 3**: Graph quadratic functions ✅
- **Obj. 9**: Apply to max/min problems ✅

**Still needed**:
- Complex conjugate roots (Obj. 4)
- Discriminant interpretation (Obj. 2)
- Polynomial degree analysis (Obj. 5)

---

## 🔗 RELATED CONCEPTS

This chapter connects to these concept nodes in the vault:

### Quadratic Functions & Forms
- [[Graphing_Quadratic_Functions]] - Complete graphing procedures (Section 3.1)
- [[Vertex_Form]] - a(x - h)² + k representation (Examples 1, 2)
- [[Standard_Form]] - ax² + bx + c representation (Example 2)
- [[Factored_Form]] - a(x - r₁)(x - r₂) representation

### Solution Methods
- [[Completing_the_Square]] - Transform to vertex form (Example 2)
- [[Quadratic_Formula]] - Universal solver (Example 2)
- [[Square_Root_Property]] - Solving x² = k form (Example 1)
- [[The_Discriminant]] - Solution type predictor

### Function Analysis
- [[Domain_and_Range]] - Input/output sets (Example 1)
- [[Quadratic_Optimization]] - Max/min applications

### Related Topics
- [[What_IS_a_Polynomial]] - Quadratics are degree-2 polynomials
- [[Polynomial_Degree_and_Shape]] - Parabola characteristics
- [[Function_Transformations]] - Vertex form shows transformations

---

**Navigation**: [[01_Course/Textbook/Index|← Textbook Index]] | [[01_Course/Exam_Resources/Exam2_Quick_Reference|Exam Quick Reference →]]