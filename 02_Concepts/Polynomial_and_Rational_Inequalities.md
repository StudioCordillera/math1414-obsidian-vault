# Solving Polynomial and Rational Inequalities
*The Sign Chart Method for Finding Solution Intervals*

---

## 🎯 CORE INSIGHT

**Inequalities Ask: Where is the Function Positive or Negative?**

Unlike equations (which ask "where equals zero?"), inequalities ask "where is the value above/below zero?" The key insight: polynomials and rational functions only change sign at zeros and vertical asymptotes. Between these critical points, the sign stays constant.

**The Pattern:**
```
Solve: f(x) > 0 (or <, ≥, ≤)

Strategy:
1. Find where f(x) = 0 (zeros)
2. Find where f(x) undefined (VAs for rationals)
3. These create intervals
4. Test sign in each interval
5. Select intervals matching inequality
```

**Why This Matters:**
Many real-world problems ask for ranges where something is positive, negative, or within bounds. The sign chart method handles all cases systematically.

---

## 📐 THE MATHEMATICAL FOUNDATION

### Key Principle: Sign Persistence

**Between critical points, continuous functions maintain their sign.**

Critical points for:
- **Polynomials:** Roots (where f(x) = 0)
- **Rational functions:** Roots AND vertical asymptotes

**Consequence:** Test ONE point in each interval to determine the sign throughout that interval.

### Why Factors Matter

**Sign of Product = Product of Signs**

If f(x) = (x - 2)(x + 3)(x - 5), the sign of f(x) equals:
```
sign(x - 2) × sign(x + 3) × sign(x - 5)
```

Each factor changes sign at its zero. Multiplying signs gives overall sign.

---

## 🔧 METHOD: THE SIGN CHART

**Universal Algorithm for Both Polynomial and Rational Inequalities:**

### Step 1: Move everything to one side
**Goal:** Get inequality in form f(x) > 0 (or <, ≥, ≤ 0)

**Example:**
```
x² + 3x > 10
x² + 3x - 10 > 0  ← Standard form
```

### Step 2: Factor completely
**For polynomials:** Factor the expression  
**For rationals:** Factor numerator AND denominator

**Example:**
```
x² + 3x - 10 > 0
(x + 5)(x - 2) > 0  ← Factored
```

### Step 3: Find critical points
**Zeros:** Set each factor = 0  
**Vertical asymptotes:** (rationals only) Denominator = 0

**Example:**
```
x + 5 = 0 → x = -5
x - 2 = 0 → x = 2

Critical points: -5, 2
```

### Step 4: Create sign chart
**Draw number line with critical points**  
**Create intervals between points**  
**Test each interval**

**Example:**
```
Test points: x = -6, 0, 3

Interval (-∞, -5): x = -6
(x + 5)(x - 2) = (-)(-)  = (+)  ✓

Interval (-5, 2): x = 0
(x + 5)(x - 2) = (+)(-) = (-)  ✗

Interval (2, ∞): x = 3
(x + 5)(x - 2) = (+)(+) = (+)  ✓
```

### Step 5: Write solution
**Select intervals where inequality is true**  
**Include/exclude endpoints based on ≤, ≥ vs <, >**

**Example:**
```
(x + 5)(x - 2) > 0

Positive in: (-∞, -5) ∪ (2, ∞)

Note: Use ( ) because > doesn't include zeros
If ≥, use [-5, 2]
```

---

## 📋 POLYNOMIAL INEQUALITY EXAMPLE

**Problem:** Solve x³ - 4x ≥ 0

**Solution:**

```
Step 1: Already in standard form

Step 2: Factor
x³ - 4x = x(x² - 4) = x(x - 2)(x + 2)

Step 3: Critical points
x = 0, x = 2, x = -2

Step 4: Sign chart
    -2      0      2
────○──────○──────○────
-∞        intervals        ∞

Test x = -3: (-)(-)(-) = (-)  ✗
Test x = -1: (-)(+)(-) = (+)  ✓
Test x = 1:  (+)(+)(-) = (-)  ✗
Test x = 3:  (+)(+)(+) = (+)  ✓

Step 5: Solution (include endpoints for ≥)
x ∈ [-2, 0] ∪ [2, ∞)
```

