---
node_type: Topic
status: in-progress
importance: critical
tags:
  - textbook/chapter2
  - functions
  - relations
  - coordinate-systems
  - circles
  - linear-functions
sources:
  - miller-gerken-2025
source_refs:
  - "Miller & Gerken §2 p.174-289"
relations:
  broader: [[01_Course/Textbook/ChapterR_Prerequisites]]
  narrower: []
  depends_on: [[01_Course/Textbook/ChapterR_Prerequisites]], [[01_Course/Textbook/Chapter1_Equations_Inequalities]]
  related: []
  used_in: []
created: 2025-10-20
updated: 2025-10-20
---

# Chapter 2: Functions and Relations

> **Core Philosophy**: Functions represent the mathematical formalization of relationships between quantities. Understanding functions is foundational to all higher mathematics.

---

## Chapter Overview

### Learning Objectives
By the end of this chapter, students will:
1. Master the rectangular coordinate system and graphing techniques
2. Understand and apply the definition of a circle
3. Distinguish between relations and functions
4. Work fluently with function notation
5. Understand linear functions and their applications
6. Apply transformations to function graphs
7. Analyze piecewise-defined functions
8. Perform operations on functions including composition

### Chapter Structure
- **Section 2.1**: Rectangular Coordinate System and Graphing Utilities (174-186)
- **Section 2.2**: Circles (187-192)
- **Section 2.3**: Functions and Relations (193-206)
- **Section 2.4**: Linear Equations in Two Variables and Linear Functions (207-223)
- **Section 2.5**: Applications of Linear Equations and Modeling (224-239)
- **Section 2.6**: Transformations of Graphs (241-255)
- **Section 2.7**: Analyzing Graphs of Functions and Piecewise-Defined Functions (256-275)
- **Section 2.8**: Algebra of Functions and Function Composition (276-289)

### Real-World Context
The chapter opens with IRS tax rate tables, demonstrating how **functions model real-world relationships** where multiple variables interact. Tax calculations involve:
- Taxable income (input variable)
- Tax brackets (piecewise structure)
- Marginal rates (slopes in different domains)
- Fixed amounts plus percentages (linear functions with offsets)

This practical application shows why functions are essential: **they formalize relationships that govern everyday life**.

---

## SECTION 2.1: The Rectangular Coordinate System and Graphing Utilities

### Conceptual Foundation

**Historical Context**: René Descartes (1597-1650) revolutionized mathematics by connecting algebra and geometry through the coordinate plane. This **unification of two mathematical domains** enabled:
- Visual representation of algebraic relationships
- Algebraic analysis of geometric shapes
- Foundation for calculus and modern mathematics

### Key Concepts

#### 1. The Rectangular Coordinate System (Cartesian Plane)

**DEFINITION**: A rectangular coordinate system consists of:
- **Origin**: Point (0, 0) where axes intersect
- **x-axis**: Horizontal number line
- **y-axis**: Vertical number line  
- **Quadrants**: Four regions labeled I, II, III, IV (counterclockwise from upper right)

**Ordered Pair Notation**: (x, y)
- **x-coordinate** (abscissa): Horizontal distance from origin
- **y-coordinate** (ordinate): Vertical distance from origin
- **Order matters**: (3, 5) ≠ (5, 3)

**Quadrant Identification**:
```
Quadrant I:   x > 0, y > 0  (upper right)
Quadrant II:  x < 0, y > 0  (upper left)
Quadrant III: x < 0, y < 0  (lower left)
Quadrant IV:  x > 0, y < 0  (lower right)
```

**Special Points**:
- Points on x-axis: (x, 0) - y-coordinate is zero
- Points on y-axis: (0, y) - x-coordinate is zero
- Origin: (0, 0) - both coordinates zero

---

### METHOD 2.1.1: Distance Formula

**Purpose**: Calculate the distance between two points in the coordinate plane

**Prerequisites**:
- Understanding of ordered pairs [[02_Concepts/Real_Number_System]]
- Pythagorean Theorem (Chapter R)
- Absolute value [[02_Concepts/Absolute_Value]]

**Formula**:
$$d = \sqrt{(x_2 - x_1)^2 + (y_2 - y_1)^2}$$

**Step-by-Step Procedure**:

1. **Label the points**: Identify (x₁, y₁) and (x₂, y₂)
   - Choice of which point is "1" vs "2" doesn't affect result

2. **Calculate horizontal distance**: |x₂ - x₁|

3. **Calculate vertical distance**: |y₂ - y₁|

4. **Apply Pythagorean theorem**:
   - Horizontal and vertical distances form legs of right triangle
   - Distance d is the hypotenuse
   - d² = (x₂ - x₁)² + (y₂ - y₁)²

5. **Take square root** to solve for d (take only positive root)

**WORKED EXAMPLE**:
Find the distance between (-5, 1) and (7, -3).

```
Given: (-5, 1) and (7, -3)
Label: (x₁, y₁) = (-5, 1), (x₂, y₂) = (7, -3)

d = √[(7 - (-5))² + (-3 - 1)²]
  = √[(12)² + (-4)²]
  = √[144 + 16]
  = √160
  = √(16 · 10)
  = 4√10 units

Approximate value: 4√10 ≈ 12.65 units
```

**Implicit Knowledge**:
1. **Why drop absolute value bars**: Since (a)² = |a|² for all real numbers, we can write (x₂ - x₁)² directly instead of |x₂ - x₁|²
2. **Alternative formula**: d = √[(x₁ - x₂)² + (y₁ - y₂)²] gives identical result
3. **Sign considerations**: Squaring eliminates concerns about positive/negative differences
4. **Geometric interpretation**: Distance formula extends 1-dimensional distance |a - b| to 2 dimensions

**Common Errors**:
1. **Conceptual (CE-C)**: Forgetting to take square root of sum of squares
   - Incorrect: d = (x₂ - x₁)² + (y₂ - y₁)²
   - Correct: d = √[(x₂ - x₁)² + (y₂ - y₁)²]

2. **Procedural (CE-P)**: Subtracting coordinates in wrong order or mixing coordinates
   - Incorrect: d = √[(x₂ - y₁)² + (y₂ - x₁)²]
   - Correct: Keep x with x, y with y

3. **Computational (CE-Com)**: Sign errors when subtracting negative numbers
   - Common: 7 - (-5) = 2 (incorrect)
   - Correct: 7 - (-5) = 7 + 5 = 12

4. **Notation (CE-N)**: Reporting distance with wrong units or as negative
   - Distance is always positive
   - Include units if given in problem

5. **Verification (CE-V)**: Not checking if result makes sense geometrically
   - Plot points to verify distance is reasonable
   - Distance should match visual estimation

**Cross-Chapter Connections**:
- **Chapter R §R.3**: Pythagorean theorem foundation
- **Chapter 3**: Distance used in conic sections (circles, ellipses, hyperbolas)
- **Chapter 9**: Extended to 3-dimensional space

---

### METHOD 2.1.2: Midpoint Formula

**Purpose**: Find the point exactly halfway between two given points

**Prerequisites**:
- Understanding of ordered pairs
- Concept of average (mean)

**Formula**:
$$M = \left(\frac{x_1 + x_2}{2}, \frac{y_1 + y_2}{2}\right)$$

**Step-by-Step Procedure**:

1. **Label the points**: Identify (x₁, y₁) and (x₂, y₂)

2. **Find x-coordinate of midpoint**: Average the x-coordinates
   - Add x₁ + x₂
   - Divide by 2

3. **Find y-coordinate of midpoint**: Average the y-coordinates
   - Add y₁ + y₂
   - Divide by 2

4. **Write as ordered pair**: (x-average, y-average)

**WORKED EXAMPLE**:
Find the midpoint of the line segment with endpoints (4.2, -4) and (-2.8, 3).

```
Given: (4.2, -4) and (-2.8, 3)
Label: (x₁, y₁) = (4.2, -4), (x₂, y₂) = (-2.8, 3)

x-coordinate of midpoint: (4.2 + (-2.8))/2 = 1.4/2 = 0.7

y-coordinate of midpoint: (-4 + 3)/2 = -1/2 = -0.5

Midpoint: M = (0.7, -0.5) or (0.7, -1/2)
```

**Implicit Knowledge**:
1. **Averaging concept**: Midpoint formula is simply averaging both coordinates
2. **Geometric meaning**: Midpoint is equidistant from both endpoints
3. **Verification method**: Distance from M to endpoint 1 should equal distance from M to endpoint 2
4. **Result is a point**: Midpoint is an ordered pair (two coordinates), not a single number

**Common Errors**:
1. **Conceptual (CE-C)**: Reporting midpoint as single number instead of ordered pair
   - Incorrect: "Midpoint = 0.7"
   - Correct: "Midpoint = (0.7, -0.5)"

2. **Procedural (CE-P)**: Adding instead of averaging, or forgetting to divide by 2
   - Incorrect: (x₁ + x₂, y₁ + y₂)
   - Correct: ((x₁ + x₂)/2, (y₁ + y₂)/2)

3. **Computational (CE-Com)**: Sign errors when adding coordinates with different signs
   - Be careful: 4.2 + (-2.8) = 4.2 - 2.8 = 1.4

4. **Notation (CE-N)**: Confusing midpoint with distance
   - Midpoint: Coordinates of a point (ordered pair)
   - Distance: A single nonnegative number

**Application - Finding Center of Circle**:
When given endpoints of a diameter, the midpoint IS the center of the circle.

Example: Endpoints (-1, 0) and (3, 4)
```
Center = ((-1+3)/2, (0+4)/2) = (2/2, 4/2) = (1, 2)
```

**Cross-Chapter Connections**:
- **Section 2.2**: Finding center of circle from diameter endpoints
- **Geometry**: Midpoint divides segment into two congruent parts
- **Optimization**: Midpoint minimizes sum of distances in certain contexts

---

### METHOD 2.1.3: Graphing Equations by Plotting Points

**Purpose**: Create visual representation of solution set of an equation

**Prerequisites**:
- Understanding that solutions are ordered pairs (x, y) [[02_Concepts/Linear_Equations]]
- Ability to substitute values and evaluate
- Coordinate plotting skills

**Step-by-Step Procedure**:

1. **Solve for y** (if possible and convenient)
   - Isolate y on one side of equation
   - Makes substitution easier

2. **Create value table**:
   - Choose several x values (typically 5-7 points)
   - Select values that make calculations easy
   - Include negative, zero, and positive values

3. **Calculate corresponding y values**:
   - Substitute each x into equation
   - Solve for y
   - Record as ordered pairs

4. **Plot points** on coordinate plane

5. **Connect points** with smooth curve or line
   - For linear equations: Draw straight line through points
   - For other equations: Draw appropriate curve

6. **Verify** (optional but recommended):
   - Check that a few more points lie on the curve
   - Ensure graph makes sense for the equation type

**WORKED EXAMPLE 1**: Graph y - |x| = -1

```
Step 1: Solve for y
y - |x| = -1
y = |x| - 1

Step 2-3: Create table
x  | y = |x| - 1    | Ordered Pair
---|-----------------|--------------
-3 | |-3| - 1 = 2  | (-3, 2)
-2 | |-2| - 1 = 1  | (-2, 1)
-1 | |-1| - 1 = 0  | (-1, 0)
 0 | |0| - 1 = -1  | (0, -1)
 1 | |1| - 1 = 0   | (1, 0)
 2 | |2| - 1 = 1   | (2, 1)
 3 | |3| - 1 = 2   | (3, 2)

Step 4-5: Plot and connect
Graph forms V-shape with vertex at (0, -1)
```

**WORKED EXAMPLE 2**: Graph y² - 1 = x

```
Step 1: Solve for y
y² - 1 = x
y² = x + 1
y = ±√(x + 1)    (Two y values for each positive x!)

Step 2-3: Create table
x  | y = ±√(x+1)      | Ordered Pairs
---|------------------|-----------------
-1 | ±√0 = 0          | (-1, 0)
 0 | ±√1 = ±1         | (0, 1), (0, -1)
 1 | ±√2 ≈ ±1.4       | (1, √2), (1, -√2)
 3 | ±√4 = ±2         | (3, 2), (3, -2)
 8 | ±√9 = ±3         | (8, 3), (8, -3)

IMPORTANT: Choose x ≥ -1 (radicand must be nonnegative)

Step 4-5: Plot and connect
Graph forms parabola opening to the right
```

**Implicit Knowledge**:
1. **Domain restrictions**: When equation involves radicals (even-indexed roots), ensure radicand ≥ 0
2. **Multiple y values**: Some equations produce two y values for single x (like y² = x + 1)
3. **Continuity**: Most "nice" equations produce smooth curves without breaks
4. **Strategic point selection**: Choose x values that make calculations easy (perfect squares under radicals, multiples that cancel denominators, etc.)
5. **Symmetry clues**: If equation involves |x| or x², graph may have symmetry
6. **More points = better accuracy**: Especially important where curve changes direction

**Common Errors**:
1. **Conceptual (CE-C)**: Not recognizing when equation has restrictions on x or y
   - For √(x + 1): Must have x ≥ -1
   - Graph only exists where both x and y are real

2. **Procedural (CE-P)**: Forgetting ± when taking square root
   - Incorrect: y = √(x + 1) only
   - Correct: y = ±√(x + 1)

3. **Computational (CE-Com)**: Arithmetic errors in substitution
   - Check work: Verify each point satisfies original equation

4. **Graphical (CE-G)**: Not plotting enough points to show curve behavior
   - Use more points near curves, turning points, or transitions
   - Linear: Minimum 2 points, recommend 3
   - Nonlinear: Minimum 5 points, recommend 7+

5. **Conceptual (CE-C)**: Connecting points with wrong curve type
   - Linear equations → straight line
   - Quadratic equations → parabola (smooth curve)
   - Absolute value → V-shape (two rays meeting at vertex)

6. **Verification (CE-V)**: Not checking if graph makes sense
   - Plug in a point from graph back into equation to verify

**Cross-Chapter Connections**:
- **Chapter R**: Order of operations used in evaluation
- **Section 2.3**: This method helps identify if relation is a function
- **Chapter 3**: More sophisticated graphing for polynomials and rational functions

---

### METHOD 2.1.4: Finding x- and y-Intercepts

**Purpose**: Identify where graph crosses the coordinate axes

**Prerequisites**:
- Understanding that x-axis has y = 0 [[02_Concepts/Coordinate_Plane]]
- Understanding that y-axis has x = 0
- Equation solving skills [[02_Concepts/Linear_Equations]]

**DEFINITIONS**:
- **x-intercept**: Point (a, 0) where graph crosses x-axis
- **y-intercept**: Point (0, b) where graph crosses y-axis

**Step-by-Step Procedure**:

**To Find x-Intercept(s)**:
1. **Substitute y = 0** into equation
2. **Solve for x**
3. **Write as ordered pair(s)**: (x, 0)

**To Find y-Intercept(s)**:
1. **Substitute x = 0** into equation
2. **Solve for y**
3. **Write as ordered pair**: (0, y)

**WORKED EXAMPLE**: Given y = |x| - 1

**Finding x-intercepts**:
```
Substitute y = 0:
0 = |x| - 1
|x| = 1
x = 1 or x = -1

x-intercepts: (1, 0) and (-1, 0)
```

**Finding y-intercept**:
```
Substitute x = 0:
y = |0| - 1
y = -1

y-intercept: (0, -1)
```

**Implicit Knowledge**:
1. **Why these matter**: Intercepts are often the easiest points to find and plot
2. **Multiple possibilities**:
   - Most functions have **at most one** y-intercept
   - Equations may have **zero, one, or many** x-intercepts
3. **Special cases**:
   - Horizontal line (y = k): No x-intercept unless k = 0
   - Vertical line (x = k): No y-intercept unless k = 0
4. **Shorthand notation**: Sometimes "x-intercept" refers just to the x-coordinate (dropping "(x, 0)" format)
5. **Connection to zeros**: x-intercepts are also called "zeros" or "roots" of the equation

**Common Errors**:
1. **Conceptual (CE-C)**: Confusing which variable to set to zero
   - For x-intercept: Set y = 0 (NOT x = 0)
   - For y-intercept: Set x = 0 (NOT y = 0)

2. **Notation (CE-N)**: Reporting intercept as single coordinate instead of ordered pair
   - Incorrect: "x-intercept = 3"
   - Correct: "x-intercept = (3, 0)" OR "x-intercept at x = 3"

3. **Conceptual (CE-C)**: Assuming every graph must have intercepts
   - Graph may have no x-intercept: y = x² + 1 (never crosses x-axis)
   - Graph may have no y-intercept: circle not containing origin

4. **Procedural (CE-P)**: Not solving equation completely
   - If equation has two solutions, report BOTH x-intercepts
   - Example: x² = 4 gives x = 2 AND x = -2

5. **Computational (CE-Com)**: Making algebraic errors when solving
   - Absolute value equation |x| = 1 has TWO solutions: x = ±1
   - Quadratic may have 0, 1, or 2 real solutions

**Cross-Chapter Connections**:
- **Chapter 1**: Equation solving techniques used to find intercepts
- **Section 2.3**: y-intercept found by evaluating f(0)
- **Chapter 3**: Zeros of polynomial functions

---

## SECTION 2.2: Circles

### Conceptual Foundation

**Geometric Definition**: A **circle** is the set of all points in a plane equidistant from a fixed point (the **center**). The fixed distance is called the **radius**.

**Key Insight**: This geometric definition translates directly into an algebraic equation using the distance formula. This is a prime example of **analytic geometry** - using algebra to describe geometric shapes.

---

### METHOD 2.2.1: Standard Form of Circle Equation

**Purpose**: Write equation of circle given center and radius OR identify center and radius from equation

**Prerequisites**:
- Distance formula [[METHOD 2.1.1]]
- Completing the square [[02_Concepts/Completing_the_Square]]
- Understanding of (x - h)² notation

**STANDARD FORM**:
$$(x - h)^2 + (y - k)^2 = r^2$$

Where:
- **Center**: (h, k)
- **Radius**: r (where r > 0)

**Derivation** (Why this formula?):
```
Let (h, k) be the center and r be the radius
Let (x, y) be ANY point on the circle
By definition: distance from (x, y) to (h, k) equals r

Apply distance formula:
√[(x - h)² + (y - k)²] = r

Square both sides:
(x - h)² + (y - k)² = r²
```

**Step-by-Step Procedure (Writing Equation)**:

1. **Identify center (h, k)** and radius r

2. **Substitute into standard form**: (x - h)² + (y - k)² = r²

3. **Simplify carefully**:
   - Watch signs: (x - (-4)) becomes (x + 4)
   - Square the radius: r = 3 means r² = 9

4. **Verify** (optional):
   - Plug in a point that should be on circle
   - Check distance from center equals radius

**WORKED EXAMPLE 1**: Write equation of circle with center (-4, 6) and radius 2

```
Given: Center (h, k) = (-4, 6), radius r = 2

Standard form: (x - h)² + (y - k)² = r²

Substitute:
[x - (-4)]² + (y - 6)² = (2)²

Simplify:
(x + 4)² + (y - 6)² = 4

This is the answer in standard form.
```

**WORKED EXAMPLE 2**: Write equation given diameter endpoints (-1, 0) and (3, 4)

```
Strategy: 
- Center is midpoint of diameter
- Radius is distance from center to either endpoint

Find center:
Midpoint = ((-1+3)/2, (0+4)/2) = (1, 2)

Find radius:
Use distance formula from (-1, 0) to center (1, 2):
r = √[(1-(-1))² + (2-0)²]
  = √[(2)² + (2)²]
  = √8
  = 2√2

Write equation:
(x - 1)² + (y - 2)² = (2√2)²
(x - 1)² + (y - 2)² = 8

Standard form answer.
```

**Implicit Knowledge**:
1. **Center is NOT on the circle**: Circle is set of points at distance r FROM center
2. **Sign patterns**:
   - (x - h)²: When h is positive, subtract in formula
   - (x + h)²: When h is negative, add in formula
3. **Special case - origin**: Circle centered at origin has equation x² + y² = r²
4. **Radius must be positive**: r > 0 always
5. **Diameter relationship**: Radius = (diameter)/2

