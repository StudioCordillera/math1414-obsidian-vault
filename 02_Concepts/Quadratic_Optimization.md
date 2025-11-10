---
layout: concept
title: "Quadratic Optimization"
topic: "Polynomials"
type: Method
status: review
importance: high
tags:
  - concept/algebra
  - chapter-1
  - math/quadratics
  - method/optimization
relations:
  broader:
    - [[02_Concepts/Real_World_Applications]]
  depends_on:
    - [[02_Concepts/Vertex_Form]]
    - [[02_Concepts/Completing_the_Square]]
    - [[02_Concepts/Quadratic_Formula]]
    - [[02_Concepts/Function_Notation]]
  related:
    - [[02_Concepts/Projectile_Motion_Model]]
    - [[02_Concepts/Revenue_and_Profit_Models]]
    - [[02_Concepts/Graphing_Quadratic_Functions]]
    - [[02_Concepts/Domain_and_Range]]
    - [[02_Concepts/Average_Rate_of_Change]]
review:
  next: 2025-11-24
updated: 2025-10-24
---

# Quadratic Optimization Problems

Finding maximum and minimum values in context by using the vertex of a quadratic model.

---

## Core insight

For f(x) = ax^2 + bx + c, the vertex (h, k) gives the optimal value:
- If a > 0, the vertex is a minimum
- If a < 0, the vertex is a maximum
- h = -b/(2a), k = f(h)

Vertex form also exposes the optimum: f(x) = a(x - h)^2 + k → optimum at x = h.

Why it matters: Many real problems (area, revenue, height, cost) reduce to a quadratic function of one variable; the vertex answers the optimization question directly.

---

## Method (universal steps)

1) Define variables and goal
- Identify the quantity to optimize (max/min)
- Choose a single control variable x
- Note real-world constraints (domain)

2) Build the model
- Express the target quantity Q in terms of x
- Reduce to Q(x) = ax^2 + bx + c (by substitution from constraints)

3) Find the vertex
- Compute h = -b/(2a)
- Compute k = Q(h)
- Determine max vs min from the sign of a

4) Interpret and verify
- Check that h lies in the realistic domain
- State answers with units and context
- Sanity-check magnitude and direction

Common alternatives: complete the square to get vertex form; or graph and read the vertex.

---

## Worked examples

Example 1: Maximize area with a river as one side
- Constraint: 2x + y = 200, Area A = xy = x(200 - 2x) = -2x^2 + 200x
- Vertex: x = -200/(2·-2) = 50, y = 100 → A_max = 5000 ft^2

Example 2: Maximize revenue with linear demand
- Price P(x) = 20 + 2x, Tickets T(x) = 500 - 20x
- Revenue R(x) = (20 + 2x)(500 - 20x) = -40x^2 + 600x + 10000
- Vertex: x = -600/(2·-40) = 7.5 → Price $35, 350 tickets, max revenue $12,250

Example 3: Projectile peak height
- h(t) = -16t^2 + 64t + 6 → t_vertex = -64/(2·-16) = 2 s
- h(2) = 70 ft; ground hit at ≈ 4.09 s (via quadratic formula)

---

## Pitfalls

- Ignoring domain constraints (e.g., negative lengths)
- Mixing up max vs min (check sign of a)
- Omitting units in final answers
- Failing to interpret x and Q(x) in context

---

## Connections

Prerequisites
- [[02_Concepts/Vertex_Form]]
- [[02_Concepts/Completing_the_Square]]
- [[02_Concepts/Quadratic_Formula]]

Related and applications
- [[02_Concepts/Revenue_and_Profit_Models]]
- [[02_Concepts/Projectile_Motion_Model]]
- [[02_Concepts/Graphing_Quadratic_Functions]]
- [[02_Concepts/Domain_and_Range]]
- [[02_Concepts/Average_Rate_of_Change]]

---

## Exam checklist

- [ ] Define variables and target clearly
- [ ] Build Q(x) as a quadratic in one variable
- [ ] Find vertex (h, k) using -b/(2a) or vertex form
- [ ] Interpret results with units and domain
- [ ] Verify max/min matches sign of a