**Visual:**
```
Sign:    -    +    -    +
      ────[═══]────[═══════→
         -2  0     2
```

---

## 📋 RATIONAL INEQUALITY EXAMPLE

**Problem:** Solve (x - 1)/(x + 3) ≤ 2

**Solution:**

```
Step 1: Move to one side
(x - 1)/(x + 3) - 2 ≤ 0

Step 2: Common denominator
(x - 1)/(x + 3) - 2(x + 3)/(x + 3) ≤ 0
(x - 1 - 2x - 6)/(x + 3) ≤ 0
(-x - 7)/(x + 3) ≤ 0

Step 3: Factor (optional: multiply by -1)
(x + 7)/(x + 3) ≥ 0  ← Flipped inequality

Step 4: Critical points
Numerator: x = -7 (zero)
Denominator: x = -3 (VA, undefined)

Step 5: Sign chart
    -7     -3
────○──────│────
           ^VA

Test x = -8: (-)/(-)  = (+)  ✓
Test x = -5: (-)/(-) = (+)  ✓
Test x = 0:  (+)/(+) = (+)  ✓

Wait—let me redo this...

Actually from (-x - 7)/(x + 3) ≤ 0:

Test x = -8: (1)/(-5) = (-)  ✓
Test x = -5: (2)/(-2) = (-)  ✓
Test x = 0:  (-7)/(3) = (-)  ✓

Let me recalculate: Actually need to be more careful.

Step 3 revisited:
(-x - 7)/(x + 3) ≤ 0
Factor out -1: -(x + 7)/(x + 3) ≤ 0
Multiply both sides by -1: (x + 7)/(x + 3) ≥ 0

Critical points: x = -7, x = -3

Test x = -8: (-1)/(-5) = (+)  ✓
Test x = -5: (2)/(-2) = (-)  ✗
Test x = 0:  (7)/(3) = (+)  ✓

Step 6: Solution
Include x = -7 (zero, ≥ allows)
Exclude x = -3 (VA, undefined)

x ∈ (-∞, -7] ∪ (-3, ∞)
```

---

## ⚠️ CRITICAL RULES

### Rule 1: NEVER Multiply by Variable Expression
**Error:** Multiplying (x-1)/(x+3) < 2 by (x+3) directly  
**Problem:** Don't know if (x+3) is positive or negative!  
**Correction:** Move to one side, create common denominator ✓

### Rule 2: Vertical Asymptotes Are NEVER in Solution
**Rule:** Rational functions undefined at VAs  
**Note:** Use ( ) never [ ] at VA locations

### Rule 3: Check Endpoints Carefully
**For ≤, ≥:** Include zeros (use [ ])  
**For <, >:** Exclude zeros (use ( ))  
**Always:** Exclude VAs (use ( ))

### Rule 4: Flip Inequality When Multiplying by Negative
**Rule:** Multiplying by -1 flips <, >, ≤, ≥

---

## 🎓 EXAM STRATEGIES

### Quick Setup Checklist
1. [ ] Everything on one side
2. [ ] Factored completely
3. [ ] Critical points identified
4. [ ] Test points chosen (one per interval)
5. [ ] Solution in interval notation

### Common Patterns
- **Polynomial ≥ 0:** Include roots in solution
- **Rational > 0:** Exclude both roots and VAs  
- **Product of factors:** Signs multiply
- **Fraction:** Sign = (sign of num)/(sign of denom)

### Verification
- Substitute a value from your solution → should satisfy inequality
- Substitute a value NOT in your solution → should NOT satisfy
- Check endpoints separately

---

*Remember: Inequalities are about REGIONS, not points. Find the boundaries (zeros and VAs), then test which regions work!*
