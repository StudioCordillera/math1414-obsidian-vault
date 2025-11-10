# Exam 2 Quick Reference Card
## Morphism-Based Solution Patterns
**Version**: 1.0 | **Tags**: #exam #quick-reference #morphism-chains

---

## 🎯 CORE MORPHISM CHAINS

### Quadratic Solution Pipeline
```
Standard Form → Complete Square → Vertex Form → Graph/Solve
   ax²+bx+c    →   a(x-h)²+k    →  (h,k) vertex → solutions
```

### Polynomial Analysis Pipeline
```
Polynomial → Degree/Lead → End Behavior → Rational Roots → Factor → Graph
   p(x)    →    n, aₙ   →   ↗↘ or ↗↗   →   p/q list   → zeros → sketch
```

### Rational Function Pipeline
```
Rational → Factor → Zeros/Holes → Asymptotes → Sign Analysis → Graph
  p(x)/q(x) → simplify → x-intercepts → H/V/Slant → test regions → sketch
```

---

## 📋 METHOD QUICK REFERENCE

### 1. Complete Square Transform
**Input**: ax² + bx + c  
**Process**: 
```
1. Factor: a(x² + (b/a)x) + c
2. Add/Sub: a(x² + (b/a)x + (b/2a)²) + c - a(b/2a)²
3. Simplify: a(x - h)² + k
```
**Output**: Vertex (h, k) where h = -b/2a

### 2. Discriminant Classifier
**Input**: ax² + bx + c  
**Calculate**: Δ = b² - 4ac  
**Output**:
- Δ > 0 → Two real roots
- Δ = 0 → One repeated root  
- Δ < 0 → Two complex conjugates

### 3. Synthetic Division
**Setup**: Divide p(x) by (x - c)
```
c | coefficients
  | ↓  multiply & add
  | quotient | remainder
```
**Result**: p(x) = (x - c)·q(x) + r

### 4. Rational Root Theorem
**For**: aₙxⁿ + ... + a₁x + a₀  
**Candidates**: ±(factors of a₀)/(factors of aₙ)  
**Test**: Use synthetic division

---

## 🚨 EMERGENCY PROTOCOLS

### "I'm stuck on completing the square"
1. Check: Did you factor out 'a' first?
2. Check: Is your added term (b/2a)²?
3. Check: Did you multiply subtracted term by 'a'?

### "My discriminant is negative"
→ Solutions are complex: x = (-b ± i√|Δ|)/(2a)

### "Polynomial won't factor"
1. Try rational root theorem
2. Use synthetic division on candidates
3. If no rational roots, use quadratic formula on remainder

### "Can't find asymptotes"
- **Vertical**: Set denominator = 0
- **Horizontal**: Compare degrees (top/bottom)
- **Slant**: If deg(num) = deg(den) + 1, divide

---

## 📊 GRAPHING CHECKLIST

### Quadratic Functions
- [ ] Opening direction (sign of 'a')
- [ ] Vertex coordinates
- [ ] x-intercepts (if real)
- [ ] y-intercept (set x = 0)
- [ ] Axis of symmetry

### Polynomial Functions
- [ ] Degree and leading coefficient
- [ ] End behavior pattern
- [ ] All zeros with multiplicities
- [ ] y-intercept
- [ ] Sign chart between zeros

### Rational Functions
- [ ] Domain restrictions
- [ ] Zeros (numerator = 0)
- [ ] Vertical asymptotes
- [ ] Horizontal/slant asymptote
- [ ] Sign analysis in regions

---

## 🔗 KEY PATTERNS

### Multiplicity Effects
- **Odd multiplicity**: Graph crosses x-axis
- **Even multiplicity**: Graph touches x-axis

### End Behavior Guide
```
Degree | Lead Coef | Behavior
Even   | Positive  | ∪ (both up)
Even   | Negative  | ∩ (both down)
Odd    | Positive  | ↗ (down-to-up)
Odd    | Negative  | ↘ (up-to-down)
```

### Asymptote Rules
```
If deg(num) < deg(den) → y = 0
If deg(num) = deg(den) → y = lead(num)/lead(den)
If deg(num) > deg(den) → No horizontal (check slant)
```

---

## 💡 COMPOSITION TIPS

