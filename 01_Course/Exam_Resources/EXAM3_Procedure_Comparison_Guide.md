---
type: Study_Guide
target: Exam3
status: active
importance: high
tags:
  - course/exam-resources
  - exam-3
  - chapter-4
  - procedure-comparison
  - transformation-recognition
  - exponential-logarithmic
created: 2025-01-27
updated: 2025-01-27
---

# Exam 3 Procedure Comparison Guide — Identical Procedures & Properties

## Overview

This guide focuses on **procedure-specific concept comparisons** for Exam 3 (Chapter 4: Exponential and Logarithmic Functions), identifying concepts that use **identical procedures or properties**. The primary example is **transformation recognition for functions compared to parent functions**.

Related: [[EXAM3_Quick_Reference_Card]], [[COMPREHENSIVE_LEARNING_OBJECTIVES_EXAM3]], [[Chapter4_Exponential_Logarithmic]]

---

## I. Function Transformation Recognition — Identical Procedures Across Function Types

### Core Procedure Pattern (Universal for ALL Function Types)
For any parent function $f(x)$ transformed to $g(x) = a \cdot f(x - h) + k$:

1. **Horizontal Shift**: $x - h$ → shift RIGHT by $h$ units (if $h > 0$)
2. **Vertical Scale**: $a$ → stretch by $|a|$, reflect over x-axis if $a < 0$
3. **Vertical Shift**: $+k$ → shift UP by $k$ units (if $k > 0$)
4. **Asymptote Movement**: Original asymptotes shift according to transformations

---

### Exponential Functions: $y = a \cdot b^{x-h} + k$

**Parent Function**: $y = b^x$ (where $b > 0, b \neq 1$)
- Domain: $(-\infty, \infty)$
- Range: $(0, \infty)$
- Horizontal Asymptote: $y = 0$
- Key Points: $(0, 1)$, $(1, b)$, $(-1, 1/b)$

**Transformed Function**: $y = a \cdot b^{x-h} + k$
- Domain: $(-\infty, \infty)$ (unchanged)
- Range: $(k, \infty)$ if $a > 0$; $(-\infty, k)$ if $a < 0$
- **Horizontal Asymptote**: $y = k$ (shifted from $y = 0$)
- Key Points Transformed: $(h, a + k)$, $(h+1, ab + k)$, $(h-1, a/b + k)$

**Example**: $f(x) = -2 \cdot 3^{x-1} + 5$
- Right 1, reflect + stretch by 2, up 5
- Asymptote: $y = 5$
- Key point: $(1, -2 + 5) = (1, 3)$

---

### Logarithmic Functions: $y = a \cdot \log_b(x-h) + k$

**Parent Function**: $y = \log_b x$ (where $b > 0, b \neq 1$)
- Domain: $(0, \infty)$
- Range: $(-\infty, \infty)$
- Vertical Asymptote: $x = 0$
- Key Points: $(1, 0)$, $(b, 1)$, $(1/b, -1)$

**Transformed Function**: $y = a \cdot \log_b(x-h) + k$
- Domain: $(h, \infty)$ (shifted from $(0, \infty)$)
- Range: $(-\infty, \infty)$ (unchanged)
- **Vertical Asymptote**: $x = h$ (shifted from $x = 0$)
- Key Points Transformed: $(h+1, k)$, $(h+b, a + k)$, $(h+1/b, -a + k)$

**Example**: $g(x) = 3 \cdot \log_2(x-4) - 1$
- Right 4, stretch by 3, down 1
- Asymptote: $x = 4$
- Key point: $(5, -1)$ since $\log_2(1) = 0$

---

## II. Inverse Function Recognition — Identical Verification Procedures

### Universal Inverse Verification Process
For functions $f$ and $g$ to be inverses:

1. **Composition Test 1**: $(f \circ g)(x) = f(g(x)) = x$ for all $x$ in domain of $g$
2. **Composition Test 2**: $(g \circ f)(x) = g(f(x)) = x$ for all $x$ in domain of $f$
3. **Domain/Range Swap**: Domain of $f$ = Range of $g$; Range of $f$ = Domain of $g$

