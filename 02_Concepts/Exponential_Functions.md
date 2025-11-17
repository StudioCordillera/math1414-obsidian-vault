---
layout: concept
type: Topic
status: review
importance: high
title: Exponential Functions
topic: Functions & Exponential Growth
tags:
- concept/algebra
- chapter-4
- math/exponential
- method/reference
created: 2025-10-25
updated: 2025-11-16
review:
  next: 2025-11-25
relations:
  broader:
  - - - What_IS_a_Function
  depends_on:
  - - - Function_Notation
  - - - Domain_and_Range
  - - - Exponent_Properties
  - - - Graph_Transformations
  related:
  - - - Logarithmic_Functions
  - - - Inverse_Functions
  - - - Properties_of_Logarithms
  - - - Change_of_Base_Formula
  used_in:
  - - - Growth_and_Decay_Models
  - - - Compound_Interest
  - - - Exponential_Equations
  - - - Logarithmic_Equations
qa_certified: true
qa_date: 2025-11-16
qa_migration: v2.0
defines:
- '[[Exponent_Properties]]'
---
# Exponential Functions — Quick Reference (Complete)

Definition and forms
- Parent: f(x) = b^x with b > 0, b ≠ 1.
- General transform: f(x) = a·b^(x − h) + k.
  - a: vertical scale (a < 0 reflects over x-axis)
  - h: horizontal shift; k: vertical shift (moves asymptote to y = k)
- Continuous-base equivalence: b^x = e^(x ln b). Any A·b^x = A·e^{kx} with k = ln b.

Core properties and graph features
- Domain: (−∞, ∞)
- Range: (k, ∞) if a > 0; (−∞, k) if a < 0 (parent has (0, ∞))
- Horizontal asymptote: y = k (parent: y = 0)
- Monotonicity (for a > 0): b > 1 increasing; 0 < b < 1 decreasing
- Intercepts:
  - y-intercept: f(0) = a·b^(−h) + k
  - x-intercept(s): solve a·b^(x−h) + k = 0 (may not exist if range stays above/below asymptote)

Transformations from y = b^x
- y = b^(x − h): shift right by h
- y = b^x + k: shift up by k; asymptote becomes y = k
- y = a·b^x: vertical stretch by |a|; reflect if a < 0
- y = b^(−x) = (1/b)^x: reflection in y-axis (decreasing if b > 1)

One-to-one and inverse (logarithms)
- Exponentials are one-to-one, so inverses exist.
- If f(x) = a·b^(x − h) + k with a > 0, then f^−1(x) = log_b((x − k)/a) + h; domain of f^−1 requires (x − k)/a > 0.
- Special case: f(x) = b^x ⇄ f^−1(x) = log_b x (domain x > 0).

Exponent rules (b > 0, b ≠ 1)
- b^m·b^n = b^(m+n);  b^m/b^n = b^(m−n);  (b^m)^n = b^(mn);  b^0 = 1;  b^(−n) = 1/b^n.

Evaluation (including irrational exponents)
- Use b^x = e^(x ln b). Example: 5^π = e^{π ln 5}.

Solving exponential equations
- Equal bases: b^{f(x)} = b^{g(x)} ⇒ f(x) = g(x).
- General case: isolate b^{f(x)} ⇒ take ln (or log) ⇒ use ln(b^{f(x)}) = f(x) ln b ⇒ solve; check domain.
- With shifts: a·b^(x − h) + k = c ⇒ b^(x − h) = (c − k)/a ⇒ x = h + ln((c − k)/a)/ln b, requiring (c − k)/a > 0.

Growth/decay models and compounding
- Discrete per period g: P(t) = P0(1 + g)^t.
- Continuous: P(t) = P0·e^{kt} (k > 0 growth, k < 0 decay). Relation e^k = 1 + g ⇒ k = ln(1 + g).
- Finance: A = P(1 + r/n)^{nt};  A = P·e^{rt} (continuous).

Doubling time and half-life
- Continuous P = P0 e^{kt}: T_d = ln 2 / k;  T_{1/2} = −ln 2 / k.
- Discrete P = P0 b^t:  T_d = ln 2 / ln b;  T_{1/2} = ln(1/2)/ln b.

Build a model from two points (x1, y1), (x2, y2)
- Assume y = C·b^x with y1, y2 > 0.
- b = (y2/y1)^{1/(x2 − x1)};  C = y1 / b^{x1}.

Common errors
- Taking logs of nonpositive numbers; not isolating the exponential before logging.
- Forgetting vertical shift moves asymptote to y = k.
- Mixing discrete and continuous rates without conversion (k = ln(1 + r)).
- Percent vs decimal confusion (8% = 0.08).

Quick examples
- Solve 3^{x+1} = 7 ⇒ (x+1) ln 3 = ln 7 ⇒ x = ln 7/ln 3 − 1.
- Model from (0, 250), (3, 675): b = (675/250)^{1/3} ≈ 1.393; model y ≈ 250(1.393)^x.
- Doubling time for y = 5000 e^{0.07 t}: T_d = ln 2 / 0.07 ≈ 9.90.

Mastery checklist
- Identify base/parameters; state domain, range, asymptote, monotonicity.
- Graph by transformations from y = b^x.
- Evaluate b^x using e^{x ln b}.
- Solve exponential equations (equal base vs log-both-sides).
- Build models from data; compute doubling/half-life; find inverses with correct domain.

See also
- [[Logarithmic_Functions]], [[Inverse_Functions]], [[Properties_of_Logarithms]], [[Change_of_Base_Formula]], [[Growth_and_Decay_Models]], [[Compound_Interest]]
# One-to-one and inverse (logarithms)

Injectivity & Inverses (explicit)
- Certification: Exponential functions with b>0, b≠1 are strictly monotone on ℝ → one-to-one; pass [[Horizontal_Line_Test]].
- Consequence: For any a>0, h,k real, f(x)=a·b^{x−h}+k with a>0 is injective on ℝ; if a<0, injective as well but range flips and inverse requires attention to domain of output.
- Inverse domain/range: dom f=ℝ ⇒ dom f^{-1} is range of f: (k,∞) if a>0 and b>1 (or (−∞,k) if a>0 and 0<b<1); adjust if a<0.
- Verification: Always verify inverse via compositions and state domain/range explicitly.
- See: [[One_to_One_Function]], [[Inverse_Functions]].
# # Exponential Functions

Injectivity & Inverses (Chapter 4 integration)
- For b>0, b≠1, f(x)=b^x is strictly monotone on ℝ (increasing if b>1; decreasing if 0<b<1), hence one-to-one.
- Inverse function is log base b: f^{-1}(x)=\log_b x with domain (0,∞) and range ℝ.
- Solving: If b^{f(x)}=b^{g(x)} with valid domains, then f(x)=g(x) (by injectivity). Applying \log_b to both sides is justified by monotonicity.
- See also: [[One_to_One_Function]], [[Inverse_Functions]], [[Logarithmic_Functions]].