---
layout: concept
title: "Point Conditions Method"
topic: "General Math"
---

# Using Point Conditions to Find Equations
*When You're Given Locations Instead of Forms*

---

## 🎯 CORE INSIGHT

**Points are Constraints That Determine Unique Equations**

When you're given specific points, a vertex, intercepts, or other conditions, you're being given a SYSTEM to solve. Each piece of information is an equation in disguise.

**The Pattern:**
```
Condition → Equation → System → Solve → Unique function

Example:
"Passes through (2, 5)" → 5 = f(2) → equation with unknown coefficients
```

**Why This Matters:**
Many problems don't give you a complete equation—they give you CLUES. Your job is to:
1. Translate conditions into equations
2. Build a system
3. Solve for unknowns
4. Construct the function

---

## 📐 TYPES OF CONDITION PROBLEMS

### Quadratic Functions (Need 3 conditions)

**Why 3?** Standard form has 3 unknowns: ax² + bx + c

**Common Scenarios:**

#### Type 1: Vertex + One Point

**Given:**
- Vertex at (h, k)
- Passes through point (x₁, y₁)

**Strategy:** Use vertex form
```
f(x) = a(x - h)² + k

Substitute the point:
y₁ = a(x₁ - h)² + k
Solve for a
```

**Example:**
```
Vertex: (3, -4)
Point: (5, 8)

f(x) = a(x - 3)² - 4
8 = a(5 - 3)² - 4
8 = a(4) - 4
12 = 4a
a = 3

f(x) = 3(x - 3)² - 4
```

#### Type 2: Three Points (No Vertex)

**Given:** Points (x₁, y₁), (x₂, y₂), (x₃, y₃)

**Strategy:** Use standard form and set up system
```
f(x) = ax² + bx + c

For each point:
y₁ = ax₁² + bx₁ + c
y₂ = ax₂² + bx₂ + c
y₃ = ax₃² + bx₃ + c

Solve 3×3 system for a, b, c
```

**Example:**
```
Points: (0, 3), (1, 6), (-1, 2)

f(x) = ax² + bx + c

Point (0, 3):   3 = a(0) + b(0) + c  →  c = 3
Point (1, 6):   6 = a + b + 3        →  a + b = 3
Point (-1, 2):  2 = a - b + 3        →  a - b = -1

From equations 2 and 3:
a + b = 3
a - b = -1
Add: 2a = 2 → a = 1
Substitute: 1 + b = 3 → b = 2

f(x) = x² + 2x + 3
```

#### Type 3: Axis of Symmetry + Two Points

**Given:**
- Axis of symmetry x = h
- Two points (x₁, y₁), (x₂, y₂)

**Strategy:** Use vertex form (even though k is unknown)
```
f(x) = a(x - h)² + k

Substitute both points → 2 equations, 2 unknowns (a and k)
```

**Example:**
```
Axis: x = 2
Points: (0, 8), (3, 5)

f(x) = a(x - 2)² + k

From (0, 8):  8 = a(0 - 2)² + k  →  8 = 4a + k
From (3, 5):  5 = a(3 - 2)² + k  →  5 = a + k

Subtract: 3 = 3a → a = 1
Substitute: 5 = 1 + k → k = 4

f(x) = (x - 2)² + 4
```

#### Type 4: Roots + Y-intercept

**Given:**
- Roots r₁, r₂
- Y-intercept (0, c)

**Strategy:** Use factored form
```
f(x) = a(x - r₁)(x - r₂)

Substitute (0, c):
c = a(0 - r₁)(0 - r₂)
c = a·r₁·r₂  (watch signs!)
a = c/(r₁·r₂)
```

**Example:**
```
Roots: x = -3, x = 5
Y-intercept: (0, 30)

f(x) = a(x + 3)(x - 5)
30 = a(0 + 3)(0 - 5)
30 = a(3)(-5)
30 = -15a
a = -2

f(x) = -2(x + 3)(x - 5)
```

---

## 🔧 POLYNOMIAL FUNCTIONS (Degree > 2)

### General Principle