**Identical Procedure for ALL Inverse Pairs**:

### Exponential-Logarithmic Inverse Pairs

**Example 1**: $f(x) = 2^x$ and $g(x) = \log_2 x$
- Check: $f(g(x)) = 2^{\log_2 x} = x$ ✓ (for $x > 0$)
- Check: $g(f(x)) = \log_2(2^x) = x$ ✓ (for all real $x$)

**Example 2**: $f(x) = e^{x+3} - 1$ and $g(x) = \ln(x+1) - 3$
- Check: $f(g(x)) = e^{(\ln(x+1) - 3) + 3} - 1 = e^{\ln(x+1)} - 1 = (x+1) - 1 = x$ ✓
- Check: $g(f(x)) = \ln((e^{x+3} - 1) + 1) - 3 = \ln(e^{x+3}) - 3 = (x+3) - 3 = x$ ✓

---

## III. Equation Solving — Identical Algebraic Procedures

### Same-Base Strategy (Identical Across Exponential and Logarithmic)

**For Exponentials**: If $b^{f(x)} = b^{g(x)}$, then $f(x) = g(x)$

**Example**: $4^{2x-1} = 4^{x+3}$
→ $2x - 1 = x + 3$
→ $x = 4$

**For Logarithms**: If $\log_b(f(x)) = \log_b(g(x))$, then $f(x) = g(x)$ (with domain checks)

**Example**: $\log_3(2x-1) = \log_3(x+5)$
→ $2x - 1 = x + 5$
→ $x = 6$
→ Check domain: $2(6) - 1 = 11 > 0$ ✓ and $6 + 5 = 11 > 0$ ✓

---

### Isolation and Logarithm/Exponentiation Strategy

**For Exponentials**: Isolate $b^{f(x)}$, then take $\ln$ of both sides

**Procedure**:
1. Isolate the exponential term
2. Take natural log of both sides
3. Use property: $\ln(b^{f(x)}) = f(x) \ln b$
4. Solve for $x$

**Example**: $5 \cdot 2^{3x} - 7 = 23$
→ $2^{3x} = 6$
→ $3x \ln 2 = \ln 6$
→ $x = \frac{\ln 6}{3 \ln 2}$

**For Logarithms**: Combine logs, then exponentiate both sides

**Procedure**:
1. Combine multiple logs using properties
2. Convert to exponential form
3. Solve the resulting equation
4. Check domain constraints

**Example**: $\ln(x-2) + \ln(x) = \ln(8)$
→ $\ln((x-2) \cdot x) = \ln(8)$
→ $x(x-2) = 8$
→ $x^2 - 2x - 8 = 0$
→ $x = 4$ or $x = -2$
→ Domain check: $x > 2$, so $x = 4$

---

## IV. Properties Application — Identical Manipulation Rules

### Logarithm Properties (Mirror Exponent Properties)

**Product Rule**: $\log_b(MN) = \log_b M + \log_b N$ ↔ $b^m \cdot b^n = b^{m+n}$

**Quotient Rule**: $\log_b(M/N) = \log_b M - \log_b N$ ↔ $b^m / b^n = b^{m-n}$

**Power Rule**: $\log_b(M^p) = p \log_b M$ ↔ $(b^m)^n = b^{mn}$

### Identical Expansion/Condensation Procedures

**Expansion Example**: $\ln\left(\frac{5x^3}{\sqrt{x-2}}\right)$

**Procedure** (identical for any base):
1. Identify products, quotients, powers
2. Apply properties systematically
3. State domain restrictions

**Solution**: $\ln 5 + 3\ln x - \frac{1}{2}\ln(x-2)$; Domain: $x > 2$

**Condensation Example**: $2\log_3 x - \frac{1}{2}\log_3 y + \log_3 7$

**Procedure** (identical for any base):
1. Convert coefficients to exponents
2. Combine sums as products, differences as quotients
3. State domain

