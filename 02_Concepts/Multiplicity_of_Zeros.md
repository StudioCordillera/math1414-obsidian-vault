---
type: concept
status: active
tags:
  - concept/polynomials
  - concept/properties
  - math/polynomials
  - math/analysis
  - chapter-3
created: 2025-11-17
updated: 2025-11-17
---

# Multiplicity of Zeros

## Definition

The **multiplicity** of a zero (root) of a polynomial is the number of times that zero appears as a factor. If $(x - c)^k$ is a factor of $f(x)$ but $(x - c)^{k+1}$ is not, then $c$ is a zero of **multiplicity** $k$.

**Formal Statement**: For polynomial $f(x)$, if:
$$f(x) = (x - c)^k \cdot q(x)$$

where $q(c) \neq 0$, then $c$ is a zero of multiplicity $k$.

**Key Insight**: Multiplicity tells you how many times the same factor appears, which determines the graph's behavior at that zero.

## Mathematical Expression

**Factored Form with Multiplicities**:
$$f(x) = a(x - c_1)^{k_1}(x - c_2)^{k_2} \cdots (x - c_n)^{k_n}$$

where:
- $c_i$ are distinct zeros
- $k_i$ is the multiplicity of zero $c_i$
- Sum of multiplicities = degree of polynomial: $k_1 + k_2 + \cdots + k_n = n$

**Classification by Multiplicity**:
- **Multiplicity 1**: Simple zero (or simple root)
- **Multiplicity 2**: Double zero (or double root)
- **Multiplicity 3**: Triple zero (or triple root)
- **Multiplicity $k \geq 2$**: Repeated zero (or repeated root)

## Example 1: Identifying Multiplicities

**Problem**: Find the zeros and their multiplicities for $f(x) = (x - 2)^3(x + 1)^2(x - 5)$

**Solution**: Reading directly from factored form:

- **Zero $x = 2$**: Multiplicity **3** (triple root)
- **Zero $x = -1$**: Multiplicity **2** (double root)
- **Zero $x = 5$**: Multiplicity **1** (simple root)

**Verification**: Sum of multiplicities = $3 + 2 + 1 = 6$ = degree of polynomial ✓

## Example 2: Finding Multiplicities from Expanded Form

**Problem**: Determine zeros and multiplicities for $f(x) = x^4 - 8x^3 + 24x^2 - 32x + 16$

**Step 1**: Recognize pattern or factor
This is actually $(x - 2)^4$ (binomial expansion):
$$(x - 2)^4 = x^4 - 4(2)x^3 + 6(4)x^2 - 4(8)x + 16$$

**Step 2**: Identify zero and multiplicity
- **Zero $x = 2$**: Multiplicity **4**

**Alternative**: If pattern not recognized, use Rational Root Theorem to test $x = 2$:
- $f(2) = 0$ ✓
- Synthetic division by $(x-2)$ → quotient $q_1(x)$
- $q_1(2) = 0$ → divide again
- Continue until $q_k(2) \neq 0$
- Number of divisions = multiplicity

## Graph Behavior by Multiplicity

**Key Property**: Multiplicity determines how the graph interacts with the x-axis at a zero.

### Odd Multiplicity (1, 3, 5, ...)
**Behavior**: Graph **crosses** the x-axis at the zero

- **Multiplicity 1**: Crosses straight through (linear behavior)
- **Multiplicity 3**: Crosses with flattening (cubic behavior, looks like $x^3$ near zero)
- **Multiplicity 5**: Even flatter crossing

### Even Multiplicity (2, 4, 6, ...)
**Behavior**: Graph **touches** (bounces off) the x-axis at the zero

- **Multiplicity 2**: Touches and turns around (parabolic behavior, looks like $x^2$)
- **Multiplicity 4**: Flatter touch (looks like $x^4$ near zero)
- **Multiplicity 6**: Even flatter touch

