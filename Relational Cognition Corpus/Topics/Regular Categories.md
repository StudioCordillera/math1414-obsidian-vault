---
type: Topic
status: in-progress
importance: high
dv_type: ""
dv_domain: ""
sources:
  - FongSpivak2019
  - LawvereRosebrugh2003
  - LawvereSchanuel2009
source_refs:
  - GRL §2
  - SfM Ch.2
  - L&S Sess32–33
relations:
  - broader:
      - "[[Categories.md]]"
    related:
      - "[[Bicategory of Relations.md]]"
      - "[[Regular Calculi and Ajax Functors.md]]"
      - "[[Subobject Classifier and Truth Values.md]]"
    depends_on:
      - "[[Finite Limits]]"
      - "[[Image Factorization.md]]"
review:
  next: 2025-11-01
  cadence: quarterly
tags:
  - node/topic
  - domain/cat
  - logic/regular
  - status/active
---
# Regular Categories

Definition and structure:
- Finite limits (terminal object, pullbacks, products; equalizers via pullbacks) and image factorization stable under pullback.
- Every morphism f factors as f = m ∘ e with e regular epi, m mono; pullback of a regular epi is regular epi.

Relations and internal logic:
- Po-category Rel_R with objects of R, morphisms as subobjects R ⊆ X×Y, composition via pullback + image.
- Internal logic interprets regular formulas; existential quantifiers correspond to image factorization.

Key facts:
- Left adjoints in Rel_R correspond to graphs of morphisms in R.
- Regular functors preserve finite limits and regular epis; they induce monotone maps on subobject lattices.

Links: [[Relational Cognition Corpus/Topics/Bicategory of Relations]], [[Relational Cognition Corpus/Topics/Regular Logic and Graphical Regular Logic - Key Results]], [[Relational Cognition Corpus/Topics/Syntactic Categories]]

Source trail: [FongSpivak2019], [SEP-CategoryTheory], [LawvereRosebrugh2003]

# Content
Definition and properties
- Regular category R: finite limits; coequalizers of kernel pairs; pullback stability of regular epis; unique epi–mono image factorizations. [GRL Def 2.1, Lem 2.2]
- Sub functor Sub_R: R→LAdj(Poset) with adjoints f_! ⊣ f^*; each Sub_R(r) a meet-semilattice; Beck–Chevalley (pullbacks), Frobenius reciprocity, stability for regular epis. [GRL Prop 2.5–2.6]
- Relations po-category Rel_R and fundamental lemma: R ≅ LAdj(Rel_R). [GRL §2.2]

From logic to category
- Regular logic fragment (=, ⊤, ∧, ∃) expresses composition of relations; internal language ↔ categorical structure. [GRL §1]

Sources
- [FongSpivak2019]
- [LawvereSchanuel2009] (images, inverse images, equalizers)