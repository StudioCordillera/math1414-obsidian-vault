---
type: Chapter
status: complete
importance: high
tags:
  - course/textbook
  - chapter-4
  - math/exponential
  - math/logarithmic
created: 2025-10-25
updated: 2025-11-04
---

# Chapter 4 — Exponential and Logarithmic Functions

Structure (to extract)
- 4.1 Inverse Functions
- 4.2 Exponential Functions
- 4.3 Logarithmic Functions
- 4.4 Properties of Logarithms
- 4.5 Exponential and Logarithmic Equations
- 4.6 Applications (Growth/Decay, Compound Interest)

Methodology
- Extract explicit methods, implicit prerequisites, common errors (6 taxonomy), worked examples.
- Build relational framework: depends_on chains and See Also networks.

Relational Integration Targets
- [[What_IS_a_Function]]
- [[Function_Notation]]
- [[Domain_and_Range]]
- [[Function_Composition]]
- [[Graphing_Functions]]

To-Do
- [x] Extract 4.1 with examples and methods
- [x] Extract 4.2 with examples and methods
- [x] Extract 4.3 with examples and methods
- [x] Extract 4.4 with examples and methods
- [x] Extract 4.5 with examples and methods
- [x] Extract 4.6 with applications and models

Recent Activity
- 2025-10-25 — Created scaffold and relational targets.
- 2025-10-30 — Drafted 4.1–4.6 extractions.
- 2025-11-01 — Added textbook-style example blocks (4.3–4.5) and verified core concept links exist.
- 2025-11-01 — Integrated all examples into section flows; removed duplicate Status/notes; unified To-Do; removed stray header; verified cross-links; basic QA pass.
- 2025-11-02 — Added Quick Reference (complete) under 4.2; updated date; QA alignment retained.


## 4.1 Inverse Functions — Extraction (draft)

> See [[Inverse_Functions]] and [[One_to_One_Function]] for detailed theory.

Orientation and targets
- Objectives: Identify one-to-one functions; define and verify inverse functions; compute f^{-1} for eligible f; handle domain restrictions.
- Relational anchors: [[What_IS_a_Function]], [[Function_Notation]], [[Domain_and_Range]], [[Function_Composition]], [[Graphing_Functions]]
- Core concepts: [[One_to_One_Function]], [[Horizontal_Line_Test]], [[Inverse_Functions]]

Key definitions and facts
- One-to-one: f is one-to-one iff a ≠ b implies f(a) ≠ f(b). Graphically: passes the horizontal line test.
- Inverse function: For a one-to-one f, f^{-1} satisfies f ∘ f^{-1} = id and f^{-1} ∘ f = id on appropriate domains.
- Graph symmetry: Graphs of f and f^{-1} are reflections across y = x. Domain(f) = Range(f^{-1}); Range(f) = Domain(f^{-1}).
- Notation alert: f^{-1} means inverse function, not reciprocal 1/f.

Methods (step-by-step)
- Method A: Determine if a function is one-to-one
  Steps (graphical):
  1) Sketch/plot representative points or use known graph. 2) Apply horizontal line test. 3) Conclude one-to-one if no horizontal line hits >1 point.
  Steps (algebraic):
  1) Assume f(a) = f(b). 2) Manipulate to deduce a = b. 3) If deduction holds for all a,b in domain, f is one-to-one.
  Preconditions: f’s rule and domain specified. Output: Boolean.
  Common errors: Confusing vertical vs horizontal line tests; ignoring domain restrictions.

- Method B: Verify two functions are inverses
  Steps: 1) Compute f(g(x)); simplify; check equals x on domain(g). 2) Compute g(f(x)); check equals x on domain(f).
  Preconditions: Domains clarified. Output: True/False.
  Common errors: Checking only one composition; ignoring domain mismatches that invalidate equality “for all x.”

- Method C: Find f^{-1} for a one-to-one f
  Steps: 1) Replace f(x) with y. 2) Swap x and y. 3) Solve explicitly for y. 4) Rename y as f^{-1}(x). 5) State domain/range correctly.
  Checks: Verify compositions on stated domains; ensure any branch choice matches domain restrictions (e.g., +√ vs −√).
  Common errors: Failing to swap variables; not restricting domain for non-one-to-one functions; forgetting to state domain/range of f^{-1}.

- Method D: Create an inverse via domain restriction (quadratics, trig, etc.)
  Steps: 1) Identify interval where f is monotone. 2) Restrict domain to that interval. 3) Apply Method C. 4) State the restricted domain and corresponding range.

Worked examples (concise)
- Example 1 (Linear): f(x) = 3x − 1 → swap/solve → f^{-1}(x) = (x + 1)/3. One-to-one globally (nonzero slope).
- Example 2 (Rational): f(x) = (3 − x)/(x + 3). Swap and solve → f^{-1}(x) = (3 − 3x)/(x + 1), with domain x ≠ −1 (matching range restriction of f).
- Example 3 (Quadratic with restriction): m(x) = x^2 + 4, x ≥ 0. Swap → x = y^2 + 4 → y = +√(x − 4). So m^{-1}(x) = √(x − 4), domain x ≥ 4.

Explicit knowledge (stated in text)
- Horizontal Line Test characterizes one-to-one.
- Composition identities define inverses. Symmetry across y = x holds.
- Domain/range swap between a function and its inverse.

Implicit knowledge (assumptions/prereqs)
- Solving equations reliably (isolate variables, handle radicals/rationals).
- Domain awareness: algebraic steps like squaring can introduce extraneous possibilities (branch choice must match domain).
- Inverse may fail to be a function if the original was not one-to-one on its domain.

Common errors (taxonomy)
- Notation: treating f^{-1} as 1/f.
- Conceptual: thinking every function has an inverse function without restriction.
- Domain/Range: forgetting to restrict domain for non-monotone functions; not stating domain/range of f^{-1}.
- Algebraic: swapping steps incorrectly; losing constraints after squaring or taking roots.
- Graphical: confusing horizontal vs vertical line tests.
- Validation: checking only one composition; not checking domain conditions of the identities.

Relational framework
- Depends on: [[What_IS_a_Function]], [[Domain_and_Range]], [[Function_Composition]], [[Graphing_Functions]].
- Defines/uses: [[Inverse_Functions]], [[One_to_One_Function]], [[Horizontal_Line_Test]].
- Used in: [[Exponential_Functions]] ↔ [[Logarithmic_Functions]] (inverses); solving equations in [[Exponential_Equations]] and [[Logarithmic_Equations]].
- See also: [[Function_Operations]], [[Piecewise_Functions]] (domain restrictions), [[Absolute_Value]] (piecewise inverses by branch).

Mastery checklist (4.1)
- Can certify one-to-one by graph or algebra.
- Can compute f^{-1} and state domain/range accurately.
- Can enforce domain restrictions to create an inverse.
- Can verify inverses with compositions and domain checks.

---

## 4.2 Exponential Functions — Extraction (draft)

> See [[Exponential_Functions]], [[Growth_and_Decay_Models]], and [[Compound_Interest]] for comprehensive coverage.

Orientation and targets
- Objectives: Define and graph b^x (b>0, b≠1); understand base e; apply compound interest; model growth/decay and half-life.
- Relational anchors: [[Exponent_Properties]], [[Graph_Transformations]], [[Domain_and_Range]], [[Average_Rate_of_Change]].
- Core concepts: [[Exponential_Functions]], [[Growth_and_Decay_Models]], [[Compound_Interest]], [[Half_Life]], [[Doubling_Time]], [[e (constant)|e]].

Definition and properties
- Exponential function (base b): f(x)=b^x, b>0, b≠1.
- Graph features: Domain (−∞,∞); Range (0,∞); Horizontal asymptote y=0; Passes (0,1). Increasing if b>1; decreasing if 0<b<1.
- Base e: e = lim_{n→∞} (1+1/n)^n ≈ 2.71828; natural exponential f(x)=e^x.

Methods (step-by-step)
- Method A: Graph f(x)=ab^{x−h}+k via transformations
  Steps: 1) Start parent y=b^x. 2) Horizontal shift h, vertical shift k, vertical scale a, reflect if a<0. 3) Track asymptote: y=k.
  Common errors: Using wrong asymptote after vertical shift; mixing up left/right shift sign.

