---
layout: concept
title: "Graphing Quadratic Functions"
topic: "Functions"
type: Topic
status: review
importance: high
tags:
  - concept/algebra
  - chapter-3
  - math/quadratics
  - method/graphing
relations:
  broader:
    - "[[Graphing_Functions]]"
  narrower: []
  depends_on:
    - "[[Vertex_Form]]"
    - "[[Quadratic_Formula]]"
    - "[[Completing_the_Square]]"
    - "[[The_Discriminant]]"
  related:
    - "[[Master_Transformation_Map]]"
    - "[[Domain_and_Range]]"
  used_in: []
review:
  next: 2025-11-24
updated: 2025-10-24
---
# Graphing Quadratic Functions
#quadratics #graphing #parabolas #vertex #transformations #foundational

---

## THE RELATIONAL TRUTH

### What's Really Happening Here

A parabola isn't just "a U-shaped curve" - it's a **geometric manifestation of a quadratic relationship**. Every point on the parabola represents a perfect balance: the distance to a fixed point (focus) equals the distance to a fixed line (directrix). But more practically, it's the **visual story of how y changes as x² dominates the relationship**.

**The Deep Why**: Quadratic functions produce parabolas because the squared term creates **symmetric acceleration**. As you move away from the vertex in either direction, the rate of change increases proportionally. This is why projectiles follow parabolic paths - gravity causes constant acceleration.

**Core Insight**: Every parabola is fundamentally the same shape - just stretched, compressed, reflected, and shifted. The function `f(x) = x²` is the "parent" parabola, and all others are transformations of this base form.

---

## THE GEOMETRIC INTUITION

```
THREE EQUIVALENT FORMS → DIFFERENT INFORMATION REVEALED

Standard Form:  f(x) = ax² + bx + c
                ↓
           Reveals: y-intercept (0, c)
                    Opens up/down (sign of a)
                    
Vertex Form:    f(x) = a(x - h)² + k
                ↓
           Reveals: Vertex (h, k)
                    Axis of symmetry: x = h
                    Transformations from parent
                    
Factored Form:  f(x) = a(x - r₁)(x - r₂)
                ↓
           Reveals: x-intercepts (r₁, 0) and (r₂, 0)
                    Zeros/roots directly visible
```

**The Five Key Features** that completely determine a parabola:
1. **Vertex** (h, k) - The turning point
2. **Axis of Symmetry** x = h - The mirror line
3. **Direction** - Opens up (a > 0) or down (a < 0)
4. **Width** - Narrow (|a| > 1) or wide (|a| < 1)
5. **Intercepts** - Where it crosses axes

---

## WHY IT WORKS (The Relational Foundation)

### The Parent Function: f(x) = x²

**Base Properties**:
- Vertex at origin (0, 0)
- Axis of symmetry: x = 0 (y-axis)
- Opens upward
- Passes through (±1, 1), (±2, 4), (±3, 9)
- Always positive except at vertex
- **Symmetric**: f(-x) = f(x) - even function

**Why This Shape?**
```
x:     -3    -2    -1     0     1     2     3
x²:     9     4     1     0     1     4     9
        ↑                 ↓                 ↑
    Same distance from 0 → Same height
```

The squaring operation **destroys sign information** (negative becomes positive), creating perfect symmetry about x = 0.

### Transformations: How We Get All Other Parabolas

**The Transformation Principle**: 
```
f(x) = a(x - h)² + k
       ↑      ↑      ↑
     Width  Horiz  Vert
     &Dir   Shift  Shift
```

**Parameter 'a' (Vertical Stretch/Compression & Reflection)**:
- `|a| > 1`: Narrower (stretched vertically) - steeper curve
- `|a| < 1`: Wider (compressed vertically) - flatter curve
- `a < 0`: Reflected over x-axis (flipped upside down)
- **Why**: Multiplying y-values scales them; negative flips

**Parameter 'h' (Horizontal Shift)**:
- `f(x - h)` shifts RIGHT by h units (counterintuitive!)
- `f(x + h)` shifts LEFT by h units
- **Why**: Input must be h units larger to produce same output
- **Relationship**: [[Function Transformations]] - horizontal shifts