**Solution**: $\log_3\left(\frac{7x^2}{\sqrt{y}}\right)$; Domain: $x > 0, y > 0$

---

## V. Change of Base — Identical Conversion Procedure

### Universal Change of Base Formula
$$\log_b x = \frac{\ln x}{\ln b} = \frac{\log x}{\log b}$$

**Identical Procedure for ANY Base**:
1. Choose target base (usually $e$ or $10$ for calculator)
2. Apply formula with chosen base
3. Evaluate numerically if needed

**Examples**:
- $\log_7 50 = \frac{\ln 50}{\ln 7} \approx 2.099$
- $\log_2 30 = \frac{\ln 30}{\ln 2} \approx 4.907$
- $\log_{1/3} 27 = \frac{\ln 27}{\ln(1/3)} = \frac{\ln 27}{-\ln 3} = -3$

---

## VI. Growth and Decay Models — Identical Parameter Relationships

### Continuous Models: $y(t) = y_0 e^{kt}$

**Identical Relationships for ALL Growth/Decay**:
- **Doubling Time**: $T_d = \frac{\ln 2}{k}$ (when $k > 0$)
- **Half-Life**: $T_{1/2} = \frac{\ln 2}{|k|}$ (when $k < 0$)
- **Rate Constant from Two Points**: $k = \frac{1}{t_2 - t_1} \ln\left(\frac{y_2}{y_1}\right)$

**Examples Using Identical Procedures**:

**Population Growth**: $P(t) = 1200e^{0.08t}$
- Doubling time: $T_d = \frac{\ln 2}{0.08} \approx 8.66$ years

**Radioactive Decay**: $A(t) = A_0 e^{-0.05t}$
- Half-life: $T_{1/2} = \frac{\ln 2}{0.05} \approx 13.86$ years

**Calibration from Data**: Population grows from 500 to 800 in 3 years
- $k = \frac{1}{3}\ln\left(\frac{800}{500}\right) = \frac{\ln(1.6)}{3} \approx 0.157$

---

## VII. Compound Interest — Identical Financial Formulas

### Universal Formulas (Identical Across All Applications)

**Periodic Compounding**: $A = P\left(1 + \frac{r}{n}\right)^{nt}$

**Continuous Compounding**: $A = Pe^{rt}$

**Solve for Time** (identical procedure):
- Periodic: $t = \frac{\ln(A/P)}{n \ln(1 + r/n)}$
- Continuous: $t = \frac{1}{r}\ln\left(\frac{A}{P}\right)$

**Example Applications** (same procedure):

**Investment Growth**: $5000 → $8000 at 6% compounded monthly
$t = \frac{\ln(8000/5000)}{12 \ln(1.005)} \approx 7.85$ years

**Loan Payoff**: Same formula structure, different interpretation

---

## VIII. Domain Analysis — Identical Constraint Procedures

### Universal Domain Rules

**For Exponentials**: $f(x) = a \cdot b^{g(x)} + k$
- Domain: Same as domain of $g(x)$ (no additional restrictions)

**For Logarithms**: $f(x) = a \cdot \log_b(g(x)) + k$
- Domain: Solve $g(x) > 0$ AND any restrictions from $g(x)$

**Multiple Logarithms**: Intersect ALL positivity conditions

**Identical Procedure**:
1. Identify each log argument
2. Set each argument $> 0$
3. Solve each inequality
4. Find intersection of solution sets

**Example**: $f(x) = \ln(x^2 - 9) + \log_2(x + 1)$
- Condition 1: $x^2 - 9 > 0$ → $x < -3$ or $x > 3$
- Condition 2: $x + 1 > 0$ → $x > -1$
- **Domain**: $x > 3$ (intersection)

---

## IX. Quick Recognition Patterns — Identical Visual Cues

### Transformation Recognition Checklist

**For ANY Function Type** (exponential, logarithmic, polynomial, etc.):

