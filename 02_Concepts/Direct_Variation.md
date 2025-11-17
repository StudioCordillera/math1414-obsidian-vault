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

# Direct Variation

## Definition

Two variables $x$ and $y$ exhibit **direct variation** if $y$ is a constant multiple of $x$. We say "$y$ varies directly as $x$" or "$y$ is directly proportional to $x$." The relationship is characterized by a constant ratio: as one variable increases, the other increases proportionally.

**Formal Statement**: $y$ varies directly as $x$ if there exists a nonzero constant $k$ such that $y = kx$.

The constant $k$ is called the **constant of variation** or **constant of proportionality**.

## Mathematical Expression

$$y = kx \quad \text{where } k \neq 0$$

Equivalently:
$$\frac{y}{x} = k \quad \text{(constant ratio)}$$

**Key insight**: In direct variation, the ratio $\frac{y}{x}$ remains constant for all corresponding pairs $(x, y)$.

## Finding the Constant of Variation

Given one pair of values $(x_1, y_1)$:

$$k = \frac{y_1}{x_1}$$

Then the complete relationship is: $y = \frac{y_1}{x_1} \cdot x$

## Example

**Problem**: If $y$ varies directly as $x$, and $y = 15$ when $x = 3$, find $y$ when $x = 7$.

**Step 1**: Find the constant of variation
$$k = \frac{y}{x} = \frac{15}{3} = 5$$

**Step 2**: Write the variation equation
$$y = 5x$$

**Step 3**: Substitute $x = 7$
$$y = 5(7) = 35$$

**Solution**: When $x = 7$, $y = 35$.

**Verification**: Check the ratio is constant
- Original: $\frac{15}{3} = 5$
- New: $\frac{35}{7} = 5$ ✓

## Key Properties

- **Linear relationship**: Graph is a straight line through the origin
- **Zero intercept**: When $x = 0$, $y = 0$ (passes through origin)
- **Sign preservation**: If $k > 0$, $x$ and $y$ have the same sign; if $k < 0$, opposite signs
- **Scaling**: Doubling $x$ doubles $y$; tripling $x$ triples $y$
- **Constant ratio**: $\frac{y_1}{x_1} = \frac{y_2}{x_2}$ for any two points

## Real-World Applications

- **Distance and time** (constant speed): $d = rt$ where $r$ is constant
- **Cost and quantity**: Total cost varies directly with number of items at constant price
- **Hooke's Law**: Spring force varies directly with displacement
- **Circumference and radius**: $C = 2\pi r$

## Relations

- `[[Inverse_Variation]]` - contrasting relationship where $y = \frac{k}{x}$
- `[[Linear_Functions]]` - direct variation is special case of linear function through origin
- `[[Proportional_Relationships]]` - direct variation establishes proportionality
- `[[Joint_Variation]]` - extends direct variation to multiple variables
- `[[Slope]]` - the constant $k$ represents the slope of the line through origin