**Visual Summary**:
```
Multiplicity 1: ／      (cross)
Multiplicity 2: ∪      (bounce)
Multiplicity 3: ～／    (flat cross)
Multiplicity 4: ∪∪     (flat bounce)
```

## Example 3: Graphical Analysis

**Problem**: Sketch the behavior near zeros for $f(x) = x^2(x - 3)^3(x + 2)$

**Analysis**:

**At $x = 0$** (multiplicity 2, even):
- Graph **touches** x-axis and bounces off
- Parabolic behavior (like $x^2$)

**At $x = 3$** (multiplicity 3, odd):
- Graph **crosses** x-axis
- Flattened cubic behavior (like $(x-3)^3$)

**At $x = -2$** (multiplicity 1, odd):
- Graph **crosses** x-axis straight through
- Linear behavior

**Summary**: Touch at 0, flat cross at 3, straight cross at -2.

## Relationship to Derivatives

**Advanced Connection**: A zero $c$ has multiplicity $k$ if and only if:
$$f(c) = f'(c) = f''(c) = \cdots = f^{(k-1)}(c) = 0$$
$$f^{(k)}(c) \neq 0$$

**Interpretation**: All derivatives up to order $k-1$ equal zero at $c$, but the $k$-th derivative doesn't.

**Example**: For $f(x) = (x-2)^3$:
- $f(2) = 0$ ✓
- $f'(x) = 3(x-2)^2$, so $f'(2) = 0$ ✓
- $f''(x) = 6(x-2)$, so $f''(2) = 0$ ✓
- $f'''(x) = 6$, so $f'''(2) = 6 \neq 0$ ✓
- Multiplicity = 3

## Key Properties

- **Degree constraint**: Sum of all multiplicities equals degree of polynomial
- **Graph behavior**: Odd multiplicity → cross; Even multiplicity → bounce
- **Factorization**: $(x-c)^k$ means $c$ appears $k$ times as a root
- **Fundamental Theorem**: Polynomial of degree $n$ has exactly $n$ zeros (counting multiplicities) over complex numbers
- **Flattening effect**: Higher multiplicity → flatter graph near zero

## Finding Multiplicity (Algorithm)

**Method 1: From Factored Form** (easiest)
- Count the exponent on each factor $(x - c)^k$

**Method 2: Repeated Division** (from expanded form)
1. Verify $c$ is a zero: $f(c) = 0$
2. Divide $f(x)$ by $(x - c)$ → get quotient $q_1(x)$
3. Test: Is $c$ still a zero of $q_1(x)$?
   - Yes → Divide again by $(x - c)$ → get $q_2(x)$
   - No → Multiplicity = 1
4. Repeat until $q_k(c) \neq 0$
5. Multiplicity = number of successful divisions

**Method 3: Derivative Test** (advanced)
- Test $f(c), f'(c), f''(c), \ldots$ until first non-zero derivative

## Common Errors

**Error 1**: Confusing degree with multiplicity
```
Wrong: f(x) = (x-2)³ has multiplicity 3 means degree 3
Right: Multiplicity is 3, but degree depends on other factors too
```

**Error 2**: Assuming all zeros have multiplicity 1
```
Wrong: "Three zeros" always means three distinct x-intercepts
Right: Could be two zeros with one repeated (e.g., (x-1)²(x-3))
```

**Error 3**: Thinking even/odd refers to the zero value
```
Wrong: Zero at x = 2 (even number) bounces
Right: Multiplicity determines behavior, not the value of c
```

## Relations

- `[[Polynomial_Roots]]` - zeros are the roots; multiplicity describes how many times each appears
- `[[Factor_Theorem]]` - $(x-c)^k$ is factor ⟺ $c$ is zero of multiplicity $k$
- `[[Fundamental_Theorem_of_Algebra]]` - total number of zeros (counting multiplicities) equals degree
- `[[Polynomial_Graphs]]` - multiplicity determines graph behavior (cross vs bounce)
- `[[Derivatives]]` - multiplicity relates to number of derivatives that vanish at the zero
