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

# Inverse Variation

## Definition

Two variables $x$ and $y$ exhibit **inverse variation** if their product is constant. We say "$y$ varies inversely as $x$" or "$y$ is inversely proportional to $x$." The relationship is characterized by: as one variable increases, the other decreases proportionally such that their product remains constant.

**Formal Statement**: $y$ varies inversely as $x$ if there exists a nonzero constant $k$ such that $y = \frac{k}{x}$ or equivalently $xy = k$.

The constant $k$ is called the **constant of variation**.

## Mathematical Expression

$$y = \frac{k}{x} \quad \text{where } k \neq 0, \, x \neq 0$$

Equivalently:
$$xy = k \quad \text{(constant product)}$$

**Key insight**: In inverse variation, the product $xy$ remains constant for all corresponding pairs $(x, y)$.

## Finding the Constant of Variation

Given one pair of values $(x_1, y_1)$:

$$k = x_1 y_1$$

Then the complete relationship is: $y = \frac{x_1 y_1}{x}$

## Example

**Problem**: If $y$ varies inversely as $x$, and $y = 12$ when $x = 5$, find $y$ when $x = 8$.

**Step 1**: Find the constant of variation
$$k = xy = (5)(12) = 60$$

**Step 2**: Write the variation equation
$$y = \frac{60}{x}$$

**Step 3**: Substitute $x = 8$
$$y = \frac{60}{8} = 7.5$$

**Solution**: When $x = 8$, $y = 7.5$.

**Verification**: Check the product is constant
- Original: $(5)(12) = 60$
- New: $(8)(7.5) = 60$ ✓

## Key Properties

- **Hyperbola graph**: Graph is a rectangular hyperbola with asymptotes at $x = 0$ and $y = 0$
- **No zero values**: Neither $x$ nor $y$ can equal zero
- **Asymptotic behavior**: As $x \to \infty$, $y \to 0$; as $x \to 0^+$, $y \to \infty$
- **Reciprocal relationship**: Doubling $x$ halves $y$; tripling $x$ reduces $y$ to one-third
- **Constant product**: $x_1 y_1 = x_2 y_2$ for any two points

## Real-World Applications

- **Speed and time** (constant distance): $t = \frac{d}{r}$ where distance is fixed
- **Pressure and volume** (Boyle's Law): At constant temperature, $PV = k$
- **Work rate**: Time to complete job varies inversely with number of workers
- **Brightness and distance**: Light intensity varies inversely with square of distance (inverse square law)

## Relations

- `[[Direct_Variation]]` - contrasting relationship where $y = kx$
- `[[Rational_Functions]]` - inverse variation is simplest rational function $f(x) = \frac{k}{x}$
- `[[Hyperbola]]` - geometric representation of inverse variation
- `[[Combined_Variation]]` - inverse variation combined with other variation types
- `[[Asymptotes]]` - inverse variation has vertical asymptote at $x=0$ and horizontal at $y=0$
