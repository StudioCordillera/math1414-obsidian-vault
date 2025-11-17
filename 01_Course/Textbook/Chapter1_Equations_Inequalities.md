# Chapter 1: Equations and Inequalities - Method Extractions
**Source**: College Algebra & Trigonometry 2nd Edition - Miller/Gerken  
**Chapter**: 1 (Pages 85-180)
**Target**: Solving equations and inequalities systematically  
**Tags**: #textbook #extraction #equations #inequalities #chapter1

---

## 📚 EXTRACTION METHODOLOGY

Following the Universal Knowledge Framework approach, this document extracts:
1. **Explicit Knowledge**: Stated definitions, formulas, procedures
2. **Implicit Knowledge**: Assumed prerequisites, unstated steps
3. **Common Errors**: What NOT to do
4. **Relational Connections**: How concepts relate across mathematics

---

## 📐 SECTION 1.1: LINEAR EQUATIONS AND RATIONAL EQUATIONS

### Core Concept: Equation as Balance

**Definition**: An equation is a statement that two expressions are equal.
- **Solution/Root**: Value(s) that make the equation true
- **Solution Set**: Collection of all solutions

**Key Principle**: Whatever you do to one side, do to the other (maintaining equality)

---

### Method 1: Solving Linear Equations

**[[Linear_Equations|Linear Equation]] in One Variable**: ax + b = 0, where a ≠ 0

**Standard Solution Process**:
```
1. Clear fractions/decimals (multiply by LCD if needed)
2. Clear parentheses (distribute)
3. Combine like terms on each side
4. Collect variable terms on one side, constants on other
5. Isolate variable
6. Check solution in original equation
```

#### Example Pattern

**Solve**: 2(3x - 4) + 5 = 3x - (x - 1)

```
Step 1: Distribute
     6x - 8 + 5 = 3x - x + 1

Step 2: Combine like terms on each side
     6x - 3 = 2x + 1

Step 3: Collect variable terms (subtract 2x from both sides)
     4x - 3 = 1

Step 4: Isolate variable (add 3 to both sides)
     4x = 4

Step 5: Solve (divide by 4)
     x = 1

Step 6: Check in original equation
     2(3(1) - 4) + 5 = 3(1) - (1 - 1)
     2(-1) + 5 = 3 - 0
     3 = 3 ✓
```

#### 🧠 Implicit Knowledge Required
- **Equality Properties**: Foundation from Chapter R
  - Addition Property: If a = b, then a + c = b + c
  - Multiplication Property: If a = b, then ac = bc (c ≠ 0)
- **Reciprocal principle**: Dividing by a is same as multiplying by 1/a
- **Distribution awareness**: -(x - 3) = -x + 3
- **Order of operations** still applies when simplifying

#### ⚠️ Common Errors
- Not distributing negative signs: -(2x - 5) ≠ -2x - 5
- Dividing only one term: (2x + 4)/2 ≠ x + 4
- Not checking solution (may reveal errors)
- Losing track of signs when combining terms

---

### Method 2: Conditional Equations, Identities, and Contradictions

**Three Equation Types**:

**1. Conditional Equation**: True for specific value(s)
```
Example: 2x + 3 = 7
Solution: x = 2 (true only when x = 2)
```

**2. Identity**: True for all values in domain
```
Example: 2(x + 3) = 2x + 6
Solution: All real numbers
Recognition: Variables cancel, true statement remains (0 = 0)
```

**3. Contradiction**: No solution
```
Example: x + 3 = x + 5
Solution: ∅ (empty set) or "no solution"
Recognition: Variables cancel, false statement remains (3 = 5)
```

#### 🧠 Implicit Knowledge Required
- Identity means the equation is always true (infinitely many solutions)
- Contradiction means the equation can never be true
- When all variables cancel:
  - If result is true (like 2 = 2), it's an identity
  - If result is false (like 2 = 5), it's a contradiction

---

### Method 3: Solving Rational Equations

**[[Rational_Equations|Rational Equation]]**: Contains rational expressions (fractions with polynomials)

**Key Strategy**: Clear fractions by multiplying by LCD of all denominators

**Critical Process**:
```
1. Factor all denominators
2. Identify LCD
3. Note restrictions (values making any denominator = 0)
4. Multiply ENTIRE equation by LCD
5. Solve resulting equation
6. CHECK solutions against restrictions (crucial!)
```

#### Example Pattern

**Solve**: 3/(x-2) + 4/(x+1) = 2

```
Step 1: Factor denominators (already factored)
     Denominators: (x-2), (x+1)

Step 2: Find LCD
     LCD = (x-2)(x+1)

Step 3: Note restrictions
     x ≠ 2, x ≠ -1

Step 4: Multiply entire equation by LCD
     (x-2)(x+1)[3/(x-2) + 4/(x+1)] = (x-2)(x+1)(2)
     3(x+1) + 4(x-2) = 2(x-2)(x+1)

Step 5: Solve
     3x + 3 + 4x - 8 = 2(x² - x - 2)
     7x - 5 = 2x² - 2x - 4
     0 = 2x² - 9x + 1
     
     Using quadratic formula:
     x = (9 ± √(81-8))/4 = (9 ± √73)/4

Step 6: Check restrictions
     Both solutions valid (neither is 2 or -1)
```