**Common Errors**:
1. **Conceptual (CE-C)**: Including center point as part of circle
   - Center is reference point, not ON the circle
   - Draw center as open dot for reference

2. **Notation (CE-N)**: Sign errors when substituting negative coordinates
   - Center (-4, 6): Write (x - (-4))² = (x + 4)²
   - Center (3, -5): Write (y - (-5))² = (y + 5)²

3. **Computational (CE-Com)**: Forgetting to square radius
   - Incorrect: (x - h)² + (y - k)² = r
   - Correct: (x - h)² + (y - k)² = r²

4. **Procedural (CE-P)**: When given diameter, using diameter instead of radius
   - Must divide diameter by 2 to get radius
   - Or: Use distance formula to find radius from center to endpoint

5. **Graphical (CE-G)**: Incorrectly plotting center or radius
   - From center, measure r units in all directions
   - Circle should look circular (not oval)

**Cross-Chapter Connections**:
- **Chapter 1**: Completing the square technique
- **Section 2.1**: Distance and midpoint formulas
- **Chapter 3**: Conic sections (circles are special ellipses)

---

### METHOD 2.2.2: General Form to Standard Form Conversion

**Purpose**: Convert circle equation from expanded form to standard form to identify center and radius

**Prerequisites**:
- Completing the square [[02_Concepts/Completing_the_Square]]
- Recognizing perfect square trinomials
- General form: x² + y² + Ax + By + C = 0

**Step-by-Step Procedure**:

1. **Rearrange equation**:
   - Move constant to right side
   - Group x terms together
   - Group y terms together

2. **Complete the square for x terms**:
   - Take half of x-coefficient: (A/2)
   - Square it: (A/2)²
   - Add to both sides

3. **Complete the square for y terms**:
   - Take half of y-coefficient: (B/2)
   - Square it: (B/2)²
   - Add to both sides

4. **Factor perfect squares**:
   - Left side: (x - h)² + (y - k)²
   - Right side: r²

5. **Identify**:
   - Center: (h, k)
   - Radius: r = √(r²)

6. **Check for degenerate cases**:
   - If r² > 0: Standard circle
   - If r² = 0: Single point (center only)
   - If r² < 0: No graph (empty set)

**WORKED EXAMPLE**: x² + y² + 10x - 6y + 25 = 0

```
Step 1: Rearrange
(x² + 10x) + (y² - 6y) = -25

Step 2: Complete square for x
Coefficient of x: 10
Half of 10: 5
Square: 25
Add 25 to both sides

(x² + 10x + 25) + (y² - 6y) = -25 + 25

Step 3: Complete square for y
Coefficient of y: -6
Half of -6: -3
Square: 9
Add 9 to both sides

(x² + 10x + 25) + (y² - 6y + 9) = -25 + 25 + 9

Step 4: Factor
(x + 5)² + (y - 3)² = 9

Step 5: Identify
Center: (-5, 3)
Radius: √9 = 3

This IS a standard circle (r² = 9 > 0)
```

**Degenerate Cases**:

**Case 1: Single Point**
```
Example: x² + y² - 14y + 49 = 0

Complete the square:
x² + (y² - 14y + 49) = 0
x² + (y - 7)² = 0

Since r² = 0, solution is single point:
{(0, 7)}

Only way sum of squares equals zero is if each term is zero:
x = 0 and y = 7
```

**Case 2: Empty Set**
```
Example: x² + y² + 2x + 5 = 0

Complete the square:
(x² + 2x + 1) + y² = -5 + 1
(x + 1)² + y² = -4

Since r² = -4 < 0, no real solutions exist.
Solution set: ∅ (empty set)

Sum of squares cannot be negative for real numbers.
```

**Implicit Knowledge**:
1. **General form requirements**: Coefficients of x² and y² must both be 1 (or factor out common coefficient first)
2. **Completing the square pattern**: Always [½(coefficient)]²
3. **Both sides balance**: Whatever you add to left, add to right
4. **Why degenerate cases occur**: Not all equations x² + y² + ... = 0 represent circles
5. **Integer coefficients preferred**: In general form, typically use integers with no common factors

**Common Errors**:
1. **Procedural (CE-P)**: Forgetting to add completing-the-square constant to BOTH sides
   - Must maintain equation balance
   - Add (A/2)² and (B/2)² to right side

2. **Computational (CE-Com)**: Errors in calculating (coefficient/2)²
   - Example: For -6y, half is -3, square is +9 (not -9)
   - Sign of squared value is always positive

3. **Conceptual (CE-C)**: Not recognizing degenerate cases
   - Check value of r²
   - If r² ≤ 0, not a standard circle

4. **Notation (CE-N)**: Misreading signs in factored form
   - (x + 5)² means center x-coordinate is -5 (not +5)
   - General pattern: (x - h)² where h is center coordinate

5. **Procedural (CE-P)**: Incomplete factoring
   - Must complete square for BOTH x and y variables
   - Don't forget y terms!

**Cross-Chapter Connections**:
- **Chapter 1 §1.4**: Completing the square method
- **Chapter 3**: Similar techniques for ellipses and hyperbolas
- **Quadratic equations**: Pattern extends to 2D

---

## SECTION 2.3: Functions and Relations

### Conceptual Foundation

**Big Idea**: **Functions** formalize the mathematical concept of "dependency" - how one quantity determines another. This is perhaps the most important concept in all of mathematics.

**Real-World Motivation**: Many relationships exist in the world:
- Cost of mailing depends on weight
- Braking distance depends on speed
- Test score depends on study time
- Perimeter depends on length and width

Functions provide a **precise mathematical language** to describe and analyze these relationships.

---

### CORE CONCEPT: Relations vs Functions

#### Definitions

**RELATION**: A set of ordered pairs (x, y)
- **Domain**: Set of all x values (inputs)
- **Range**: Set of all y values (outputs)

**FUNCTION**: A special relation where each x value is paired with **exactly one** y value
- Formal definition: For each x in the domain, there is **exactly one** corresponding y in the range
- Denoted: "y is a function of x"

**Critical Distinction**:
- ALL functions are relations
- NOT all relations are functions

**FUNCTION TEST**: A relation is a function if and only if no x value appears with two different y values.

---

### METHOD 2.3.1: Determining if a Relation is a Function

**Purpose**: Identify whether a given relation defines y as a function of x

**Prerequisites**:
- Understanding of ordered pairs
- Concept of domain and range
- Ability to identify patterns

**Approaches** (Multiple ways to represent relations):

#### Approach A: From Set of Ordered Pairs

**Procedure**:
1. **Examine all ordered pairs**
2. **Check for repeated x values**:
   - If any x appears with different y values → NOT a function
   - If all x values unique OR same x always has same y → IS a function

**WORKED EXAMPLE 1**:
```
Relation: {(3, 1), (2, 5), (-4, 2), (-1, 0), (3, -4)}

Check x values:
x = 3 appears twice:
  (3, 1) and (3, -4)  ← Different y values!

Conclusion: NOT a function
Reason: x = 3 paired with both y = 1 and y = -4
```

**WORKED EXAMPLE 2**:
```
Relation: {(-1, 4), (2, 3), (3, 4), (-4, 5)}

Check x values:
Each x appears only once:
  x = -1 → y = 4
  x = 2  → y = 3
  x = 3  → y = 4
  x = -4 → y = 5

Conclusion: IS a function
Note: It's OK for different x values to have same y (like y = 4)
```

#### Approach B: Vertical Line Test (from Graph)

**Procedure**:
1. **Draw (or imagine) vertical lines** at various x positions
2. **Check intersections**:
   - If ANY vertical line intersects graph more than once → NOT a function
   - If EVERY vertical line intersects at most once → IS a function

**Why it works**: A vertical line x = a represents all points with x-coordinate a. If the line hits the graph twice, then that x value is paired with two different y values.

**Visual Examples**:
```
FUNCTION:
   ╱
  ╱
 ╱
────────── Any vertical line hits curve only once
  
NOT A FUNCTION:
    ○
   ╱ ╲
  ╱   ╲
────────── Some vertical lines hit curve twice
```

#### Approach C: From Equation

**Procedure**:
1. **Solve equation for y** (if possible)
2. **Examine result**:
   - If solving for y gives y = ±√(...) → NOT a function (two y values)
   - If solving gives y = single expression → IS a function

**WORKED EXAMPLE 3**: Is y² = x a function?
```
Solve for y:
y² = x
y = ±√x

For any x > 0, there are TWO y values.
Example: If x = 4:
  y = +2 or y = -2
  Points: (4, 2) and (4, -2)

Conclusion: NOT a function
```

**WORKED EXAMPLE 4**: Is y = x² a function?
```
Already solved for y: y = x²

For each x value, there is exactly ONE y value.
Example: If x = 3:
  y = 9 only
  Point: (3, 9)

Conclusion: IS a function
```

#### Approach D: From Mapping Diagram

**Procedure**:
1. **Examine arrows** from domain to range
2. **Check for split arrows**:
   - If any domain element has arrows to multiple range elements → NOT function
   - If each domain element has exactly one arrow → IS a function

**Visual Example**:
```
FUNCTION:          NOT A FUNCTION:
Domain  Range      Domain  Range
  1  →  2            1  →  2
  3  →  2            3  →  4  ← Multiple outputs!
  5  →  4            5  →  6
```

**Implicit Knowledge**:
1. **One-to-many prohibited**: One input cannot produce multiple outputs
2. **Many-to-one allowed**: Multiple inputs CAN produce same output
3. **Vertical vs horizontal**: 
   - Vertical line test checks if function
   - Horizontal line test checks if one-to-one (different concept)
4. **Domain first**: Always think "for each x, how many y?"

**Common Errors**:
1. **Conceptual (CE-C)**: Confusing "same y for different x" with "different y for same x"
   - Multiple x → same y: ALLOWED in function
   - Same x → multiple y: NOT ALLOWED in function

2. **Conceptual (CE-C)**: Thinking circles or horizontal parabolas are functions
   - Circle: Fails vertical line test (except at endpoints)
   - x = y²: Not a function (y² = x rearranged)

3. **Procedural (CE-P)**: Not checking ALL ordered pairs
   - Must verify EVERY x value is unique

4. **Conceptual (CE-C)**: Confusing function notation f(x) with multiplication
   - f(x) means "function f evaluated at x"
   - NOT f times x

**Cross-Chapter Connections**:
- **Section 2.4**: Linear functions are special case where relation IS a function
- **Chapter 3**: Polynomial functions all pass vertical line test
- **Future**: Inverse functions reverse the relationship

---

### METHOD 2.3.2: Function Notation and Evaluation

**Purpose**: Understand and use function notation; evaluate functions at specific inputs

**Prerequisites**:
- Understanding that function is a rule (input → output)
- Substitution skills [[Chapter R]]
- Order of operations [[02_Concepts/Order_of_Operations]]

#### Function Notation Basics

**Standard Form**: f(x) = [expression in x]

**Interpretation**:
- **f** = name of the function
- **x** = input variable (independent variable)
- **f(x)** = output value (dependent variable)
  - Read as "f of x" or "f at x"
  - Equivalent to y in equation y = [expression]

**Example**: f(x) = x - 2

This means:
- Function named "f"
- Takes input x
- Produces output that is 2 less than x
- Can write y = f(x) = x - 2

**Evaluation**: f(4) = 4 - 2 = 2
- Input: x = 4
- Output: f(4) = 2
- As ordered pair: (4, 2)

---

### STEP-BY-STEP EVALUATION PROCEDURE

**To Evaluate f(a)**:

1. **Write the function definition**
   f(x) = [expression]

2. **Substitute a for EVERY occurrence of x**
   f(a) = [expression with a substituted for x]

3. **Simplify using order of operations**
   - Parentheses first
   - Exponents
   - Multiplication/Division left to right
   - Addition/Subtraction left to right

4. **Write result**
   f(a) = [simplified value]

**WORKED EXAMPLE 1**: Evaluate g(x) = 2x + 1 for x = -2, -1, 0, 1, 2

```
g(-2) = 2(-2) + 1 = -4 + 1 = -3  → Point: (-2, -3)
g(-1) = 2(-1) + 1 = -2 + 1 = -1  → Point: (-1, -1)
g(0)  = 2(0) + 1  = 0 + 1  = 1   → Point: (0, 1)
g(1)  = 2(1) + 1  = 2 + 1  = 3   → Point: (1, 3)
g(2)  = 2(2) + 1  = 4 + 1  = 5   → Point: (2, 5)

These points lie on the line y = 2x + 1
```

**WORKED EXAMPLE 2**: Evaluate f(x) = 3x² + 2x for f(a) and f(x + h)

**Part (a)**: f(a)
```
f(x) = 3x² + 2x
f(a) = 3a² + 2a    Substitute a for x
```

**Part (b)**: f(x + h)
```
f(x) = 3x² + 2x
f(x + h) = 3(x + h)² + 2(x + h)    Substitute (x+h) for x

Expand (x + h)²:
= 3(x² + 2xh + h²) + 2(x + h)

Distribute:
= 3x² + 6xh + 3h² + 2x + 2h

This is the simplified form of f(x + h)
```

---

### Special Evaluation Cases

#### Case 1: Constant Function
```
h(x) = 5

h(-2) = 5
h(0) = 5
h(100) = 5

Output is ALWAYS 5, regardless of input
```

#### Case 2: Absolute Value Function
```
k(x) = |x + 1|

k(-3) = |-3 + 1| = |-2| = 2
k(-1) = |-1 + 1| = |0| = 0
k(2) = |2 + 1| = |3| = 3
```

#### Case 3: Square Root Function
```
f(x) = √(x + 1)

f(-1) = √(-1 + 1) = √0 = 0
f(0) = √(0 + 1) = √1 = 1
f(3) = √(3 + 1) = √4 = 2
f(8) = √(8 + 1) = √9 = 3

NOTE: Can only evaluate where x + 1 ≥ 0
```

#### Case 4: Piecewise Evaluation (Preview)
```
f(x) = { x + 1   if x < 0
       { x²      if x ≥ 0

f(-2) = -2 + 1 = -1  (use first piece since -2 < 0)
f(0) = 0² = 0        (use second piece since 0 ≥ 0)
f(3) = 3² = 9        (use second piece since 3 ≥ 0)
```

---

### Difference Quotient (Important for Calculus!)

**Form**: [f(x + h) - f(x)] / h

**Purpose**: Measures average rate of change; foundation of derivative

**Procedure**:
1. **Find f(x + h)**: Substitute (x + h) for x
2. **Subtract f(x)**: Compute f(x + h) - f(x)
3. **Divide by h**: Form quotient [f(x + h) - f(x)] / h
4. **Simplify** (usually factor and cancel h)

**WORKED EXAMPLE**: f(x) = x² + 3x

```
Step 1: Find f(x + h)
f(x + h) = (x + h)² + 3(x + h)
         = x² + 2xh + h² + 3x + 3h

Step 2: Compute f(x + h) - f(x)
f(x + h) - f(x) = (x² + 2xh + h² + 3x + 3h) - (x² + 3x)
                = x² + 2xh + h² + 3x + 3h - x² - 3x
                = 2xh + h² + 3h
                = h(2x + h + 3)

Step 3-4: Form quotient and simplify
[f(x + h) - f(x)] / h = h(2x + h + 3) / h
                       = 2x + h + 3  (for h ≠ 0)
```

**Implicit Knowledge**:
1. **Function notation ≠ multiplication**: f(x) does NOT mean f × x
2. **Parentheses indicate substitution**: Everything in parentheses replaces x
3. **f(x + h) requires careful expansion**: Treat (x + h) as single unit
4. **Order matters for composition**: f(g(x)) ≠ g(f(x)) generally
5. **Domain restrictions apply**: Can only evaluate where function is defined

**Common Errors**:
1. **Computational (CE-Com)**: Not substituting for ALL occurrences of x
   - Incorrect: f(a) = 3x² + 2a (forgot to replace x in first term)
   - Correct: f(a) = 3a² + 2a

2. **Computational (CE-Com)**: Errors expanding (x + h)²
   - Common mistake: (x + h)² = x² + h² (WRONG!)
   - Correct: (x + h)² = x² + 2xh + h²

3. **Conceptual (CE-C)**: Confusing f(a + b) with f(a) + f(b)
   - In general: f(a + b) ≠ f(a) + f(b)
   - Example: If f(x) = x², then f(3 + 2) = 25 but f(3) + f(2) = 9 + 4 = 13

4. **Notation (CE-N)**: Treating f(3) as "f times 3"
   - f(3) means "evaluate function f at x = 3"
   - NOT the same as 3f

5. **Procedural (CE-P)**: Not simplifying completely
   - Must combine like terms
   - Factor and cancel where possible (especially in difference quotient)

6. **Conceptual (CE-C)**: Evaluating function outside its domain
   - Check domain restrictions first
   - √(x + 1) requires x ≥ -1

**Cross-Chapter Connections**:
- **Section 2.4**: Linear functions in form f(x) = mx + b
- **Chapter 3**: Polynomial function evaluation
- **Calculus**: Difference quotient leads to derivative

---

### METHOD 2.3.3: Finding Intercepts Using Function Notation

**Purpose**: Find where function graph crosses axes using function notation

**Prerequisites**:
- Function notation understanding
- Intercept concepts from [[METHOD 2.1.4]]
- Equation solving [[02_Concepts/Linear_Equations]]

**Using Function Notation**:

**For x-intercepts**: Solve f(x) = 0
- Set output equal to zero
- Solve resulting equation for x
- Write as points: (x, 0)

**For y-intercept**: Evaluate f(0)
- Substitute x = 0
- Calculate f(0)
- Write as point: (0, f(0))

**WORKED EXAMPLE**: f(x) = x² - 4

**Finding x-intercepts**:
```
Set f(x) = 0:
x² - 4 = 0
x² = 4
x = ±2

x-intercepts: (2, 0) and (-2, 0)

Interpretation: Function equals zero at x = -2 and x = 2
Also called "zeros" or "roots" of the function
```

**Finding y-intercept**:
```
Evaluate f(0):
f(0) = (0)² - 4
     = -4

y-intercept: (0, -4)

Interpretation: When x = 0, function value is -4
```

**Implicit Knowledge**:
1. **"Zeros" terminology**: x-intercepts are also called zeros (where function equals zero)
2. **Real solutions only**: Complex solutions don't correspond to x-intercepts on real plane
3. **At most one y-intercept**: Functions can have only one y-intercept (by vertical line test)
4. **Multiple x-intercepts possible**: Function can cross x-axis multiple times

**Common Errors**:
1. **Conceptual (CE-C)**: Setting x = 0 to find x-intercepts
   - Incorrect: x = 0 finds y-intercept
   - Correct: f(x) = 0 finds x-intercepts

2. **Procedural (CE-P)**: Only finding one x-intercept when there are two
   - x² = 4 has TWO solutions: x = ±2
   - Must report both intercepts

---

### METHOD 2.3.4: Determining Domain and Range

**Purpose**: Identify all valid input values (domain) and all possible output values (range)

**Prerequisites**:
- Understanding of real number restrictions
- Interval notation [[02_Concepts/Interval_Notation]]
- Rational expressions [[Chapter R §R.6]]
- Radicals [[Chapter R §R.3]]

#### Domain Guidelines

**Default Domain**: All real numbers (ℝ)
- Unless there are restrictions, assume domain is (−∞, ∞)

**Must EXCLUDE values that cause**:

1. **Division by zero**
   - Find values that make denominator = 0
   - Exclude those values from domain

2. **Even root of negative number**
   - Find values that make radicand < 0
   - Exclude those values from domain
   - Note: ODD roots (∛x) work for all real numbers

3. **Explicit restrictions stated**
   - If problem states "for x ≥ 0", respect that restriction

**WORKED EXAMPLES**:

**Example 1**: f(x) = (x + 3)/(2x - 5)
```
Denominator: 2x - 5
Set denominator ≠ 0:
2x - 5 ≠ 0
2x ≠ 5
x ≠ 5/2

Domain: All real numbers except 5/2
Interval notation: (−∞, 5/2) ∪ (5/2, ∞)
```