**For degree n polynomial:**
Need (n + 1) conditions to determine uniquely

- Degree 2 → 3 conditions
- Degree 3 → 4 conditions
- Degree 4 → 5 conditions

### Type 5: Roots + One Point

**Given:**
- All roots (possibly with multiplicities)
- One additional point

**Strategy:** Write factored form, solve for 'a'
```
f(x) = a(x - r₁)(x - r₂)...(x - rₙ)

Substitute the point, solve for a
```

**Example:**
```
Cubic with roots: -2, 1, 4
Passes through: (0, -16)

f(x) = a(x + 2)(x - 1)(x - 4)

-16 = a(0 + 2)(0 - 1)(0 - 4)
-16 = a(2)(-1)(-4)
-16 = 8a
a = -2

f(x) = -2(x + 2)(x - 1)(x - 4)
```

### Type 6: Partial Roots + Multiple Points

**Given:**
- Some roots (not all)
- Additional points to determine remaining coefficients

**Strategy:** Mixed approach
```
1. Use known roots in factored form
2. Leave remaining part as polynomial
3. Set up system from points
```

**Example:**
```
Quartic with roots at x = 0 (mult 2) and x = 3
Passes through (1, 8) and (2, 4)

f(x) = ax²(x - 3)(x - r)  [one unknown root]

OR if we know degree but not all roots:
f(x) = ax²(x - 3)(x - b)  [unknown root and LC]

Use both points to create system
```

---

## 📋 WORKED EXAMPLES

### Example 1: Vertex and Point (Quadratic)

**Problem:** Find quadratic with vertex (-1, 5) passing through (2, -4)

**Solution:**
```
Step 1: Use vertex form
f(x) = a(x - (-1))² + 5
f(x) = a(x + 1)² + 5

Step 2: Substitute point (2, -4)
-4 = a(2 + 1)² + 5
-4 = a(9) + 5
-9 = 9a
a = -1

Step 3: Final equation
f(x) = -(x + 1)² + 5

Step 4: Expand if needed (standard form)
f(x) = -(x² + 2x + 1) + 5
f(x) = -x² - 2x - 1 + 5
f(x) = -x² - 2x + 4
```

**Verify:**
- Vertex: h = -b/(2a) = -(-2)/(2(-1)) = -2/-2 = -1 ✓
- k = f(-1) = -(-1)² - 2(-1) + 4 = -1 + 2 + 4 = 5 ✓
- Point: f(2) = -(2)² - 2(2) + 4 = -4 - 4 + 4 = -4 ✓

---

### Example 2: Three Points (Quadratic)

**Problem:** Find quadratic passing through (1, 0), (3, 0), and (0, 6)

**Solution:**
```
Step 1: Notice first two points are roots!
Roots: x = 1, x = 3

Step 2: Use factored form
f(x) = a(x - 1)(x - 3)

Step 3: Use third point (0, 6)
6 = a(0 - 1)(0 - 3)
6 = a(-1)(-3)
6 = 3a
a = 2

Step 4: Final equation
f(x) = 2(x - 1)(x - 3)

Step 5: Expand to standard form
f(x) = 2(x² - 4x + 3)
f(x) = 2x² - 8x + 6
```

**Verify:**
- f(1) = 2(1-1)(1-3) = 0 ✓
- f(3) = 2(3-1)(3-3) = 0 ✓
- f(0) = 2(-1)(-3) = 6 ✓

---

### Example 3: System of Equations (No Special Structure)

**Problem:** Find quadratic through (-1, 7), (0, 4), (2, 2)

**Solution:**
```
Step 1: Set up system using f(x) = ax² + bx + c

From (-1, 7):  7 = a(-1)² + b(-1) + c  →  a - b + c = 7
From (0, 4):   4 = a(0)² + b(0) + c    →  c = 4
From (2, 2):   2 = a(2)² + b(2) + c    →  4a + 2b + c = 2

Step 2: Substitute c = 4 into other equations
a - b + 4 = 7   →  a - b = 3
4a + 2b + 4 = 2  →  4a + 2b = -2  →  2a + b = -1

Step 3: Solve system
a - b = 3
2a + b = -1
Add: 3a = 2  →  a = 2/3

From a - b = 3:
2/3 - b = 3
-b = 7/3
b = -7/3

Step 4: Final equation
f(x) = (2/3)x² - (7/3)x + 4

Or multiply by 3: f(x) = 2x² - 7x + 12
```

