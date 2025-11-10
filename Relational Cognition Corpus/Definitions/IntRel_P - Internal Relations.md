---
type: Definition
status: draft
importance: high
dv_type: ""
dv_domain: ""
sources:
  - FongSpivak2019
source_refs:
  - GRL §4
relations:
  defines:
    - "[[Relational Cognition Corpus/Topics/Syntactic Categories]]"
    - "[[Relational Cognition Corpus/Topics/Regular Categories]]"
  defined_in: []
  broader:
    - "[[Relational Cognition Corpus/Topics/Regular Calculi and Ajax Functors]]"
  related:
    - "[[Relational Cognition Corpus/Definitions/Regular Category.md]]"
    - "[[Relational Cognition Corpus/Definitions/Regular Calculus.md]]"
  depends_on:
    - "[[Relational Cognition Corpus/Definitions/Regular Calculus.md]]"
tags: "tags: [node/definition, math/cat, logic/regular]"
---
# IntRel_P — Internal Relations from a Regular Calculus P

Definition: Given a regular calculus P: FRg(T) → Poset, IntRel_P is the regular po-category whose objects are contexts Γ of FRg(T) and whose hom-posets IntRel_P(Γ,Δ) are the P-predicates on Γ×Δ. Composition is defined by relational composition via pullback and image, using the ajax structure of P.

Source trail: [FongSpivak2019]

Anchors (added)
- GRL §6: Internal relations category IntRel_P definition; composition via comp_{Γ1,Γ2,Γ3}; identity id_φ via δ_Γ.
- GRL Prop 6.2: Agreement with Rel_R for prd(R).

Example
- Given φ1∈P(Γ1), φ2∈P(Γ2), θ∈P(Γ1⊕Γ2) with π1!θ⊢φ1 and π2!θ⊢φ2, then θ∈IntRel_P(φ1,φ2). Graphical verification via breaking and discarding.

Relations
- defines → [[Relational Cognition Corpus/Topics/Syntactic Categories]]
- depends_on → [[Relational Cognition Corpus/Definitions/Regular Calculus]], [[Relational Cognition Corpus/Definitions/Relations Po-Category]]