- Method B: Evaluate e^x and b^x (incl. irrational exponents)
  Steps: Use calculator e^x or b^x; or rewrite b^x = e^{x ln b}. For irrational exponents, interpret via limits/continuity.
  Common errors: Treating negative base as valid for all real exponents (domain fails for non-integer exponents).

- Method C: Compound interest
  Formulas: A = P(1 + r/n)^{nt}; A = Pe^{rt} (continuous).
  Steps: Identify P, r, n, t; choose correct formula; compute A; interest = A − P.
  Common errors: Omitting “+1” in periodic compounding; using r as percent instead of decimal; mixing t and n.

- Method D: Growth/Decay models
  Forms: y = y_0 e^{kt} (k>0 growth, k<0 decay). Half-life h: y = y_0 (1/2)^{t/h} = y_0 e^{(ln 1/2)(t/h)}.
  Steps: Calibrate k (or h) from a data point; solve for unknowns via logs.
  Common errors: Wrong sign on k; forgetting units on h or t; applying (1/2)^{h/t} instead of (1/2)^{t/h}.

Worked examples (concise)
- Graph: f(x)=3^{x−2}+4 → shift right 2, up 4; asymptote y=4; increasing; sample points from 3^x table.
- Continuous compounding: A=Pe^{rt}. For P=$5000, r=0.065, t=10 → A = 5000 e^{0.65} (compute as needed).
- Half-life: A(t)=A_0 (1/2)^{t/1620} for Ra-226; evaluate at integer multiples of h to see halving.

Explicit knowledge (stated in text)
- Domain/range and asymptote behavior of b^x and e^x; definition of e via a limit; compounding formulas; half-life interpretation.

Implicit knowledge (assumptions/prereqs)
- Exponent rules (Chapter R), calculator literacy (exp/log keys), transformation maps from [[Graph_Transformations]].
- Asymptote interpretation: “approaches” not “reaches”; range strictly positive.

Common errors (taxonomy)
- Conceptual: Calling b=1 or b<0 “exponential functions”; misreading asymptote as x-axis always after shifts.
- Procedural: Dropping +1 in (1+r/n); wrong n or t; rounding prematurely.
- Algebraic: Using (ab)^x = a^x b^x incorrectly when a depends on x; mishandling ln when solving for t.
- Domain/Range: Claiming negative outputs for pure b^x; allowing b<0.
- Calculator: Using log instead of ln (or vice versa) without change-of-base when needed.

Relational framework
- Depends on: [[Exponent_Properties]], [[Graph_Transformations]], [[Domain_and_Range]].
- Defines/uses: [[e (constant)|e]], [[Growth_and_Decay_Models]], [[Compound_Interest]], [[Half_Life]], [[Doubling_Time]].
- Used in: [[Logarithmic_Functions]] (inverse), [[Exponential_Equations]], [[Logarithmic_Equations]], modeling in 4.6.
- See also: [[Change_of_Base_Formula]] to evaluate b^x via e^{x ln b}; [[Average_Rate_of_Change]] for growth comparisons.

Mastery checklist (4.2)
- Can graph shifted/scaled exponentials and state asymptotes.
- Can evaluate and compare b^x values (growth vs decay).
- Can solve finance (periodic/continuous) and half-life/doubling problems.
- Can move between b^x and e^{x ln b} comfortably.

### Textbook-style examples (4.2)
- [Ex 4.2.1] Graph with reflections and shifts
  - f(x) = -3·2^{x+1} - 4. Steps: Parent y=2^x; left 1; reflect/scale by -3; down 4. Asymptote y = -4. Domain: (−∞, ∞); Range: (−∞, −4). (uses [[Graph_Transformations]], [[Exponential_Functions]])
- [Ex 4.2.2] Time to target with periodic compounding
  - 7500→12000 at 5.2% monthly. t = ln(1.6)/(12·ln(1+0.052/12)) ≈ 9.06 years. (uses [[Compound_Interest]])
- [Ex 4.2.3] Doubling time (discrete annual growth)
  - A = A_0(1.08)^t; t = ln 2 / ln 1.08 ≈ 9.01 years. (uses [[Change_of_Base_Formula]])
- [Ex 4.2.4] Model from two points
  - Points (1,12), (4,96) → y = 6·2^x. (uses [[Exponential_Functions]])
- [Ex 4.2.5] Evaluate irrational exponent
  - 10^{2.3} = e^{2.3 ln 10} ≈ 199.53. (uses [[Change_of_Base_Formula]])

#### Quick Reference — Exponential Functions (Complete)
(see also [[Exponential_Functions]], [[Change_of_Base_Formula]], [[Growth_and_Decay_Models]], [[Compound_Interest]], [[Half_Life]], [[Doubling_Time]])

1) Definition and general forms
- Parent: f(x) = b^x with b > 0, b ≠ 1.
- General transform: f(x) = a·b^(x − h) + k.
  - a: vertical scale; a < 0 reflects over x-axis.
  - h: horizontal shift; k: vertical shift (moves asymptote to y = k).
- Continuous-base equivalence: b^x = e^(x ln b). Any A·b^x = A·e^(kx) with k = ln b.

2) Core properties and graph features
- Domain: (−∞, ∞).  Horizontal asymptote: y = k.
- Range: (k, ∞) if a > 0; (−∞, k) if a < 0 (unshifted parent: (0, ∞)).
- Monotonicity (parent a > 0): b > 1 increasing; 0 < b < 1 decreasing.
- Intercepts:
  - y-intercept: f(0) = a·b^(−h) + k.
  - x-intercept(s): solve a·b^(x−h) + k = 0; may not exist (e.g., a > 0, k ≥ 0).

3) Transformations from y = b^x
- y = b^(x − h): right by h.  y = b^x + k: up by k (asymptote y = k).
- y = a·b^x: vertical stretch |a|, reflect if a < 0.
- y = b^(−x) = (1/b)^x: reflection in y-axis (decreasing if b > 1).

4) One-to-one and inverse (logarithms)
- Exponentials are one-to-one, so inverses exist (logarithms).
- If f(x) = a·b^(x − h) + k (a > 0), then f^−1(x) = log_b((x − k)/a) + h.
  Domain of f^−1: x such that (x − k)/a > 0. Range: (−∞, ∞).
- Special: f(x) = b^x ⇄ f^−1(x) = log_b x.

5) Exponent rules (b > 0, b ≠ 1)
- b^m·b^n = b^(m+n);  b^m/b^n = b^(m−n);  (b^m)^n = b^(mn);  b^0 = 1;  b^(−n) = 1/b^n.

6) Evaluating b^x (incl. irrational x)
- Compute via b^x = e^(x ln b). Example: 5^π = e^(π ln 5).

7) Solving exponential equations
- Same base: b^{f(x)} = b^{g(x)} ⇒ f(x) = g(x).
- General: isolate b^{f(x)}; take ln; use ln(b^{f(x)}) = f(x) ln b; solve; check.
- With shifts: a·b^(x − h) + k = c ⇒ x = h + ln((c − k)/a)/ln b, requiring (c − k)/a > 0.

8) Growth/decay models and compounding
- Discrete per period g: P(t) = P0(1 + g)^t.
- Continuous: P(t) = P0·e^{kt} (k > 0 growth, k < 0 decay). Relation: e^k = 1 + g → k = ln(1 + g).
- Finance: A = P(1 + r/n)^{nt};  A = P·e^{rt} (continuous).

9) Doubling time and half-life
- Continuous P = P0 e^{kt}:  T_d = ln 2 / k;  T_1/2 = −ln 2 / k.
- Discrete P = P0 b^t:  T_d = ln 2 / ln b;  T_1/2 = ln(1/2)/ln b.

10) Build a model from two points (x1, y1), (x2, y2)
- Assume y = C·b^x with y1, y2 > 0.
- b = (y2/y1)^{1/(x2 − x1)};  C = y1 / b^{x1}.

11) Common errors
- Not isolating the exponential before logging; logging negatives/zero.
- Forgetting asymptote shift y = k; assuming x-intercepts when range forbids.
- Mixing discrete/continuous rates without conversion (k = ln(1 + r)).
- Percent vs decimal confusion (8% = 0.08).