**Example 2**: g(x) = x/(x² + 4)
```
Denominator: x² + 4

Check when denominator = 0:
x² + 4 = 0
x² = -4
No real solutions! (x² is never negative)

Denominator x² + 4 is always positive
Therefore x² + 4 > 0 for all real x

Domain: All real numbers
Interval notation: (−∞, ∞) or ℝ
```

**Example 3**: h(t) = √(2 - t)
```
Radicand: 2 - t
Must have radicand ≥ 0:
2 - t ≥ 0
2 ≥ t
t ≤ 2

Domain: t ≤ 2
Interval notation: (−∞, 2]
```

**Example 4**: k(x) = ∛(x - 5)
```
Odd root (cube root)
Cube root defined for all real numbers

No restrictions needed

Domain: All real numbers
Interval notation: (−∞, ∞)
```

**Example 5**: m(a) = |4 + a|
```
Absolute value defined for all real numbers

No fractions, no even roots

Domain: All real numbers
Interval notation: (−∞, ∞)
```

#### Range Determination (from Graph)

**Procedure**:
1. **Examine graph** (or sketch if needed)
2. **Identify lowest y value** (if exists)
3. **Identify highest y value** (if exists)
4. **Write range as all y values between extremes**

**Visual Strategy**:
- Project graph onto y-axis
- Shaded region on y-axis shows range

**Example from Graph**: Parabola y = x² - 4
```
Vertex at (0, -4) is minimum point
Graph extends upward infinitely

Lowest y value: -4
Highest y value: ∞ (unbounded above)

Range: [-4, ∞) or {y | y ≥ -4}
```

**Implicit Knowledge**:
1. **Domain is about inputs**: "What x values can I put into function?"
2. **Range is about outputs**: "What y values can function produce?"
3. **Domain restrictions often algebraic**: Based on function structure
4. **Range often requires graphical analysis**: Or advanced techniques (calculus)
5. **Interval notation preferred**: Use (−∞, ∞), [a, b], etc.
6. **Combining restrictions**: If multiple restrictions exist, take intersection

**Common Errors**:
1. **Conceptual (CE-C)**: Confusing domain and range
   - Domain: x values (horizontal)
   - Range: y values (vertical)

2. **Procedural (CE-P)**: Forgetting to exclude multiple problematic values
   - If denominator is (x - 2)(x + 3), exclude BOTH x = 2 and x = -3

3. **Computational (CE-Com)**: Solving inequality in wrong direction
   - From 2 - t ≥ 0, correctly get t ≤ 2 (not t ≥ 2)

4. **Conceptual (CE-C)**: Thinking odd roots require restrictions
   - ∛x works for all real x (including negative)
   - Only even roots (√x, ∜x) require non-negative radicand

5. **Notation (CE-N)**: Using wrong interval notation
   - Bracket [ ] for included endpoints
   - Parenthesis ( ) for excluded endpoints or infinity
   - Never use bracket with ∞: Write (−∞, 5] not [−∞, 5]

6. **Conceptual (CE-C)**: Not respecting explicit domain restrictions
   - If problem states "for x ≥ 0", that IS the domain even if no algebraic restriction

**Domain Decision Tree**:
```
Is there a fraction?
├─ YES → Exclude values making denominator = 0
└─ NO → Continue

Is there an even root?
├─ YES → Require radicand ≥ 0
└─ NO → Continue

Are there explicit restrictions?
├─ YES → Apply those restrictions
└─ NO → Domain is all real numbers ℝ
```

**Cross-Chapter Connections**:
- **Chapter R**: Understanding of fractions, radicals, real numbers
- **Section 2.4**: Linear functions have domain ℝ
- **Chapter 3**: Polynomial domains always ℝ; rational function domains exclude zeros of denominator
- **Calculus**: Continuity and limits depend on domain

---

## SECTION 2.4: Linear Equations in Two Variables and Linear Functions

### Conceptual Foundation

**Big Idea**: Linear functions are the simplest and most important class of functions. They model **constant rate of change** and appear throughout mathematics, science, economics, and everyday life.

**Real-World Example** (from Chapter 2 opening):
- Median income for bachelor's degree holders: y = 1261x + 33,296
- **Slope (1261)**: Income increases $1,261 per year on average
- **y-intercept (33,296)**: Starting median income in base year

---

### CORE CONCEPT: Linear Equations

**DEFINITION - Standard Form**:
$$Ax + By = C$$

Where:
- A, B, C are real numbers
- A and B are not both zero
- Variables x and y are each of **first degree** (power 1)

**Key Insight**: Standard form can represent:
- **Slanted lines** (A ≠ 0, B ≠ 0)
- **Vertical lines** (B = 0, so x = k)
- **Horizontal lines** (A = 0, so y = k)

---

### METHOD 2.4.1: Slope of a Line

**Purpose**: Measure the steepness and direction of a line

**Prerequisites**:
- Two points on the line
- Understanding of rise and run
- Ratio/fraction concepts

**DEFINITION - Slope Formula**:
$$m = \frac{\Delta y}{\Delta x} = \frac{y_2 - y_1}{x_2 - x_1} \quad \text{(where } x_2 \neq x_1\text{)}$$

Where:
- **m** = slope
- **Δy** = change in y (rise)
- **Δx** = change in x (run)
- **"rise over run"** interpretation

**Geometric Interpretation**:
```
Positive slope (m > 0): Line rises left to right  ⟋
Negative slope (m < 0): Line falls left to right  ⟍
Zero slope (m = 0):     Horizontal line          —
Undefined slope:        Vertical line            |
```

**Step-by-Step Procedure**:

1. **Label two points**: (x₁, y₁) and (x₂, y₂)
   - Order doesn't matter for final result

2. **Calculate change in y**: y₂ - y₁

3. **Calculate change in x**: x₂ - x₁

4. **Form ratio**: m = (y₂ - y₁)/(x₂ - x₁)

5. **Simplify fraction** (if possible)

6. **Interpret**: 
   - Sign indicates direction
   - Magnitude indicates steepness

**WORKED EXAMPLE 1**: Find slope of line through (-3, -2) and (2, 5)

```
Label points:
(x₁, y₁) = (-3, -2)
(x₂, y₂) = (2, 5)

Calculate:
m = (y₂ - y₁)/(x₂ - x₁)
  = [5 - (-2)]/[2 - (-3)]
  = 7/5

Interpretation:
- Positive slope: line rises
- For every 5 units right, line rises 7 units
- Slope = 7/5 = 1.4
```

**WORKED EXAMPLE 2**: Find slope through (-5/2, 0) and (1, -7)

```
Label points:
(x₁, y₁) = (-5/2, 0)
(x₂, y₂) = (1, -7)

Calculate:
m = (-7 - 0)/[1 - (-5/2)]
  = -7/(1 + 5/2)
  = -7/(7/2)
  = -7 · (2/7)
  = -2

Interpretation:
- Negative slope: line falls
- For every 1 unit right, line drops 2 units
- Slope = -2
```

**Special Cases**:

**Horizontal Line** (y = k):
```
Two points: (2, 3) and (4, 3)

m = (3 - 3)/(4 - 2)
  = 0/2
  = 0

Slope of horizontal line is ZERO
No vertical change → zero slope
```

**Vertical Line** (x = k):
```
Two points: (2, 1) and (2, 3)

m = (3 - 1)/(2 - 2)
  = 2/0
  = UNDEFINED

Slope of vertical line is UNDEFINED
Division by zero → no slope exists
```

**Implicit Knowledge**:
1. **Units of slope**: If x is time (years) and y is dollars, slope has units "dollars per year"
2. **Rate of change**: Slope represents **constant rate of change** for linear relationships
3. **Reversing order**: m = (y₁ - y₂)/(x₁ - x₂) gives same result
4. **Parallel lines**: Have equal slopes
5. **Perpendicular lines**: Have negative reciprocal slopes (if neither is vertical)
6. **Slope-intercept connection**: Slope appears directly in y = mx + b form

**Common Errors**:
1. **Computational (CE-Com)**: Subtracting in wrong order or mixing up coordinates
   - Incorrect: m = (y₂ - x₁)/(x₂ - y₁)
   - Correct: m = (y₂ - y₁)/(x₂ - x₁)
   - Keep x with x, y with y

2. **Computational (CE-Com)**: Sign errors with negative coordinates
   - Be careful: 5 - (-2) = 5 + 2 = 7, not 3

3. **Conceptual (CE-C)**: Saying vertical line has zero slope
   - Horizontal line: slope = 0
   - Vertical line: slope = undefined

4. **Conceptual (CE-C)**: Confusing "no slope" (undefined) with "zero slope"
   - These are different concepts!
   - Zero slope: flat line
   - Undefined slope: vertical line

5. **Notation (CE-N)**: Not simplifying slope to lowest terms
   - Write 6/9 as 2/3
   - Write -4/-2 as 2 (positive)

6. **Procedural (CE-P)**: Inverting the fraction (run over rise)
   - Incorrect: Δx/Δy
   - Correct: Δy/Δx (rise over run)

**Cross-Chapter Connections**:
- **Section 2.5**: Applications use slope as rate
- **Calculus**: Slope generalizes to derivative
- **Statistics**: Slope in regression lines

---

### METHOD 2.4.2: Slope-Intercept Form

**Purpose**: Write and analyze linear equations in most useful form for graphing

**Prerequisites**:
- Understanding of slope [[METHOD 2.4.1]]
- y-intercept concept [[METHOD 2.1.4]]
- Equation solving

**SLOPE-INTERCEPT FORM**:
$$y = mx + b$$

Where:
- **m** = slope of the line
- **b** = y-intercept (the y-value where line crosses y-axis)
- **x, y** = variables

**Why this form is powerful**:
- Slope is immediately visible (coefficient of x)
- y-intercept is immediately visible (constant term)
- Easy to graph (plot y-intercept, use slope to find second point)
- Easy to write equation if slope and y-intercept are known

**Step-by-Step Procedure (Writing Equation)**:

**Given slope m and y-intercept b**:
1. **Substitute m and b** into y = mx + b
2. **Simplify** if needed
3. **Done** - that's the equation!

**WORKED EXAMPLE 1**: Write equation with slope 3 and y-intercept -2

```
Given: m = 3, b = -2

Substitute into y = mx + b:
y = 3x + (-2)
y = 3x - 2

This is the equation in slope-intercept form.
```

**Step-by-Step Procedure (Converting to Slope-Intercept Form)**:

**Given equation in standard form Ax + By = C**:
1. **Isolate y term**: Move x term to right side
2. **Solve for y**: Divide both sides by coefficient of y
3. **Identify**: m = coefficient of x, b = constant term

**WORKED EXAMPLE 2**: Convert 2x + 3y = 6 to slope-intercept form

```
Given: 2x + 3y = 6

Step 1: Isolate y term
3y = -2x + 6

Step 2: Divide by 3
y = (-2x + 6)/3
y = -2x/3 + 6/3
y = -(2/3)x + 2

Identify:
Slope: m = -2/3
y-intercept: b = 2 (point (0, 2))
```

**Graphing Using Slope-Intercept Form**:

**Procedure**:
1. **Plot y-intercept** (0, b)
2. **Use slope to find second point**:
   - Write slope as fraction: m = rise/run
   - From y-intercept, move "run" units horizontally
   - Then move "rise" units vertically
3. **Draw line** through two points

**WORKED EXAMPLE 3**: Graph y = (2/3)x - 1

```
Step 1: Plot y-intercept
Point: (0, -1)

Step 2: Use slope m = 2/3
From (0, -1):
- Move 3 units right (run = 3)
- Move 2 units up (rise = 2)
- Arrive at point (3, 1)

Step 3: Draw line through (0, -1) and (3, 1)
```

**Implicit Knowledge**:
1. **Coefficient of x IS the slope**: Can read slope directly
2. **Constant term IS y-intercept**: Where line crosses y-axis
3. **b can be negative**: y = mx - 3 has y-intercept at (0, -3)
4. **Fractional slopes common**: Often express as fraction for graphing
5. **Comparison to standard form**: Solving for y converts Ax + By = C to y = mx + b

**Common Errors**:
1. **Conceptual (CE-C)**: Confusing b with x-intercept
   - b is y-intercept (on y-axis)
   - x-intercept requires solving mx + b = 0

2. **Procedural (CE-P)**: Not completely isolating y
   - Incorrect: 3y = -2x + 6 (not in slope-intercept form)
   - Correct: y = -(2/3)x + 2

3. **Computational (CE-Com)**: Sign errors when rearranging
   - When moving 2x to right side of 2x + 3y = 6:
   - Correct: 3y = -2x + 6
   - Common error: 3y = 2x + 6 (forgetting to change sign)

4. **Graphical (CE-G)**: Using slope incorrectly
   - If m = -2/3, must go down 2 when going right 3
   - OR go up 2 when going left 3

5. **Notation (CE-N)**: Writing slope-intercept form incorrectly
   - Incorrect: mx + b = y
   - Correct: y = mx + b (y isolated on left)

**Cross-Chapter Connections**:
- **Section 2.6**: Transformations relate to changing m and b
- **Statistics**: Regression line in form ŷ = mx + b
- **Chapter 3**: Linear functions are degree-1 polynomials

---

### METHOD 2.4.3: Point-Slope Form

**Purpose**: Write equation of line given a point and slope (or two points)

**Prerequisites**:
- Slope formula [[METHOD 2.4.1]]
- Understanding that (x₁, y₁) represents a specific point
- Algebraic manipulation

**POINT-SLOPE FORM**:
$$y - y_1 = m(x - x_1)$$

Where:
- **m** = slope
- **(x₁, y₁)** = known point on the line
- **(x, y)** = any other point on the line

**Step-by-Step Procedure**:

**Given: slope m and point (x₁, y₁)**
1. **Substitute values** into y - y₁ = m(x - x₁)
2. **Simplify** if needed
3. **Convert to slope-intercept form** (if requested):
   - Distribute m
   - Solve for y

**WORKED EXAMPLE 1**: Write equation of line with slope -3 through point (2, 5)

```
Given: m = -3, point (x₁, y₁) = (2, 5)

Step 1: Substitute
y - 5 = -3(x - 2)

This is point-slope form (acceptable answer).

Step 2: Convert to slope-intercept (if needed)
y - 5 = -3x + 6
y = -3x + 11

Slope-intercept form: y = -3x + 11
```

**Given: two points (x₁, y₁) and (x₂, y₂)**
1. **Find slope**: m = (y₂ - y₁)/(x₂ - x₁)
2. **Choose either point** as (x₁, y₁)
3. **Apply point-slope form**: y - y₁ = m(x - x₁)
4. **Simplify**

**WORKED EXAMPLE 2**: Write equation through (-1, 4) and (3, -2)

```
Step 1: Find slope
m = (-2 - 4)/(3 - (-1))
  = -6/4
  = -3/2

Step 2: Choose point (use (-1, 4))
(x₁, y₁) = (-1, 4)

Step 3: Apply point-slope form
y - 4 = (-3/2)[x - (-1)]
y - 4 = (-3/2)(x + 1)

Step 4: Simplify to slope-intercept
y - 4 = (-3/2)x - 3/2
y = (-3/2)x - 3/2 + 4
y = (-3/2)x + 5/2

Final answer: y = (-3/2)x + 5/2
```

**Comparison of Forms**:

| Form | Formula | Best Used When |
|------|---------|----------------|
| Slope-Intercept | y = mx + b | Know slope and y-intercept |
| Point-Slope | y - y₁ = m(x - x₁) | Know slope and any point |
| Standard | Ax + By = C | Need integer coefficients |

**Special Cases**:

**Horizontal Line** (slope = 0):
```
Through point (3, 5) with slope 0:
y - 5 = 0(x - 3)
y - 5 = 0
y = 5

Horizontal line equation: y = k
```

**Vertical Line** (undefined slope):
```
Through point (3, 5) (vertical):
Cannot use point-slope form!
Vertical line equation: x = 3

All points have same x-coordinate.
```

**Implicit Knowledge**:
1. **Point-slope most general**: Works for any point, not just y-intercept
2. **Multiple correct forms**: Same line can be written many ways
3. **Sign watching**: (x - (-2)) becomes (x + 2)
4. **Verification method**: Plug in known point - should satisfy equation
5. **Converting between forms**: All forms equivalent, just rearranged

**Common Errors**:
1. **Notation (CE-N)**: Sign errors in point-slope substitution
   - Point (-2, 3): Write y - 3 = m[x - (-2)] = m(x + 2)
   - NOT y - 3 = m(x - 2)

2. **Procedural (CE-P)**: Using wrong form for vertical lines
   - Vertical line: Use x = k (not point-slope form)

3. **Computational (CE-Com)**: Distribution errors when simplifying
   - y - 4 = (-3/2)(x + 1)
   - Correct: y - 4 = (-3/2)x - 3/2
   - Common error: Forgetting to distribute to constant term

4. **Conceptual (CE-C)**: Thinking point must be y-intercept
   - Can use ANY point on the line
   - y-intercept is just one convenient choice

---

## SECTION 2.5: Applications of Linear Equations (Summary)

### Key Application Types

**1. Direct Variation**: y = kx
- Represents proportional relationships
- Passes through origin

**2. Revenue/Cost/Profit Models**:
- Cost: C(x) = fixed cost + (variable cost per unit)·x
- Revenue: R(x) = (price per unit)·x
- Profit: P(x) = R(x) - C(x)

**3. Linear Modeling from Data**:
- Find slope from two data points
- Write equation in slope-intercept form
- Use for predictions (interpolation and extrapolation)

**Key Skills**:
- Interpreting slope in context (rate of change with units)
- Interpreting y-intercept in context (initial value)
- Using equations to make predictions
- Understanding domain restrictions in applications

---

## SECTION 2.6: Transformations of Graphs

### Core Transformation Rules

Let y = f(x) be a function. Then:

**Vertical Transformations**:
- **y = f(x) + k**: Shift UP k units (k > 0)
- **y = f(x) - k**: Shift DOWN k units (k > 0)
- **y = a·f(x)**: Vertical STRETCH if |a| > 1, COMPRESS if 0 < |a| < 1
- **y = -f(x)**: Reflect over x-axis

**Horizontal Transformations** (opposite of what you expect!):
- **y = f(x - h)**: Shift RIGHT h units (h > 0)
- **y = f(x + h)**: Shift LEFT h units (h > 0)
- **y = f(a·x)**: Horizontal COMPRESS if |a| > 1, STRETCH if 0 < |a| < 1
- **y = f(-x)**: Reflect over y-axis

**Key Insights**:
- **Vertical transformations intuitive**: Add → up, subtract → down
- **Horizontal transformations counterintuitive**: Minus → right, plus → left
- **Order matters**: Apply inside transformations (horizontal) before outside (vertical)

---

## SECTION 2.7: Piecewise-Defined Functions

### Core Concept

**Piecewise Function**: Different formulas for different parts of domain

**General Form**:
```
       ⎧ f₁(x)  if condition 1
f(x) = ⎨ f₂(x)  if condition 2
       ⎩ f₃(x)  if condition 3
```

**Evaluation Procedure**:
1. **Check which condition** input satisfies
2. **Use corresponding formula** for that piece
3. **Evaluate** as normal function

**Example**: Absolute Value as Piecewise
```
       ⎧ -x  if x < 0
|x| =  ⎨
       ⎩  x  if x ≥ 0
```

**Graphing Strategy**:
- Graph each piece separately on its domain
- Check endpoints carefully (open vs closed dots)
- Look for continuity or jumps

**Applications**: Tax brackets, shipping costs, overtime pay

---

## SECTION 2.8: Algebra of Functions and Function Composition

### Operations on Functions

**Sum**: (f + g)(x) = f(x) + g(x)
**Difference**: (f - g)(x) = f(x) - g(x)
**Product**: (f · g)(x) = f(x) · g(x)
**Quotient**: (f/g)(x) = f(x)/g(x), where g(x) ≠ 0

**Domain**: Intersection of individual domains (plus g(x) ≠ 0 for quotient)

### Function Composition

**Notation**: (f ∘ g)(x) = f(g(x))
- Read as "f composed with g" or "f of g of x"
- **g is applied first**, then f

**Procedure**:
1. **Evaluate inner function**: Find g(x)
2. **Substitute result into outer function**: Compute f(g(x))