**Parameter 'k' (Vertical Shift)**:
- Adding k shifts UP by k units
- Subtracting k shifts DOWN by k units
- **Why**: Directly adds to every y-value
- **Relationship**: [[Function Transformations]] - vertical shifts


**The Combined Effect**:
```
Parent: f(x) = x²
        ↓
Apply transformations in order:
1. Vertical stretch/compress/reflect (multiply by a)
2. Horizontal shift (replace x with x-h)
3. Vertical shift (add k)
        ↓
Result: f(x) = a(x - h)² + k
```

---

## THE COMPLETE PROCEDURE

### Context: When to Use Graphing

✓ **Use when you need**:
- Visual representation of quadratic relationship
- To find maximum/minimum values geometrically
- To analyze domain and range
- To solve equations/inequalities graphically
- To understand transformation effects

✓ **Recognizable by**:
- Question asks "sketch," "graph," or "plot"
- Need to visualize solution set
- Analyzing real-world scenarios (trajectories, areas, profits)

---

### Method 1: From Vertex Form (Fastest)

**Given**: `f(x) = a(x - h)² + k`

**STEP 1: Identify vertex directly**
- Vertex: (h, k)
- **Why**: This form reveals vertex immediately
- **Watch out**: Remember (x - h) means shift RIGHT by h

**STEP 2: Determine direction and width**
- If a > 0: Opens up (∪), minimum at vertex
- If a < 0: Opens down (∩), maximum at vertex
- |a| > 1: Narrow
- |a| < 1: Wide

**STEP 3: Plot vertex and axis of symmetry**
- Mark point (h, k)
- Draw vertical dashed line x = h
- **Why**: Everything else is symmetric about this line

**STEP 4: Find additional points**
- Use symmetry: Pick x-values on one side, mirror to other
- Common choices: x = h ± 1, x = h ± 2
- Calculate y-values using function

**STEP 5: Find intercepts (if needed)**
- y-intercept: Let x = 0, find f(0) = a(0 - h)² + k
- x-intercepts: Solve a(x - h)² + k = 0
  - (x - h)² = -k/a
  - x - h = ±√(-k/a)
  - x = h ± √(-k/a)
- **Check discriminant**: If -k/a < 0, no x-intercepts!

**STEP 6: Sketch smooth curve**
- Connect points with smooth parabola
- Ensure symmetry about axis
- Label key features

---

### Method 2: From Standard Form (Most Common)

**Given**: `f(x) = ax² + bx + c`

**STEP 1: Find vertex using formulas**
- h = -b/(2a) → x-coordinate of vertex
- k = f(h) = f(-b/(2a)) → y-coordinate of vertex
- **Why**: Derived from completing the square
- **Relationship**: [[Completing the Square]]

**STEP 2: Determine direction**
- a > 0: Opens up
- a < 0: Opens down

**STEP 3: Find y-intercept**
- Point: (0, c)
- **Why**: f(0) = a(0)² + b(0) + c = c
- **Always exists**: Every polynomial has one y-intercept

**STEP 4: Find x-intercepts using discriminant**
- Calculate discriminant: Δ = b² - 4ac
- **Relationship**: [[The Discriminant]]

If Δ > 0 (two x-intercepts):
  - Use quadratic formula or factor
  - Plot both intercepts

If Δ = 0 (one x-intercept - vertex on x-axis):
  - x = -b/(2a)
  - This equals h (vertex x-coordinate)

If Δ < 0 (no x-intercepts):
  - Parabola doesn't cross x-axis
  - Skip this step, use additional points instead

**STEP 5: Plot axis of symmetry**
- Line: x = -b/(2a)
- Vertical dashed line through vertex

**STEP 6: Find additional symmetric points**
- Pick x-value: x = h + d (where d is any number)
- Calculate y = f(h + d)
- Mirror point: (h - d, y) has same y-value
- **Why**: Symmetry property of parabolas

**STEP 7: Sketch curve**
- Connect all points smoothly
- Ensure symmetry
- Label key features: vertex, intercepts, axis

---

### Method 3: From Factored Form (When Given Roots)