12) Quick worked examples
- A) Solve 5^{2x − 1} = 3^{x + 2} → (2x − 1) ln 5 = (x + 2) ln 3 → x = (ln 5 + 2 ln 3)/(2 ln 5 − ln 3) ≈ 1.24.
- B) 200 = 120(1.08)^t → t = ln(5/3)/ln 1.08 ≈ 5.94.
- C) Through (0, 250), (3, 675): b = (675/250)^{1/3} ≈ 1.393; model y ≈ 250(1.393)^x.
- D) P(t) = 5000 e^{0.07 t}: doubling time T_d = ln 2 / 0.07 ≈ 9.90.
- E) N(t) = N0 e^{−0.023 t}: half-life T_1/2 ≈ ln 2 / 0.023 ≈ 30.1.
- F) Inverse: f(x) = 2^{x − 3} + 5 → f^−1(x) = log_2(x − 5) + 3; domain x > 5.

13) Mastery checklist
- Identify parameters/base; state domain, range, asymptote, monotonicity.
- Graph via transformations; evaluate b^x using e^{x ln b}.
- Solve exponential equations (same base vs log-both-sides).
- Build models from two points and rates; compute doubling/half-life.
- Find inverses with correct domain/range.

---

## 4.3 Logarithmic Functions — Extraction (draft)

> See [[Logarithmic_Functions]], [[Natural_Logarithm]], and [[Change_of_Base_Formula]] for detailed theory.

Orientation and targets
- Objectives: Define logarithms as inverses of exponentials; convert between log and exponential forms; evaluate ln and log; graph logs and interpret domains/asymptotes.
- Relational anchors: [[Inverse_Functions]] ↔ [[Exponential_Functions]]; [[Domain_and_Range]]; [[Graph_Transformations]].
- Core concepts: [[Logarithmic_Functions]], [[Natural_Logarithm]], [[Common_Logarithm]], [[Change_of_Base_Formula]].

Definitions and core facts
- Definition (inverse): y = log_b(x) iff b^y = x, with base b>0, b≠1.
- Domain: (0, ∞). Range: (−∞, ∞). Vertical asymptote: x = 0. Key points: (1,0), (b,1), (1/b, −1).
- Monotonicity: Increasing if b>1; decreasing if 0<b<1.
- Special bases: Natural log ln(x) = log_e(x); Common log log(x) = log_{10}(x).
- Inverse symmetry: log graphs reflect exponential graphs across y = x.

Methods (step-by-step)
- Method A: Convert forms
  Steps: b^y = x ⇄ y = log_b x. Use to evaluate exact values (e.g., log_3 27 = 3) and to rewrite equations for solving.
  Errors: Treating log_b(x) as log(x)/b; forgetting base constraints.

- Method B: Evaluate logs (exact/approximate)
  Steps: 1) Exact by recognition (powers of base). 2) Otherwise use calculators: ln, log. 3) For base b, use change-of-base: log_b x = ln x / ln b (or log x / log b).
  Domain check: Require x>0.

- Method C: Graph y = a + c·log_b(x − h)
  Steps: 1) Start with y = log_b x. 2) Horizontal shift to x = h (asymptote). 3) Vertical shift a; vertical stretch/reflect by c. 4) Plot anchor points from preimage: x − h = 1, b, 1/b.
  Errors: Misplacing asymptote after horizontal shift; attempting x≤0 inputs.

- Method D: Domain analysis for log expressions
  Steps: For expressions like log_b(g(x)), solve g(x) > 0. For sums/differences, each log argument must be positive.
  Errors: Allowing zero/negative arguments; forgetting to intersect domain conditions across multiple logs.

Worked examples (concise)
- Example 1: Convert/evaluate. b^y = 1/125 with b=5 → y = log_5(1/125) = −3.
- Example 2: Approximate. log_7(20) = ln 20 / ln 7 ≈ (2.9957)/(1.9459) ≈ 1.54.
- Example 3: Graph transform. y = 2 + 3·log_2(x − 4): asymptote x=4; base points at x=5 (y=2), x=6 (y≈2+3·1=5), x=4.5 (y≈2+3·(−1)=−1).
- Example 4: Domain. ln(x^2 − 9) requires x^2 − 9 > 0 → x < −3 or x > 3.

Implicit knowledge
- Logarithms undo exponentials; composition ln(e^x)=x and e^{ln x}=x hold on their domains.
- Calculator care: understanding ln vs log and using change-of-base when base ≠ e or 10.

Common errors (taxonomy)
- Domain: Plugging nonpositive x into log; ignoring domain from composed expressions.
- Notation: Writing log_b x = log x / b; confusing ln with log.
- Graphical: Treating y=0 as the asymptote; forgetting vertical asymptote moves to x=h.

Relational framework
- Depends on: [[Inverse_Functions]], [[Exponential_Functions]], [[Domain_and_Range]], [[Graph_Transformations]].
- Defines/uses: [[Logarithmic_Functions]], [[Natural_Logarithm]], [[Common_Logarithm]], [[Change_of_Base_Formula]].
- Used in: [[Properties_of_Logarithms]], [[Logarithmic_Equations]], modeling in 4.6.

Mastery checklist (4.3)
- Can convert between b^y=x and y=log_b x.
- Can evaluate ln/log and use change-of-base to compute log_b x.
- Can graph transformed logs and state domain/asymptote.
- Can state/solve domain conditions for log expressions.

### Textbook-style examples (4.3)
- [Ex 4.3.1] Evaluate and approximate
  - a) log_3(27) = 3
  - b) log_2(1/8) = −3
  - c) log_5(20) = ln 20 / ln 5 ≈ 2.9957 / 1.6094 ≈ 1.86
- [Ex 4.3.2] Domain analysis
  - Find the domain of f(x) = ln(x^2 − 9). Condition: x^2 − 9 > 0 → x < −3 or x > 3.
- [Ex 4.3.3] Graph transform
  - y = 2 + 3·log_2(x − 4). Asymptote: x = 4. Anchor points: x = 5 → y = 2; x = 6 → y = 5; x = 4.5 → y ≈ −1.
- [Ex 4.3.4] Solve with domain check
  - Solve log_3(x) + log_3(x−2) = 2. Domain: x>2.
  - Combine: log_3(x(x−2))=2 ⇒ x^2−2x=9 ⇒ x^2−2x−9=0 ⇒ x = 1 ± √10.
  - Domain keeps x = 1 + √10 ≈ 4.162; reject 1 − √10. (uses [[Properties_of_Logarithms]], [[Logarithmic_Equations]])
- [Ex 4.3.5] Evaluate with a base < 1
  - log_{1/4}(64) = −3 since (1/4)^{−3} = 4^3 = 64. (uses [[Logarithmic_Functions]])
- [Ex 4.3.6] Graph transform and domain
  - y = log_5(2x+10) − 3. Asymptote from 2x+10=0 → x = −5. Domain x> −5.
  - Anchors: 2x+10 = 1 → x = −4 → y = −3; 2x+10 = 5 → x = −2.5 → y = −2; 2x+10 = 1/5 → x = −4.5 → y = −4. (uses [[Graph_Transformations]], [[Logarithmic_Functions]])
- [Ex 4.3.7] Solve log equation (single log)
  - log_5(2x−3) = 2 ⇒ 2x−3 = 25 ⇒ x = 14; domain x>1.5 ✓. (uses [[Logarithmic_Equations]])
- [Ex 4.3.8] Graph with scale/shift/reflection
  - g(x) = 1 − 2·ln(x+3). Asymptote x = −3; domain x> −3; monotone decreasing (−2 factor). (uses [[Graph_Transformations]])

---

## 4.4 Properties of Logarithms — Extraction (draft)

Orientation and targets
- Objectives: Use product, quotient, and power properties; expand/condense log expressions; apply change-of-base.
- Relational anchors: [[Exponent_Properties]] ↔ log properties by inversion; [[Algebraic_Manipulation]].
- Core concepts: [[Properties_of_Logarithms]], [[Change_of_Base_Formula]].

Properties (for b>0, b≠1; M,N>0; p real)
- Product: log_b(MN) = log_b M + log_b N.
- Quotient: log_b(M/N) = log_b M − log_b N.
- Power: log_b(M^p) = p·log_b M.
- Base identities: log_b 1 = 0; log_b b = 1.
- Change-of-base: log_b x = (ln x)/(ln b) = (log x)/(log b).

Methods (step-by-step)
- Method A: Expand a log expression
  Steps: 1) Identify products/quotients/powers inside the log. 2) Apply properties to write as a sum/difference of logs and pull exponents out front. 3) Ensure all arguments remain positive expressions.
  Errors: Splitting across addition inside log: log(M+N) ≠ log M + log N.