**Example**:
```
If f(x) = x² and g(x) = x + 1:

(f ∘ g)(x) = f(g(x))
           = f(x + 1)
           = (x + 1)²
           = x² + 2x + 1

Note: (g ∘ f)(x) = g(x²) = x² + 1
      Different result! Composition is NOT commutative.
```

**Domain of Composition**:
- Start with domain of inner function (g)
- Restrict to values where g(x) is in domain of outer function (f)

**Applications**: Multi-step processes, nested operations, chain rule (calculus)

---

## RELATIONAL COGNITION FRAMEWORK

### Vertical Integration (Within Chapter 2)

**Foundation → Building → Advanced**:

```
Level 1: Coordinate System Basics
↓
├─ Plotting points
├─ Distance between points
└─ Midpoint of segment

Level 2: Geometric Objects
↓
├─ Circles (distance definition)
├─ Linear equations (graphing)
└─ Intercepts

Level 3: Functions Concept
↓
├─ Relations vs Functions
├─ Function notation
├─ Domain and Range
└─ Function evaluation

Level 4: Linear Functions
↓
├─ Slope (rate of change)
├─ Forms of linear equations
├─ Applications and modeling
└─ Parallel and perpendicular lines

Level 5: Advanced Function Concepts
↓
├─ Transformations of graphs
├─ Piecewise-defined functions
├─ Function operations
└─ Composition of functions
```

**Key Dependencies**:
- **Circles depend on**: Distance formula, midpoint formula
- **Functions depend on**: Relations, ordered pairs, domain/range concepts
- **Linear functions depend on**: Slope, intercepts, function notation
- **Transformations depend on**: Function notation, graphing skills
- **Composition depends on**: Function evaluation, order of operations

---

### Horizontal Integration (Cross-Chapter Connections)

**Chapter R → Chapter 2**:
- Pythagorean theorem → Distance formula
- Real number system → Domain restrictions
- Radicals → Even root domain considerations
- Factoring → Finding x-intercepts (solving f(x) = 0)
- Rational expressions → Domain of rational functions

**Chapter 1 → Chapter 2**:
- Linear equations → Linear functions
- Completing the square → Circle equations (general to standard form)
- Quadratic formula → Finding x-intercepts of quadratics
- Absolute value → Absolute value functions
- Compound inequalities → Domain/range notation

**Chapter 2 → Chapter 3**:
- Function basics → Polynomial functions
- Linear functions → Special case of polynomials (degree 1)
- Slope → Average rate of change
- Function composition → Inverse functions
- Transformations → Polynomial and rational function graphing

**Chapter 2 → Calculus**:
- Slope → Derivative (instantaneous rate of change)
- Distance formula → 3D extensions
- Difference quotient → Limit definition of derivative
- Function composition → Chain rule
- Transformations → Graph analysis

---

### Conceptual Theme: "Functions as Mathematical Machines"

**Input-Process-Output Model**:
```
Domain → [Function] → Range
  x    →    f(x)   →   y
```

**Key Conceptual Connections**:

1. **Functions formalize relationships**
   - Real world: "Income depends on education level"
   - Mathematical: y = f(x) where x is education, y is income

2. **Different representations, same function**
   - Equation: y = 2x + 1
   - Table: {(0,1), (1,3), (2,5), ...}
   - Graph: Slanted line
   - Words: "Output is twice the input plus one"
   - **All equivalent representations**

3. **Restrictions have meaning**
   - Domain restriction √(x - 5) requires x ≥ 5
   - Real-world: "Can't take square root of negative area"
   - Mathematics formalizes real-world constraints

4. **Composition models multi-step processes**
   - f(x) = convert Fahrenheit to Celsius
   - g(x) = convert Celsius to Kelvin
   - (g ∘ f)(x) = convert Fahrenheit to Kelvin directly
   - **Composition chains operations**

---

## MASTERY CHECKLIST: Chapter 2

### Level 1: Recognition (Can you identify?)

□ Quadrants in coordinate plane
□ Relations vs functions
□ Slope (positive/negative/zero/undefined)
□ Linear vs nonlinear equations
□ Domain vs range
□ x-intercepts vs y-intercepts
□ Horizontal vs vertical lines
□ Function notation: f(x) means "function f at x"

### Level 2: Comprehension (Do you understand?)

□ Why vertical line test works for functions
□ How distance formula derives from Pythagorean theorem
□ What slope represents (rate of change)
□ Why domain excludes certain values
□ Difference between f(a + b) and f(a) + f(b)
□ Why horizontal lines have slope 0
□ Why vertical lines have undefined slope
□ How circle equation connects to distance definition
□ What f(g(x)) means (composition order)

### Level 3: Application (Can you use it?)

□ Plot points accurately in all four quadrants
□ Calculate distance between two points
□ Find midpoint of line segment
□ Determine if relation is a function (4 methods)
□ Evaluate f(a), f(x + h), f(a + b)
□ Find domain from equation (identify restrictions)
□ Find range from graph
□ Calculate slope from two points
□ Write equation in slope-intercept form
□ Write equation in point-slope form
□ Convert between equation forms
□ Graph linear equations (multiple methods)
□ Find x- and y-intercepts
□ Graph circles from standard form
□ Convert circle equation to standard form
□ Evaluate piecewise functions
□ Perform function operations (+, -, ·, /)
□ Compose functions (f ∘ g)

### Level 4: Analysis (Can you break it down?)

□ Given graph, identify all key features (domain, range, intercepts, extrema)
□ Determine whether functions are one-to-one
□ Analyze how transformations affect graphs
□ Compare different forms of linear equations
□ Identify when composition is/isn't commutative
□ Explain why certain values are excluded from domain
□ Determine where piecewise function is/isn't continuous
□ Interpret slope and y-intercept in context

### Level 5: Synthesis (Can you create and connect?)

□ Model real-world situations with linear functions
□ Create piecewise function from word description
□ Design function with specific domain/range/intercepts
□ Construct function composition to model multi-step process
□ Generate examples and counterexamples for function properties
□ Connect geometric and algebraic representations
□ Create transformations to achieve specific graph characteristics
□ Build applications using multiple function concepts together

---

## COMMON ERROR PREVENTION MATRIX

### Critical Distinction Pairs (Don't Confuse!)

| Often Confused | Correct Distinction |
|----------------|---------------------|
| x-intercept vs y-intercept | x-intercept: where y = 0; y-intercept: where x = 0 |
| Domain vs Range | Domain: inputs (x); Range: outputs (y) |
| f(x + h) vs f(x) + h | First: evaluate at (x+h); Second: add h to output |
| (f ∘ g)(x) vs (g ∘ f)(x) | Order matters! Apply inner function first |
| f(x) vs f · x | f(x) = function notation; f · x = multiplication |
| Horizontal vs Vertical shift | Inside f( ) affects horizontal; outside affects vertical |
| Slope 0 vs undefined | Zero: horizontal; Undefined: vertical |
| Point (a, b) vs distance |a - b| | Points are coordinates; distance is nonnegative number |

### Section-Specific Error Patterns

**Section 2.1**: Distance and Midpoint
- ❌ Forgetting square root in distance formula
- ❌ Not averaging coordinates for midpoint
- ✓ Remember: Distance uses Pythagorean theorem, midpoint uses averages

**Section 2.2**: Circles
- ❌ Confusing (x - h)² with (x + h)²
- ❌ Not squaring radius in equation
- ✓ Remember: Standard form is (x - h)² + (y - k)² = r²

**Section 2.3**: Functions
- ❌ Thinking relations and functions are same thing
- ❌ Confusing "multiple x → same y" with "same x → multiple y"
- ✓ Remember: Function = each input has exactly ONE output

**Section 2.4**: Linear Functions
- ❌ Inverting slope (run over rise instead of rise over run)
- ❌ Sign errors in point-slope form
- ✓ Remember: m = Δy/Δx (rise over run); watch signs carefully

**Section 2.6**: Transformations
- ❌ Horizontal shift direction (thinking minus → left)
- ❌ Applying transformations in wrong order
- ✓ Remember: Inside function affects horizontal (opposite of expected)

**Section 2.8**: Composition
- ❌ Thinking (f ∘ g) = (g ∘ f)
- ❌ Not finding correct domain for composition
- ✓ Remember: Apply inner function first; composition is NOT commutative

---

## CHAPTER 2 SUMMARY

### Big Ideas

1. **Coordinate Plane**: Foundation for visualizing mathematical relationships
2. **Functions**: Formalize dependency between quantities
3. **Linear Functions**: Model constant rate of change
4. **Transformations**: Modify graphs systematically
5. **Composition**: Chain functions for multi-step processes

### Essential Formulas

| Concept | Formula | Note |
|---------|---------|------|
| Distance | d = √[(x₂-x₁)² + (y₂-y₁)²] | Pythagorean theorem |
| Midpoint | M = ((x₁+x₂)/2, (y₁+y₂)/2) | Average coordinates |
| Slope | m = (y₂-y₁)/(x₂-x₁) | Rise over run |
| Circle (standard) | (x-h)² + (y-k)² = r² | Center (h,k), radius r |
| Slope-intercept | y = mx + b | m = slope, b = y-int |
| Point-slope | y - y₁ = m(x - x₁) | Through (x₁, y₁) |
| Composition | (f ∘ g)(x) = f(g(x)) | Apply g first |

### Proof of Understanding Questions

Test your mastery with these questions:

1. Why does the vertical line test work to identify functions?
2. Why does horizontal shift seem "backwards" in transformations?
3. How does function composition relate to real-world processes?
4. Why can't a function have two different y-intercepts?
5. Why is the distance formula always nonnegative?
6. Why does completing the square help convert circle equations?
7. Why does slope represent rate of change?
8. Why isn't function composition commutative?

**If you can explain these "why" questions, you've mastered Chapter 2!**

---

## PRACTICE PROBLEM RECOMMENDATIONS

### Foundation Level
- §2.1: Problems 11-18 (distance/midpoint), 51-62 (intercepts)
- §2.2: Problems 17-32 (circle equations)
- §2.3: Problems 15-32 (function identification), 75-84 (intercepts)
- §2.4: Problems 11-30 (slope), 43-56 (equations of lines)

### Intermediate Level
- §2.3: Problems 97-110 (domain), 111-114 (graph interpretation)
- §2.5: Application problems
- §2.6: Transformation problems
- §2.7: Piecewise function problems

### Advanced Level
- §2.8: Composition problems
- Mixed review problems combining multiple concepts
- Real-world modeling scenarios

---

**Chapter Status**: EXTRACTION COMPLETE ✅  
**Total Sections**: 8  
**Total Methods**: 15+ comprehensive procedures  
**Integration Level**: High (vertical & horizontal connections documented)  
**Ready for**: Concept node extraction and cross-referencing

---

**Next Steps**:
1. Extract atomic concept nodes from Chapter 2 content
2. Create bidirectional links to existing concepts
3. Begin Chapter 3 extraction
4. Update Project Dashboard with completion status

---
node_type: Topic
status: in-progress
importance: critical
tags:
  - textbook/chapter2
  - functions
  - relations
  - graphing
  - coordinate-geometry
sources:
  - textbook-chapter2
source_refs:
  - "Miller & Gerken Chapter 2 pp.174-289"
relations:
  broader: [[01_Course/Textbook/Chapter1_Equations_Inequalities]]
  narrower: []
  depends_on: [[01_Course/Textbook/ChapterR_Prerequisites]], [[01_Course/Textbook/Chapter1_Equations_Inequalities]]
  defines: [[Functions]], [[Relations]], [[Domain]], [[Range]], [[Slope]]
  related: [[Coordinate_Systems]], [[Graphing_Utilities]]
created: 2025-10-20
updated: 2025-10-20
---

# Chapter 2: Functions and Relations

> **Core Principle**: Functions represent relationships between variables where each input produces exactly one output. Understanding functions is fundamental to all of mathematics and its applications.

---

## 📋 CHAPTER OVERVIEW

### Chapter Purpose
This chapter transitions from solving equations to understanding **relationships between variables**. Functions are the language of mathematics—they describe how one quantity depends on another, from simple linear relationships to complex transformations.

### Key Learning Objectives
By mastering this chapter, you will:
1. Understand rectangular coordinate systems and plotting
2. Work with circles as algebraic and geometric objects
3. Define and identify functions versus relations
4. Apply function notation and evaluation
5. Graph and analyze linear functions
6. Model real-world scenarios with linear equations
7. Transform and analyze function graphs
8. Compose and combine functions algebraically

### Prerequisite Knowledge
- **From Chapter R**: Order of operations, real number system, absolute value, radical operations
- **From Chapter 1**: Equation solving, completing the square, quadratic formula
- **Essential Skills**: Algebraic manipulation, coordinate plotting, equation solving

---

## 🎯 SECTION 2.1: THE RECTANGULAR COORDINATE SYSTEM AND GRAPHING UTILITIES

### 🔑 Core Concepts

#### The Rectangular Coordinate System
**Definition**: A system created by two perpendicular number lines (x-axis and y-axis) intersecting at the origin (0, 0), dividing the plane into four quadrants.

**Historical Context**: Developed by René Descartes (1597-1650), this system unified algebra and geometry, creating analytic geometry.

**Structure**:
- **Quadrant I**: x > 0, y > 0 (upper right)
- **Quadrant II**: x < 0, y > 0 (upper left)
- **Quadrant III**: x < 0, y < 0 (lower left)
- **Quadrant IV**: x > 0, y < 0 (lower right)
- **Axes**: Points on axes are NOT in any quadrant

#### Ordered Pairs and Points
**Notation**: (x, y) where x is the **x-coordinate** (horizontal position) and y is the **y-coordinate** (vertical position)

**Reading Ordered Pairs**:
- First coordinate always represents horizontal displacement
- Second coordinate always represents vertical displacement
- Order matters: (3, 5) ≠ (5, 3)

---

### 📐 METHOD 2.1.1: PLOTTING POINTS ON THE COORDINATE PLANE

**When to Use**: Whenever you need to visually represent a point location or data

**Procedure**:
1. Start at the origin (0, 0)
2. Move horizontally according to x-coordinate:
   - Positive x → move right
   - Negative x → move left
3. From that position, move vertically according to y-coordinate:
   - Positive y → move up
   - Negative y → move down
4. Mark the point at final position

**Example**: Plot (−3, 5)
- Start at origin
- Move 3 units LEFT (x = −3)
- Move 5 units UP (y = 5)
- Mark point

**Common Errors**:
1. ❌ **Coordinate Reversal**: Plotting (5, −3) instead of (−3, 5)
   - **Prevention**: Always read x-coordinate first
2. ❌ **Sign Errors**: Moving right when x is negative
   - **Prevention**: Check sign carefully before moving

---

### 📏 METHOD 2.1.2: DISTANCE FORMULA

**When to Use**: Finding the distance between any two points in the plane

**Formula**:
$$d = \sqrt{(x_2 - x_1)^2 + (y_2 - y_1)^2}$$

**Mathematical Foundation**: Derived from the Pythagorean theorem

**Procedure**:
1. Label points as $(x_1, y_1)$ and $(x_2, y_2)$
2. Substitute into formula
3. Simplify: $(x_2 - x_1)^2$ and $(y_2 - y_1)^2$
4. Add the squares
5. Take square root
6. Simplify radical if possible

**Example**: Find distance between (−5, 1) and (7, −3)

**Solution**:
```
d = √[(7 − (−5))² + (−3 − 1)²]
d = √[(12)² + (−4)²]
d = √[144 + 16]
d = √160
d = √(16 × 10)
d = 4√10 ≈ 12.65 units
```

**Common Errors**:
1. ❌ **Order Matters in Subtraction**: Confusing which point is $(x_1, y_1)$
   - **Prevention**: Label clearly, but note that $(x_2 - x_1)^2 = (x_1 - x_2)^2$
2. ❌ **Forgetting to Square**: Computing |x₂ − x₁| + |y₂ − y₁|
   - **Prevention**: Remember: squares THEN add, THEN square root
3. ❌ **Sign Errors**: Not handling negatives in subtraction
   - **Prevention**: Use parentheses: [7 − (−5)] becomes [7 + 5]

---

### 📍 METHOD 2.1.3: MIDPOINT FORMULA

**When to Use**: Finding the point exactly halfway between two points

**Formula**:
$$M = \left(\frac{x_1 + x_2}{2}, \frac{y_1 + y_2}{2}\right)$$

**Intuition**: The midpoint coordinates are the **averages** of the endpoint coordinates

**Procedure**:
1. Label points as $(x_1, y_1)$ and $(x_2, y_2)$
2. Add x-coordinates and divide by 2
3. Add y-coordinates and divide by 2
4. Write as ordered pair

**Example**: Find midpoint of (4.2, −4) and (−2.8, 3)

**Solution**:
```
M = ((4.2 + (−2.8))/2, (−4 + 3)/2)
M = (1.4/2, −1/2)
M = (0.7, −0.5)
```

**Common Errors**:
1. ❌ **Using Distance Formula**: Confusing midpoint with distance
   - **Prevention**: Midpoint = AVERAGE (add and divide by 2)
2. ❌ **Forgetting Parentheses**: Getting wrong answer with negative coordinates
   - **Prevention**: Always use parentheses: 4.2 + (−2.8)
3. ❌ **Single Number Answer**: Giving one number instead of ordered pair
   - **Prevention**: Midpoint is a POINT (two coordinates)

---

### ✅ METHOD 2.1.4: VERIFYING RIGHT TRIANGLES

**When to Use**: Determining if three points form a right triangle

**Mathematical Foundation**: **Pythagorean Theorem**: If $a^2 + b^2 = c^2$, then the triangle is a right triangle

**Procedure**:
1. Find distances between all three pairs of points
2. Identify the longest distance (potential hypotenuse c)
3. Label the two shorter distances as a and b
4. Check if $a^2 + b^2 = c^2$
5. If yes → right triangle; If no → not a right triangle

**Example**: Do M(−2, −3), P(4, 1), and Q(−1, 7) form a right triangle?

**Solution**:
```
d(M, P) = √[(4−(−2))² + (1−(−3))²] = √(36 + 16) = √52
d(P, Q) = √[(−1−4)² + (7−1)²] = √(25 + 36) = √61
d(M, Q) = √[(−1−(−2))² + (7−(−3))²] = √(1 + 100) = √101

Longest side: √101
Check: (√52)² + (√61)² = 52 + 61 = 113 ≠ 101

NOT a right triangle
```

**Common Errors**:
1. ❌ **Not Identifying Hypotenuse**: Using wrong side as c
   - **Prevention**: Hypotenuse is ALWAYS the longest side
2. ❌ **Calculation Errors**: Arithmetic mistakes in distance formula
   - **Prevention**: Check work carefully, use calculator for verification

---

### 📊 METHOD 2.1.5: GRAPHING EQUATIONS BY PLOTTING POINTS

**When to Use**: When you need to visualize the solution set of an equation

**Procedure**:
1. Solve equation for y if possible (isolate y)
2. Create a table of values:
   - Select several x values (choose convenient values)
   - Calculate corresponding y values
3. Plot all (x, y) pairs on coordinate plane
4. Connect points with smooth curve
5. Draw arrows to indicate continuation

**Example**: Graph $y − |x| = −1$

**Solution**:
```
Solve for y: y = |x| − 1

Table:
x  | y = |x| − 1 | Point
−3 | |−3| − 1 = 2 | (−3, 2)
−2 | |−2| − 1 = 1 | (−2, 1)
−1 | |−1| − 1 = 0 | (−1, 0)
 0 | |0| − 1 = −1  | (0, −1)
 1 | |1| − 1 = 0   | (1, 0)
 2 | |2| − 1 = 1   | (2, 1)
 3 | |3| − 1 = 2   | (3, 2)

Graph: V-shaped curve with vertex at (0, −1)
```

**Common Errors**:
1. ❌ **Too Few Points**: Not plotting enough points to see pattern
   - **Prevention**: Use at least 5-7 points, more for complex curves
2. ❌ **Domain Restrictions Ignored**: Including x values that make y undefined
   - **Prevention**: Check for restrictions (square roots, denominators)
3. ❌ **Wrong Curve Shape**: Connecting points incorrectly
   - **Prevention**: Consider the equation type (linear, quadratic, absolute value)

---

