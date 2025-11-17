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

# Joint Variation

## Definition

A variable $z$ exhibits **joint variation** with respect to two or more variables when $z$ varies directly as the product of those variables. We say "$z$ varies jointly as $x$ and $y$" when $z$ is directly proportional to the product $xy$.

**Formal Statement**: $z$ varies jointly as $x$ and $y$ if there exists a nonzero constant $k$ such that $z = kxy$.

The constant $k$ is called the **constant of joint variation**.

**Extension**: Joint variation can involve any number of variables: $z = kxyw$ means $z$ varies jointly as $x$, $y$, and $w$.

## Mathematical Expression

$$z = kxy \quad \text{where } k \neq 0$$

More generally, for $n$ variables:
$$z = kx_1 x_2 x_3 \cdots x_n$$

**Key insight**: Each variable contributes multiplicatively. Doubling any one variable doubles $z$; doubling two variables quadruples $z$.

## Finding the Constant of Variation

Given one set of values $(x_1, y_1, z_1)$:

$$k = \frac{z_1}{x_1 y_1}$$

Then the complete relationship is: $z = \frac{z_1}{x_1 y_1} \cdot xy$

## Example

**Problem**: If $z$ varies jointly as $x$ and $y$, and $z = 72$ when $x = 3$ and $y = 4$, find $z$ when $x = 5$ and $y = 6$.

**Step 1**: Find the constant of variation
$$k = \frac{z}{xy} = \frac{72}{(3)(4)} = \frac{72}{12} = 6$$

**Step 2**: Write the variation equation
$$z = 6xy$$

**Step 3**: Substitute $x = 5$ and $y = 6$
$$z = 6(5)(6) = 6(30) = 180$$

**Solution**: When $x = 5$ and $y = 6$, $z = 180$.

**Verification**: Check the ratio is constant
- Original: $\frac{72}{3 \cdot 4} = \frac{72}{12} = 6$
- New: $\frac{180}{5 \cdot 6} = \frac{180}{30} = 6$ ✓

## Key Properties

- **Multivariate direct variation**: Joint variation is direct variation extended to multiple variables
- **Multiplicative scaling**: If both $x$ and $y$ double, $z$ increases by factor of $2 \times 2 = 4$
- **Independence**: Each variable independently affects $z$ in direct proportion
- **Three-dimensional surface**: Graph is a surface in 3D space (for two independent variables)
- **Constant ratio**: $\frac{z}{xy}$ remains constant for all corresponding triples

## Real-World Applications

- **Area of rectangle**: $A = \ell w$ (area varies jointly as length and width)
- **Volume of cylinder**: $V = \pi r^2 h$ (volume varies jointly as $r^2$ and $h$)
- **Kinetic energy**: $KE = \frac{1}{2}mv^2$ (energy varies jointly as mass and square of velocity)
- **Electrical power**: $P = VI$ (power varies jointly as voltage and current)

## Relations

- `[[Direct_Variation]]` - joint variation extends direct variation to multiple variables
- `[[Combined_Variation]]` - joint variation can be combined with inverse variation
- `[[Multivariable_Functions]]` - joint variation is a simple multivariable relationship
- `[[Proportionality]]` - joint variation establishes multi-factor proportionality
- `[[Product_Rule]]` - algebraic manipulation of joint variation uses product operations
