---
type: concept
status: active
tags:
  - concept/algebra
  - concept/properties
  - math/algebra
  - math/functions
  - chapter-3
created: 2025-11-16
updated: 2025-11-16
---

# Combined Variation

## Definition

A variable exhibits **combined variation** when it varies according to a combination of direct, inverse, and/or joint variation with respect to multiple variables. Combined variation allows for complex relationships where some variables affect the result directly (in the numerator) and others inversely (in the denominator).

**Formal Statement**: $z$ varies directly as $x$ and inversely as $y$ if there exists a nonzero constant $k$ such that:
$$z = k \cdot \frac{x}{y}$$

More generally, combined variation can involve any mix of direct, inverse, and joint relationships.

## Mathematical Expression

**General Form**:
$$z = k \cdot \frac{x_1^{a_1} x_2^{a_2} \cdots x_m^{a_m}}{y_1^{b_1} y_2^{b_2} \cdots y_n^{b_n}}$$

where:
- Variables in numerator: direct or joint variation
- Variables in denominator: inverse variation
- Exponents indicate powers (e.g., $x^2$ means varies as square of $x$)

**Common Forms**:
- Direct-Inverse: $z = k \frac{x}{y}$
- Joint-Inverse: $z = k \frac{xy}{w}$
- Direct-Square-Inverse: $z = k \frac{x^2}{y}$

## Finding the Constant of Variation

Given one complete set of values, solve for $k$ by substituting into the variation equation.

**Example**: If $z = k \frac{x}{y}$ and we know $(x_1, y_1, z_1)$:
$$k = \frac{z_1 y_1}{x_1}$$

## Example

**Problem**: $z$ varies directly as $x$ and inversely as the square of $y$. If $z = 20$ when $x = 10$ and $y = 2$, find $z$ when $x = 15$ and $y = 3$.

**Step 1**: Write the variation equation
$$z = k \cdot \frac{x}{y^2}$$

**Step 2**: Find the constant of variation using given values
$$20 = k \cdot \frac{10}{2^2} = k \cdot \frac{10}{4}$$
$$20 = 2.5k$$
$$k = 8$$

**Step 3**: Complete variation equation
$$z = 8 \cdot \frac{x}{y^2}$$

**Step 4**: Substitute new values $x = 15$, $y = 3$
$$z = 8 \cdot \frac{15}{3^2} = 8 \cdot \frac{15}{9} = 8 \cdot \frac{5}{3} = \frac{40}{3} \approx 13.33$$

**Solution**: When $x = 15$ and $y = 3$, $z = \frac{40}{3}$ or approximately $13.33$.

**Verification**:
- Original: $z = 8 \cdot \frac{10}{4} = 20$ ✓
- New: $z = 8 \cdot \frac{15}{9} = \frac{40}{3}$ ✓

## Key Properties

- **Hybrid behavior**: Combines increasing effects (direct) with decreasing effects (inverse)
- **Complex scaling**: Effects compound multiplicatively
- **Multiple dependencies**: Multiple independent variables interact
- **Real-world accuracy**: Better models actual phenomena than simple variation alone

## Real-World Applications

- **Newton's Law of Gravitation**: $F = G \frac{m_1 m_2}{r^2}$ (force varies jointly as masses, inversely as square of distance)
- **Electrical resistance**: $R = \rho \frac{L}{A}$ (resistance varies directly as length, inversely as cross-sectional area)
- **Intensity of sound/light**: Varies directly as power, inversely as square of distance
- **Gas laws**: $PV = nRT$ can be rearranged to show combined variation

## Solution Strategy

**Step-by-step approach**:

1. **Translate** the statement into equation form
   - "varies directly as $x$" → numerator contains $x$
   - "varies inversely as $y$" → denominator contains $y$
   - "varies jointly as $x$ and $y$" → numerator contains $xy$
   - "varies as square of $x$" → use $x^2$

2. **Find $k$** using given values

3. **Write complete equation** with calculated $k$

4. **Substitute** new values to find unknown

## Relations

- `[[Direct_Variation]]` - component of combined variation in numerator
- `[[Inverse_Variation]]` - component of combined variation in denominator
- `[[Joint_Variation]]` - can appear in numerator for multiple direct factors
- `[[Rational_Functions]]` - combined variation produces rational expressions
- `[[Proportionality]]` - complex proportional relationships in real applications