### 🎯 METHOD 2.1.6: FINDING x- AND y-INTERCEPTS

**Definitions**:
- **x-intercept**: Point where graph crosses x-axis (form: (a, 0))
- **y-intercept**: Point where graph crosses y-axis (form: (0, b))

**When to Use**: Intercepts are key features for understanding and sketching graphs

**Procedure for x-intercepts**:
1. Substitute y = 0 into equation
2. Solve for x
3. Write as ordered pairs: (x, 0)

**Procedure for y-intercepts**:
1. Substitute x = 0 into equation
2. Solve for y
3. Write as ordered pair: (0, y)

**Example**: Given $y = |x| − 1$, find intercepts

**Solution**:
```
x-intercepts (set y = 0):
0 = |x| − 1
|x| = 1
x = 1 or x = −1
x-intercepts: (1, 0) and (−1, 0)

y-intercept (set x = 0):
y = |0| − 1
y = −1
y-intercept: (0, −1)
```

**Common Errors**:
1. ❌ **Confusing Which to Find**: Setting wrong variable to zero
   - **Prevention**: x-intercept → set y = 0; y-intercept → set x = 0
2. ❌ **Missing Multiple Intercepts**: Stopping after finding one x-intercept
   - **Prevention**: Solve equation completely
3. ❌ **Stating as Single Number**: Saying "x-intercept is 3" instead of "(3, 0)"
   - **Prevention**: Intercepts are POINTS (ordered pairs)

---

### 💻 METHOD 2.1.7: USING GRAPHING UTILITIES

**When to Use**: When precise graphs are needed or when plotting many points manually would be time-consuming

**Viewing Window Notation**: [Xmin, Xmax, Xscl] by [Ymin, Ymax, Yscl]
- Example: [−10, 10, 1] by [−10, 10, 1] means:
  - x: from −10 to 10, tick marks every 1 unit
  - y: from −10 to 10, tick marks every 1 unit

**Procedure (Calculator)**:
1. Press Y= to access equation editor
2. Enter equation with y isolated
3. Press WINDOW to set viewing parameters
4. Press GRAPH to display
5. Use TABLE feature to verify points

**Common Errors**:
1. ❌ **Equation Not Solved for y**: Entering 2x + 3y = 6 directly
   - **Prevention**: Solve for y first: y = (6 − 2x)/3
2. ❌ **Poor Window Choice**: Graph not showing key features
   - **Prevention**: Consider intercepts and scale when choosing window
3. ❌ **Forgetting Parentheses**: Order of operations errors
   - **Prevention**: Use extra parentheses in calculator

---

## 🔗 RELATIONAL FRAMEWORK: SECTION 2.1

### Vertical Integration (Prerequisites)

**From Chapter R**:
- Real number line → extends to 2D plane
- Absolute value → appears in distance formula
- Radical simplification → needed for distance formula
- Perfect squares → help simplify distance calculations

**From Chapter 1**:
- Equation solving → finding intercepts
- Quadratic formula → may be needed for intercepts
- Pythagorean theorem → foundation for distance formula

### Horizontal Integration (Cross-Connections)

**Within Chapter 2**:
- Plotting points → foundation for ALL graphing in chapter
- Distance/midpoint → used with circles (Section 2.2)
- Intercepts → critical for function analysis (Section 2.3)
- Graphing basics → leads to function transformations (Section 2.6)

**To Future Chapters**:
- Coordinate systems → 3D coordinates (if covered)
- Distance → used in conic sections
- Graphing → foundation for all future curve sketching

### Common Student Misconceptions

1. **"The axes are in the quadrants"**
   - Reality: Axes DIVIDE the plane; points on axes are in NO quadrant

2. **"Distance can be negative"**
   - Reality: Distance is ALWAYS non-negative (≥ 0)

3. **"Midpoint and distance are the same thing"**
   - Reality: Midpoint is a POINT; distance is a NUMBER

4. **"I can use any formula for any problem"**
   - Reality: Distance → number; Midpoint → point; Right triangle → check condition

---

## 📋 SECTION 2.1 SUMMARY

### Essential Formulas
```
Distance: d = √[(x₂−x₁)² + (y₂−y₁)²]
Midpoint: M = ((x₁+x₂)/2, (y₁+y₂)/2)
x-intercept: Set y = 0, solve for x
y-intercept: Set x = 0, solve for y
```

### Key Takeaways
1. Coordinate plane organizes 2D space systematically
2. Distance formula comes from Pythagorean theorem
3. Midpoint coordinates are averages of endpoints
4. Intercepts show where graphs cross axes
5. Graphing technology extends manual plotting

---

## 🎯 SECTION 2.2: CIRCLES

### 🔑 Core Concepts

#### Definition of a Circle
**Geometric Definition**: A circle is the set of all points in a plane that are equidistant from a fixed point called the **center**.

**Key Components**:
- **Center**: Fixed point (h, k) - NOT part of the circle itself
- **Radius**: Distance r from center to any point on circle (r > 0)
- **Diameter**: Distance across circle through center (d = 2r)

**Important**: The center is drawn as an open dot for reference only

---

### 📐 METHOD 2.2.1: WRITING EQUATION OF CIRCLE (GIVEN CENTER AND RADIUS)

**Standard Form (Center-Radius Form)**:
$$(x − h)^2 + (y − k)^2 = r^2$$

where:
- (h, k) is the center
- r is the radius (r > 0)

**When to Use**: When center and radius are known

**Procedure**:
1. Identify center (h, k)
2. Identify radius r
3. Substitute into standard form
4. Simplify if needed

**Example**: Write equation of circle with center (−4, 6) and radius 2

**Solution**:
```
h = −4, k = 6, r = 2
[x − (−4)]² + (y − 6)² = (2)²
(x + 4)² + (y − 6)² = 4
```

**Common Errors**:
1. ❌ **Sign Errors**: Writing (x − 4)² instead of (x + 4)²
   - **Prevention**: (x − h)² with h = −4 becomes [x − (−4)]² = (x + 4)²
2. ❌ **Forgetting to Square Radius**: Writing r instead of r²
   - **Prevention**: Right side is r², not r
3. ❌ **Including Center in Graph**: Drawing filled dot at center
   - **Prevention**: Center is NOT on the circle (use open dot)

---

### 📏 METHOD 2.2.2: FINDING CIRCLE EQUATION (DIAMETER ENDPOINTS)</p>
<parameter>


**When to Use**: When endpoints of a diameter are given

**Key Insight**: The center of a circle is the midpoint of any diameter

**Procedure**:
1. Find center using midpoint formula on diameter endpoints
2. Find radius using distance formula (center to either endpoint)
3. Write standard form equation

**Example**: Write equation with diameter endpoints (−1, 0) and (3, 4)

**Solution**:
```
Step 1: Find center (midpoint)
M = ((−1 + 3)/2, (0 + 4)/2) = (1, 2)

Step 2: Find radius (distance from center to endpoint)
r = √[(1 − (−1))² + (2 − 0)²]
r = √[(2)² + (2)²]
r = √8 = 2√2

Step 3: Write equation
(x − 1)² + (y − 2)² = (√8)²
(x − 1)² + (y − 2)² = 8
```

**Common Errors**:
1. ❌ **Using Endpoint as Center**: Not finding midpoint first
   - **Prevention**: Diameter endpoints → midpoint = center
2. ❌ **Using Diameter as Radius**: Confusing d and r
   - **Prevention**: Radius = half diameter, OR distance from center to endpoint

---

### 🔄 METHOD 2.2.3: CONVERTING GENERAL FORM TO STANDARD FORM

**General Form**: $x^2 + y^2 + Ax + By + C = 0$
**Goal**: Convert to $(x − h)^2 + (y − k)^2 = r^2$ to identify center and radius

**When to Use**: When circle equation is given in expanded form

**Procedure**:
1. Group x terms and y terms separately
2. Move constant to right side
3. Complete the square for x terms:
   - Take coefficient of x, divide by 2, square it
   - Add result to both sides
4. Complete the square for y terms:
   - Take coefficient of y, divide by 2, square it
   - Add result to both sides
5. Factor left side as perfect squares
6. Identify center (h, k) and radius r

**Example**: Convert $x^2 + y^2 + 10x − 6y + 25 = 0$ to standard form

**Solution**:
```
Step 1-2: Group and move constant
(x² + 10x) + (y² − 6y) = −25

Step 3: Complete square for x
[½(10)]² = 25
(x² + 10x + 25) + (y² − 6y) = −25 + 25

Step 4: Complete square for y
[½(−6)]² = 9
(x² + 10x + 25) + (y² − 6y + 9) = −25 + 25 + 9

Step 5: Factor
(x + 5)² + (y − 3)² = 9

Step 6: Identify
Center: (−5, 3)
Radius: √9 = 3
```

**Common Errors**:
1. ❌ **Not Adding to Both Sides**: Changing equation when completing square
   - **Prevention**: Whatever you add to left, add to right
2. ❌ **Sign Errors in Center**: Reading (x + 5)² as center at (5, 3)
   - **Prevention**: (x − h)² means h = −5 when you see (x + 5)²
3. ❌ **Forgetting to Take Square Root**: Stating radius as 9 instead of 3
   - **Prevention**: r² = 9, so r = 3

---

### ⚠️ METHOD 2.2.4: RECOGNIZING DEGENERATE CASES

**Standard Form After Completing Square**: $(x − h)^2 + (y − k)^2 = c$

**Three Cases**:
1. **c > 0**: Circle with radius $r = \sqrt{c}$ ✓
2. **c = 0**: Single point at (h, k) - point circle (degenerate)
3. **c < 0**: No graph (empty set) - imaginary circle (degenerate)

**When to Check**: After converting to standard form

**Example 1 (Point Circle)**: $x^2 + y^2 − 14y + 49 = 0$

**Solution**:
```
x² + (y² − 14y) = −49
x² + (y² − 14y + 49) = −49 + 49
x² + (y − 7)² = 0

Since r² = 0, solution set is {(0, 7)} - a single point
```

**Example 2 (No Graph)**: $x^2 + y^2 + 2x + 5 = 0$

**Solution**:
```
(x² + 2x) + y² = −5
(x² + 2x + 1) + y² = −5 + 1
(x + 1)² + y² = −4

Since r² = −4 < 0, solution set is { } - empty set
(sum of squares cannot equal negative number)
```

**Common Errors**:
1. ❌ **Assuming All Equations Are Circles**: Not checking c value
   - **Prevention**: Always examine the value on right side after completing square
2. ❌ **Graphing Imaginary Circle**: Trying to graph when c < 0
   - **Prevention**: Negative r² means NO real solutions

---

## 🔗 RELATIONAL FRAMEWORK: SECTION 2.2

### Vertical Integration (Prerequisites)

**From Section 2.1**:
- Distance formula → derives circle equation
- Midpoint formula → finds circle center from diameter
- Completing the square → converts general to standard form

**From Chapter 1**:
- Completing the square (1.4) → essential technique here
- Solving quadratics → may appear in circle problems

### Horizontal Integration (Cross-Connections)

**Within Chapter 2**:
- Circles as specific relations → leads to function discussion (2.3)
- Circle equations → fail vertical line test (not functions)
- Graphing circles → uses coordinate system tools

**To Future Chapters**:
- Circles → one type of conic section (later course)
- Standard form strategy → used for other conics
- Completing square → appears throughout algebra

### Real-World Applications
1. **Cell Tower Coverage**: Circle equation models signal range
2. **Radar Systems**: Detection radius as circle
3. **Earthquake Location**: Triangulation using circles from multiple sensors
4. **GPS Technology**: Intersection of circular ranges

---

## 📋 SECTION 2.2 SUMMARY

### Essential Forms
```
Standard Form: (x − h)² + (y − k)² = r²
  Center: (h, k)
  Radius: r

General Form: x² + y² + Ax + By + C = 0
  Convert to standard form by completing the square

Degenerate Cases:
  c = 0 → Single point {(h, k)}
  c < 0 → Empty set { }
```

### Key Techniques
1. Write equation from center and radius
2. Find equation from diameter endpoints
3. Complete the square to convert forms
4. Identify degenerate cases

---

## 🎯 SECTION 2.3: FUNCTIONS AND RELATIONS

### 🔑 Core Concepts

#### Relations
**Definition**: A **relation** is a set of ordered pairs (x, y)

**Components**:
- **Domain**: Set of all x values (inputs)
- **Range**: Set of all y values (outputs)

**Example**: {(8, 92), (3, 58), (11, 98), (5, 72), (8, 86)}
- Domain: {8, 3, 11, 5}
- Range: {92, 58, 98, 72, 86}

#### Functions
**Definition**: A **function** is a relation where each input (x value) corresponds to exactly ONE output (y value)

**Critical Distinction**:
- Relation: Can have multiple y values for same x
- Function: Must have EXACTLY ONE y value for each x

**The Defining Property**: For a function, if $(x_1, y_1)$ and $(x_1, y_2)$ are in the relation, then $y_1 = y_2$

**Example Analysis**:
```
Relation A: {(3, 1), (2, 5), (−4, 2), (−1, 0), (3, −4)}
NOT a function (x = 3 appears with y = 1 AND y = −4)

Relation B: {(−1, 4), (2, 3), (3, 4), (−4, 5)}
IS a function (each x appears only once)
```

**Key Insight**: A function can have same y value for different x values, but NOT same x value for different y values

---

### ✅ METHOD 2.3.1: VERTICAL LINE TEST

**Purpose**: Quickly determine if a graph represents a function

**The Test**: If ANY vertical line intersects the graph in MORE than one point, then the relation is NOT a function

**Why It Works**: A vertical line represents all points with the same x-coordinate. If it hits the graph twice, that x value has two different y values → not a function

**Procedure**:
1. Look at the graph
2. Mentally (or actually) draw vertical lines across the graph
3. Check if any vertical line hits graph more than once
4. If yes → not a function; If no → is a function

**Examples**:

**Graph 1** (Parabola opening upward):
- No vertical line intersects more than once
- IS a function ✓

**Graph 2** (Sideways parabola):
- Many vertical lines intersect twice
- NOT a function ✗

**Graph 3** (Circle):
- Vertical lines through interior intersect twice
- NOT a function ✗

**Common Errors**:
1. ❌ **Using Horizontal Line Test**: That's for one-to-one functions (different concept)
   - **Prevention**: VERTICAL line test for functions
2. ❌ **Missing Intersections**: Not checking entire graph
   - **Prevention**: Scan systematically left to right

---

### 🔢 METHOD 2.3.2: FUNCTION NOTATION AND EVALUATION

**Function Notation**: $f(x)$ read as "f of x"

**Components**:
- f: name of function
- x: input variable
- f(x): output value (equivalent to y)

**Key Relationships**:
- $f(x) = y$
- $f(2) = 4$ means the point (2, 4) is on the graph
- $f(a)$ means "substitute a for x"

**Procedure for Evaluation**:
1. Take the function definition
2. Replace every x with the given input value
3. Simplify using order of operations
4. State the result

**Example 1**: Given $f(x) = 2x + 1$, evaluate f(−2), f(0), f(2)

**Solution**:
```
f(−2) = 2(−2) + 1 = −4 + 1 = −3
f(0) = 2(0) + 1 = 0 + 1 = 1
f(2) = 2(2) + 1 = 4 + 1 = 5

Ordered pairs: (−2, −3), (0, 1), (2, 5)
```

**Example 2**: Given $f(x) = 3x^2 + 2x$, evaluate f(a) and f(x + h)

**Solution**:
```
f(a) = 3a² + 2a

f(x + h) = 3(x + h)² + 2(x + h)
         = 3(x² + 2xh + h²) + 2x + 2h
         = 3x² + 6xh + 3h² + 2x + 2h
```

**Common Errors**:
1. ❌ **Thinking f(x) Means Multiplication**: f(x) ≠ f · x
   - **Prevention**: f(x) is notation for function value, not multiplication
2. ❌ **Not Substituting Everywhere**: Missing some x's when substituting
   - **Prevention**: Replace EVERY occurrence of x
3. ❌ **Order of Operations Errors**: Getting wrong result when simplifying
   - **Prevention**: Follow PEMDAS carefully
4. ❌ **Parentheses Errors**: f(x + h) ≠ f(x) + f(h)
   - **Prevention**: Substitute entire expression (x + h) for x

---

### 🎯 METHOD 2.3.3: FINDING INTERCEPTS USING FUNCTION NOTATION

**x-intercepts**: Points where graph crosses x-axis (y = 0)
- **Procedure**: Solve f(x) = 0
- **Result**: Ordered pairs (x, 0)

**y-intercept**: Point where graph crosses y-axis (x = 0)
- **Procedure**: Evaluate f(0)
- **Result**: Ordered pair (0, f(0))

**Example**: Given $f(x) = x^2 − 4$

**Solution**:
```
x-intercepts (solve f(x) = 0):
x² − 4 = 0
x² = 4
x = ±2
x-intercepts: (2, 0) and (−2, 0)

y-intercept (evaluate f(0)):
f(0) = 0² − 4 = −4
y-intercept: (0, −4)
```

**Common Errors**:
1. ❌ **Confusing Intercept Types**: Setting wrong variable to zero
   - **Prevention**: x-intercepts → set f(x) = 0; y-intercept → find f(0)
2. ❌ **Stopping at First Solution**: Missing multiple x-intercepts
   - **Prevention**: Solve equation completely
3. ❌ **Imaginary Solutions**: Trying to graph complex number intercepts
   - **Prevention**: If solutions are imaginary, there are NO intercepts

---

### 📊 METHOD 2.3.4: DETERMINING DOMAIN FROM EQUATION

**Domain**: Set of all possible input values (x values) that produce real number outputs

**Default Domain**: All real numbers ℝ (unless restricted)

**Key Restrictions**:
1. **Fractions**: Denominator cannot be zero
2. **Even Roots**: Radicand must be non-negative
3. **Logarithms**: Argument must be positive (future topic)

**Procedure**:
1. Identify any fractions → set denominator ≠ 0
2. Identify any even-indexed roots → set radicand ≥ 0
3. Solve resulting inequalities
4. Write domain in interval notation

**Example 1**: $f(x) = \frac{x + 3}{2x − 5}$

**Solution**:
```
Restriction: 2x − 5 ≠ 0
2x ≠ 5
x ≠ 5/2

Domain: (−∞, 5/2) ∪ (5/2, ∞)
```

**Example 2**: $g(x) = \sqrt{2 − x}$

**Solution**:
```
Restriction: 2 − x ≥ 0
−x ≥ −2
x ≤ 2

Domain: (−∞, 2]
```

**Example 3**: $h(t) = \sqrt[3]{t − 5}$

**Solution**:
```
Odd root → no restriction
Domain: (−∞, ∞) or ℝ
```

**Common Errors**:
1. ❌ **Forgetting Denominator Restriction**: Including values that make denominator zero
   - **Prevention**: Always check denominators
2. ❌ **Wrong Inequality for Roots**: Using > instead of ≥
   - **Prevention**: Radicand can equal zero (√0 = 0)
3. ❌ **Restricting Odd Roots**: Thinking all roots need restrictions
   - **Prevention**: Only EVEN roots (√, ∜, etc.) need radicand ≥ 0
4. ❌ **Not Reversing Inequality**: Forgetting to flip when dividing by negative
   - **Prevention**: −x ≥ −2 becomes x ≤ 2 (flip inequality)

---

### 📈 METHOD 2.3.5: DETERMINING RANGE FROM GRAPH

**Range**: Set of all possible output values (y values) in the function

**Procedure**:
1. Look at graph vertically
2. Identify lowest y value (if any)
3. Identify highest y value (if any)
4. Determine if endpoints are included (closed/open dots)
5. Write range in interval notation

**Graph Analysis**:
- Solid dot → value included (use [ or ])
- Open dot → value excluded (use ( or ))
- Arrow → continues infinitely (use ∞)

**Example**: Given graph of function

**Solution**:
```
Lowest y value: −2 (open dot, not included)
Highest y value: 5 (closed dot, included)
Graph continuous between

Range: (−2, 5]
```

**Common Errors**:
1. ❌ **Reading Domain Instead**: Looking horizontally instead of vertically
   - **Prevention**: Range is about y-axis (vertical)
