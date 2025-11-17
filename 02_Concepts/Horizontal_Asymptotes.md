---
type: concept
status: active
tags:
  - concept/analysis
  - concept/properties
  - math/functions
  - math/limits
  - chapter-3
created: 2025-11-17
updated: 2025-11-17
---

# Horizontal Asymptotes

## Definition

A **horizontal asymptote** is a horizontal line $y = b$ that a function approaches as $x$ approaches positive or negative infinity. The function gets arbitrarily close to the line but may or may not actually reach it.

**Formal Statement**: The line $y = b$ is a horizontal asymptote of $f(x)$ if:
$$\lim_{x \to +\infty} f(x) = b \quad \text{or} \quad \lim_{x \to -\infty} f(x) = b$$

**Key Difference from Vertical**: Describes **end behavior** (what happens as $x \to \pm\infty$), NOT undefined points.

## Mathematical Expression

**For Rational Functions**: $f(x) = \frac{a_nx^n + \cdots + a_0}{b_mx^m + \cdots + b_0}$

Horizontal asymptote determined by **comparing degrees** of numerator and denominator:

### Rule 1: Degree of Numerator < Degree of Denominator ($n < m$)
$$y = 0 \quad \text{(x-axis is horizontal asymptote)}$$

**Example**: $f(x) = \frac{3x + 1}{x^2 + 5}$ has degree 1 < degree 2 → $y = 0$

### Rule 2: Degree of Numerator = Degree of Denominator ($n = m$)
$$y = \frac{a_n}{b_m} \quad \text{(ratio of leading coefficients)}$$

**Example**: $f(x) = \frac{3x^2 + 7x}{2x^2 - 1}$ has degree 2 = degree 2 → $y = \frac{3}{2}$

### Rule 3: Degree of Numerator > Degree of Denominator ($n > m$)
$$\text{No horizontal asymptote}$$

**Example**: $f(x) = \frac{x^3 + 1}{x^2 - 4}$ has degree 3 > degree 2 → No horizontal asymptote (may have oblique asymptote)

**Key insight**: The degrees of numerator and denominator completely determine horizontal asymptote behavior.

## Example 1: Degree of Numerator < Degree of Denominator

**Problem**: Find the horizontal asymptote of $f(x) = \frac{5x - 3}{2x^2 + 7x + 1}$

**Step 1**: Identify degrees
- Numerator: degree 1
- Denominator: degree 2
- $1 < 2$ (numerator degree less than denominator degree)

**Step 2**: Apply Rule 1
When degree of numerator < degree of denominator:

**Horizontal asymptote**: $y = 0$

**Interpretation**: As $x \to \pm\infty$, the denominator grows much faster than numerator, so fraction approaches 0.

## Example 2: Equal Degrees

**Problem**: Find the horizontal asymptote of $f(x) = \frac{4x^2 - 3x + 1}{3x^2 + 5x - 2}$

**Step 1**: Identify degrees
- Numerator: degree 2 (leading term $4x^2$)
- Denominator: degree 2 (leading term $3x^2$)
- Degrees are equal

**Step 2**: Apply Rule 2 (ratio of leading coefficients)
$$y = \frac{4}{3}$$

**Horizontal asymptote**: $y = \frac{4}{3}$

**Verification** (informal): As $x \to \infty$, lower-degree terms become negligible:
$$f(x) \approx \frac{4x^2}{3x^2} = \frac{4}{3}$$

## Example 3: No Horizontal Asymptote

**Problem**: Determine horizontal asymptote of $f(x) = \frac{x^3 + 2x}{x^2 - 1}$

**Step 1**: Identify degrees
- Numerator: degree 3
- Denominator: degree 2
- $3 > 2$ (numerator degree greater than denominator degree)

**Step 2**: Apply Rule 3

**Horizontal asymptote**: None (no horizontal asymptote exists)

**Note**: This function has an **oblique (slant) asymptote** instead, found by polynomial division.

## Key Properties

- **End behavior**: Describes where function "settles" as $x \to \pm\infty$
- **May cross**: Unlike vertical asymptotes, function CAN cross horizontal asymptote (in middle, but not at ends)
- **At most two**: Function can have different horizontal asymptotes as $x \to +\infty$ vs $x \to -\infty$ (rare for rational functions)
- **Not exclusive**: Can have both horizontal and vertical asymptotes
- **Degree rule decisive**: For rational functions, degrees alone determine horizontal asymptote

## Why the Degree Rules Work

**Intuition**: As $x \to \infty$, highest-degree terms dominate.

**Case 1** ($n < m$): Denominator grows faster
$$\frac{x}{x^2} = \frac{1}{x} \to 0 \text{ as } x \to \infty$$

**Case 2** ($n = m$): Numerator and denominator grow at same rate
$$\frac{3x^2}{2x^2} = \frac{3}{2} \text{ (constant ratio)}$$

**Case 3** ($n > m$): Numerator grows faster
$$\frac{x^3}{x^2} = x \to \infty \text{ (unbounded, no horizontal asymptote)}$$

## Crossing Horizontal Asymptotes

**Important distinction**:
- **Vertical asymptotes**: NEVER crossed (function undefined there)
- **Horizontal asymptotes**: CAN be crossed in the middle, but function approaches asymptote as $x \to \pm\infty$

**Example**: $f(x) = \frac{x}{x^2 + 1}$ has horizontal asymptote $y = 0$
- Function crosses $y = 0$ at $x = 0$
- But as $x \to \pm\infty$, $f(x) \to 0$

## Common Errors

**Error 1**: Using constant terms instead of leading coefficients
```
Wrong: f(x) = (3x² + 5)/(2x² + 7) has asymptote y = 5/7
Right: Use leading coefficients: y = 3/2
```

**Error 2**: Forgetting to check degrees
```
Wrong: Every rational function has a horizontal asymptote
Right: Only if degree of numerator ≤ degree of denominator
```

**Error 3**: Thinking horizontal asymptotes can't be crossed
```
Wrong: Function never crosses y = L
Right: Can cross in middle, but approaches at infinities
```

## Relations

- `[[Rational_Functions]]` - horizontal asymptotes describe end behavior of rational functions
- `[[Vertical_Asymptotes]]` - complementary concept describing behavior at undefined points
- `[[Oblique_Asymptotes]]` - occurs when numerator degree exceeds denominator by exactly 1
- `[[End_Behavior]]` - horizontal asymptotes characterize end behavior of rational functions
- `[[Limits_at_Infinity]]` - horizontal asymptotes formalized using limits as $x \to \pm\infty$