#### 🧠 Implicit Knowledge Required
- **[[Extraneous_Solutions|Extraneous solutions]]**: Values that satisfy transformed equation but not original
- Always arise when:
  - Multiplying by variable expression
  - Squaring both sides
  - Any operation that might introduce false solutions
- **Domain restrictions** come from ORIGINAL equation denominators
- Checking is mandatory, not optional

#### ⚠️ Common Errors
- Forgetting to check solutions against restrictions
- Not finding LCD correctly
- Losing solutions when simplifying
- Canceling terms instead of factors

---

### Method 4: Literal Equations (Solving for a Variable)

**Literal Equation**: Equation with multiple variables; solve for one in terms of others

**Applications**: 
- Physics formulas
- Geometric formulas  
- Financial formulas

**Strategy**: Treat target variable as "the variable" and all others as constants

#### Example Pattern

**Solve for h**: A = ½bh

```
Method: Isolate h
     A = ½bh
     2A = bh          (multiply both sides by 2)
     2A/b = h         (divide both sides by b)
     h = 2A/b
```

**Solve for r**: A = P(1 + rt)

```
Method: Isolate r
     A = P(1 + rt)
     A = P + Prt      (distribute)
     A - P = Prt      (subtract P)
     (A - P)/(Pt) = r (divide by Pt)
     r = (A - P)/(Pt)
```