2. ❌ **Wrong Bracket Type**: Using [ when dot is open
   - **Prevention**: Open dot → ( or ); Closed dot → [ or ]

---

## 🔗 RELATIONAL FRAMEWORK: SECTION 2.3

### Vertical Integration (Prerequisites)

**From Chapter R**:
- Set notation → domain and range as sets
- Inequalities → domain restrictions
- Order of operations → function evaluation

**From Chapter 1**:
- Equation solving → finding x-intercepts (solve f(x) = 0)
- Quadratic formula → may be needed for intercepts

### Horizontal Integration (Cross-Connections)

**Within Chapter 2**:
- Functions → basis for linear functions (2.4)
- Domain/range → analyzed graphically (2.7)
- Function notation → used in composition (2.8)

**To Future Chapters**:
- Functions → foundation for ALL future topics
- Function properties → expanded in higher courses
- Domain analysis → critical for rational and radical functions

### Critical Misconceptions

1. **"All relations are functions"**
   - Reality: All functions are relations, but not all relations are functions

2. **"f(x + h) = f(x) + f(h)"**
   - Reality: Generally FALSE. Must substitute (x + h) for x entirely

3. **"Domain is always all real numbers"**
   - Reality: Domain may be restricted by fractions, roots, or other factors

4. **"The y-intercept is found by setting x = 0"**
   - Reality: TRUE! But easy to confuse with x-intercepts

---

## 📋 SECTION 2.3 SUMMARY

### Key Definitions
```
Relation: Set of ordered pairs (x, y)
Domain: Set of x values
Range: Set of y values
Function: Relation where each x has exactly ONE y

Vertical Line Test: If any vertical line hits graph
  more than once → NOT a function
```

### Function Notation
```
f(x): Function value at x (same as y)
f(a): Substitute a for x
f(x + h): Substitute (x + h) for x [NOT f(x) + f(h)]

x-intercepts: Solve f(x) = 0
y-intercept: Evaluate f(0)
```

### Domain Restrictions
```
Fractions: Denominator ≠ 0
Even Roots: Radicand ≥ 0
Odd Roots: No restriction
```

---

*Chapter 2 extraction continues... Sections 2.4-2.8 will be added next*



## 🎯 SECTION 2.4: LINEAR EQUATIONS IN TWO VARIABLES AND LINEAR FUNCTIONS

### 🔑 Core Concepts

#### Linear Equations in Two Variables
**Definition**: An equation that can be written in the form:
$$Ax + By = C$$
where A, B, and C are real numbers and A and B are not both zero

**This is called STANDARD FORM**

**Key Characteristics**:
- Variables x and y are each of **first degree** (power of 1)
- No products of variables (no xy term)
- No variables in denominators
- No variables under radicals
- Graph is always a **straight line**

**Examples**:
```
Linear:                  Not Linear:
2x + 3y = 6   ✓        xy = 5       (product of variables)
x = 5         ✓        y = x²       (x squared)
y = −3        ✓        y = 1/x      (x in denominator)
4x − y = 0    ✓        y = √x       (x under radical)
```

---

### 📏 METHOD 2.4.1: FINDING THE SLOPE OF A LINE

**Definition**: The **slope** m of a line is the ratio of the vertical change (rise) to the horizontal change (run) between any two points on the line

**Slope Formula**: Given points $(x_1, y_1)$ and $(x_2, y_2)$:
$$m = \frac{y_2 − y_1}{x_2 − x_1} = \frac{\Delta y}{\Delta x} = \frac{\text{rise}}{\text{run}}$$

where $x_2 ≠ x_1$

**Interpretation**:
- **Positive slope**: Line rises from left to right (↗)
- **Negative slope**: Line falls from left to right (↘)
- **Zero slope**: Horizontal line (→)
- **Undefined slope**: Vertical line (↕)

**Procedure**:
1. Label points as $(x_1, y_1)$ and $(x_2, y_2)$
2. Compute $y_2 − y_1$ (vertical change)
3. Compute $x_2 − x_1$ (horizontal change)
4. Form ratio: m = (vertical change)/(horizontal change)
5. Simplify fraction if possible

**Example 1**: Find slope through (−3, −2) and (2, 5)

**Solution**:
```
Label: (x₁, y₁) = (−3, −2) and (x₂, y₂) = (2, 5)

m = (y₂ − y₁)/(x₂ − x₁)
  = [5 − (−2)]/[2 − (−3)]
  = 7/5

Slope is 7/5 (positive → line rises)
```

**Example 2**: Find slope through $(−\frac{5}{2}, 0)$ and $(1, −7)$

**Solution**:
```
m = (−7 − 0)/(1 − (−5/2))
  = −7/(1 + 5/2)
  = −7/(7/2)
  = −7 × 2/7
  = −2

Slope is −2 (negative → line falls)
```

**Special Cases**:

**Horizontal Line** (y = k):
- All points have same y-coordinate
- $(x_1, k)$ and $(x_2, k)$
- $m = (k − k)/(x_2 − x_1) = 0/(x_2 − x_1) = 0$
- **Slope is ZERO**

**Vertical Line** (x = k):
- All points have same x-coordinate
- $(k, y_1)$ and $(k, y_2)$
- $m = (y_2 − y_1)/(k − k) = (y_2 − y_1)/0$ 
- **Slope is UNDEFINED** (division by zero)

**Common Errors**:
1. ❌ **Subtracting in Wrong Order**: $\frac{y_1 − y_2}{x_2 − x_1}$ (mixing order)
   - **Prevention**: Keep consistent order: both numerator and denominator must be $(2 − 1)$
2. ❌ **Sign Errors**: Not handling negatives in subtraction correctly
   - **Prevention**: Use parentheses: $2 − (−3)$ becomes $2 + 3$
3. ❌ **Saying Vertical Has Zero Slope**: Confusing undefined with zero
   - **Prevention**: HORIZONTAL = 0 slope; VERTICAL = undefined slope
4. ❌ **Simplifying Complex Fractions Wrong**: Making arithmetic errors
   - **Prevention**: $\frac{−7}{7/2} = −7 \times \frac{2}{7}$ (multiply by reciprocal)

---

### 📊 METHOD 2.4.2: SLOPE-INTERCEPT FORM

**Form**: $y = mx + b$

where:
- **m** = slope of the line
- **b** = y-intercept (the y-coordinate where line crosses y-axis)

**Why It's Useful**: Immediately reveals slope and y-intercept

**To Convert from Standard Form** $Ax + By = C$:
1. Solve for y
2. Identify m (coefficient of x)
3. Identify b (constant term)

**Example**: Convert $2x + 3y = 6$ to slope-intercept form

**Solution**:
```
2x + 3y = 6
3y = −2x + 6
y = (−2/3)x + 2

Slope: m = −2/3
y-intercept: b = 2 (point (0, 2))
```

**Graphing Using Slope-Intercept Form**:
1. Plot y-intercept (0, b)
2. From that point, use slope as rise/run
3. Plot second point
4. Draw line through points

**Example**: Graph $y = \frac{3}{4}x − 2$

**Solution**:
```
Step 1: Plot y-intercept (0, −2)

Step 2: Use slope m = 3/4 = rise 3/run 4
        From (0, −2): move RIGHT 4, UP 3
        
Step 3: Plot point (4, 1)

Step 4: Draw line through (0, −2) and (4, 1)
```

**Common Errors**:
1. ❌ **Confusing m and b**: Thinking y-intercept is the slope
   - **Prevention**: y = mx + b → m is with x, b is alone
2. ❌ **Wrong Sign on Slope**: Losing negative when solving for y
   - **Prevention**: Carefully track signs when isolating y
3. ❌ **Interpreting Slope Wrong**: Using 3/4 as "right 3, up 4"
   - **Prevention**: Slope = rise/run → numerator is VERTICAL

---

### ✏️ METHOD 2.4.3: POINT-SLOPE FORM

**Form**: $y − y_1 = m(x − x_1)$

where:
- **m** = slope
- $(x_1, y_1)$ = a known point on the line

**When to Use**: When you know slope and ONE point (not necessarily y-intercept)

**Procedure**:
1. Identify slope m
2. Identify point $(x_1, y_1)$
3. Substitute into point-slope form
4. (Optional) Convert to slope-intercept or standard form

**Example 1**: Write equation of line with slope $m = 4$ through point $(−2, 3)$

**Solution**:
```
m = 4, (x₁, y₁) = (−2, 3)

Point-slope form:
y − 3 = 4(x − (−2))
y − 3 = 4(x + 2)

Convert to slope-intercept:
y − 3 = 4x + 8
y = 4x + 11
```

**Example 2**: Write equation through points $(2, −1)$ and $(4, 5)$

**Solution**:
```
Step 1: Find slope
m = (5 − (−1))/(4 − 2) = 6/2 = 3

Step 2: Use either point (using (2, −1))
y − (−1) = 3(x − 2)
y + 1 = 3(x − 2)

Step 3: Convert to slope-intercept
y + 1 = 3x − 6
y = 3x − 7
```

**Common Errors**:
1. ❌ **Sign Errors with Negative Coordinates**: $y − y_1$ when $y_1$ is negative
   - **Prevention**: $y − (−3) = y + 3$
2. ❌ **Not Distributing Correctly**: Forgetting to multiply through by m
   - **Prevention**: Carefully distribute: $m(x − x_1) = mx − mx_1$
3. ❌ **Using Wrong Point**: Using point not on line
   - **Prevention**: Verify point satisfies equation

---

### 🔀 METHOD 2.4.4: WRITING EQUATIONS FROM VARIOUS CONDITIONS

**Case 1: Given Slope and y-Intercept**
- Use: $y = mx + b$ directly

**Case 2: Given Slope and One Point**
- Use: Point-slope form, then convert

**Case 3: Given Two Points**
- Step 1: Find slope
- Step 2: Use point-slope with either point

**Case 4: Horizontal Line through Point** $(x_0, y_0)$
- Equation: $y = y_0$

**Case 5: Vertical Line through Point** $(x_0, y_0)$
- Equation: $x = x_0$

**Case 6: Parallel to Given Line**
- Use SAME slope as given line
- Use point-slope with given point

**Case 7: Perpendicular to Given Line**
- Use NEGATIVE RECIPROCAL of given slope
- If given slope is $m_1$, use $m_2 = −\frac{1}{m_1}$
- Use point-slope with given point

**Example (Perpendicular)**: Write equation perpendicular to $y = 2x − 5$ through $(4, 1)$

**Solution**:
```
Given line has slope m₁ = 2
Perpendicular slope: m₂ = −1/2

Point-slope form:
y − 1 = (−1/2)(x − 4)
y − 1 = (−1/2)x + 2
y = (−1/2)x + 3
```

**Parallel vs. Perpendicular Summary**:
```
Original line: y = 3x + 7 (slope = 3)
Parallel line: slope = 3 (SAME)
Perpendicular line: slope = −1/3 (negative reciprocal)

Original line: y = (−2/5)x + 1 (slope = −2/5)
Parallel line: slope = −2/5 (SAME)
Perpendicular line: slope = 5/2 (negative reciprocal)
```

**Common Errors**:
1. ❌ **Using Same Slope for Perpendicular**: Should use negative reciprocal
   - **Prevention**: Perpendicular → flip AND change sign
2. ❌ **Wrong Reciprocal**: Using positive reciprocal
   - **Prevention**: Perpendicular slope = −1/m (negative reciprocal)
3. ❌ **Parallel Confusion**: Using different slope for parallel line
   - **Prevention**: Parallel lines have IDENTICAL slopes

---

### 📈 METHOD 2.4.5: AVERAGE RATE OF CHANGE

**Definition**: The average rate of change of function f over interval $[x_1, x_2]$ is:
$$\text{Average Rate} = \frac{f(x_2) − f(x_1)}{x_2 − x_1} = \frac{\Delta y}{\Delta x}$$

**Note**: This is the same as slope between points $(x_1, f(x_1))$ and $(x_2, f(x_2))$

**Interpretation**: Average rate of change measures "how fast" y changes as x changes over an interval

**Procedure**:
1. Evaluate $f(x_1)$
2. Evaluate $f(x_2)$  
3. Compute $f(x_2) − f(x_1)$ (change in output)
4. Compute $x_2 − x_1$ (change in input)
5. Form ratio

**Example**: Find average rate of change of $f(x) = x^2$ over $[1, 4]$

**Solution**:
```
f(1) = 1² = 1
f(4) = 4² = 16

Average rate = (f(4) − f(1))/(4 − 1)
             = (16 − 1)/3
             = 15/3
             = 5

Interpretation: f increases by 5 units per 1 unit increase in x (on average over [1,4])
```

**For Linear Functions**: Average rate of change is CONSTANT (equals the slope)

**Common Errors**:
1. ❌ **Computing $f(x_2 − x_1)$**: Wrong order of operations
   - **Prevention**: Evaluate f at each point FIRST, then subtract
2. ❌ **Forgetting Negative Signs**: Sign errors in subtraction
   - **Prevention**: Use parentheses carefully

---

## 🔗 RELATIONAL FRAMEWORK: SECTION 2.4

### Vertical Integration (Prerequisites)

**From Chapter R**:
- Solving for a variable → isolating y to get slope-intercept form
- Fractions and simplification → simplifying slopes

**From Section 2.1**:
- Graphing on coordinate plane → graphing lines
- Intercepts → y-intercept appears in slope-intercept form

**From Section 2.3**:
- Functions → linear functions are special case
- Function notation → used in average rate of change

### Horizontal Integration (Cross-Connections)

**Within Chapter 2**:
- Linear functions → simplest functions to analyze
- Slope → related to rate of change
- Applications → Section 2.5 uses linear equations for modeling

**To Future Chapters**:
- Linear equations → foundation for systems of equations
- Slope → leads to derivative concept (calculus)
- Lines → used to approximate curves (tangent lines in calculus)

### Real-World Applications
1. **Economics**: Supply and demand curves (linear approximations)
2. **Physics**: Constant velocity (distance = rate × time)
3. **Business**: Cost functions, revenue functions, break-even analysis
4. **Statistics**: Linear regression (best-fit lines through data)

---

## 📋 SECTION 2.4 SUMMARY

### Forms of Linear Equations
```
Standard Form: Ax + By = C
  General form, both variables on left side

Slope-Intercept Form: y = mx + b
  m = slope, b = y-intercept
  Best for quick graphing and identifying properties

Point-Slope Form: y − y₁ = m(x − x₁)
  m = slope, (x₁, y₁) = point on line
  Best when you know slope and one point

Horizontal Line: y = k (slope = 0)
Vertical Line: x = k (slope undefined)
```

### Slope Properties
```
Positive slope (m > 0): Line rises ↗
Negative slope (m < 0): Line falls ↘
Zero slope (m = 0): Horizontal line →
Undefined slope: Vertical line ↕

Parallel lines: SAME slope (m₁ = m₂)
Perpendicular lines: NEGATIVE RECIPROCAL slopes (m₂ = −1/m₁)
```

### Key Formulas
```
Slope: m = (y₂ − y₁)/(x₂ − x₁)

Average Rate of Change: [f(x₂) − f(x₁)]/(x₂ − x₁)

For linear function: Average rate = slope (constant)
```

---

*Chapter 2 extraction continues... I'll complete Sections 2.5-2.8 next to finish the chapter*



## 🎯 SECTION 2.5: APPLICATIONS OF LINEAR EQUATIONS AND MODELING

### 🔑 Core Concepts

#### Mathematical Modeling
**Definition**: Using mathematical structures (equations, functions, graphs) to represent real-world situations

**Linear Models**: Situations where one quantity changes at a constant rate relative to another

**Key Features of Linear Models**:
- Constant rate of change (slope)
- Can make predictions via interpolation or extrapolation
- Form: $y = mx + b$ where m and b have real-world meaning

---

### 📊 METHOD 2.5.1: INTERPRETING SLOPE AND Y-INTERCEPT IN CONTEXT

**When to Use**: When given a linear model of real-world data

**slope m**: Rate of change with units
- "per" language: dollars per year, miles per hour, etc.
- Positive m → increasing relationship
- Negative m → decreasing relationship

**y-intercept b**: Initial value when x = 0
- Starting amount, base cost, initial population, etc.
- Context determines if b = 0 makes sense

**Procedure**:
1. Identify variables and units
2. Interpret slope m with units
3. Interpret y-intercept b in context
4. State reasonable domain based on situation

**Example**: Median income for bachelor's degree holders: $y = 1261x + 33,296$
where x = years since 1990, y = median income in dollars

**Interpretation**:
```
Slope m = 1261:
  "Median income increases by $1,261 per year"
  
y-intercept b = 33,296:
  "In 1990 (when x = 0), median income was $33,296"
  
Domain restriction:
  x ≥ 0 (can't have negative years since 1990)
  Model validity may be limited to data range
```

**Common Errors**:
1. ❌ **Forgetting Units**: Stating "slope is 1261" without units
   - **Prevention**: Always include units in interpretation
2. ❌ **Wrong Unit for Slope**: Using wrong "per" unit
   - **Prevention**: Slope units = (y units)/(x units)
3. ❌ **Extrapolating Too Far**: Using model outside valid range
   - **Prevention**: Note limitations of model

---

### 💰 METHOD 2.5.2: COST, REVENUE, AND PROFIT MODELS

**Key Relationships**:
- **Cost**: Total expense to produce/provide something
  - Fixed cost: Constant regardless of quantity
  - Variable cost: Depends on quantity
  - Total cost: C(x) = (variable cost per unit)·x + fixed cost

- **Revenue**: Income from sales
  - R(x) = (price per unit)·x

- **Profit**: Revenue minus cost
  - P(x) = R(x) − C(x)

- **Break-even**: When profit = 0 (revenue = cost)
  - Solve: R(x) = C(x)

**Procedure for Break-Even Analysis**:
1. Write cost function C(x)
2. Write revenue function R(x)
3. Set R(x) = C(x)
4. Solve for x (break-even quantity)
5. Interpret result in context

**Example**: Fixed cost $2000, variable cost $15 per item, selling price $35 per item

**Solution**:
```
Cost: C(x) = 15x + 2000
Revenue: R(x) = 35x

Break-even (C(x) = R(x)):
15x + 2000 = 35x
2000 = 20x
x = 100

Interpretation: Must sell 100 items to break even
```

**Common Errors**:
1. ❌ **Confusing Cost Types**: Mixing fixed and variable costs
   - **Prevention**: Fixed cost = constant term; variable cost = coefficient of x
2. ❌ **Wrong Profit Formula**: Using P(x) = R(x) + C(x)
   - **Prevention**: Profit = Revenue MINUS Cost
3. ❌ **Not Checking Reasonableness**: Getting negative or fractional items
   - **Prevention**: Context determines valid x values

---

### 🔬 METHOD 2.5.3: DIRECT VARIATION

**Definition**: y varies directly as x (or y is directly proportional to x) if:
$$y = kx$$
where k is the **constant of variation** (k ≠ 0)

**Key Characteristics**:
- Graph passes through origin (0, 0)
- As x increases, y increases (if k > 0)
- As x increases, y decreases (if k < 0)

**Procedure**:
1. Write variation equation: y = kx
2. Use given values to find k
3. Write specific equation with k value
4. Use equation to answer questions

**Example**: y varies directly as x, and y = 12 when x = 4. Find y when x = 7.

**Solution**:
```
Step 1: y = kx

Step 2: Find k
12 = k(4)
k = 3

Step 3: Specific equation
y = 3x

Step 4: Find y when x = 7
y = 3(7) = 21
```

**Common Errors**:
1. ❌ **Wrong Variation Type**: Confusing direct with inverse variation
   - **Prevention**: Direct → product form (y = kx); Inverse → quotient (y = k/x)
2. ❌ **Not Solving for k**: Using wrong value
   - **Prevention**: Always find k first using given information

---

### 📐 METHOD 2.5.4: MIXTURE PROBLEMS

**Types**:
1. **Solution Mixtures**: Combining liquids with different concentrations
2. **Monetary Mixtures**: Combining items with different values
3. **Ingredient Mixtures**: Combining substances in specific ratios

**General Strategy**:
1. Define variables clearly
2. Set up equation based on conservation principle:
   - Total = Part 1 + Part 2
   - Or: Concentration × Volume = Amount of pure substance
3. Solve equation
4. Check answer makes sense

**Example (Solution Mixture)**: Mix 20% acid solution with 50% acid solution to get 30 L of 35% acid

**Solution**:
```
Let x = liters of 20% solution
Then 30 − x = liters of 50% solution

Equation (amount of pure acid):
0.20x + 0.50(30 − x) = 0.35(30)
0.20x + 15 − 0.50x = 10.5
−0.30x = −4.5
x = 15

Answer: 15 L of 20% solution, 15 L of 50% solution
```

**Common Errors**:
1. ❌ **Mixing Percentages Incorrectly**: Adding percentages directly
   - **Prevention**: Convert to decimals, multiply by amounts
2. ❌ **Wrong Variable Definition**: Defining both amounts as separate variables without constraint
   - **Prevention**: If total is known, second amount = total − first amount
3. ❌ **Units Mismatch**: Mixing liters and milliliters, etc.
   - **Prevention**: Convert all to same units first

---

### 🚗 METHOD 2.5.5: DISTANCE-RATE-TIME PROBLEMS

**Fundamental Relationship**: $d = rt$ (distance = rate × time)

**Three Main Types**:
1. **Opposite Directions**: Objects moving apart
   - Total distance = d₁ + d₂

2. **Same Direction**: One object catching another
   - Distance equation based on meeting point

3. **Round Trip**: Going and returning
   - Total time = time going + time returning

**Procedure**:
1. Draw diagram of situation
2. Create table with d, r, t columns
3. Use d = rt to fill in table
4. Write equation based on problem condition
5. Solve and verify

**Example (Opposite Directions)**: Two cars leave from same point in opposite directions. One travels 60 mph, other 70 mph. When are they 325 miles apart?

**Solution**:
```
Let t = time in hours

Table:
         d        r    t
Car 1: 60t      60    t
Car 2: 70t      70    t

Equation (total distance = 325):
60t + 70t = 325
130t = 325
t = 2.5 hours
```

**Common Errors**:
1. ❌ **Using Wrong Distance Relationship**: Adding when should subtract, etc.
   - **Prevention**: Draw diagram to visualize
2. ❌ **Time Units Mismatch**: Mixing hours and minutes
   - **Prevention**: Convert all to same unit (usually hours)
3. ❌ **Not Using d = rt Correctly**: Solving for wrong variable
   - **Prevention**: Always write d = rt for each moving object

---

## 🔗 RELATIONAL FRAMEWORK: SECTION 2.5

### Vertical Integration (Prerequisites)

**From Section 2.4**:
- Linear equations → applied to real-world contexts
- Slope-intercept form → y = mx + b interpreted in context
- Solving linear equations → used in all application problems

**From Chapter 1**:
- Equation solving techniques → solving application equations
- Setting up equations from word problems

### Horizontal Integration (Cross-Connections)

**Within Mathematics**:
- Linear models → foundation for more complex models
- Rate of change → connects to calculus derivatives
- Optimization → leads to max/min problems (quadratic functions)

**To Real World**:
- Business: Cost analysis, break-even, profit maximization
- Science: Constant rate processes (radioactive decay at small scale)
- Social Science: Population trends, economic indicators

### Problem-Solving Strategy

**General Approach to Applications**:
1. **Read carefully** - What is being asked?
2. **Define variables** - Be specific with units
3. **Draw diagram** if applicable
4. **Find equation** - Based on relationships in problem
5. **Solve** - Use appropriate techniques
6. **Check** - Does answer make sense in context?
7. **State conclusion** - Answer original question with units

---

## 📋 SECTION 2.5 SUMMARY

### Model Interpretation
```
Linear Model: y = mx + b
  m (slope): Rate of change (with units per unit)
  b (y-intercept): Initial value when x = 0

Units for slope: (y units)/(x units)
```

### Business Formulas
```
Cost: C(x) = (variable cost)x + fixed cost
Revenue: R(x) = (price per unit)x  
Profit: P(x) = R(x) − C(x)
Break-even: Solve R(x) = C(x)
```

### Key Relationships
```
Direct Variation: y = kx
Distance-Rate-Time: d = rt
Mixture: Total = Part 1 + Part 2
```

---

## 🎯 SECTION 2.6: TRANSFORMATIONS OF GRAPHS

### 🔑 Core Concepts

#### Function Transformations
**Definition**: Systematic changes to a function's equation that produce predictable changes to its graph

**Why Important**: Allows us to graph complex functions by starting with basic "parent" functions and applying transformations

**Parent Functions** (basic functions we transform):
- $f(x) = x$ (identity/linear)
- $f(x) = x^2$ (quadratic)
- $f(x) = x^3$ (cubic)
- $f(x) = \sqrt{x}$ (square root)
- $f(x) = |x|$ (absolute value)
- $f(x) = \frac{1}{x}$ (reciprocal)

---

### 🔄 METHOD 2.6.1: VERTICAL SHIFTS

**Transformation**: $y = f(x) + k$

**Effect**:
- If k > 0: Shift graph UP k units
- If k < 0: Shift graph DOWN |k| units

**How to Apply**:
1. Start with parent function graph
2. Take every point (x, y) on original
3. Move to (x, y + k)

**Example**: Graph $y = x^2 + 3$

**Solution**:
```
Parent function: f(x) = x²
Transformation: Add 3

Effect: Shift parabola UP 3 units
Vertex moves from (0, 0) to (0, 3)
```

**Common Errors**:
1. ❌ **Shifting Wrong Direction**: Moving down when should go up
   - **Prevention**: + means UP, − means DOWN
2. ❌ **Confusing with Horizontal Shift**: Thinking about x-coordinates
   - **Prevention**: Adding to entire function affects y-values

---

### ↔️ METHOD 2.6.2: HORIZONTAL SHIFTS

**Transformation**: $y = f(x − h)$

**Effect**:
- If h > 0: Shift graph RIGHT h units
- If h < 0: Shift graph LEFT |h| units

**⚠️ CRITICAL**: The sign is OPPOSITE to intuition!
- $f(x − 2)$ shifts RIGHT 2 (even though there's a minus)
- $f(x + 3)$ shifts LEFT 3 (even though there's a plus)

**How to Apply**:
1. Start with parent function graph
2. Take every point (x, y) on original
3. Move to (x + h, y) for f(x − h)

**Example**: Graph $y = (x − 2)^2$

**Solution**:
```
Parent function: f(x) = x²
Transformation: Replace x with (x − 2)

Effect: Shift parabola RIGHT 2 units
Vertex moves from (0, 0) to (2, 0)
```

**Memory Aid**: "Do the opposite"
- f(x − 2) → move RIGHT 2
- f(x + 3) → move LEFT 3

**Common Errors**:
1. ❌ **Shifting Wrong Direction**: Most common error!
   - $f(x − 2)$ shifts RIGHT, not left
   - **Prevention**: "Do the opposite of the sign"
2. ❌ **Applying to y-coordinate**: Moving vertically instead of horizontally
   - **Prevention**: Change inside f( ) affects x; outside affects y

---

### ↕️ METHOD 2.6.3: VERTICAL STRETCH/COMPRESSION

**Transformation**: $y = af(x)$ where $a ≠ 0$

**Effect**:
- If |a| > 1: **Stretch** vertically by factor of |a|
- If 0 < |a| < 1: **Compress** vertically by factor of |a|
- If a < 0: Also **reflect** across x-axis

**How to Apply**:
1. Start with parent function graph
2. Multiply all y-coordinates by a
3. x-coordinates stay the same

**Example**: Graph $y = 3x^2$

**Solution**:
```
Parent function: f(x) = x²
Transformation: Multiply by 3

Effect: Vertical stretch by factor of 3
Point (1, 1) becomes (1, 3)
Point (2, 4) becomes (2, 12)
Parabola becomes "narrower"
```

**Common Errors**:
1. ❌ **Multiplying x-coordinates**: Changing both x and y
   - **Prevention**: Vertical transformation affects ONLY y-values
2. ❌ **Confusing Stretch/Compression**: Thinking 2 compresses
   - **Prevention**: a > 1 stretches (makes taller); 0 < a < 1 compresses

---

### ↔️ METHOD 2.6.4: HORIZONTAL STRETCH/COMPRESSION

**Transformation**: $y = f(bx)$ where $b ≠ 0$

**Effect**:
- If |b| > 1: **Compress** horizontally by factor of 1/|b|
- If 0 < |b| < 1: **Stretch** horizontally by factor of 1/|b|
- If b < 0: Also **reflect** across y-axis

**⚠️ CRITICAL**: Effect is INVERSE of what you might expect!
- f(2x) compresses by factor of 1/2 (not stretches)
- f(x/2) stretches by factor of 2 (not compresses)

**How to Apply**:
1. Start with parent function graph
2. Divide all x-coordinates by b
3. y-coordinates stay the same

**Example**: Graph $y = \sqrt{2x}$

**Solution**:
```
Parent function: f(x) = √x
Transformation: Replace x with 2x

Effect: Horizontal compression by factor of 1/2
Point (4, 2) becomes (2, 2)
Point (9, 3) becomes (4.5, 3)
```

**Common Errors**:
1. ❌ **Wrong Direction**: Thinking f(2x) stretches
   - **Prevention**: f(bx) with b > 1 COMPRESSES
2. ❌ **Not Taking Reciprocal**: Using b instead of 1/b
   - **Prevention**: Factor is 1/b for horizontal

---

### 🪞 METHOD 2.6.5: REFLECTIONS

**Reflection Across x-axis**: $y = −f(x)$
- Multiply all y-coordinates by −1
- Changes sign of function output
- "Flip upside down"

**Reflection Across y-axis**: $y = f(−x)$
- Multiply all x-coordinates by −1
- Replace x with −x in equation
- "Flip left-right"

**Example 1**: Graph $y = −x^2$

**Solution**:
```
Parent: f(x) = x² (parabola opening up)
Transformation: Negative sign in front

Effect: Reflection across x-axis
Parabola opens DOWN instead of up
Vertex still at (0, 0)
```

**Example 2**: Graph $y = \sqrt{−x}$

**Solution**:
```
Parent: f(x) = √x (starts at origin, goes right)
Transformation: Negative inside square root

Effect: Reflection across y-axis  
Graph starts at origin, goes LEFT
Domain changes to x ≤ 0
```

**Common Errors**:
1. ❌ **Confusing x-axis and y-axis Reflections**: Wrong direction
   - **Prevention**: Negative OUTSIDE → x-axis; INSIDE → y-axis
2. ❌ **Forgetting Domain Changes**: Not adjusting domain after reflection
   - **Prevention**: Check domain after reflecting functions with restrictions

---

### 🔗 METHOD 2.6.6: COMBINING TRANSFORMATIONS

**Order of Operations for Multiple Transformations**:

**Reading from equation** $y = a·f(b(x − h)) + k$:
1. **Horizontal shift**: by h
2. **Horizontal stretch/compress**: by factor 1/|b|
3. **Reflect across y-axis**: if b < 0
4. **Vertical stretch/compress**: by factor |a|
5. **Reflect across x-axis**: if a < 0
6. **Vertical shift**: by k

**Applying to graph**:
1. Start with parent function
2. Apply transformations IN ORDER listed above
3. Check key points after each transformation

**Example**: Graph $y = −2(x + 1)^2 − 3$

**Solution**:
```
Parent: f(x) = x²

Step-by-step:
1. f(x + 1): Shift LEFT 1 → vertex at (−1, 0)
2. 2f(x + 1): Vertical stretch by 2 → vertex at (−1, 0)
3. −2f(x + 1): Reflect across x-axis → vertex at (−1, 0), opens DOWN
4. −2f(x + 1) − 3: Shift DOWN 3 → vertex at (−1, −3)

Final: Parabola opening DOWN, vertex (−1, −3), stretched by factor 2
```

**Common Errors**:
1. ❌ **Wrong Order**: Applying transformations in wrong sequence
   - **Prevention**: Follow order: horizontal → vertical
2. ❌ **Forgetting Reflections**: Missing negative signs
   - **Prevention**: Check for negatives both inside and outside function

---

## 🔗 RELATIONAL FRAMEWORK: SECTION 2.6

### Vertical Integration (Prerequisites)

**From Section 2.3**:
- Function notation → needed to understand f(x + h), f(−x), etc.
- Domain → must track domain changes with transformations

**From Previous Math**:
- Basic function shapes → parent functions
- Coordinate geometry → plotting transformed points

### Horizontal Integration (Cross-Connections)

**Within Chapter 2**:
- Function transformations → applied to specific functions in 2.7
- Graph analysis → uses transformation concepts

**To Future Topics**:
- Transformations → used for trigonometric functions
- Transformations → used in calculus (shifting integrals)
- Parent functions → foundation for function families

---

## 📋 SECTION 2.6 SUMMARY

### Transformation Rules
```
Vertical Shift: f(x) + k
  k > 0: UP k units
  k < 0: DOWN |k| units

Horizontal Shift: f(x − h)  
  h > 0: RIGHT h units ⚠️ (opposite of sign)
  h < 0: LEFT |h| units ⚠️

Vertical Stretch/Compress: a·f(x)
  |a| > 1: Stretch by |a|
  0 < |a| < 1: Compress by |a|
  a < 0: Also reflect across x-axis

Horizontal Stretch/Compress: f(bx)
  |b| > 1: Compress by 1/|b| ⚠️ (reciprocal)
  0 < |b| < 1: Stretch by 1/|b| ⚠️
  b < 0: Also reflect across y-axis

Reflections:
  −f(x): Reflect across x-axis
  f(−x): Reflect across y-axis
```

### Key Insights
1. **Inside vs. Outside**: Changes inside f( ) affect x (horizontal); outside affects y (vertical)
2. **Opposite Signs**: Horizontal shifts do opposite of sign
3. **Reciprocals**: Horizontal stretch/compress uses reciprocal factor
4. **Order Matters**: Apply transformations in correct sequence

---

*Final sections 2.7-2.8 will complete the chapter...*



## 🎯 SECTION 2.7: ANALYZING GRAPHS OF FUNCTIONS AND PIECEWISE-DEFINED FUNCTIONS

### 🔑 Core Concepts

#### Analyzing Function Behavior from Graphs
**Key Features to Identify**:
1. **Domain**: All x values where function is defined
2. **Range**: All y values function produces
3. **Intercepts**: Where graph crosses axes
4. **Intervals of Increase/Decrease**: Where function goes up or down
5. **Maximum/Minimum Values**: Highest/lowest points
6. **Continuity**: Whether graph has breaks or jumps

---

### 📈 METHOD 2.7.1: DETERMINING INCREASING/DECREASING INTERVALS

**Definitions**:
- Function **increasing** on interval I if: for all $x_1 < x_2$ in I, we have $f(x_1) < f(x_2)$
  - As you move right, graph goes UP
  
- Function **decreasing** on interval I if: for all $x_1 < x_2$ in I, we have $f(x_1) > f(x_2)$
  - As you move right, graph goes DOWN
  
- Function **constant** on interval I if: for all x in I, f(x) = k for some constant k
  - Graph is horizontal

**Procedure from Graph**:
1. Scan graph from left to right
2. Mark points where direction changes
3. State intervals using interval notation
4. Use x-values for intervals (not y-values)

**Example**: Analyze function behavior

**Solution**:
```
Increasing: (−∞, −2) ∪ (1, 4)
  Graph goes UP on these intervals

Decreasing: (−2, 1) ∪ (4, ∞)
  Graph goes DOWN on these intervals

Constant: nowhere
  Graph never horizontal
```

**Common Errors**:
1. ❌ **Using y-coordinates**: Stating range instead of domain values
   - **Prevention**: Intervals are in terms of x (domain values)
2. ❌ **Including Endpoint When Shouldn't**: Using closed bracket at turning point
   - **Prevention**: Typically use open intervals for increasing/decreasing
3. ❌ **Confusing "Going Up" with "Positive"**: Thinking increasing means f(x) > 0
   - **Prevention**: Increasing means slope is positive, not y-value

---

### 🎯 METHOD 2.7.2: IDENTIFYING LOCAL AND ABSOLUTE EXTREMA

**Definitions**:
- **Local Maximum** at x = c: f(c) ≥ f(x) for all x near c
  - "Peak" in the graph
  - Function changes from increasing to decreasing
  
- **Local Minimum** at x = c: f(c) ≤ f(x) for all x near c
  - "Valley" in the graph
  - Function changes from decreasing to increasing
  
- **Absolute Maximum**: Largest value f takes over entire domain
- **Absolute Minimum**: Smallest value f takes over entire domain

**Procedure**:
1. Find local maxima (peaks)
2. Find local minima (valleys)
3. Check endpoints (if domain is closed interval)
4. Compare all values to find absolute extrema

**Example**: Given graph, identify extrema

**Solution**:
```
Local Maximum:
  At x = −1, f(−1) = 4 (peak)
  
Local Minimum:
  At x = 2, f(2) = −2 (valley)
  
Absolute Maximum:
  f(−1) = 4 (highest point on graph)
  
Absolute Minimum:
  None (graph extends down to −∞)
```

**Common Errors**:
1. ❌ **Confusing x-value with y-value**: Saying "maximum is x = 3"
   - **Prevention**: Maximum VALUE is f(c), occurs AT x = c
2. ❌ **Missing Absolute Extrema**: Not checking endpoints or considering full domain
   - **Prevention**: Check entire domain including boundaries

---

### 📐 METHOD 2.7.3: DETERMINING CONTINUITY

**Intuitive Definition**: Function is **continuous** if you can draw it without lifting your pencil

**Technical Definition**: Function f is continuous at x = c if:
1. f(c) is defined
2. $\lim_{x \to c} f(x)$ exists
3. $\lim_{x \to c} f(x) = f(c)$

**Discontinuity Types**:
1. **Point Discontinuity** (Hole): Open circle in graph
2. **Jump Discontinuity**: Graph "jumps" from one value to another
3. **Infinite Discontinuity**: Vertical asymptote

**Procedure**:
1. Check for holes (open circles)
2. Check for jumps (different left/right values)
3. Check for vertical asymptotes
4. Identify location (x-value) of any discontinuities

**Common Errors**:
1. ❌ **Confusing with Domain**: Thinking discontinuity means not in domain
   - **Prevention**: Function can have point in domain but still be discontinuous there

---

### 🔢 METHOD 2.7.4: PIECEWISE-DEFINED FUNCTIONS

**Definition**: Function defined by different expressions on different parts of domain

**General Form**:
$$f(x) = \begin{cases}
\text{expression}_1 & \text{if condition}_1 \\
\text{expression}_2 & \text{if condition}_2 \\
\vdots & \vdots \\
\text{expression}_n & \text{if condition}_n
\end{cases}$$

**When to Use**: When function behavior changes at specific x-values

---

### 📊 METHOD 2.7.5: EVALUATING PIECEWISE FUNCTIONS

**Procedure**:
1. Identify which piece to use based on x-value
2. Check which condition x satisfies
3. Use corresponding expression
4. Evaluate that expression at x

**Example**: Evaluate $f(x) = \begin{cases} x^2 & \text{if } x < 0 \\ 2x + 1 & \text{if } x \geq 0 \end{cases}$

Find: f(−3), f(0), f(2)

**Solution**:
```
f(−3): Since −3 < 0, use x²
  f(−3) = (−3)² = 9

f(0): Since 0 ≥ 0, use 2x + 1
  f(0) = 2(0) + 1 = 1

f(2): Since 2 ≥ 0, use 2x + 1
  f(2) = 2(2) + 1 = 5
```

**Common Errors**:
1. ❌ **Using Wrong Piece**: Not checking which condition x satisfies
   - **Prevention**: Always verify which inequality x satisfies
2. ❌ **Confusion at Boundary**: When x equals boundary value
   - **Prevention**: Check carefully whether inequality uses < or ≤

---

### 📈 METHOD 2.7.6: GRAPHING PIECEWISE FUNCTIONS

**Procedure**:
1. Graph each piece separately on its domain
2. Use open circles for excluded endpoints
3. Use closed circles for included endpoints
4. Check continuity at boundaries
5. Label each piece

**Example**: Graph $f(x) = \begin{cases} −x + 2 & \text{if } x \leq 1 \\ x^2 & \text{if } x > 1 \end{cases}$

**Solution**:
```
Piece 1: y = −x + 2 for x ≤ 1
  Line with slope −1, y-intercept 2
  At x = 1: f(1) = −1 + 2 = 1
  Use CLOSED circle at (1, 1)
  
Piece 2: y = x² for x > 1
  Parabola starting after x = 1
  At x = 1: Would be 1² = 1
  Use OPEN circle at (1, 1)
  
Continuity: Function is discontinuous at x = 1
  (left side reaches (1, 1), right side starts just after)
```

**Common Errors**:
1. ❌ **Wrong Circle Type**: Closed when should be open, or vice versa
   - **Prevention**: ≤ or ≥ → closed circle; < or > → open circle
2. ❌ **Extending Pieces Too Far**: Graphing piece outside its domain
   - **Prevention**: Pay attention to inequality boundaries
3. ❌ **Missing Discontinuities**: Not showing jumps or holes
   - **Prevention**: Carefully check values at boundaries

---

### 🎯 METHOD 2.7.7: ABSOLUTE VALUE AS PIECEWISE FUNCTION

**Key Insight**: Absolute value can be written piecewise:
$$|x| = \begin{cases} x & \text{if } x \geq 0 \\ −x & \text{if } x < 0 \end{cases}$$

**General Form**: $|ax + b|$ can be rewritten as piecewise function
1. Find where expression equals zero: solve ax + b = 0
2. Split domain at that point
3. Use (ax + b) when expression is positive
4. Use −(ax + b) when expression is negative

**Example**: Write $|x − 2|$ as piecewise function

**Solution**:
```
Find split point: x − 2 = 0 → x = 2

For x ≥ 2: (x − 2) is positive, so |x − 2| = x − 2
For x < 2: (x − 2) is negative, so |x − 2| = −(x − 2) = −x + 2

Piecewise form:
|x − 2| = {  x − 2    if x ≥ 2
          { −x + 2    if x < 2
```

**Common Errors**:
1. ❌ **Wrong Split Point**: Not solving correctly for where expression = 0
   - **Prevention**: Carefully solve ax + b = 0
2. ❌ **Wrong Sign in Second Piece**: Forgetting to distribute negative
   - **Prevention**: −(x − 2) = −x + 2 (change both signs)

---

## 🔗 RELATIONAL FRAMEWORK: SECTION 2.7

### Vertical Integration (Prerequisites)

**From Section 2.3**:
- Domain and range → analyzed graphically here
- Function notation → used throughout analysis

**From Section 2.6**:
- Graph transformations → create interesting graphs to analyze
- Parent functions → basis for piecewise pieces

### Horizontal Integration (Cross-Connections)

**Within Mathematics**:
- Increasing/decreasing → relates to derivatives (calculus)
- Extrema → optimization problems
- Piecewise functions → model real-world situations with different rules

**Real-World Applications**:
- **Tax brackets**: Piecewise linear functions
- **Shipping costs**: Step functions (piecewise constant)
- **Overtime pay**: Different rates for different hours

---

## 📋 SECTION 2.7 SUMMARY

### Graph Analysis Checklist
```
✓ Domain and Range
✓ Intercepts (x and y)
✓ Increasing/Decreasing intervals
✓ Local and absolute extrema
✓ Continuity/Discontinuities
```

### Piecewise Functions
```
Format:
f(x) = { expression₁  if condition₁
       { expression₂  if condition₂

Evaluation: Check which condition x satisfies

Graphing:
  • Closed circle (•) for ≤ or ≥
  • Open circle (○) for < or >
  • Check continuity at boundaries
```

---

## 🎯 SECTION 2.8: ALGEBRA OF FUNCTIONS AND FUNCTION COMPOSITION

### 🔑 Core Concepts

#### Operations on Functions
Just as we add, subtract, multiply, and divide numbers, we can perform these operations on functions

**Key Idea**: Operations are performed on the **outputs** (y-values) of functions

---

### ➕ METHOD 2.8.1: SUM AND DIFFERENCE OF FUNCTIONS

**Definitions**:
- **Sum**: $(f + g)(x) = f(x) + g(x)$
- **Difference**: $(f − g)(x) = f(x) − g(x)$

**Domain**: Intersection of domains of f and g
- Domain of (f ± g) = (Domain of f) ∩ (Domain of g)

**Procedure**:
1. Evaluate f(x)
2. Evaluate g(x)
3. Add or subtract the results
4. Determine domain (intersection)

**Example**: Given $f(x) = x^2$ and $g(x) = 2x + 1$

**Solution**:
```
(f + g)(x) = f(x) + g(x)
           = x² + (2x + 1)
           = x² + 2x + 1

(f − g)(x) = f(x) − g(x)
           = x² − (2x + 1)
           = x² − 2x − 1

Domain: Both f and g have domain ℝ
Domain of f ± g: ℝ
```

**Common Errors**:
1. ❌ **Forgetting Parentheses**: Not distributing negative in subtraction
   - **Prevention**: $(f − g)(x) = f(x) − [g(x)]$ (parentheses around g(x))

---

### ✖️ METHOD 2.8.2: PRODUCT AND QUOTIENT OF FUNCTIONS

**Definitions**:
- **Product**: $(f · g)(x) = f(x) · g(x)$
- **Quotient**: $\left(\frac{f}{g}\right)(x) = \frac{f(x)}{g(x)}$ where $g(x) ≠ 0$

**Domain**:
- Product: Domain of (f · g) = (Domain of f) ∩ (Domain of g)
- Quotient: Domain of (f/g) = (Domain of f) ∩ (Domain of g) AND g(x) ≠ 0

**Procedure**:
1. Evaluate f(x)
2. Evaluate g(x)
3. Multiply or divide
4. Simplify if possible
5. For quotient: exclude values where g(x) = 0

**Example**: Given $f(x) = x − 3$ and $g(x) = x^2 − 9$

**Solution**:
```
(f · g)(x) = (x − 3)(x² − 9)
           = (x − 3)(x − 3)(x + 3)
           = (x − 3)²(x + 3)
Domain: ℝ

(f/g)(x) = (x − 3)/(x² − 9)
         = (x − 3)/[(x − 3)(x + 3)]
         = 1/(x + 3)  for x ≠ 3

Domain: ℝ except x = 3 and x = −3
(g(x) = 0 at these values)
```

**Common Errors**:
1. ❌ **Forgetting to Exclude Zeros of Denominator**: Not finding where g(x) = 0
   - **Prevention**: Always solve g(x) = 0 for quotient domain
2. ❌ **Canceling Before Considering Domain**: Simplifying then stating wrong domain
   - **Prevention**: Find domain BEFORE simplifying, then simplify

---

### 🔗 METHOD 2.8.3: FUNCTION COMPOSITION

**Definition**: **Composition** of functions f and g:
$$(f \circ g)(x) = f(g(x))$$

Read as "f composed with g" or "f of g of x"

**Process**:
1. Evaluate inner function g at x
2. Take that output and use as input to f
3. Result is f(g(x))

**Key Insight**: Composition is "function of a function"

**Example 1**: Given $f(x) = 2x + 1$ and $g(x) = x^2$
Find $(f \circ g)(x)$ and $(g \circ f)(x)$

**Solution**:
```
(f ∘ g)(x) = f(g(x))
           = f(x²)
           = 2(x²) + 1
           = 2x² + 1

(g ∘ f)(x) = g(f(x))
           = g(2x + 1)
           = (2x + 1)²
           = 4x² + 4x + 1

Note: f ∘ g ≠ g ∘ f (composition is NOT commutative)
```

**Domain of Composition**:
Domain of $(f \circ g)$ consists of all x in domain of g such that g(x) is in domain of f

**Procedure for Finding Domain**:
1. Find domain of g
2. Find domain of f
3. Determine which x values in domain of g produce g(x) values in domain of f
4. Domain of composition = those x values

**Example 2**: Find domain of $(f \circ g)(x)$ where $f(x) = \sqrt{x}$ and $g(x) = x − 4$

**Solution**:
```
Domain of g: ℝ (all real numbers)
Domain of f: x ≥ 0 (need non-negative input)

For f(g(x)) to be defined:
  g(x) must be ≥ 0
  x − 4 ≥ 0
  x ≥ 4

Domain of (f ∘ g): [4, ∞)
```

**Common Errors**:
1. ❌ **Thinking Composition is Commutative**: $(f \circ g) = (g \circ f)$
   - **Prevention**: Order matters! $(f \circ g) ≠ (g \circ f)$ in general
2. ❌ **Wrong Domain**: Using domain of f instead of analyzing g(x)
   - **Prevention**: Domain depends on both functions and their interaction
3. ❌ **Confusing with Multiplication**: Thinking $(f \circ g)(x) = f(x) · g(x)$
   - **Prevention**: $(f \circ g)(x) = f(g(x))$ is substitution, not multiplication

---

### 🔍 METHOD 2.8.4: DECOMPOSING FUNCTIONS

**Purpose**: Express a complicated function as a composition of simpler functions

**Strategy**: Look for "function inside a function"

**Procedure**:
1. Identify the inner operation (what happens first)
2. Identify the outer operation (what happens to result)
3. Define g(x) as inner operation
4. Define f(x) as outer operation
5. Verify: $f(g(x))$ equals original function

**Example**: Decompose $h(x) = (2x + 5)^3$

**Solution**:
```
Inner operation: 2x + 5
Outer operation: cubing

Define: g(x) = 2x + 5
Define: f(x) = x³

Verify: f(g(x)) = f(2x + 5) = (2x + 5)³ = h(x) ✓

Answer: h = f ∘ g where f(x) = x³ and g(x) = 2x + 5
```

**Note**: Decomposition is not unique (multiple valid answers possible)

**Common Errors**:
1. ❌ **Wrong Order**: Making g the outer function and f the inner
   - **Prevention**: Inner function is g, outer is f in $(f \circ g)$
2. ❌ **Not Verifying**: Not checking that $f(g(x))$ equals original
   - **Prevention**: Always verify your decomposition works

---

## 🔗 RELATIONAL FRAMEWORK: SECTION 2.8

### Vertical Integration (Prerequisites)

**From Section 2.3**:
- Function notation → essential for operations
- Function evaluation → used throughout section
- Domain analysis → needed for operation domains

**From Chapter 1**:
- Algebraic operations → applied to functions
- Factoring → used in simplifying function operations

### Horizontal Integration (Cross-Connections)

**Within Mathematics**:
- Function composition → foundation for chain rule (calculus)
- Inverse functions → related to composition (f ∘ f⁻¹ = identity)
- Transformations → can be viewed as compositions

**Real-World Applications**:
- **Supply Chain**: Sequential processing (composition)
- **Currency Conversion**: Multiple conversion rates (composition)
- **Temperature Scales**: Converting between Celsius/Fahrenheit (composition)

---

## 📋 SECTION 2.8 SUMMARY

### Function Operations
```
Sum: (f + g)(x) = f(x) + g(x)
Difference: (f − g)(x) = f(x) − g(x)
Product: (f · g)(x) = f(x) · g(x)
Quotient: (f/g)(x) = f(x)/g(x), g(x) ≠ 0

Domain: Intersection of individual domains
        (Plus g(x) ≠ 0 for quotient)
```

### Function Composition
```
Definition: (f ∘ g)(x) = f(g(x))
Process: Evaluate g first, then f

Properties:
  • Order matters: f ∘ g ≠ g ∘ f (generally)
  • Associative: f ∘ (g ∘ h) = (f ∘ g) ∘ h
  • Domain: Requires analysis of both functions

Decomposition: Breaking h(x) into f(g(x))
  Inner function = g(x)
  Outer function = f(x)
```

---

## 🎊 CHAPTER 2 COMPLETE: MASTERY CHECKLIST

### Level 1: Recognition (Can you identify?)
- [ ] Rectangular coordinate system components
- [ ] Standard forms of circle equations
- [ ] Functions vs. relations
- [ ] Domain and range from graphs
- [ ] Slope types (positive, negative, zero, undefined)
- [ ] Forms of linear equations
- [ ] Parent function shapes
- [ ] Types of transformations

### Level 2: Comprehension (Do you understand?)
- [ ] Why distance formula comes from Pythagorean theorem
- [ ] Why vertical line test determines functions
- [ ] Why f(x + h) ≠ f(x) + f(h)
- [ ] Why perpendicular slopes are negative reciprocals
- [ ] Why horizontal shift appears opposite to sign
- [ ] How piecewise functions model different rules
- [ ] Why composition order matters

### Level 3: Application (Can you use?)
- [ ] Plot points and find distances/midpoints
- [ ] Write circle equations (various conditions)
- [ ] Determine if relation is function
- [ ] Evaluate functions (including composition)
- [ ] Find domains with restrictions
- [ ] Write linear equations from various information
- [ ] Apply transformations to parent functions
- [ ] Graph piecewise functions
- [ ] Perform function operations

### Level 4: Analysis (Can you explain?)
- [ ] Analyze function behavior from graph
- [ ] Determine increasing/decreasing intervals
- [ ] Identify extrema and continuity
- [ ] Interpret slope and intercepts in context
- [ ] Compare parallel vs. perpendicular lines
- [ ] Predict effects of multiple transformations
- [ ] Analyze domains of composite functions

### Level 5: Synthesis (Can you create/combine?)
- [ ] Solve real-world problems with linear models
- [ ] Model situations with piecewise functions
- [ ] Decompose complex functions
- [ ] Combine multiple transformations systematically
- [ ] Create function models from data
- [ ] Solve application problems requiring multiple concepts

---

## 🔄 CHAPTER 2: COMPREHENSIVE RELATIONAL FRAMEWORK

### Vertical Knowledge Chains

**Foundation → Application**:
```
Coordinate System (2.1)
    ↓
Circles (2.2) — Uses distance formula
    ↓
Functions (2.3) — Circles fail vertical line test
    ↓
Linear Functions (2.4) — Simplest functions
    ↓
Applications (2.5) — Linear models in real world
    ↓
Transformations (2.6) — Modifying function graphs
    ↓
Analysis (2.7) — Understanding behavior
    ↓
Composition (2.8) — Combining functions
```

### Horizontal Connections Within Chapter 2

**Graphing Thread**:
- 2.1: Plotting points → 2.2: Graphing circles → 2.4: Graphing lines → 2.6: Transforming graphs → 2.7: Analyzing graphs

**Function Thread**:
- 2.3: Definition of functions → 2.4: Linear functions → 2.6: Transformed functions → 2.7: Piecewise functions → 2.8: Function operations

**Domain/Range Thread**:
- 2.3: Basic domain/range → 2.4: Linear function domain → 2.7: Reading from graphs → 2.8: Composition domains

**Application Thread**:
- 2.1: Distance/midpoint → 2.2: Circle applications → 2.4: Slope interpretation → 2.5: Real-world modeling

### Cross-Chapter Integration

**From Chapter R**:
- Real number system → coordinates on axes
- Absolute value → distance, piecewise functions
- Radicals → distance formula, domain restrictions
- Exponent rules → not directly used, but algebraic foundation

**From Chapter 1**:
- Equation solving → finding intercepts, intersections
- Quadratic formula → may appear in domain analysis
- Completing square → converting circle equations

**To Chapter 3** (Polynomial and Rational Functions):
- Function concepts → applied to polynomials
- Domain analysis → essential for rational functions
- Transformations → applied to higher-degree functions
- Composition → creating rational functions

**To Future Calculus**:
- Functions → extended to limits, continuity
- Slope → becomes derivative
- Average rate of change → becomes instantaneous rate
- Composition → chain rule
- Transformations → integration techniques

---

## 📚 CHAPTER 2 SUMMARY: KEY TAKEAWAYS

### The Big Picture
**Chapter 2 is about RELATIONSHIPS**:
- How do two variables relate to each other?
- When does a relationship qualify as a function?
- How do we represent, analyze, and use these relationships?

### Essential Skills Acquired
1. **Coordinate Geometry**: Plotting, distance, midpoint, circles
2. **Function Fundamentals**: Definition, notation, evaluation, domain/range
3. **Linear Functions**: Equations, slopes, graphing, applications
4. **Function Transformations**: Shifts, stretches, reflections
5. **Function Analysis**: Behavior, extrema, piecewise functions
6. **Function Algebra**: Operations and composition

### Why This Chapter Matters
- **Foundation**: Functions are THE central concept in mathematics
- **Applications**: Modeling real-world relationships
- **Preparation**: Essential for all future math courses
- **Thinking**: Develops analytical and abstract reasoning

### Key Insights
1. **Functions are ubiquitous**: Most mathematical relationships are functions
2. **Visual and algebraic views**: Graphs and equations complement each other
3. **Building complexity**: Start with simple (linear), build to complex
4. **Transformations are powerful**: Modify known graphs systematically
5. **Context matters**: Same math, different interpretations in applications

---

## 🎯 COMMON PITFALLS ACROSS CHAPTER 2

### Top 10 Mistakes to Avoid

1. **Coordinate Confusion** (2.1)
   - ❌ Plotting (y, x) instead of (x, y)
   - ✓ First coordinate is ALWAYS x (horizontal)

2. **Function Test Failure** (2.3)
   - ❌ Thinking all relations are functions
   - ✓ Use vertical line test

3. **Notation Misunderstanding** (2.3)
   - ❌ Thinking f(x + h) = f(x) + f(h)
   - ✓ Substitute entire expression (x + h) for x

4. **Domain Neglect** (2.3, 2.8)
   - ❌ Forgetting to find domain restrictions
   - ✓ Check denominators and even roots

5. **Slope Direction** (2.4)
   - ❌ Confusing positive/negative with horizontal/vertical
   - ✓ Positive = rising; negative = falling

6. **Horizontal Shift** (2.6)
   - ❌ Shifting f(x − 2) to the LEFT
   - ✓ f(x − 2) shifts RIGHT (opposite of sign!)

7. **Stretch/Compress** (2.6)
   - ❌ Thinking 2f(x) compresses
   - ✓ |a| > 1 stretches; 0 < |a| < 1 compresses

8. **Piecewise Boundaries** (2.7)
   - ❌ Wrong circle type (open vs. closed)
   - ✓ ≤ or ≥ gets closed circle; < or > gets open

9. **Composition Order** (2.8)
   - ❌ Thinking (f ∘ g) = (g ∘ f)
   - ✓ Order matters! Usually not equal

10. **Operation Domains** (2.8)
    - ❌ Forgetting to exclude zeros for quotient
    - ✓ Find where denominator = 0 and exclude

---

## 📖 CHAPTER 2 VOCABULARY INDEX

**Core Terms (Must Know)**:
- Relation, Domain, Range, Function
- Ordered Pair, Coordinate, Quadrant
- x-intercept, y-intercept
- Slope, Rate of Change
- Standard Form, Slope-Intercept Form, Point-Slope Form
- Transformation, Translation, Reflection, Dilation
- Increasing, Decreasing, Extrema
- Continuous, Discontinuous
- Piecewise Function
- Composition

**See**: [[02_Concepts/Vocabulary_Guide]] for complete definitions

---

## 🔗 CONNECTIONS TO CONCEPT LIBRARY

**Concepts Needing Atomic Nodes** (Priority for extraction):
1. [ ] [[Functions]] - Core definition
2. [ ] [[Domain_and_Range]] - Essential property
3. [ ] [[Slope]] - Rate of change concept
4. [ ] [[Linear_Functions]] - Simplest function family
5. [ ] [[Function_Composition]] - Combining functions
6. [ ] [[Function_Transformations]] - Systematic modifications
7. [ ] [[Piecewise_Functions]] - Multi-rule functions
8. [ ] [[Continuity]] - Smoothness property
9. [ ] [[Parallel_and_Perpendicular_Lines]] - Geometric relationships
10. [ ] [[Average_Rate_of_Change]] - Precursor to derivative

---

**Document Status**: Chapter 2 Extraction COMPLETE ✅
**Created**: 2025-10-20
**Extraction Method**: Universal Knowledge Framework
**Total Sections**: 8 complete
**Total Methods**: 40+ comprehensive procedures documented
**Estimated Lines**: ~4,500 lines
**Quality**: Comprehensive with examples, errors, and cross-references

---

*End of Chapter 2: Functions and Relations*

