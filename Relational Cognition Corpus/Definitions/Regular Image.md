---
 type: Definition
 status: in-progress
 importance: high
 dv_type: Definition
 dv_domain: cat
 sources: [FongSpivak2019, LawvereRosebrugh2003, LawvereSchanuel2009]
 source_refs: ["GRL §2", "SfM Ch.2", "L&S Article VI"]
 relations:
   defines: [[Relational Cognition Corpus/Topics/Regular Categories.md]]
   depends_on: [[Relational Cognition Corpus/Definitions/Image Factorization.md]]
 tags: [node/definition, domain/cat, logic/regular, status/active]
---
# Regular Image

Given f: X → Y in a regular category R, the regular image Im(f) is the mono part m: I ↪ Y of the regular epi–mono factorization f = m ∘ e (with e regular epi). Im(f) is stable under pullback: for any g: Z → Y, pullback of m along g is mono and exhibits the image of the pullback of f.

Properties
- Stability: pullback of regular epis are regular epis; images commute with pullbacks along monos. [GRL §2]
- Logical reading: existential quantification ∃_f corresponds to image along f; composition of relations corresponds to pullback + image. [GRL §1–2]
- In Set: image is the usual subset {y ∈ Y | ∃x, f(x)=y}; in Poset-enriched Sub lattices, this is left adjoint to inverse image.

Source trail: [FongSpivak2019], [LawvereRosebrugh2003], [LawvereSchanuel2009].
