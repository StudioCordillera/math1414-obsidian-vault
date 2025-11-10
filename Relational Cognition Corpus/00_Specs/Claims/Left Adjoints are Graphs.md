---
type: Claim
status: in-progress
importance: high
dv_type: Claim
dv_domain: cat
sources: [FongSpivak2019]
source_refs: ["FongSpivak2019 §2 Lemma"]
relations:
  broader: ["[[Relational Cognition Corpus/Topics/Bicategory of Relations.md]]"]
  narrower: []
  related: []
  depends_on: ["[[Relational Cognition Corpus/Definitions/Regular Category.md]]"]
  defines: []
  defined_in: []
  proves: ["[[Relational Cognition Corpus/Topics/Regular Categories.md]]"]
  about: ["[[Relational Cognition Corpus/Topics/Bicategory of Relations.md]]"]
  
---
# Left Adjoints in Rel_R are Graphs

Claim
- In Rel_R for a regular category R, a relation L: X⇸Y has a right adjoint iff it is the graph of a morphism f: X→Y in R. Consequently, R ≅ LAdj(Rel_R).

Sketch / Proof idea
- Units/counits force functionality and totality constraints; use image factorization and pullback stability.

Dependencies
- Regular category structure; definition of Rel_R; adjunction in posets.

Source
- [FongSpivak2019 §2]
