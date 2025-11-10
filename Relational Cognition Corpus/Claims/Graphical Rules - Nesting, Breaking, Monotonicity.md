---
type: claim
dv_type: ""
status: active
importance: 3
sources:
  - FongSpivak2019
source_refs:
  - GRL §§2–3
relations:
  proves:
    - "[[Relational Cognition Corpus/Topics/Regular Logic and Graphical Regular
      Logic - Key Results]]"
  about:
    - "[[Relational Cognition Corpus/Topics/Regular Logic and Graphical Regular
      Logic]]"
    - "[[Relational Cognition Corpus/Topics/Diagrams and Commutativity]]"
  depends_on:
    - "[[Relational Cognition Corpus/Definitions/FRg(T) - Free Regular
      Category]]"
    - "[[Relational Cognition Corpus/Definitions/Regular Calculus]]"
    - "[[Relational Cognition Corpus/Definitions/Image Factorization]]"
tags: "tags: [node/claim, math/cat, cat/relations, logic/regular,
  method/diagrammatic, status/active]"
---

# Graphical Rules — Nesting, Breaking, Monotonicity

Claim
- The correctness of the graphical regular logic calculus is governed by the nesting and breaking rules for shells/wires and the monotonicity rule for inclusion. Together these generate the derivable entailments corresponding to regular formulas and their proofs under the ajax interpretation.

Notes
- Nesting reflects composition with ∃; breaking corresponds to weakening contexts; monotonicity aligns with inclusion of subobjects.
- These rules are sound and complete for the regular fragment when interpreted via the prd/syn correspondence.

See also
- [[Relational Cognition Corpus/Definitions/FRg(T) - Free Regular Category]]
- [[Relational Cognition Corpus/Topics/Regular Logic and Graphical Regular Logic]]
- [[Relational Cognition Corpus/Topics/Diagrams and Commutativity]]

## Worked example (GRL)
- Formula: R(x,y) ∧ S(y,z), composed via ∃y.
- Diagram: two boxes R and S sharing a wire y; composition equals pullback of R,S along y followed by image along x,z.
- Breaking: introduce a fresh cut wire y′ with equality constraint; rewiring preserves entailment (monotonicity ensures soundness).
- Nesting: scopes as regions; pulling ∃ outside corresponds to hiding a wire; admissible when the variable is not free outside the region.

Source trail: [FongSpivak2019] GRL §§2–3.

---
Update 2025-10-19 — Worked example
---
- Composition: R ⊆ X×Y and S ⊆ Y×Z compose as (S∘R)(x,z) ≔ ∃y.(R(x,y) ∧ S(y,z)). Diagrammatically: break along shared Y, nest the y-wire, then close it via ∃.
- Monotonicity: if R ≤ R′ and S ≤ S′ then S∘R ≤ S′∘R′ (order by inclusion of predicates).