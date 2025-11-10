---
dv_type: Claim
status: active
importance: 4
sources: [FongSpivak2019]
source_refs: ["GRL §6–§7"]
relations:
  proves: [[Relational Cognition Corpus/Topics/Syntactic Categories]]
  about: [[Relational Cognition Corpus/Definitions/IntRel_P - Internal Relations]], [[Relational Cognition Corpus/Definitions/R_P - Internal Functions]]
  depends_on: [[Relational Cognition Corpus/Definitions/FRg(T) - Free Regular Category]], [[Relational Cognition Corpus/Topics/Regular Calculi and Ajax Functors]]
tags: [node/claim, domain/cat, cat/relations, logic/regular, status/active]
---

# IntRel_P and R_P — Constructions

Claim
- Given a regular calculus P: FRg(T)→Poset with ajax structure, one constructs the internal relations po-category IntRel_P and its subcategory of internal functions R_P; these together yield a regular category equivalent to the syntactic category associated to P.

Sketch
- Objects: contexts Γ from FRg(T); predicates P(Γ) as subobjects; morphisms Γ→Δ recorded by relations R⊆Γ×Δ satisfying compatibility.
- Composition via pullback+image internal to P; identities via diagonals; functions are relations with right adjoints.

Consequences
- prd: RgCat→RgCalc is fully faithful; syn: RgCalc→RgCat left adjoint; counit is an equivalence on regular categories arising from calculi.

---
Update 2025-10-19 — Anchors and example
---
Anchors
- GRL §6: Internal relations IntRel_P: objects are contexts Γ; 1-cells are predicates P(Γ×Δ); composition via pullback and image (∃-elimination).
- GRL §7: Internal functions R_P: maps whose graphs are left adjoints in IntRel_P.

Example (sketch)
- Given φ(x,y) ∈ P(X×Y) and ψ(y,z) ∈ P(Y×Z), the composite (ψ∘φ)(x,z) ≔ ∃y. (φ(x,y) ∧ ψ(y,z)). Graphically: nest the y-wire, compose via pullback along projections, then take image (∃ over y).