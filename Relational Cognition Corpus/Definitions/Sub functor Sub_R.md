---
type: Definition
status: in-progress
importance: high
dv_type: Definition
dv_domain: cat
sources: [FongSpivak2019, LawvereRosebrugh2003, LawvereSchanuel2009]
source_refs: ["GRL §2", "SfM Ch.2", "L&S Article VI"]
relations:
  defines: [[Relational Cognition Corpus/Topics/Subobject Classifier and Truth Values.md]]
  related: [[Relational Cognition Corpus/Definitions/Image Factorization.md]]
  depends_on: [[Relational Cognition Corpus/Definitions/Regular Category.md]]
tags: [node/definition, domain/cat, logic/regular, status/active]
---
# Sub functor Sub_R

For a regular category R, Sub_R: R^op → Poset assigns to each object X the poset of subobjects Sub_R(X), and to each morphism f: X→Y the inverse image map f^*: Sub_R(Y)→Sub_R(X).

Adjoints and structure
- For any f: X→Y, the inverse image f^* has a left adjoint (direct image) f_!: Sub_R(X)→Sub_R(Y) taking a subobject A↪X to the image of A→X→Y.
- Each Sub_R(X) is a meet-semilattice (∧, ⊤); direct image preserves finite meets along regular epis; Beck–Chevalley and Frobenius reciprocity hold for pullback squares.
- As a functor into Poset with meet, Sub_R carries canonical adjoint-monoid structure; equivalently, it is ajax in the sense of GRL.

Logical reading
- f^* is substitution; f_! corresponds to ∃_f (existential quantification) on predicates; meets correspond to conjunction.

Source trail: [FongSpivak2019] GRL §2; [LawvereRosebrugh2003] SfM Ch.2; [LawvereSchanuel2009] Article VI.