- Method B: Condense to a single log
  Steps: 1) Push coefficients inside as exponents. 2) Combine sums as products and differences as quotients. 3) State final base and domain requirements.
  Errors: Losing parentheses when converting differences to quotients.

- Method C: Evaluate/compare using change-of-base
  Steps: Rewrite to ln or log base your calculator supports; compare magnitudes by evaluating numerically or by monotonicity when bases equal.

Worked examples (concise)
- Expand: ln(5x^3/√(x−2)) = ln 5 + ln x^3 − ln (x−2)^{1/2} = ln 5 + 3 ln x − (1/2) ln(x−2); domain x>2.
- Condense: 2 log_3(x) − (1/2) log_3(y) + log_3(7) = log_3(x^2) − log_3(y^{1/2}) + log_3(7) = log_3(7x^2/√y); domain x>0, y>0.
- Change-of-base: log_2(50) = ln 50/ln 2 ≈ 5.643/0.693 ≈ 8.14.

Implicit knowledge
- Properties derive from exponent rules: e.g., b^{log_b M + log_b N} = MN.
- Domain constraints accompany every manipulation (arguments > 0).

Common errors (taxonomy)
- Misuse: Splitting log over addition/subtraction; forgetting to distribute exponents when pulling/pushing.
- Domain: Dropping positivity constraints after condensation/expansion.

Relational framework
- Depends on: [[Exponent_Properties]], [[Logarithmic_Functions]].
- Defines/uses: [[Properties_of_Logarithms]], [[Change_of_Base_Formula]].
- Used in: [[Exponential_Equations]], [[Logarithmic_Equations]], modeling calibrations.

Mastery checklist (4.4)
- Can expand and condense log expressions correctly.
- Can apply change-of-base to compute or simplify log_b x.
- Keeps track of domain constraints through manipulations.

### Textbook-style examples (4.4)
- [Ex 4.4.1] Expand fully and state domain
  - ln(5x^3/√(x−2)) = ln5 + 3 ln x − (1/2) ln(x−2); domain x>2.
- [Ex 4.4.2] Condense to a single logarithm
  - 2 log_3 x − (1/2) log_3 y + log_3 7 = log_3(7x^2/√y); domain x>0, y>0.
- [Ex 4.4.3] Change of base and compare
  - Compare log_2 50 and log_3 50: log_2 50 ≈ ln50/ln2 ≈ 5.64/0.693 ≈ 8.14; log_3 50 ≈ 5.64/1.10 ≈ 5.13 → log_2 50 > log_3 50.
- [Ex 4.4.4] Expand fully and state domain
  - log_2( √(x^2−9) / ( x (x+1)^3 ) ) = (1/2) log_2(x^2−9) − log_2 x − 3 log_2(x+1).
  - Domain: x^2−9>0 and x>0 and x+1>0 ⇒ x>3. (uses [[Properties_of_Logarithms]])
- [Ex 4.4.5] Condense to a single natural log
  - (1/2) ln(3x) + 2 ln(x−1) − ln 5 = ln( (3x)^{1/2} (x−1)^2 / 5 ). Domain: x>1. (uses [[Properties_of_Logarithms]])
- [Ex 4.4.6] Symbolic evaluation via p, q
  - Given p = log_b 2 and q = log_b 3, find log_b(54/√6).
  - 54/√6 = 9·√6 ⇒ log_b 9 + (1/2) log_b 6 = 2q + (1/2)(p+q) = (1/2)p + (5/2)q. (uses [[Properties_of_Logarithms]])
- [Ex 4.4.7] Fully worked expansion (with domain)
  - ln((x+2)^3 √y / (5(x−1)^2)) = 3 ln(x+2) + (1/2) ln y − ln 5 − 2 ln(x−1); domain: x>−2, x≠1, y>0. (uses [[Properties_of_Logarithms]])
- [Ex 4.4.8] Fully worked condensation
  - 4 log_7 a − 2 log_7 b + log_7 3 = log_7(3a^4/b^2); domain: a>0, b>0. (uses [[Properties_of_Logarithms]])

---

## 4.5 Exponential and Logarithmic Equations — Extraction (draft)

Orientation and targets
- Objectives: Solve equations involving b^x and log_b x; choose methods (match bases, isolate and log/exp both sides, combine logs and exponentiate); check solutions against domains.
- Relational anchors: [[Algebraic_Equations]], [[Properties_of_Logarithms]], [[Exponent_Properties]].
- Core concepts: [[Exponential_Equations]], [[Logarithmic_Equations]].

Solution workflows
- Exponential equations
  A) Same-base strategy: If a·b^{f(x)} = c·b^{g(x)}, divide and equate exponents f(x)=g(x) when a=c or after isolating b^{...}.
  B) General strategy: Isolate b^{f(x)}; take ln (or log) both sides; use ln(b^{f(x)})=f(x)·ln b; solve for x; check.

- Logarithmic equations
  A) Single log: log_b(f(x)) = k → rewrite as f(x) = b^k; solve; check f(x)>0.
  B) Many logs: Combine to one log using properties; then exponentiate. Always enforce each log’s argument > 0 before solving, and check solutions.

- Mixed equations
  Use inverse relationships to isolate x (e.g., ln both sides when e^{...} present; apply log to power to bring exponent down).

Common pitfalls and checks
- Always state and apply domain requirements: log arguments > 0; bases b>0, b≠1.
- After algebra, plug candidates back to detect extraneous solutions (esp. from squaring or from domain violations in logs).

Worked examples (concise)
- Exponential (same base): 5^{2x−1} = 125 → 125 = 5^3 → 2x−1 = 3 → x = 2.
- Exponential (general): 3^{x+1} = 7 → take ln: (x+1) ln 3 = ln 7 → x = ln 7/ln 3 − 1 ≈ 0.771.
- Log (single): log_4(2x−1) = 3 → 2x−1 = 4^3 = 64 → x = 32.5; check 2x−1>0 ✓.
- Log (combined): ln(x−2) + ln x = ln 12 → ln((x−2)x)=ln 12 → x(x−2)=12 → x^2−2x−12=0 → x=6 or x=−2 → domain x>2 → x=6.
- Mixed: 7·e^{0.2x} = 40 → e^{0.2x}=40/7 → 0.2x = ln(40/7) → x = 5·ln(40/7) ≈ 8.34.

Mastery checklist (4.5)
- Selects appropriate strategy (match base vs logs) and executes cleanly.
- Brings exponents down via logs and combines logs correctly.
- Checks domain and extraneous solutions.

### Textbook-style examples (4.5)
- [Ex 4.5.1] Same-base exponential
  - 5^{2x−1} = 125 = 5^3 ⇒ 2x−1 = 3 ⇒ x = 2.
- [Ex 4.5.2] General exponential (log both sides)
  - 3^{x+1} = 7 ⇒ (x+1) ln 3 = ln 7 ⇒ x = ln 7/ln 3 − 1 ≈ 0.771.
- [Ex 4.5.3] Single-log equation with domain check
  - log_4(2x−1) = 3 ⇒ 2x−1 = 64 ⇒ x = 32.5; require 2x−1>0 ⇒ x>0.5 ✓.
- [Ex 4.5.4] Combined logs → one log → exponentiate
  - ln(x−2) + ln x = ln 12 ⇒ ln(x(x−2)) = ln 12 ⇒ x^2−2x−12=0 ⇒ {−2,6}; domain x>2 ⇒ x=6.
- [Ex 4.5.5] Exponential with shift/constant
  - 4·5^{x} + 7 = 60 ⇒ 5^{x} = 53/4 ⇒ x = log_5(53/4) = ln(13.25)/ln 5 ≈ 1.61. (uses [[Logarithmic_Equations]])
- [Ex 4.5.6] Combine logs then solve
  - ln x − ln(x−4) = 2 ⇒ ln(x/(x−4)) = 2 ⇒ x/(x−4) = e^2 ⇒ x = 4e^2/(e^2−1) ≈ 4.63; domain: x>4. (uses [[Properties_of_Logarithms]])
- [Ex 4.5.7] Equation with logs on both sides
  - log_2(x+1) = 1 − log_2(x−3) ⇒ log_2((x+1)(x−3)) = 1 ⇒ (x+1)(x−3) = 2 ⇒ x = 1 ± √6; domain x>3 ⇒ keep x ≈ 3.449.
