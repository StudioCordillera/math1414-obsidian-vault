---
dv_type: Claim
status: active
importance: 3
sources: [FongSpivak2019]
source_refs: ["§2 Lemma 2.8 (Fundamental lemma)"]
relations:
  about: [[Topics/Bicategory of Relations]], [[Topics/Regular Categories]]
  depends_on: [[Definitions/Regular Category]]
  uses: [[Definitions/Image Factorization]]
tags: [node/claim, domain/cat, logic/regular, cat/relations, method/proof, status/active]
---

Statement
- In Rel_R, a relation x ⊆ r×s is a left adjoint iff it is the graph of a morphism f:r→s. (Right adjoints are co-graphs.)

Sketch
- Unit/counit force the span legs to be isos; then x ≅ ⟨id_r, f⟩ and x' ≅ ⟨f, id_s⟩. See GRL §2 Lemma 2.8.

Anchors (added)
- GRL Lemma 2.8: Fundamental lemma — left adjoints in Rel_R are precisely graphs of morphisms; right adjoints are cographs.
- Proof sketch: Using unit/counit of adjunctions in Rel_R, show g is iso and identify f' = g^{-1}∘f.

---
Update 2025-10-19 — Example and anchor
---
Anchor
- GRL §2 (Relations in a regular category; fundamental lemma).

Example (sketch)
- For f: A → B in a regular category R, its graph Γ_f ⊆ A×B defines a relation with left adjoint Γ_f ⊣ Γ_f^⊣ in Rel_R; relational composition of graphs corresponds to function composition via pullback+image.