| Inside Function | Outside Function | Effect |
|----------------|------------------|---------|
| $f(x - h)$ | | Horizontal shift RIGHT by $h$ |
| $f(x + h)$ | | Horizontal shift LEFT by $h$ |
| | $a \cdot f(x)$ | Vertical stretch by $\|a\|$, reflect if $a < 0$ |
| | $f(x) + k$ | Vertical shift UP by $k$ |
| | $f(x) - k$ | Vertical shift DOWN by $k$ |

### Asymptote Movement (Identical Rules)

**Exponential**: $y = a \cdot b^{x-h} + k$
- Original asymptote $y = 0$ → New asymptote $y = k$

**Logarithmic**: $y = a \cdot \log_b(x-h) + k$
- Original asymptote $x = 0$ → New asymptote $x = h$

---

## X. Practice Problems — Identical Procedure Application

### Problem Set A: Transformation Recognition

1. **Exponential**: Describe transformations of $f(x) = -3 \cdot 2^{x+1} - 4$
2. **Logarithmic**: Describe transformations of $g(x) = 2 \log_5(x-3) + 1$

**Solution Process** (identical for both):
- Identify $a$, $h$, $k$ values
- Apply transformation rules
- State new domain/range/asymptotes

### Problem Set B: Inverse Verification

Verify these are inverse pairs using identical procedure:
1. $f(x) = 3^{x-2} + 1$ and $g(x) = \log_3(x-1) + 2$
2. $f(x) = \ln(2x) - 5$ and $g(x) = \frac{e^{x+5}}{2}$

### Problem Set C: Equation Solving

Solve using appropriate identical strategy:
1. **Same Base**: $5^{2x-1} = 5^{x+3}$
2. **Log Both Sides**: $3 \cdot 4^x - 7 = 20$
3. **Combine Logs**: $\log_2(x-1) + \log_2(x+3) = 4$

---

## XI. Error Pattern Recognition — Identical Mistakes Across Topics

### Common Error Types (Universal Across Chapter 4)

**Domain Errors**:
- Exponential: Assuming restricted domain (false - always all reals)
- Logarithmic: Forgetting positivity requirement
- **Prevention**: Always state and check domain conditions

**Asymptote Errors**:
- Forgetting asymptote shifts with transformations
- **Prevention**: Track how $h$ and $k$ affect asymptotes

**Algebraic Errors**:
- Splitting logs over addition: $\log(a+b) \neq \log a + \log b$
- **Prevention**: Review log properties vs. invalid operations

**Sign Errors**:
- Transformation direction confusion
- **Prevention**: Use specific numerical examples to verify

---

## XII. Mastery Checklist — Procedure Verification

### Core Procedures Mastered ✓

- [ ] **Function Transformations**: Can identify and apply $y = a \cdot f(x-h) + k$ for exponentials and logarithms
- [ ] **Inverse Verification**: Can verify inverse pairs using composition tests
- [ ] **Same-Base Solving**: Can equate exponents/arguments when bases match
- [ ] **Isolation Strategies**: Can solve by isolating and taking logs/exponentiating
- [ ] **Properties Application**: Can expand/condense logs using identical rules
- [ ] **Change of Base**: Can convert between bases using universal formula
- [ ] **Domain Analysis**: Can find domains for log expressions systematically
- [ ] **Growth/Decay Models**: Can calibrate and solve using identical parameter relationships
- [ ] **Compound Interest**: Can apply financial formulas consistently
- [ ] **Error Recognition**: Can identify and avoid common mistake patterns

---

## Related Resources

- [[EXAM3_Quick_Reference_Card]] — Formulas and key facts
- [[COMPREHENSIVE_LEARNING_OBJECTIVES_EXAM3]] — Complete topic coverage
- [[Chapter4_Exponential_Logarithmic]] — Full chapter extraction
- [[PRIORITIZED_STUDY_LIST_EXAM3]] — Study order recommendations
- [[Common_Errors_Guide]] — Detailed error analysis
- [[Practice_Problems]] — Additional problem sets

---

*Guide created for Math 1414 Exam 3 preparation focusing on procedure recognition and cross-concept patterns.*