- [Ex 4.5.8] Fully worked: isolate exponential, take logs
  - 9·e^{0.3x} − 12 = 25 ⇒ e^{0.3x} = 37/9 ⇒ x = (1/0.3) ln(37/9) ≈ 4.71. (uses [[Exponential_Equations]])
- [Ex 4.5.9] Fully worked: combine logs → exponentiate
  - log_2(x−1) + log_2(x+3) = 4 ⇒ (x−1)(x+3) = 16 ⇒ x^2+2x−19=0 ⇒ x = −1 ± 2√5; domain x>1 ⇒ keep x ≈ 3.472. (uses [[Properties_of_Logarithms]])

---

## 4.6 Applications — Growth/Decay, Finance, Logistic — Extraction (draft)

Orientation and targets
- Objectives: Model growth/decay with exponentials; compute compound interest (periodic/continuous); solve for time/rate using logs; understand logistic growth basics.
- Relational anchors: [[Growth_and_Decay_Models]], [[Compound_Interest]], [[Half_Life]], [[Doubling_Time]], [[Logistic_Growth]].

Templates and methods
- Continuous exponential model: y(t) = y_0·e^{kt}.
  Calibration: Given (t_1, y_1), k = (1/t_1)·ln(y_1/y_0). Doubling time T_d = ln 2 / k; half-life h = ln(1/2)/k.

- Periodic compounding: A = P(1 + r/n)^{nt}; Continuous compounding: A = P·e^{rt}.
  Solve for t: t = (1/(n ln(1+r/n)))·ln(A/P); or t = (1/r)·ln(A/P).
  Solve for r (continuous): r = (1/t)·ln(A/P).

- Decay/half-life: A(t) = A_0·(1/2)^{t/h} = A_0·e^{(ln 1/2)(t/h)}.
  Find h from data: If A(t_1)=α·A_0, then h = (t_1·ln 1/2)/(ln α).

- Logistic growth (overview): P(t) = L / (1 + A·e^{−kt}), L>0 carrying capacity.
  Initial condition P(0)=P_0 → A = (L−P_0)/P_0. Midpoint/inflection at P = L/2 when t = (1/k)·ln A.
  Solving for t from a data point P(t)=P_1: t = (1/k)·[ln A − ln((L/P_1) − 1)].

Worked examples (concise)
- Finance (time to double, continuous): A = P·e^{rt}; A/P = 2 → t = ln 2 / r. For r=6% → t ≈ 11.55 years.
- Finance (periodic): P=$3000 at 4.5% compounded monthly to A=$5000: t = ln(5000/3000) / (12·ln(1+0.045/12)) ≈ 9.89 years.
- Growth calibration: Bacteria count 200 → 500 in 3 h: k = (1/3) ln(500/200) ≈ 0.305; model y = 200·e^{0.305 t}. Doubling time ≈ ln 2 / 0.305 ≈ 2.27 h.
- Decay/half-life: Tritium h ≈ 12.3 y; after 30 y: A = A_0·(1/2)^{30/12.3} ≈ 0.145·A_0.
- Logistic (parameter fit with given L): If L=10,000, P_0=500 → A=(10000−500)/500=19. Given P(6)=3000 and k unknown: 3000 = 10000/(1+19 e^{−6k}) → 1+19 e^{−6k} = 10/3 → 19 e^{−6k} = 7/3 → e^{−6k} = 7/57 → k = −(1/6) ln(7/57) ≈ 0.349.

Implicit knowledge
- Units: Keep consistent time units across k, t, n.
- Interpretation: Asymptote y=0 for decay; horizontal asymptote y=k-shifted for transformed exponentials; logistic capped at L.

Common errors (taxonomy)
- Using percent instead of decimal for r; mixing time units; wrong placement of t in (1/2)^{t/h}; assuming logistic behaves like pure exponential indefinitely.

Relational framework
- Depends on: [[Exponential_Functions]], [[Logarithmic_Functions]], [[Properties_of_Logarithms]].
- Defines/uses: [[Compound_Interest]], [[Doubling_Time]], [[Half_Life]], [[Logistic_Growth]].
- Used in: Problem solving and modeling across 4.2–4.6; connects to future topics in differential modeling.

Mastery checklist (4.6)
- Can set up and calibrate exponential models from data.
- Can compute compound interest and solve for unknown time/rate.
- Can work with half-life/doubling-time and basic logistic forms.

### Textbook-style examples (4.6)
- [Ex 4.6.1] Half-life calibration
  - A(6) = 0.70 A_0 ⇒ k = (1/6) ln 0.70 ≈ −0.0598 ⇒ h = ln(1/2)/k ≈ 11.59 y. (uses [[Growth_and_Decay_Models]], [[Half_Life]])
- [Ex 4.6.2] Logistic parameter k from a data point
  - L=12000, P_0=600 ⇒ A=19. Given P(10)=8000 ⇒ e^{−10k} = 1/38 ⇒ k = (1/10) ln 38 ≈ 0.363. (uses [[Logistic_Growth]])
- [Ex 4.6.3] Find nominal rate with periodic compounding
  - P = 10,000 → A = 15,000 in 6 y, n=12 ⇒ r = 12[(1.5)^{1/72} − 1] ≈ 6.78%. (uses [[Compound_Interest]])
- [Ex 4.6.4] Decay: time to reach a fraction
  - A(t) = A_0 e^{−0.12 t}. Solve A = 0.20 A_0 ⇒ t = ln 0.20 / (−0.12) ≈ 13.41 h. (uses [[Growth_and_Decay_Models]])
- [Ex 4.6.5] Logistic: time to 90% of carrying capacity
  - t = (1/k) ln(9A). Example A=19, k≈0.349 ⇒ t ≈ 14.7 (units). (uses [[Logistic_Growth]])

---

Status/notes
- 2025-10-30 — Added draft extractions for 4.3–4.6 with definitions, methods, examples, errors, and relational links. Next: tighten examples to textbook problem styles and verify cross-link targets exist; then mark To-Do checkboxes complete for 4.3–4.6.
- 2025-10-30 — Completed draft extractions for 4.3–4.6; checked To-Do items; ready for cross-link verification and example refinement.
- 2025-11-01 — Integrated examples into main sections; deduplicated Status/notes; unified To-Do; removed stray header; verified cross-links; basic QA pass complete.
- 2025-11-02 — Added Quick Reference (complete) under 4.2; QA alignment retained.


---
## Appendix — Quick References (Chapter 4)

### Quick Reference — Logarithmic Functions (Complete)
(see also [[Logarithmic_Functions]], [[Natural_Logarithm]], [[Common_Logarithm]], [[Change_of_Base_Formula]], [[Inverse_Functions]], [[Exponential_Functions]])

- Definition: y = log_b x iff b^y = x with b>0, b≠1.
- Domain: (0, ∞). Range: (−∞, ∞). Vertical asymptote: x = 0.
- Key points: (1,0), (b,1), (1/b, −1). Increasing if b>1; decreasing if 0<b<1.
- Special logs: ln x = log_e x; log x = log_{10} x.
- Inverse identities: b^{log_b x} = x (x>0); log_b(b^y) = y.
- Transform: y = a + c·log_b(x − h) → asymptote x = h; c scales/reflects, a shifts.
- Change of base: log_b x = ln x / ln b = log x / log b.
- Domain analysis: For log_b(g(x)), require g(x) > 0. Intersect all such conditions if multiple logs.
- Properties preview: product, quotient, power (see 4.4).
- Solving patterns:
  - Single log: log_b(f(x)) = k ⇒ f(x) = b^k; require f(x) > 0.
  - Combined logs: use properties to one log ⇒ exponentiate ⇒ solve ⇒ check domain.
- Common errors: Allowing nonpositive arguments; splitting over addition; misplacing asymptote after shifts; ignoring base constraints b>0, b≠1.
- Micro examples: log_7(49) = 2; log_{1/3}(27) = −3; log_3(x) + log_3(x−2) = 2 ⇒ x = 1 + √10 (domain x>2).

### Quick Reference — Properties of Logarithms (Complete)
(see also [[Properties_of_Logarithms]], [[Exponent_Properties]], [[Change_of_Base_Formula]])

