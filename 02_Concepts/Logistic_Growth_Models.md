---
type: concept
status: active
tags:
  - concept/modeling
  - concept/applications
  - math/functions
  - math/exponentials
  - chapter-4
created: 2025-11-17
updated: 2025-11-17
---

# Logistic Growth Models

## Definition

A **logistic growth model** describes growth that is initially exponential but slows as it approaches a maximum capacity (carrying capacity). Unlike pure exponential growth, which increases without bound, logistic growth exhibits an S-shaped curve, reflecting real-world constraints like limited resources.

**Formal Statement**: A quantity growing logistically follows the model:
$$P(t) = \frac{L}{1 + ae^{-kt}}$$

where:
- $P(t)$ is the population (or quantity) at time $t$
- $L$ is the **carrying capacity** (maximum sustainable value)
- $a$ is a constant determined by initial conditions
- $k$ is the **growth rate** constant ($k > 0$)
- $t$ is time

**Significance**: Logistic models are more realistic than exponential models for population growth, disease spread, market saturation, and learning curves.

## Mathematical Expression

**Standard Form**:
$$P(t) = \frac{L}{1 + ae^{-kt}}$$

**Alternative Form** (using initial population $P_0$):
$$P(t) = \frac{L}{1 + \left(\frac{L - P_0}{P_0}\right)e^{-kt}}$$

where $P_0 = P(0)$ is the initial population.

**Key Behaviors**:
- **As $t \to 0$**: $P(t) \to P_0$ (initial value)
- **As $t \to \infty$**: $P(t) \to L$ (approaches carrying capacity)
- **At $t$ large and negative**: $P(t) \to 0$ (exponential term dominates)

**Inflection Point**: Maximum growth rate occurs at $P = \frac{L}{2}$ (half of carrying capacity)

## Example: Population Growth with Carrying Capacity

**Problem**: A population of deer in a forest follows the logistic model:
$$P(t) = \frac{500}{1 + 24e^{-0.3t}}$$

where $t$ is in years. Find:
(a) Initial population  
(b) Carrying capacity  
(c) Population after 10 years

**Part (a): Initial population**

Substitute $t = 0$:
$$P(0) = \frac{500}{1 + 24e^{0}} = \frac{500}{1 + 24(1)} = \frac{500}{25} = 20$$

**Answer**: Initial population is 20 deer.

**Part (b): Carrying capacity**

The carrying capacity is the coefficient $L$ in the numerator:
$$L = 500$$

**Answer**: Carrying capacity is 500 deer.

**Part (c): Population after 10 years**

Substitute $t = 10$:
$$P(10) = \frac{500}{1 + 24e^{-0.3(10)}} = \frac{500}{1 + 24e^{-3}}$$

Calculate $e^{-3} \approx 0.0498$:
$$P(10) = \frac{500}{1 + 24(0.0498)} = \frac{500}{1 + 1.195} = \frac{500}{2.195} \approx 228$$

**Answer**: After 10 years, the population is approximately 228 deer.

**Verification of behavior**:
- Initial: $P(0) = 20$ ✓
- Long-term: As $t \to \infty$, $e^{-0.3t} \to 0$, so $P(t) \to \frac{500}{1+0} = 500$ ✓
- Intermediate: $P(10) = 228$ is between 20 and 500 ✓

## Key Properties

- **S-shaped curve**: Slow start, rapid middle growth, levels off at carrying capacity
- **Three phases**:
  1. **Lag phase** ($t$ small): Nearly exponential growth, $P \ll L$
  2. **Log phase** (mid-range): Maximum growth rate near $P = L/2$
  3. **Stationary phase** ($t$ large): Growth slows, $P \to L$
- **Bounded**: $0 < P(t) < L$ for all $t$
- **Horizontal asymptote**: $y = L$ (carrying capacity is upper limit)
- **Symmetry**: Curve is symmetric about inflection point at $P = L/2$

## Comparison with Exponential Growth

| Property | Exponential: $P(t) = P_0 e^{kt}$ | Logistic: $P(t) = \frac{L}{1 + ae^{-kt}}$ |
|----------|----------------------------------|-------------------------------------------|
| **Long-term behavior** | Unbounded growth | Approaches carrying capacity $L$ |
| **Curve shape** | J-curve (always increasing rate) | S-curve (rate decreases after inflection) |
| **Realism** | Unrealistic for long-term | More realistic (resource limits) |
| **Growth rate** | Constant percentage | Decreases as $P \to L$ |

## Real-World Applications

- **Population biology**: Animal populations in limited ecosystems
- **Epidemiology**: Disease spread in finite population (SIR models)
- **Market adoption**: Product saturation (early adopters → mainstream → saturation)
- **Learning curves**: Skill acquisition (rapid initial learning → plateau)
- **Technology diffusion**: New technology adoption rates

## Relations

- `[[Exponential_Growth]]` - logistic growth reduces to exponential when $P \ll L$
- `[[Carrying_Capacity]]` - the limiting value $L$ in logistic models
- `[[Exponential_Functions]]` - the $e^{-kt}$ term drives the transition from growth to plateau
- `[[Horizontal_Asymptotes]]` - logistic functions have horizontal asymptote at $y = L$
- `[[Mathematical_Modeling]]` - logistic model is key example of realistic population modeling