**Given**: `f(x) = a(x - r₁)(x - r₂)`

**STEP 1: Plot x-intercepts immediately**
- Points: (r₁, 0) and (r₂, 0)
- **Why**: Factored form reveals zeros directly

**STEP 2: Find vertex using midpoint**
- h = (r₁ + r₂)/2 → midpoint of roots
- **Why**: Symmetry - vertex is always between roots
- k = f(h) → calculate by substitution

**STEP 3: Find y-intercept**
- f(0) = a(0 - r₁)(0 - r₂) = a·r₁·r₂
- Point: (0, a·r₁·r₂)

**STEP 4: Check direction**
- a > 0: Opens up
- a < 0: Opens down

**STEP 5: Plot and sketch**
- Mark intercepts and vertex
- Use symmetry for additional points if needed
- Connect with smooth curve

---

## WORKED EXAMPLES (Multiple Contexts)

### Example 1: From Vertex Form

**Problem**: Graph `f(x) = 2(x - 3)² - 8`

**Solution**:
```
STEP 1: Identify vertex
        a = 2, h = 3, k = -8
        Vertex: (3, -8)

STEP 2: Direction and width
        a = 2 > 0 → Opens up
        |a| = 2 > 1 → Narrow (stretched)

STEP 3: Axis of symmetry
        x = 3 (vertical line through vertex)

STEP 4: Additional points (use symmetry)
        x = 4: f(4) = 2(4-3)² - 8 = 2(1) - 8 = -6
        Point: (4, -6)
        Mirror: (2, -6) ← by symmetry
        
        x = 5: f(5) = 2(5-3)² - 8 = 2(4) - 8 = 0
        Point: (5, 0) ← This is an x-intercept!
        Mirror: (1, 0) ← by symmetry

STEP 5: y-intercept
        f(0) = 2(0-3)² - 8 = 2(9) - 8 = 10
        Point: (0, 10)

STEP 6: Sketch
        Plot: (3, -8), (4, -6), (2, -6), (5, 0), (1, 0), (0, 10)
        Connect with upward-opening parabola
        Label vertex and intercepts
```

**Key Features**:
- Vertex (minimum): (3, -8)
- x-intercepts: (1, 0) and (5, 0)
- y-intercept: (0, 10)
- Axis: x = 3
- Opens up, narrow

---

### Example 2: From Standard Form

**Problem**: Graph `f(x) = -x² + 4x - 3`

**Solution**:
```
STEP 1: Find vertex
        a = -1, b = 4, c = -3
        h = -b/(2a) = -4/(2(-1)) = -4/(-2) = 2
        k = f(2) = -(2)² + 4(2) - 3 = -4 + 8 - 3 = 1
        Vertex: (2, 1)

STEP 2: Direction
        a = -1 < 0 → Opens down
        This is a MAXIMUM at (2, 1)

STEP 3: y-intercept
        f(0) = -0² + 4(0) - 3 = -3
        Point: (0, -3)

STEP 4: x-intercepts
        Discriminant: Δ = b² - 4ac = 16 - 4(-1)(-3) = 16 - 12 = 4
        Δ > 0 → Two x-intercepts exist
        
        Using quadratic formula:
        x = [-4 ± √4] / [2(-1)] = [-4 ± 2] / (-2)
        x = (-4 + 2)/(-2) = -2/(-2) = 1
        x = (-4 - 2)/(-2) = -6/(-2) = 3
        
        Points: (1, 0) and (3, 0)

STEP 5: Axis of symmetry
        x = 2 (through vertex)

STEP 6: Additional point (optional)
        x = 4: f(4) = -(4)² + 4(4) - 3 = -16 + 16 - 3 = -3
        Point: (4, -3)
        Mirror: (0, -3) ← We already have this as y-intercept!

STEP 7: Sketch
        Plot all points, connect with downward parabola
        Label: vertex (2,1), x-intercepts (1,0) & (3,0), y-intercept (0,-3)
```

**Geometric Insight**: The parabola opens down, peaks at (2, 1), and crosses x-axis at equal distances (1 unit) on either side of the vertex.