#### 🧠 Implicit Knowledge Required
- Work backwards from final form
- Use same properties as numerical equations
- May need to factor out target variable
- Result may contain other variables (that's okay!)

---

## 📐 SECTION 1.2: APPLICATIONS WITH LINEAR AND RATIONAL EQUATIONS

### Core Concept: Mathematical Modeling

**Problem-Solving Strategy**:
```
1. Read problem completely
2. Identify what you're looking for (assign variable)
3. Write known information and relationships
4. Translate words to equation
5. Solve equation
6. Check answer in context of problem
7. State answer with appropriate units
```

---

### Method 1: Translating Word Problems

**Common Translation Patterns**:

| Phrase | Mathematical Expression |
|--------|------------------------|
| "sum of a and b" | a + b |
| "difference of a and b" | a - b |
| "product of a and b" | a · b or ab |
| "quotient of a and b" | a/b |
| "a more than b" | b + a |
| "a less than b" | b - a |
| "a increased by b" | a + b |
| "a decreased by b" | a - b |
| "a is b% of c" | a = (b/100)c |
| "twice a" | 2a |
| "half of a" | a/2 or ½a |

#### 🧠 Implicit Knowledge Required
- "More than" and "less than" reverse order: "5 less than x" = x - 5, not 5 - x
- "Of" often means multiply in percentage problems
- "Is" often translates to equals sign
- Consecutive integers: n, n+1, n+2, ...
- Consecutive even/odd integers: n, n+2, n+4, ... (skip by 2)

---

### Method 2: Mixture Problems

**Types**:
1. Solution mixtures (concentrations)
2. Monetary mixtures (coins, investments)
3. Ingredient mixtures

**Key Principle**: 
```
Amount of substance = (Concentration/Value) × Total amount
```

#### Example Pattern: Solution Mixture

**Problem**: How many liters of 20% acid solution must be mixed with 5 L of 50% acid solution to obtain 30% acid solution?

```
Step 1: Identify variable
     Let x = liters of 20% solution needed

Step 2: Set up equation (amount of acid equals)
     Acid from 20% + Acid from 50% = Acid in mixture
     0.20x + 0.50(5) = 0.30(x + 5)

Step 3: Solve
     0.20x + 2.5 = 0.30x + 1.5
     2.5 - 1.5 = 0.30x - 0.20x
     1 = 0.10x
     x = 10

Step 4: Check context
     10 L of 20% solution makes sense
     Total: 10 + 5 = 15 L
     Acid: 0.20(10) + 0.50(5) = 2 + 2.5 = 4.5 L
     Percentage: 4.5/15 = 0.30 = 30% ✓

Answer: 10 liters
```

#### 🧠 Implicit Knowledge Required
- Convert percentages to decimals for calculation
- Total amount = sum of individual amounts
- Amount of pure substance = rate × total
- Units must be consistent throughout

---

### Method 3: Distance-Rate-Time Problems

**Fundamental Relationship**:
```
Distance = Rate × Time
d = rt

Derived forms:
r = d/t
t = d/r
```

**Problem Types**:
1. **Opposite directions** (moving apart)
2. **Same direction** (catching up)
3. **Round trip**

#### Example Pattern: Opposite Directions

**Problem**: Two trains leave a station at the same time going opposite directions. One travels at 60 mph, the other at 80 mph. How long until they are 350 miles apart?

```
Step 1: Identify variable
     Let t = time (hours) until 350 miles apart

Step 2: Set up equation
     Train 1 distance + Train 2 distance = Total separation
     60t + 80t = 350

Step 3: Solve
     140t = 350
     t = 2.5

Answer: 2.5 hours (or 2 hours 30 minutes)
```

#### 🧠 Implicit Knowledge Required
- Same time for both when they start together
- Opposite directions: distances add
- Same direction: distances subtract (for catching up)
- Units must match (convert minutes to hours if needed)

---

### Method 4: Work Problems

**Fundamental Relationship**:
```
Work rate = 1/(time to complete alone)

Combined work: Rate₁ + Rate₂ = Combined rate
```

#### Example Pattern

**Problem**: Pipe A fills a pool in 4 hours. Pipe B fills it in 6 hours. How long to fill together?

```
Step 1: Find individual rates
     Pipe A rate = 1/4 pool per hour
     Pipe B rate = 1/6 pool per hour

Step 2: Set up equation
     Let t = time to fill together
     (1/4)t + (1/6)t = 1 pool

Step 3: Solve
     LCD = 12
     3t + 2t = 12
     5t = 12
     t = 12/5 = 2.4 hours

Answer: 2.4 hours (or 2 hours 24 minutes)
```

#### 🧠 Implicit Knowledge Required
- Total work = 1 (one complete job)
- When working together, rates add
- When working against each other (filling/draining), rates subtract
- Result should be less time than fastest worker alone

---

## 📐 SECTION 1.3: COMPLEX NUMBERS

### Core Concept: Extending the Number System

**Motivation**: √(-1) has no real solution, but we need it!

**Imaginary Unit**: i = √(-1)

> See [[Complex_Numbers]] for full theory and properties.
```
Key property: i² = -1
Powers of i cycle:
i¹ = i
i² = -1
i³ = -i
i⁴ = 1
i⁵ = i (cycle repeats)
```

**Complex Number**: a + bi where a, b ∈ ℝ
- **Real part**: a
- **Imaginary part**: b (not bi!)
- **Pure imaginary**: a = 0 (form: bi)
- **Real number**: b = 0 (form: a)

---

### Method 1: Powers of i

**Strategy**: Reduce exponent modulo 4

**Pattern**:
```
i⁴ⁿ = 1
i⁴ⁿ⁺¹ = i  
i⁴ⁿ⁺² = -1
i⁴ⁿ⁺³ = -i
```

#### Example Pattern

**Simplify**: i⁴⁷

```
Step 1: Divide exponent by 4
     47 ÷ 4 = 11 remainder 3

Step 2: Apply pattern
     i⁴⁷ = i⁴⁽¹¹⁾⁺³ = (i⁴)¹¹ · i³ = 1¹¹ · i³ = i³ = -i
```

#### 🧠 Implicit Knowledge Required
- Powers of i repeat every 4
- Use remainder when dividing exponent by 4
- i⁴ = (i²)² = (-1)² = 1

---

### Method 2: Operations with Complex Numbers

**Addition/Subtraction**: Combine real parts and imaginary parts separately

```
(a + bi) + (c + di) = (a + c) + (b + d)i
(a + bi) - (c + di) = (a - c) + (b - d)i
```

**Multiplication**: Use FOIL, then simplify using i² = -1

```
(a + bi)(c + di) = ac + adi + bci + bdi²
                 = ac + adi + bci - bd
                 = (ac - bd) + (ad + bc)i
```

#### Example Pattern

**(3 + 2i)(1 - 4i)**
```
F: 3(1) = 3
O: 3(-4i) = -12i
I: 2i(1) = 2i
L: 2i(-4i) = -8i² = -8(-1) = 8

= 3 - 12i + 2i + 8
= 11 - 10i
```

#### 🧠 Implicit Knowledge Required
- Treat i like a variable when using FOIL
- Replace i² with -1 whenever it appears
- Combine like terms (real with real, imaginary with imaginary)
- Final answer in standard form a + bi

---

### Method 3: Complex Conjugates and Division

**[[Complex_Conjugate|Complex Conjugate]]**: Change sign of imaginary part
```
Conjugate of (a + bi) is (a - bi)
Notation: z̄ or z*
```

**Key Property**: 
```
(a + bi)(a - bi) = a² + b² (real number!)
```

**Division Strategy**: Multiply by conjugate of denominator

#### Example Pattern

**Simplify**: (2 + 3i)/(1 - 4i)

```
Step 1: Identify conjugate of denominator
     Conjugate of (1 - 4i) is (1 + 4i)

Step 2: Multiply numerator and denominator by conjugate
     = [(2 + 3i)(1 + 4i)] / [(1 - 4i)(1 + 4i)]

Step 3: Expand numerator
     = [2 + 8i + 3i + 12i²] / [1 + 4i - 4i - 16i²]
     = [2 + 11i - 12] / [1 + 16]
     = [-10 + 11i] / 17

Step 4: Write in standard form
     = -10/17 + (11/17)i
```

#### 🧠 Implicit Knowledge Required
- Conjugates eliminate imaginary part when multiplied
- Process is like rationalizing radical denominators
- Final answer should be in a + bi form
- Dividing complex numbers requires conjugate multiplication

---

## 📐 SECTION 1.4: QUADRATIC EQUATIONS

### Core Concept: Second-Degree Equations

**[[Quadratic_Equations|Standard Form]]**: ax² + bx + c = 0, where a ≠ 0

**Solution Methods**:
1. Factoring
2. Square Root Property
3. Completing the Square
4. Quadratic Formula

---

### Method 1: Solving by Factoring

**Strategy**: Use [[Zero_Product_Property]]

**[[Zero_Product_Property|Zero Product Property]]**: If AB = 0, then A = 0 or B = 0

**Process**:
```
1. Write in standard form (= 0 on one side)
2. Factor completely
3. Set each factor equal to zero
4. Solve each equation
5. Check solutions
```

#### Example Pattern

**Solve**: x² + 5x = 14

```
Step 1: Standard form
     x² + 5x - 14 = 0

Step 2: Factor
     (x + 7)(x - 2) = 0

Step 3: Apply Zero Product Property
     x + 7 = 0  or  x - 2 = 0

Step 4: Solve
     x = -7  or  x = 2

Step 5: Check both solutions
     For x = -7: (-7)² + 5(-7) = 49 - 35 = 14 ✓
     For x = 2: (2)² + 5(2) = 4 + 10 = 14 ✓
```

#### 🧠 Implicit Knowledge Required
- MUST equal zero to use Zero Product Property
- Both solutions are valid unless context restricts
- Factoring review from Chapter R.5
- Check is important (especially in applications)

---

### Method 2: Square Root Property

**Square Root Property**: 
```
If x² = k, then x = ±√k
```

**When to Use**: 
- Perfect square on one side
- No linear term (no x term)
- After completing the square

#### Example Pattern

**Solve**: (x - 3)² = 16

```
Step 1: Apply square root property
     x - 3 = ±√16
     x - 3 = ±4

Step 2: Solve both cases
     x - 3 = 4  or  x - 3 = -4
     x = 7      or  x = -1

Solutions: x = 7, x = -1
```

#### 🧠 Implicit Knowledge Required
- ± means TWO solutions (positive and negative)
- Can have irrational solutions: x² = 7 gives x = ±√7
- Can have imaginary solutions: x² = -4 gives x = ±2i
- Number of solutions depends on k value

---

### Method 3: Completing the Square

**Goal**: Transform ax² + bx + c = 0 into perfect square form

> See [[Completing_the_Square]] for detailed theory and applications.

**Process** (when a = 1):
```
1. Move constant to right side: x² + bx = -c
2. Add (b/2)² to both sides
3. Factor left side as perfect square
4. Apply square root property
5. Solve for x
```

#### Example Pattern

**Solve**: x² + 6x - 1 = 0

```
Step 1: Move constant
     x² + 6x = 1

Step 2: Complete the square
     Add (6/2)² = 9 to both sides
     x² + 6x + 9 = 1 + 9
     x² + 6x + 9 = 10

Step 3: Factor perfect square
     (x + 3)² = 10

Step 4: Square root property
     x + 3 = ±√10

Step 5: Solve
     x = -3 ± √10
```

**When a ≠ 1**: First divide entire equation by a, then complete the square

#### 🧠 Implicit Knowledge Required
- (b/2)² is the "magic number" to add
- Perfect square trinomial: x² + bx + (b/2)² = (x + b/2)²
- This method works for ALL quadratics
- Leads to quadratic formula derivation

---

### Method 4: Quadratic Formula

**The [[Quadratic_Formula|Quadratic Formula]]**:
```
For ax² + bx + c = 0:

x = [-b ± √(b² - 4ac)] / (2a)
```

**When to Use**: Universal method (works for all quadratics)

**[[The_Discriminant|Discriminant]]**: b² - 4ac
```
If b² - 4ac > 0: Two distinct real solutions
If b² - 4ac = 0: One repeated real solution
If b² - 4ac < 0: Two complex conjugate solutions
```

#### Example Pattern

**Solve**: 2x² - 3x - 4 = 0

```
Step 1: Identify a, b, c
     a = 2, b = -3, c = -4

Step 2: Calculate discriminant
     b² - 4ac = (-3)² - 4(2)(-4)
              = 9 + 32 = 41 > 0
     (Two distinct real solutions)

Step 3: Apply formula
     x = [-(-3) ± √41] / (2·2)
     x = [3 ± √41] / 4

Solutions: x = (3 + √41)/4  or  x = (3 - √41)/4
```

#### 🧠 Implicit Knowledge Required
- Memorize the formula (critical!)
- Always check discriminant first (predicts solution type)
- Be careful with signs, especially with b
- Can leave answer with ± or split into two solutions
- Simplify radicals when possible

#### ⚠️ Common Errors
- Sign errors with b (especially when b is negative)
- Forgetting to multiply a by 2 in denominator
- Not simplifying √(b² - 4ac)
- Canceling incorrectly: (3 ± √41)/4 ≠ 3/4 ± √41/4

---


## 📐 SECTION 1.5: APPLICATIONS OF QUADRATIC EQUATIONS

### Core Concept: Real-World Quadratic Models

**Common Application Types**:
1. Geometry (area, Pythagorean theorem)
2. Projectile motion
3. Revenue/profit optimization
4. Number relationships

---

### Method 1: Pythagorean Theorem Applications

**[[Pythagorean_Theorem]]**: For right triangle with legs a, b and hypotenuse c:
```
a² + b² = c²
```

#### Example Pattern

**Problem**: A ladder 13 ft long leans against a wall. The base is 5 ft from the wall. How high up the wall does the ladder reach?

```
Step 1: Identify knowns
     Hypotenuse (ladder): c = 13
     One leg (base): a = 5
     Other leg (height): b = ?

Step 2: Set up equation
     5² + b² = 13²

Step 3: Solve
     25 + b² = 169
     b² = 144
     b = ±12

Step 4: Check context
     Height must be positive: b = 12 ft
     Reject negative solution

Answer: 12 feet
```

#### 🧠 Implicit Knowledge Required
- Longest side is hypotenuse
- Legs are perpendicular sides
- Negative solutions often rejected in context
- Check if triangle is actually right triangle

---

### Method 2: Projectile Motion

**Height Formula**: 
```
h(t) = -16t² + v₀t + h₀
```
Where:
- h(t) = height at time t (feet)
- t = time (seconds)
- v₀ = initial velocity (ft/s)
- h₀ = initial height (feet)
- -16 = gravity constant (ft/s²)

Note: Use -4.9 if using meters and seconds

#### Example Pattern

**Problem**: Ball thrown upward at 64 ft/s from height of 6 ft. When does it hit the ground?

```
Step 1: Write equation
     h(t) = -16t² + 64t + 6

Step 2: Set height to zero (ground level)
     0 = -16t² + 64t + 6

Step 3: Solve using quadratic formula
     a = -16, b = 64, c = 6
     
     t = [-64 ± √(64² - 4(-16)(6))] / (2(-16))
     t = [-64 ± √(4096 + 384)] / (-32)
     t = [-64 ± √4480] / (-32)
     t = [-64 ± 66.93] / (-32)
     
     t = 2.93/(-32) = -0.09  or  t = -130.93/(-32) = 4.09

Step 4: Check context
     Time must be positive after launch
     t ≈ 4.09 seconds

Answer: Approximately 4.09 seconds
```

#### 🧠 Implicit Knowledge Required
- Two solutions: one may be before launch (reject)
- Maximum height occurs at vertex of parabola
- Object hits ground when h(t) = 0
- Initial velocity positive = upward, negative = downward

---

### Method 3: Revenue and Profit Models

**Revenue**: R = (price per unit) × (number of units)
**Profit**: P = Revenue - Cost

Often modeled as quadratic because:
- Increasing price decreases demand
- Relationship is typically parabolic

#### Example Pattern

**Problem**: Company can sell x items per week at price p = 100 - 0.5x dollars. Find x that maximizes revenue.

```
Step 1: Write revenue function
     R(x) = x · p = x(100 - 0.5x)
     R(x) = 100x - 0.5x²

Step 2: Find vertex (maximum of parabola)
     For R(x) = ax² + bx + c, vertex at x = -b/(2a)
     x = -100 / (2(-0.5)) = -100 / (-1) = 100

Step 3: Calculate maximum revenue
     R(100) = 100(100) - 0.5(100)²
            = 10,000 - 5,000
            = 5,000

Answer: Sell 100 items for maximum revenue of $5,000
```

#### 🧠 Implicit Knowledge Required
- Parabola opens down (negative leading coefficient) → has maximum
- Vertex formula: x = -b/(2a) gives optimal value
- Should verify it's a maximum, not minimum
- Context determines if fractional answers make sense

---

## 📐 SECTION 1.6: MORE EQUATIONS AND APPLICATIONS

### Core Concept: Non-Standard Equation Types

**Strategies**:
1. Polynomial equations (degree > 2)
2. Equations with radicals
3. Equations quadratic in form

---

### Method 1: Polynomial Equations by Factoring

**Higher-Degree Polynomials**: Factor and use Zero Product Property

#### Example Pattern

**Solve**: x³ - 7x² + 12x = 0

```
Step 1: Factor GCF
     x(x² - 7x + 12) = 0

Step 2: Factor further
     x(x - 3)(x - 4) = 0

Step 3: Apply Zero Product Property
     x = 0  or  x - 3 = 0  or  x - 4 = 0

Solutions: x = 0, 3, 4
```

#### 🧠 Implicit Knowledge Required
- Always factor GCF first
- May need grouping, special patterns, or synthetic division
- Degree n polynomial has at most n real solutions
- Complex solutions come in conjugate pairs

---

### Method 2: Radical Equations

**Strategy**: Isolate radical, then square both sides

**CRITICAL**: Squaring can introduce [[Extraneous_Solutions|extraneous solutions]] - MUST CHECK!

**Process**:
```
1. Isolate radical on one side
2. Square both sides
3. Solve resulting equation
4. CHECK all solutions in original equation
```

#### Example Pattern

**Solve**: √(2x + 3) = x

```
Step 1: Radical already isolated

Step 2: Square both sides
     (√(2x + 3))² = x²
     2x + 3 = x²

Step 3: Rearrange and solve
     0 = x² - 2x - 3
     0 = (x - 3)(x + 1)
     x = 3  or  x = -1

Step 4: CHECK both in original
     For x = 3: √(2(3) + 3) = √9 = 3 ✓
     For x = -1: √(2(-1) + 3) = √1 = 1 ≠ -1 ✗

Solution: x = 3 only (x = -1 is extraneous)
```

#### 🧠 Implicit Knowledge Required
- Squaring both sides is NOT a reversible operation
- Extraneous solutions are common - checking is mandatory
- If radical is on both sides, may need to square twice
- Domain restriction: expression under radical must be ≥ 0

#### ⚠️ Common Errors
- Not checking solutions (missing extraneous solutions)
- Squaring only part of one side: √(x + 1) = x - 2, then x + 1 ≠ x² - 4
- Forgetting domain restrictions

---

### Method 3: Equations Quadratic in Form

**Quadratic in Form**: Can substitute u to make it quadratic

**Pattern Recognition**:
```
If equation has form: au²ⁿ + bu^n + c = 0
Let u = xⁿ, then: au² + bu + c = 0
```

#### Example Pattern

**Solve**: x⁴ - 5x² + 4 = 0

```
Step 1: Recognize form
     Let u = x²
     Then u² = x⁴

Step 2: Substitute
     u² - 5u + 4 = 0

Step 3: Factor (or use quadratic formula)
     (u - 1)(u - 4) = 0
     u = 1  or  u = 4

Step 4: Back-substitute
     x² = 1  or  x² = 4
     x = ±1  or  x = ±2

Solutions: x = -2, -1, 1, 2
```

#### 🧠 Implicit Knowledge Required
- Common substitutions:
  - u = x² for x⁴ terms
  - u = √x for x terms with √x
  - u = 1/x for rational expressions
- Always back-substitute to find x values
- May generate more solutions than standard quadratic
- Check all solutions in original equation

---

## 📐 SECTION 1.7: LINEAR, COMPOUND, AND ABSOLUTE VALUE INEQUALITIES

### Core Concept: Inequality Solutions

**Key Difference from Equations**: 
- Solution is typically an interval or union of intervals
- Graphed on number line

**Inequality Notation**:
```
<   : less than
>   : greater than
≤   : less than or equal to
≥   : greater than or equal to
```

---

### Method 1: Linear Inequalities

**Process**: Similar to equations, BUT:

**CRITICAL RULE**: When multiplying or dividing by negative number, REVERSE inequality sign!

#### Example Pattern

**Solve and graph**: -3x + 7 > -2

```
Step 1: Isolate variable term
     -3x > -9

Step 2: Divide by -3 (REVERSE inequality!)
     x < 3

Step 3: Write in [[Interval_Notation|interval notation]]
     (-∞, 3)

Step 4: Graph
     ←―――――――○
            3
     (open circle at 3, shade left)
```

#### 🧠 Implicit Knowledge Required
- Reversal ONLY when multiplying/dividing by negative
- Adding/subtracting never reverses inequality
- Open circle for < or >
- Closed circle for ≤ or ≥
- Check solution by testing a value in the interval

#### ⚠️ Common Errors
- Forgetting to reverse when multiplying/dividing by negative
- Using wrong circle type (open vs. closed)
- Wrong interval notation: x < 3 is (-∞, 3), not (3, ∞)

---

### Method 2: Compound Inequalities

> See [[Compound_Inequalities]] for detailed theory.

**Two Types**:

**1. AND (Intersection)**: Both conditions must be true
```
a < x AND x < b  →  a < x < b
Solution: intersection of both intervals
```

**2. OR (Union)**: At least one condition true
```
x < a OR x > b
Solution: union of both intervals
```

#### Example Pattern: AND

**Solve**: -2 ≤ 3x + 1 < 7

```
Step 1: Split into two inequalities
     -2 ≤ 3x + 1  AND  3x + 1 < 7

Step 2: Solve each
     -3 ≤ 3x       AND  3x < 6
     -1 ≤ x        AND  x < 2

Step 3: Find intersection
     -1 ≤ x < 2

Interval notation: [-1, 2)

Graph: ●―――――○
       -1    2
```

#### Example Pattern: OR

**Solve**: x + 2 < -1 OR x + 2 > 5

```
Step 1: Solve each inequality
     x < -3  OR  x > 3

Step 2: Union of intervals
     (-∞, -3) ∪ (3, ∞)

Graph: ←―――○     ○―――→
           -3     3
```

#### 🧠 Implicit Knowledge Required
- AND = intersection (overlap)
- OR = union (either or both)
- Can solve three-part inequality all at once: same operation to all three parts
- No solution if AND gives contradiction (like x < 2 AND x > 5)
- All real numbers if OR gives tautology

---

### Method 3: Absolute Value Inequalities

> See [[Absolute_Value_Inequalities]] for complete coverage.

**Two Cases Based on Inequality**:

**Type 1: |x| < k** (distance less than k)
```
Means: -k < x < k
(Compound AND inequality)
```

**Type 2: |x| > k** (distance greater than k)
```
Means: x < -k OR x > k
(Compound OR inequality)
```

#### Example Pattern: Type 1

**Solve**: |2x - 3| ≤ 5

```
Step 1: Rewrite as compound AND
     -5 ≤ 2x - 3 ≤ 5

Step 2: Solve
     -5 + 3 ≤ 2x ≤ 5 + 3
     -2 ≤ 2x ≤ 8
     -1 ≤ x ≤ 4

Interval notation: [-1, 4]
```

#### Example Pattern: Type 2

**Solve**: |3x + 2| > 7

```
Step 1: Rewrite as compound OR
     3x + 2 < -7  OR  3x + 2 > 7

Step 2: Solve each
     3x < -9  OR  3x > 5
     x < -3   OR  x > 5/3

Interval notation: (-∞, -3) ∪ (5/3, ∞)
```

#### 🧠 Implicit Knowledge Required
- |expression| < k splits to AND (-k < expression < k)
- |expression| > k splits to OR (expression < -k OR expression > k)
- Same rules apply to ≤ and ≥
- If k < 0:
  - |x| < negative has no solution
  - |x| > negative is all real numbers
- If k = 0:
  - |x| < 0 has no solution
  - |x| ≤ 0 means x = 0
  - |x| > 0 means x ≠ 0
  - |x| ≥ 0 is all real numbers

#### ⚠️ Common Errors
- Mixing up < (AND) with > (OR)
- Forgetting to split into two cases
- Sign errors when negating: |x| < 5 means -5 < x < 5, not 5 < x < -5

---

## 🔄 RELATIONAL COGNITION FRAMEWORK

### Vertical Integration: Prerequisites → Applications

**Foundation Chain**:
```
Chapter R Skills
    ↓
Linear Equations (1.1)
    ↓
Applications (1.2) ← Models real scenarios
    ↓
Complex Numbers (1.3) ← Extends number system
    ↓
Quadratic Equations (1.4) ← New equation type
    ↓
Applications (1.5) ← Models parabolic scenarios
    ↓
Advanced Equations (1.6) ← Higher degree, radicals
    ↓
Inequalities (1.7) ← Solution sets instead of points
```

**Builds Forward To**:
- **Chapter 2**: Functions (equations define functions)
- **Chapter 3**: Polynomial graphs (uses all solving techniques)
- **Chapter 4**: Exponential/logarithmic equations
- **Chapter 5-6**: Trigonometric equations

---

### Horizontal Integration: Connections Within Chapter 1

**Equation-Solving Hierarchy**:
```
Linear (degree 1)
    ↓
Quadratic (degree 2) ← Multiple methods
    ↓
Higher degree ← Factor or transform
    ↓
Radical ← Square to reduce
    ↓
Quadratic in form ← Substitute to reduce
```

**Key Insight**: Complex problems often reduce to simpler ones through transformation

**Method Selection Decision Tree**:
```
What type of equation?
├─ Linear → Standard process
├─ Quadratic
│   ├─ Can factor? → Use Zero Product Property
│   ├─ Perfect square? → Use Square Root Property
│   ├─ Need exact answer? → Complete the Square
│   └─ Default → Quadratic Formula
├─ Higher degree → Try factoring (GCF, grouping, patterns)
├─ Radical → Isolate and square (CHECK solutions!)
└─ Quadratic in form → Substitute u, solve, back-substitute
```

---

### Cross-Chapter Connections

**To Chapter R**:
- Real number properties (1.1)
- Factoring skills (1.4, 1.6)
- Rational expressions (1.1)
- Radicals (1.6)
- Order of operations (all sections)

**To Chapter 2**:
- Equations define functions
- Solutions are x-intercepts (zeros)
- Inequalities describe domains/ranges

**To Chapter 3**:
- Quadratic equations → parabolas
- Polynomial equations → polynomial functions
- Zeros are solutions

**To Chapter 4**:
- Complex numbers in exponential form
- Equations with exponentials and logarithms

---

## 📋 COMMON ERROR TAXONOMY

### Category 1: Sign Errors
1. Not distributing negative: -(x - 3) ≠ -x - 3
2. Losing negative when moving terms
3. Forgetting to reverse inequality when multiplying/dividing by negative
4. Sign errors in quadratic formula with negative b

### Category 2: Algebraic Manipulation Errors
1. Canceling terms instead of factors: (x + 3)/x ≠ 1 + 3
2. Distributing exponents: (a + b)² ≠ a² + b²
3. Dividing only one term: (2x + 4)/2 ≠ x + 4
4. Square root errors: √(a² + b²) ≠ a + b

### Category 3: Solution Method Errors
1. Using Zero Product Property without = 0
2. Not checking for extraneous solutions (radicals)
3. Rejecting valid negative solutions
4. Missing second solution in quadratic

### Category 4: Complex Number Errors
1. Forgetting i² = -1
2. Not simplifying powers of i
3. Conjugate errors in division
4. Treating i like a variable in equations

### Category 5: Inequality Errors
1. Not reversing inequality sign with negatives
2. Wrong interval notation
3. Mixing up AND (intersection) vs OR (union)
4. Absolute value inequality case errors

### Category 6: Application Errors
1. Not checking context (negative time, negative length)
2. Wrong units or unit conversion
3. Misidentifying variables
4. Not answering the actual question asked

---

## 🎯 MASTERY CHECKLIST

### Level 1: Recognition & Setup
- [ ] Identify equation type (linear, quadratic, higher, radical)
- [ ] Choose appropriate solution method
- [ ] Recognize when answer needs checking (radicals, rational)
- [ ] Identify domain restrictions
- [ ] Translate word problems to equations

### Level 2: Basic Execution
- [ ] Solve linear equations
- [ ] Solve quadratic equations by factoring
- [ ] Use quadratic formula correctly
- [ ] Perform operations with complex numbers
- [ ] Solve basic inequalities

### Level 3: Advanced Techniques
- [ ] Complete the square
- [ ] Solve radical equations (with checking)
- [ ] Solve equations quadratic in form
- [ ] Solve compound inequalities
- [ ] Solve absolute value inequalities

### Level 4: Applications
- [ ] Set up and solve mixture problems
- [ ] Set up and solve distance-rate-time problems
- [ ] Solve work problems
- [ ] Apply Pythagorean theorem
- [ ] Model with quadratic functions (projectile, revenue)

### Level 5: Analysis & Synthesis
- [ ] Interpret discriminant to predict solution types
- [ ] Recognize extraneous solutions before checking
- [ ] Choose most efficient solution method
- [ ] Verify solutions make sense in context
- [ ] Connect equation solutions to function behavior

---

## 💡 KEY INSIGHTS

### Foundational Principles

**1. Equations as Balance**
> Every operation maintains equality. The art of solving is systematic simplification while preserving the equation's truth.

**2. Method Selection Matters**
> While multiple methods may work, choosing efficiently saves time and reduces errors. Factoring beats formula when possible.

**3. Checking is Not Optional**
> For radical equations and rational equations, checking is mandatory. Extraneous solutions are common and must be rejected.

**4. Context Determines Validity**
> Mathematical solutions may be rejected based on real-world constraints (negative time, negative length, etc.).

**5. Transformation Reduces Complexity**
> Many complex equations reduce to simpler forms through substitution, isolation, or algebraic manipulation.

---

## 🔗 RELATED CONCEPTS

This chapter connects to these concept nodes in the vault:

### Equation Types
- [[Linear_Equations]] - First-degree equations (Section 1.1)
- [[Quadratic_Equations]] - Second-degree equations (Section 1.4)
- [[Rational_Equations]] - Equations with fractions (Section 1.1)
- [[Radical_Equations]] - Equations with radicals (Section 1.6)
- [[Polynomial_Equations]] - Higher-degree equations (Section 1.6)

### Solution Methods
- [[Zero_Product_Property]] - Foundation for solving by factoring (Section 1.4)
- [[Completing_the_Square]] - Quadratic solution technique (Section 1.4)
- [[Quadratic_Formula]] - Universal quadratic solver (Section 1.4)
- [[The_Discriminant]] - Predicts solution types (Section 1.4)

### Number Systems
- [[Complex_Numbers]] - Extending real numbers (Section 1.3)
- [[Complex_Conjugate]] - Division technique (Section 1.3)
- [[Imaginary_Unit]] - Powers of i (Section 1.3)

### Inequalities
- [[Compound_Inequalities]] - AND/OR combinations (Section 1.7)
- [[Absolute_Value_Inequalities]] - Distance-based inequalities (Section 1.7)
- [[Interval_Notation]] - Solution set representation (Section 1.7)

### Applications
- [[Pythagorean_Theorem]] - Right triangle applications (Section 1.5)
- [[Distance_Rate_Time_Problems]] - Motion problems (Section 1.2)
- [[Mixture_Problems]] - Concentration problems (Section 1.2)

### Solution Verification
- [[Extraneous_Solutions]] - False solutions from transformations (Sections 1.1, 1.6)

---

## 🔗 NAVIGATION

**Previous**: [[01_Course/Textbook/ChapterR_Prerequisites|← Chapter R: Prerequisites]]  
**Next**: [[01_Course/Textbook/Chapter2_Functions_Relations|Chapter 2: Functions →]]  
**Index**: [[01_Course/Textbook/Index|Textbook Index]]  
**Concepts**: [[02_Concepts/Concept_Library|Concept Library]]  
**Dashboard**: [[System/Project_Dashboard|Project Dashboard]]

---

**Chapter 1 Extraction**: Complete ✅  
**Sections Covered**: 1.1 - 1.7 (All)  
**Methods Documented**: 20+  
**Status**: Ready for integration

---

*This comprehensive extraction follows the Universal Knowledge Framework methodology, documenting explicit procedures, implicit knowledge requirements, common errors, and relational connections across the mathematical landscape.*