**Verify:**
- f(-1) = 2(1) - 7(-1) + 12 = 2 + 7 + 12 = 21? NO! Error...

Let me recalculate:
```
From a - b = 3 and 2a + b = -1:
a = 2/3, substitute into first:
2/3 - b = 3
b = 2/3 - 3 = 2/3 - 9/3 = -7/3

Check in second equation:
2(2/3) + (-7/3) = 4/3 - 7/3 = -3/3 = -1 ✓

f(x) = (2/3)x² - (7/3)x + 4

Verify (-1, 7):
f(-1) = (2/3)(1) - (7/3)(-1) + 4
      = 2/3 + 7/3 + 12/3
      = 21/3 = 7 ✓
```

---

## 💡 PROBLEM-SOLVING STRATEGIES

### Choosing the Right Form

| Given Information | Best Form | Why |
|-------------------|-----------|-----|
| Vertex + point | Vertex form | h and k directly given |
| Roots + point | Factored form | Roots directly given |
| Random points | Standard form | Most general approach |
| Axis + points | Vertex form | h given, solve for a and k |
| Y-intercept included | Standard form | c = y-intercept |

### System-Solving Tips

**For 2×2 systems:**
- Elimination (add/subtract equations)
- Substitution (solve for one, plug into other)

**For 3×3 systems:**
- Look for easy elimination (c is often easy to find)
- Reduce to 2×2 system
- Use calculator if permitted

### Verification is Critical

**Always check:**
1. Substitute each given point
2. Verify all conditions are met
3. Check arithmetic carefully

---

## ⚠️ COMMON PITFALLS

### Mistake 1: Wrong Number of Conditions
**Error:** Trying to find quadratic with only 2 points  
**Correction:** Need 3 conditions for unique quadratic (3 unknowns) ✓

### Mistake 2: Arithmetic Errors in Systems
**Error:** Sign errors when manipulating equations  
**Correction:** Use parentheses, work carefully ✓

### Mistake 3: Forgetting to Distribute 'a'
**Error:** f(x) = a(x - h)² + k, forgetting a when expanding  
**Correction:** Distribute a to entire squared term ✓

### Mistake 4: Confusing Vertex and Point
**Error:** Using vertex form when vertex isn't given  
**Correction:** Match form to given information ✓

---

## 🔗 CONNECTIONS

**Prerequisites:**
- [[Completing_the_Square]] - Understanding vertex form
- [[Factoring_Polynomials]] - Understanding factored form
- [[Systems_of_Equations]] - Solving multiple equations

**Related Concepts:**
- [[Constructing_Polynomials_from_Roots]] - Special case
- [[Graph_to_Equation]] - Visual version of this process
- [[Quadratic_Formula]] - Useful for verification

**Applications:**
- [[Curve_Fitting]] - Matching equations to data
- [[Modeling_Real_World_Scenarios]] - Finding equations from constraints
- [[Interpolation]] - Finding equations through points

---

## 🎓 EXAM STRATEGIES

### Quick Decision Tree

**Given vertex?**
→ Use vertex form: f(x) = a(x - h)² + k

**Given roots?**
→ Use factored form: f(x) = a(x - r₁)(x - r₂)...

**Given only random points?**
→ Use standard form: f(x) = ax² + bx + c (or higher degree)

### Time Management
- Vertex + point problems: ~2 minutes
- Three-point problems: ~4 minutes
- Higher degree: ~5-7 minutes

### Common Exam Patterns
- "Find quadratic with vertex ____ passing through ____"
- "Find equation of parabola through points ____"
- "Polynomial with roots ____ and point ____"

---

*Remember: Every condition is an equation waiting to be written. Translate conditions → Build system → Solve → Verify!*
