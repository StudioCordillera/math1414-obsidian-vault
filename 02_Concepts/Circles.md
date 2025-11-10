---
title: Circles in the Coordinate Plane
type: Definition
status: review
importance: high
tags:
  - node/definition
  - domain/functions
  - chapter2
sources:
  - MillerGerken_AlgTrig2e
source_refs:
  - "Ch2 §2.2 Circles"
relations:
  broader:
    - "[[Rectangular_Coordinate_System]]"
  narrower: []
  depends_on:
    - "[[Rectangular_Coordinate_System]]"
  defines: []
  related:
    - "[[Graphing_Functions]]"
    - "[[Distance_Rate_Time_Problems]]"
  used_in:
    - "[[01_Course/Textbook/Chapter2_Functions_Relations]]"
review:
  cadence: semester
  next: 2026-01-10
created: 2025-10-21
updated: 2025-10-21
---

# Circles in the Coordinate Plane
Equation forms, center-radius, and graphing

---

## Definition and Standard Form
A circle is the set of all points (x, y) at a fixed distance r (the radius) from a fixed point (h, k) (the center).

Standard form of a circle:
- (x − h)^2 + (y − k)^2 = r^2

General form:
- x^2 + y^2 + Dx + Ey + F = 0
  - Complete the square in x and y to convert to standard form and identify (h, k), r.

---

## Methods
1) Given center and radius → write equation
- Center (h, k), radius r → (x − h)^2 + (y − k)^2 = r^2

2) Given equation in general form → find center and radius
- Group x-terms and y-terms, complete the square
- Ensure r^2 > 0; if r^2 = 0 → point; if r^2 < 0 → no real circle

3) Given diameter endpoints → find equation
- Midpoint of endpoints → center
- Distance between endpoints / 2 → radius

---

## Examples
1) Center (2, −3), radius 5 → (x − 2)^2 + (y + 3)^2 = 25
2) x^2 + y^2 − 6x + 4y − 3 = 0
   - (x^2 − 6x) + (y^2 + 4y) = 3
   - (x^2 − 6x + 9) + (y^2 + 4y + 4) = 3 + 9 + 4
   - (x − 3)^2 + (y + 2)^2 = 16 → center (3, −2), r = 4
3) Diameter endpoints A(−1, 5), B(7, −3)
   - Center = midpoint = (3, 1)
   - r = distance(A, B)/2 = √[(8)^2 + (−8)^2]/2 = √(128)/2 = 4√2
   - Equation: (x − 3)^2 + (y − 1)^2 = (4√2)^2 = 32

---

## Common Misconceptions
- Forgetting to square r when writing r^2
- Losing signs while completing the square
- Assuming every quadratic in x and y is a circle (ellipses/parabolas exist)

---

## Connections
- Distance formula derives the standard form
- Intersects with lines to solve systems (line-circle intersection)
- Foundations for conic sections

---

## See Also
- [[Rectangular_Coordinate_System]]
- [[Linear_Equations]]
- [[Graphing_Functions]]