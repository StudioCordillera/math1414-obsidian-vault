# Syntactic Categories and Internal Relations

From a regular calculus P: FRg(T) → Poset:
- IntRel_P: internal relations; contexts as objects; predicates as 1-cells.
- R_P: internal functions; subcategory of IntRel_P formed by functional relations; yields a regular category.

Bridge:
- Provides a semantics-from-syntax path: build a regular category equivalent to the one recovered by prd/syn adjunction (Fong–Spivak).

Tasks:
- Work through an example: T with objects X,Y and a predicate R⊆X×Y; show composition and existential elimination.

Sources: [FongSpivak2019]
# Content
Syntactic category from a regular calculus
- Given P: FRg(T)→Poset ajax, define IntRel_P with objects (Γ, φ) and morphisms θ∈P(Γ⊕Γ') satisfying domain/codomain entailments; composition via wiring comp and ∃-composition. [GRL §6]
- Internal functions R_P := LAdj(IntRel_P) form a regular category (finite limits; image factorizations stable under pullback). [GRL §7 Thm 7.3]
- Adjunction: prd: RgCat→RgCalc fully faithful; left adjoint syn maps (T,P)↦R_P; counit syn(prd(R))≃R. [GRL Thm 1.2, §8]

Cross-links
- Regular Categories; Bicategory of Relations; Regular Logic and GRL; Regular Calculi and Ajax Functors.

Sources
- [FongSpivak2019]