- For base b>0, b≠1 and positive M, N, real p:
  - Product: log_b(MN) = log_b M + log_b N.
  - Quotient: log_b(M/N) = log_b M − log_b N.
  - Power: log_b(M^p) = p·log_b M.
  - Identities: log_b 1 = 0; log_b b = 1.
  - Change of base: log_b x = ln x / ln b = log x / log b.
- Expansion workflow: identify products/quotients/powers → apply rules → keep arguments positive.
- Condensation workflow: push coefficients as exponents → combine sums/differences → state domain.
- Domain tracking: every log argument must remain > 0 after each step.
- Do not: split over addition/subtraction inside arguments, e.g., log(M+N) ≠ log M + log N.
- Micro examples:
  - Expand with domain: ln(5x^3/√(x−2)) = ln 5 + 3 ln x − (1/2) ln(x−2); x>2.
  - Condense: 2 log_3 x − (1/2) log_3 y + log_3 7 = log_3(7x^2/√y); x>0, y>0.

### Quick Reference — Exponential and Logarithmic Equations (Complete)
(see also [[Exponential_Equations]], [[Logarithmic_Equations]], [[Properties_of_Logarithms]])

- Exponential equations
  - Same base: b^{f(x)} = b^{g(x)} ⇒ f(x) = g(x).
  - General: isolate b^{f(x)} ⇒ take ln (or log) ⇒ solve; require isolated right side > 0.
  - With shifts: a·b^{x−h} + k = c ⇒ b^{x−h} = (c−k)/a ⇒ x = h + ln((c−k)/a)/ln b; require (c−k)/a > 0.
- Logarithmic equations
  - Single log: log_b(f(x)) = k ⇒ f(x) = b^k; require f(x) > 0.
  - Sum/difference: combine using properties to one log ⇒ exponentiate ⇒ solve; intersect domain conditions first.
- Mixed equations: use inverse pairs (ln with e^x; log_b with b^x) to isolate x.
- Always check: domain of logs (arguments > 0), extraneous solutions after algebraic manipulations.
- Micro examples:
  - 3^{x+1} = 7 ⇒ (x+1) ln 3 = ln 7 ⇒ x = ln 7/ln 3 − 1.
  - ln(x−2) + ln x = ln 12 ⇒ x^2 − 2x − 12 = 0 ⇒ x=6 (domain x>2).
  - log_2(x+1) = 1 − log_2(x−3) ⇒ log_2((x+1)(x−3)) = 1 ⇒ x = 1 + √6, domain x>3.

### Quick Reference — Applications: Growth/Decay, Finance, Logistic (Complete)
(see also [[Growth_and_Decay_Models]], [[Compound_Interest]], [[Half_Life]], [[Doubling_Time]], [[Logistic_Growth]])

- Continuous model: y(t) = y_0 e^{k t} (k>0 growth, k<0 decay).
  - From two points: k = (1/Δt) ln(y_2/y_1) when times differ by Δt and model holds.
  - Doubling/half-life: T_d = ln 2 / k; T_{1/2} = −ln 2 / k.
- Discrete model: y(t) = y_0 b^t, b = 1+g per period.
  - Convert: k = ln b; b = e^k; T_d = ln 2 / ln b.
- Finance:
  - Periodic compounding: A = P(1 + r/n)^{n t}.
  - Continuous compounding: A = P e^{r t}.
  - Solve for t: t = ln(A/P)/(n ln(1 + r/n)) or t = (1/r) ln(A/P).
  - Solve for r (periodic): r = n[(A/P)^{1/(n t)} − 1]; (continuous): r = (1/t) ln(A/P).
- Decay fraction/time: A(t) = A_0 e^{k t}; for target fraction q (0<q<1): t = ln q / k.
- Logistic (overview): P(t) = L/(1 + A e^{−k t}); A = (L − P_0)/P_0; inflection at P = L/2 when t = (1/k) ln A.
  - Solve for t given P_1: t = (1/k)[ln A − ln((L/P_1) − 1)].
- Micro examples:
  - Time to reach 0.2 of initial with k = −0.12: t = ln(0.2)/−0.12 ≈ 13.41.
  - Nominal rate (monthly): P→A in t years: r = 12[(A/P)^{1/(12 t)} − 1].
  - Logistic calibration (given L, P_0, P(t)): k = −(1/t) ln( (L/P(t)) − 1 ) + (1/t) ln A, where A = (L − P_0)/P_0; example from 4.6 gives k ≈ 0.349.


### Practice — Exponential Functions (4.2)

Instructions
- Solve symbolically when possible; give decimal approximations to 3–4 sig figs. Show domain checks where applicable.

1) Evaluate 7^{−2.5}
Answer: 7^{−2.5} = e^{−2.5 ln 7} ≈ 0.01998

2) Write a model through (0, 120) and (4, 540) assuming y = C·b^x
Answer: b = (540/120)^{1/4} = (4.5)^{1/4} ≈ 1.456; C = 120; y ≈ 120(1.456)^x

3) Graph features: f(x) = −2·3^{x−1} + 5
Answer: Domain (−∞, ∞); Range (−∞, 5); Asymptote y = 5; y-intercept f(0) = −2·3^{−1} + 5 = −2/3 + 5 = 13/3 ≈ 4.333; Decreasing (a < 0 reflects);

4) Solve 2^{3x+1} = 10
Answer: (3x+1) ln 2 = ln 10 ⇒ x = (ln 10/ln 2 − 1)/3 ≈ 0.768

5) Solve 5·4^{x} − 7 = 60
Answer: 4^{x} = 67/5 ⇒ x = ln(67/5)/ln 4 ≈ 2.408

6) Continuous compounding: P = 8000 grows at 4.2% for 9 years
Answer: A = 8000 e^{0.042·9} ≈ 8000 e^{0.378} ≈ $11,459.47

7) Periodic compounding: $3000 at 5.4% compounded monthly for t years to reach $5000; find t
Answer: t = ln(5000/3000) / (12·ln(1 + 0.054/12)) ≈ 9.07 years

8) Doubling time: y = 250 e^{0.063 t}
Answer: T_d = ln 2 / 0.063 ≈ 11.00 time units

9) Half-life: N(t) = N_0 e^{−0.085 t}; find T_{1/2}
Answer: T_{1/2} = ln 2 / 0.085 ≈ 8.159

10) Inverse function and domain: f(x) = 3^{x+2} − 7
Answer: y + 7 = 3^{x+2} ⇒ log_3(y + 7) = x + 2 ⇒ f^{−1}(x) = log_3(x + 7) − 2; Domain of f^{−1}: x > −7


### Practice — Logarithmic Functions (4.3)
Instructions
- Solve symbolically when possible; include domain checks. Approximate to 3–4 sig figs when needed.

1) Evaluate: log_3(1/27)
Answer: −3

2) Approximate: log_7(50)
Answer: ln 50 / ln 7 ≈ 2.099

3) Convert and solve: log_5(3x − 4) = 2
Answer: 3x − 4 = 25 ⇒ x = 29/3; require x > 4/3 ✓

4) Combine then solve: log_2(x) + log_2(x − 3) = 4
Answer: log_2(x(x − 3)) = 4 ⇒ x^2 − 3x = 16 ⇒ x = (3 ± √73)/2; domain x > 3 ⇒ x = (3 + √73)/2 ≈ 5.772

5) Domain: f(x) = ln(2x^2 − 8x)
Answer: 2x^2 − 8x > 0 ⇒ 2x(x − 4) > 0 ⇒ x < 0 or x > 4

6) Graph features: g(x) = 1 − 2·log_3(x + 6)
Answer: Asymptote x = −6; domain x > −6; decreasing (−2 factor); points: x = −5 → y = 1; x = −3 → y = −1; x = −5.667 → y = 3

7) Evaluate base < 1: log_{1/5}(125)
Answer: −3 (since (1/5)^{−3} = 125)

8) Solve: ln(x) − ln(x − 2) = 1
Answer: ln(x/(x − 2)) = 1 ⇒ x/(x − 2) = e ⇒ x = 2e/(e − 1) ≈ 3.164; domain x > 2 ✓

9) Expand and state domain: ln(7x^2/√(x − 1))
Answer: ln 7 + 2 ln x − (1/2) ln(x − 1); domain x > 1

10) Change of base exact: log_4(30)
Answer: ln 30 / ln 4 (or log 30 / log 4)

