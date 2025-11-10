---
type: claim
dv_type: ""
status: active
importance: 3
title: prd ⊣ syn adjunction and essential reflection
sources:
  - FongSpivak2019
source_refs:
  - GRL §§5–8
relations:
  proves:
    - "[[Relational Cognition Corpus/Topics/Syntactic Categories]]"
    - "[[Relational Cognition Corpus/Topics/Regular Calculi and Ajax Functors]]"
  depends_on:
    - "[[Relational Cognition Corpus/Definitions/Regular Calculus]]"
    - "[[Relational Cognition Corpus/Definitions/Regular Category]]"
  about:
    - "[[Relational Cognition Corpus/Topics/Regular Logic and Graphical Regular
      Logic - Key Results]]"
tags: |-
  tags:
    - node/claim
    - math/cat
    - logic/regular
    - cat/relations
    - status/active
---

# The prd ⊣ syn adjunction and essential reflection

Claim
- The functor prd: RgCat → RgCalc is fully faithful with left adjoint syn: RgCalc → RgCat; moreover, the counit syn∘prd ⇒ id is an equivalence (i.e., RgCat is an essentially reflective subcategory of RgCalc).

Sketch
- Fully faithfulness follows from uniqueness of regular interpretations preserving ∧ and ∃, tracked by ajax structure on Sub_R.
- Left adjoint syn builds a regular category R_P from a regular calculus P via IntRel_P and R_P; the counit equivalence identifies syn(prd(R)) ≃ R.

Source trail
- [FongSpivak2019] GRL §§5–8 (e.g., Thm 1.2, Prop 4.15, Thm 8.5, Prop 8.3, Cor 8.4).


---
Update 2025-10-19
---
Statement
- prd: RgCat → RgCalc is fully faithful; syn ⊣ prd with counit an equivalence for any regular category R.

Anchors
- GRL: Theorem 1.2; Sections 6–8 (internal relations, internal functions, syntactic category); Eq. (19), (24), (29–30).

Notes
- prd maps a regular category R to (Ob R, Sub_R∘⟨-⟩): contexts ↦ predicate posets; ajax structure via Sub_R.
- syn(T,P) ≔ LAdj(IntRel_P) yields a regular category with finite limits and pullback-stable image factorizations.
- Essential reflection: syn(prd(R)) ≃ R (counit equivalence); prd is full and faithful (Cor. 8.4).

Source trail
- [FongSpivak2019] GRL §§6–8, Thm 1.2.
