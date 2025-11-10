---
type: Topic
status: in-progress
importance: high
dv_type: Topic
dv_domain: cat
sources:
  - FongSpivak2019
  - LawvereSchanuel2009
source_refs:
  - FongSpivak2019 §1–7
  - LawvereSchanuel2009 Sess32–35
relations:
  broader:
    - "[[Relational Cognition Corpus/Topics/Regular Logic and Graphical Regular
      Logic]]"
  narrower: []
  related:
    - "[[Relational Cognition Corpus/Topics/Conjunctive Queries and Databases]]"
    - "[[Relational Cognition Corpus/Topics/Syntactic Categories]]"
    - "[[Relational Cognition Corpus/Topics/Regular Calculi and Ajax Functors]]"
    - "[[Relational Cognition Corpus/Topics/Bicategory of Relations]]"
  depends_on:
    - "[[Relational Cognition Corpus/Topics/Regular Categories]]"
    - "[[Relational Cognition Corpus/Topics/Relations and Relational Algebra]]"
  defines: []
  defined_in: []
  proves: []
  about: []
tags:
  - node/topic
  - domain/cat
  - logic/regular
  - cat/relations
  - status/active
---
# Regular Logic and Graphical Regular Logic — Key Results

Scope: Regular logic fragment with equality, truth, conjunction, existential quantification; its categorical semantics via regular categories; and the graphical calculus of Fong & Spivak (2019).

Key ideas (content-first; source trail aggregated):
- Regular logic fragment: formulas built from ⊤, =, ∧, ∃; morphisms in relations compose via ∃-conjunction over shared context.
- Regular categories: have finite limits and stable image factorizations (every map factors as reg-epi then mono; stable under pullback).
- Bicategory/po-category of relations Rel_R: objects of R; 1-cells are subobjects of products; composition via pullback + image.
- Free regular category FRg(T) on a context T; regular calculus as a poset-valued functor P: FRg(T) → Poset.
- Syntactic category R_P (internal functions) and IntRel_P (internal relations) from a regular calculus; build a regular category from syntax.
- Adjoint-lax (“ajax”) functors to Poset with laxators as right adjoints; explain monotonicity and meet behavior of predicate posets P(Γ).
- Main equivalence: prd : RgCat → RgCalc is fully faithful; left adjoint syn; counit equivalence for calculi arising from regular categories.
- Graphical rules: nesting (scope), breaking (context decomposition), monotonicity (weakening/strengthening), with string-diagram-like equational reasoning.

Source trail:
- [FongSpivak2019], [SEP-CategoryTheory], [LawvereSchanuel1997-2009]

Open tasks:
- Add concrete theorems/lemmas with page/section refs; worked examples of composition and existential elimination in the diagrammatic calculus.
- Cross-link to Regular Categories, Bicategory of Relations, Syntactic Categories.

# Sources
- [FongSpivak2019] Graphical Regular Logic (arXiv:1812.05765v2, Feb 4, 2019). Key results: Def 1.1 Regular calculus (ajax P: FRg(T)→Poset); Thm 1.2 prd:RgCat→RgCalc fully faithful; left adjoint syn; counit equivalence. §2–4: Rel_R; fundamental lemma (left adjoints are graphs); Sub functor is ajax; FRg(T) and Rel_FRg(T).
- [LawvereSchanuel2009] Conceptual Mathematics 2e: Sessions 32–35 (parts, Ω, inverse image, images, equalizers; components and adjunctions; actions).