---

### Practice — Properties of Logarithms (4.4)
Instructions
- Expand or condense fully. State domain restrictions.

1) Expand: ln(9x^3/√(x − 2))
Answer: ln 9 + 3 ln x − (1/2) ln(x − 2); domain x > 2

2) Condense: 2 log_5(x) − (1/2) log_5(y) + log_5(3)
Answer: log_5(3x^2/√y); domain x > 0, y > 0

3) Expand: log_2( (x + 1)^4 / (x(x − 3)) )
Answer: 4 log_2(x + 1) − log_2 x − log_2(x − 3); domain x > 3

4) Condense to ln of a single expression: (1/3) ln(2x) + ln(x − 4) − ln 7
Answer: ln( (2x)^{1/3} (x − 4) / 7 ); domain x > 4

5) Evaluate symbolically given p = log_b 2, q = log_b 3: find log_b(108/√6)
Answer: 108/√6 = 18√6 ⇒ log_b 18 + (1/2) log_b 6 = (log_b 2 + 2 log_b 3) + (1/2)(log_b 2 + log_b 3) = (3/2)p + (5/2)q

6) Identify error: “log(x + y) = log x + log y”
Answer: False. No log rule for sums/differences inside the argument.

7) Change of base compare: Which is larger, log_2 30 or log_3 30?
Answer: ln 30/ln 2 ≈ 4.907; ln 30/ln 3 ≈ 3.096 ⇒ log_2 30 > log_3 30

8) Expand with careful domain: ln( (x − 2)^2 √(y + 1) / (5y) )
Answer: 2 ln(x − 2) + (1/2) ln(y + 1) − ln 5 − ln y; domain x > 2, y > 0

---

### Practice — Exponential and Logarithmic Equations (4.5)
Instructions
- Isolate, choose strategy (match base vs log/exp), solve, and check domain.

1) 9^{x − 2} = 27^{2x}
Answer: 9 = 3^2, 27 = 3^3 ⇒ 3^{2(x − 2)} = 3^{6x} ⇒ 2x − 4 = 6x ⇒ x = −1

2) 5^{2x + 1} = 11
Answer: (2x + 1) ln 5 = ln 11 ⇒ x = (ln 11/ln 5 − 1)/2 ≈ 0.206

3) 4·3^{x} − 7 = 20
Answer: 3^{x} = 27/4 ⇒ x = ln(27/4)/ln 3 ≈ 1.262

4) log_4(x − 1) + log_4(x + 5) = 2
Answer: log_4((x − 1)(x + 5)) = 2 ⇒ x^2 + 4x − 5 = 16 ⇒ x^2 + 4x − 21 = 0 ⇒ x = 3 or x = −7; domain x > 1 ⇒ x = 3

5) ln(x) − ln(x − 4) = 2
Answer: ln(x/(x − 4)) = 2 ⇒ x/(x − 4) = e^2 ⇒ x = 4e^2/(e^2 − 1) ≈ 4.63; domain x > 4 ✓

6) log_2(x + 1) = 1 − log_2(x − 3)
Answer: log_2((x + 1)(x − 3)) = 1 ⇒ (x + 1)(x − 3) = 2 ⇒ x^2 − 2x − 5 = 0 ⇒ x = 1 ± √6; domain x > 3 ⇒ x ≈ 3.449

7) e^{0.3x} − 5e^{0.15x} = 0
Answer: Let u = e^{0.15x} > 0 ⇒ u^2 − 5u = 0 ⇒ u(u − 5) = 0 ⇒ u = 5 ⇒ e^{0.15x} = 5 ⇒ x = (1/0.15) ln 5 ≈ 10.73

8) 2^{x+1} + 2^{x} = 48
Answer: 2^{x}(2 + 1) = 48 ⇒ 2^{x} = 16 ⇒ x = 4

9) ln(x^2 − 9) = 2
Answer: x^2 − 9 = e^2 ⇒ x = ±√(e^2 + 9); domain x^2 − 9 > 0 ⇒ both valid: x ≤ −3 or x ≥ 3

10) log_5(x) − 2 log_5(3) = 1
Answer: log_5(x/9) = 1 ⇒ x/9 = 5 ⇒ x = 45; domain x > 0 ✓

---

### Practice — Applications (4.6)
Instructions
- Choose the right model (discrete vs continuous vs logistic). Keep units consistent.

1) Continuous compounding: P = 6000 at r = 3.9% for 7 years
Answer: A = 6000 e^{0.039·7} ≈ $7,923.51

2) Periodic compounding: P = 4500 at r = 5.1% compounded quarterly; find t to reach A = 9000
Answer: t = ln(9000/4500)/(4 ln(1 + 0.051/4)) ≈ 13.60 years

3) Calibrate growth rate: N(0) = 120, N(5) = 360; model N = 120 e^{kt}
Answer: k = (1/5) ln(360/120) = (1/5) ln 3 ≈ 0.2197; N(t) = 120 e^{0.2197 t}

4) Doubling time (continuous): P(t) = P0 e^{0.056 t}
Answer: T_d = ln 2 / 0.056 ≈ 12.38 time units

5) Half-life: A(t) = A0 e^{−0.087 t}
Answer: T_{1/2} = ln 2 / 0.087 ≈ 7.965

6) Logistic time to reach 90% of L: P(t) = L/(1 + A e^{−kt}), with L = 10,000, P0 = 400 ⇒ A = (10000 − 400)/400 = 24; k = 0.31
Answer: 0.9L = L/(1 + A e^{−kt}) ⇒ t = (1/k) ln(9A) = (1/0.31) ln(216) ≈ 17.2 time units

7) Find nominal annual rate r with monthly compounding: P = 10,000 grows to 14,000 in t = 8 years
Answer: r = 12[(1.4)^{1/(12·8)} − 1] ≈ 3.93%

8) Decay to a fraction: A(t) = A0 e^{−0.12 t}. Time to reach 15% of A0
Answer: t = ln(0.15)/(−0.12) ≈ 15.8 time units
# ### Textbook-style examples (4.3)
#### Quick Reference — Logarithmic Functions (Complete)
(see also [[Logarithmic_Functions]], [[Natural_Logarithm]], [[Common_Logarithm]], [[Change_of_Base_Formula]], [[Inverse_Functions]], [[Exponential_Functions]])

1) Definition and inverse relationship
- log_b(x) is the inverse of b^x, with base b > 0, b ≠ 1.
- Inverse equivalence: y = log_b(x) ⇔ b^y = x.
- Domain: x > 0. Range: (−∞, ∞).
- Notation: ln x = log_e x; log x = log_{10} x (common log).
- Monotonicity: b > 1 → increasing; 0 < b < 1 → decreasing.

2) Core properties (x, y > 0; b > 0, b ≠ 1)
- Product: log_b(xy) = log_b x + log_b y
- Quotient: log_b(x/y) = log_b x − log_b y
- Power: log_b(x^r) = r·log_b x (valid for real r; requires x > 0)
- Identities: log_b b = 1, log_b 1 = 0; b^{log_b x} = x; log_b(b^x) = x
- Change-of-base: log_b x = ln x / ln b = log x / log b

3) Graph features and transformations
- Parent: y = log_b x; passes (1,0) and (b,1) (if b>1); vertical asymptote x = 0
- General transform: y = a·log_b(x − h) + k
  - Domain: x > h; Asymptote: x = h; a scales/reflects; k shifts vertically
  - Key points from parent transformed: (h + 1, k), (h + b, k + a)

4) Evaluation and simplification
- Use change-of-base: log_b x = ln x / ln b (or log x / log b)
- For 0 < b < 1: ln b < 0, so signs flip in inequalities when comparing via logs
- Examples: log_2 8 = 3; log_10 0.01 = −2; ln e^π = π; 10^{log x} = x (x > 0)

5) Expanding and condensing
- Expand: log_b(12x^2/3y) = log_b 12 + 2 log_b x − log_b 3 − log_b y
- Condense: 2 ln(x − 1) + 1/2 ln(x + 3) − ln 5 = ln[(x − 1)^2 (x + 3)^{1/2} / 5]

6) Solving logarithmic equations (workflow)
- Isolate and combine logs into one when possible; then exponentiate
- Single log: log_b(f(x)) = c ⇒ f(x) = b^c (require f(x) > 0)
- Sum/difference: log_b A ± log_b B ⇒ log_b(AB) or log_b(A/B)
- Domain check: each log argument > 0; reject extraneous solutions

