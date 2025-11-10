---
type: claim
dv_type: ""
status: draft
importance: high
sources:
  - FongSpivak2019
  - LawvereSchanuel2009
source_refs:
  - GRL §2
  - L&S Sessions 32–33
relations:
  proves:
    - "[[Relational Cognition Corpus/Topics/Regular Calculi and Ajax Functors]]"
  about:
    - "[[Relational Cognition Corpus/Definitions/Regular Calculus]]"
    - "[[Relational Cognition Corpus/Topics/Regular Categories]]"
  depends_on:
    - "[[Relational Cognition Corpus/Definitions/Regular Category]]"
    - "[[Relational Cognition Corpus/Definitions/Image Factorization]]"
tags: "tags: [node/claim, math/cat, cat/poset, logic/regular, status/in-progress]"
---

# Sub functor is ajax

Claim
- For any regular category R, the Sub functor Sub: R^op → Poset is adjoint-lax (ajax): its laxator maps admit right adjoints, coherently. This equips each fiber Sub(Γ) with finite meets (∧) and truth (⊤), with substitutions preserving ∧ and ⊤ and admitting left adjoints (∃) that satisfy Beck–Chevalley and Frobenius.

Notes
- In the GRL development, ajax structure allows interpreting regular formulas graphically, with conjunction realized by meet and existential quantification by left adjoints to substitution.
- In L&S, the action of Ω induces a meet-semilattice of “parts,” aligning with Sub(Γ).

See also
- [[Relational Cognition Corpus/Definitions/Regular Calculus]]
- [[Relational Cognition Corpus/Topics/Regular Categories]]
- [[Relational Cognition Corpus/Topics/Regular Logic and Graphical Regular Logic]]


Anchors
- GRL Theorem 3.16 (Sub_R is ajax); Corollary 3.17 (Sub_R(−) sends objects to meet-semilattices)