### Morphism Composition
Think of each method as a transformation that preserves certain properties:
- Completing square preserves **solutions**
- Factoring reveals **zeros** 
- Vertex form reveals **optimization**

### Working Backwards
If given a graph, reconstruct the function:
1. Count zeros → degree
2. Check end behavior → lead coefficient sign
3. Note multiplicities → factor pattern
4. Find y-intercept → constant term

---

**Quick Access**: Keep this open during practice and exams!

**Related**: [[02_Concepts/Concept_Library|Concept Library]] | [[03_Methods/Method_Templates|Method Templates]]


---

## ⚡ ULTRA-QUICK FORMULAS (Last-Minute Review)

### Critical Formulas
```
Vertex (h, k):              h = -b/(2a),  k = f(h)
Quadratic Formula:          x = [-b ± √(b² - 4ac)] / 2a
Discriminant:               Δ = b² - 4ac
Complex Conjugate Product:  (a + bi)(a - bi) = a² + b²
Sum of Conjugates:          (a + bi) + (a - bi) = 2a
Powers of i Cycle:          i, -1, -i, 1, i, -1, -i, 1... (mod 4)
Quadratic Factor:           x² - (sum)x + (product) = 0
```

### Instant Recognition Patterns

**Discriminant Decision Tree:**
```
Δ > 0 → 2 real roots
  └─ Perfect square? → Rational roots
  └─ Not perfect? → Irrational roots
Δ = 0 → 1 repeated root (always rational)
Δ < 0 → 2 complex conjugates (a ± bi)
```

**Polynomial Degree → Max Features:**
```
Degree n → Max (n-1) turns
Degree n → Exactly n roots (count multiplicity + complex)
```

**End Behavior (Quick Check):**
```
Even degree + positive LC → ↑↑ (U shape)
Even degree + negative LC → ↓↓ (∩ shape)
Odd degree + positive LC → ↓↑ (/ shape)  
Odd degree + negative LC → ↑↓ (\ shape)
```

**Rational Root Candidates:**
```
p/q where p | a₀ and q | aₙ
Test with synthetic division
```

**Asymptotes (Rational Functions):**
```
Vertical: denominator = 0 (after reducing)
Horizontal: 
  - deg(num) < deg(den) → y = 0
  - deg(num) = deg(den) → y = aₙ/bₙ
  - deg(num) > deg(den) → none (check slant)
Slant: deg(num) = deg(den) + 1 → long division
```

### One-Line Checks

✓ **Factor Theorem:** (x - c) is factor ⟺ P(c) = 0  
✓ **Remainder Theorem:** P(x) ÷ (x - c) → remainder = P(c)  
✓ **Conjugate Pair Theorem:** Real coefficients + complex root → conjugate also root  
✓ **Multiplicity:** Even → bounce, Odd → cross  
✓ **Optimization:** Vertex of parabola = max (if a < 0) or min (if a > 0)

### Common Trap Avoiders

⚠️ **Sign of c:** (x + 3) = (x - (-3)) → use c = -3  
⚠️ **Missing terms:** x⁴ + 5 → [1, 0, 0, 0, 5] in synthetic division  
⚠️ **i² = -1:** Not +1, not i·2  
⚠️ **Complex conjugate:** Flip ONLY imaginary sign: 3 + 4i → 3 - 4i  
⚠️ **Radical multiplication:** √(-a)·√(-b) ≠ √(ab) → Convert to i first!  
⚠️ **Quotient degree:** Always one less than dividend degree

---

## 🎯 30-SECOND PRE-EXAM MANTRA

**Read this right before the exam starts:**

1. **Quadratics:** Δ first, then solve
2. **Polynomials:** Degree → shape, Leading term → ends
3. **Complex roots:** Come in pairs (a ± bi)
4. **Synthetic division:** c comes from (x - c), not (x + c)
5. **Rational functions:** Factor first, cancel common factors
6. **Multiplicity:** Even = bounce, Odd = cross
7. **When stuck:** Try Rational Root Theorem candidates
8. **Check your work:** Plug roots back into original equation

**Breathe. You know this. Trust your preparation.**

---

*Last updated: October 16, 2025 - EXAM DAY EDITION*