7) Common errors
- Taking log of nonpositive numbers; splitting over +/− inside a log (invalid)
- Forgetting asymptote shift x = h for y = a·log_b(x − h) + k
- Mixing bases incorrectly in change-of-base

8) Modeling and linearization
- If y = C·b^x, then ln y = ln C + x ln b (linear in x) → fit slope ln b, intercept ln C
- Scientific contexts: pH = −log_10[H+]; decibels dB = 10 log_10(I/I0)

9) Quick worked examples
- A) Solve log_3(2x − 1) = 4 ⇒ 2x − 1 = 81 ⇒ x = 41; domain x > 1/2 ✓
- B) Solve ln(x + 5) − ln(2x − 1) = 0 ⇒ (x + 5)/(2x − 1) = 1 ⇒ x = 6; domain x > 1/2 ✓
- C) 2 log_5(x − 1) + log_5 4 = 3 ⇒ log_5[4(x − 1)^2] = 3 ⇒ x = 1 + (5√5)/2; domain x > 1 ✓

10) Mastery checklist
- State domain/range/asymptote and monotonicity for y = a·log_b(x − h) + k
- Convert between log and exponential forms; apply product/quotient/power rules
- Solve log equations with isolation/combination and domain checks
- Use change-of-base; recognize linearization of exponential data via ln
# ### Textbook-style examples (4.4)
#### Quick Reference — Properties of Logarithms (Complete)
(see also [[Properties_of_Logarithms]], [[Exponent_Properties]], [[Change_of_Base_Formula]])

1) Core properties (b>0, b≠1; M,N>0; p real)
- Product: log_b(MN) = log_b M + log_b N
- Quotient: log_b(M/N) = log_b M − log_b N
- Power: log_b(M^p) = p·log_b M
- Identities: log_b 1 = 0; log_b b = 1
- Change-of-base: log_b x = ln x / ln b = log x / log b

2) Workflows
- Expand: identify products/quotients/powers → apply rules → keep each argument positive
- Condense: push coefficients as exponents → combine sums/differences → one log of a single positive expression

3) Domain tracking
- Every log argument must remain > 0 at each step; intersect constraints when multiple logs appear

4) Common errors
- Splitting across addition inside a log: log(M+N) ≠ log M + log N
- Losing parentheses when converting differences to quotients
- Dropping domain conditions after manipulation

5) Quick examples
- Expand with domain: ln(5x^3/√(x−2)) = ln 5 + 3 ln x − (1/2) ln(x−2); domain x>2
- Condense: 2 log_3 x − (1/2) log_3 y + log_3 7 = log_3(7x^2/√y); x>0, y>0
- Compare: log_2 50 vs log_3 50 → ln50/ln2 ≈ 8.14 > ln50/ln3 ≈ 5.13

6) Mastery checklist
- Expand/condense correctly with domain statements
- Apply change-of-base reliably
- Map log properties to exponent rules
# ### Textbook-style examples (4.5)
#### Quick Reference — Exponential and Logarithmic Equations (Complete)
(see also [[Exponential_Equations]], [[Logarithmic_Equations]], [[Properties_of_Logarithms]])

1) Exponential equations
- Same base: b^{f(x)} = b^{g(x)} ⇒ f(x) = g(x)
- General: isolate b^{f(x)} ⇒ take ln/log ⇒ solve; require isolated side > 0
- With shifts: a·b^{x−h} + k = c ⇒ b^{x−h} = (c−k)/a ⇒ x = h + ln((c−k)/a)/ln b; require (c−k)/a > 0

2) Logarithmic equations
- Single log: log_b(f(x)) = k ⇒ f(x) = b^k; require f(x) > 0
- Many logs: combine with properties ⇒ one log ⇒ exponentiate ⇒ solve; enforce each argument > 0

3) Mixed equations
- Use inverse pairs (ln with e^x; log_b with b^x) to isolate x

4) Always check
- Domains of logs (arguments > 0); extraneous solutions from squaring or invalid arguments

5) Micro examples
- 3^{x+1} = 7 ⇒ (x+1) ln 3 = ln 7 ⇒ x = ln 7/ln 3 − 1
- ln(x−2) + ln x = ln 12 ⇒ x=6 (domain x>2)
- log_2(x+1) = 1 − log_2(x−3) ⇒ x = 1 + √6, domain x>3


### Practice — Logarithmic Functions (4.3) — Additions
11) Evaluate exact: log_{1/4}(64)
Answer: −3 (since (1/4)^{−3} = 64)

12) Solve with domain: log_2(x) + log_2(x − 2) = 3
Answer: log_2(x(x − 2)) = 3 ⇒ x^2 − 2x = 8 ⇒ x = 1 ± 3; domain x > 2 ⇒ x = 4

13) Graph transform quick check: y = −2 log_3(x − 1) + 4
Answer: Asymptote x = 1; domain x > 1; points: x = 2 → y = 4; x = 4 → y = 2; decreasing due to −2 factor


---

## 🔗 RELATED CONCEPTS

This chapter connects to these concept nodes in the vault:

### Function Foundations
- [[Inverse_Functions]] - Core relationship between exponential and logarithmic (Sections 4.1, 4.2, 4.3)
- [[One_to_One_Function]] - Requirement for inverse functions (Section 4.1)
- [[Horizontal_Line_Test]] - Verifying one-to-one property (Section 4.1)
- [[Function_Composition]] - Verifying inverse relationships (Section 4.1)

### Exponential Functions & Models
- [[Exponential_Functions]] - Base b^x functions (Section 4.2)
- [[e (constant)]] - Natural exponential base (Section 4.2)
- [[Growth_and_Decay_Models]] - Applications (Sections 4.2, 4.6)
- [[Compound_Interest]] - Financial applications (Section 4.2)
- [[Half_Life]] - Decay modeling (Section 4.2)
- [[Doubling_Time]] - Growth modeling (Section 4.2)

### Logarithmic Functions
- [[Logarithmic_Functions]] - Inverse of exponential (Section 4.3)
- [[Natural_Logarithm]] - Base e logarithm (Section 4.3)
- [[Common_Logarithm]] - Base 10 logarithm (Section 4.3)
- [[Change_of_Base_Formula]] - Converting between bases (Sections 4.3, 4.4)
- [[Properties_of_Logarithms]] - Product, quotient, power rules (Section 4.4)

### Equation Solving
- [[Exponential_Equations]] - Solving b^x = c (Section 4.5)
- [[Logarithmic_Equations]] - Solving log equations (Section 4.5)

### Supporting Concepts
- [[Domain_and_Range]] - Function analysis (all sections)
- [[Exponent_Properties]] - Foundation for exponentials (Section 4.2)
- [[Graph_Transformations]] - Shifting and scaling (Sections 4.2, 4.3)

### Advanced Applications
- [[Logistic_Growth]] - Bounded growth model (Section 4.6)
- [[Exponential_Regression]] - Data modeling (applications)

---
## Textbook Page Links — Chapter 4 (for quick reference)
- Exponential functions: [[00_Books/Algebra_by_section/pages/p440]]–[[00_Books/Algebra_by_section/pages/p448]]
- Logarithmic functions: [[00_Books/Algebra_by_section/pages/p455]]–[[00_Books/Algebra_by_section/pages/p464]]
- Properties/Change-of-base: [[00_Books/Algebra_by_section/pages/p471]]–[[00_Books/Algebra_by_section/pages/p477]]
- Exponential/log equations: [[00_Books/Algebra_by_section/pages/p481]]–[[00_Books/Algebra_by_section/pages/p490]]
- Modeling (growth/decay/logistic): [[00_Books/Algebra_by_section/pages/p495]]–[[00_Books/Algebra_by_section/pages/p504]]
- Reference pages: [[00_Books/Algebra_by_section/pages/p512]], [[00_Books/Algebra_by_section/pages/p513]], [[00_Books/Algebra_by_section/pages/p514]]
# # ### Textbook-style examples (4.3)
<!-- removed duplicate block during cleanup (4.3) -->
# # ### Textbook-style examples (4.4)
<!-- removed duplicate block during cleanup (4.4) -->
# # # ### Textbook-style examples (4.3)
<!-- removed duplicate block during cleanup (4.3) pass 2 -->