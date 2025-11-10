---
frontmatter:
  type: topic
  status: in-progress
  tags:
    - topic
    - relations
    - cat-theory
  sources:
    - FongSpivak2019
    - LawvereSchanuel2009
  pages: []
  created: 2025-10-16
  updated: 2025-10-16
  broader:
    - "[[Regular Categories]]"
  related:
    - "[[Relations and Relational Algebra]]"
    - "[[Regular Logic and Graphical Regular Logic]]"
  requires:
    - "[[Regular Categories]]"
    - "[[Sets and Functions]]"
  supports:
    - "[[Regular Logic and Graphical Regular Logic - Key Results]]"
    - "[[Conjunctive Queries and Databases]]"
  examples: []
---
# Bicategory of Relations

Setup:
- Objects: objects of an ambient regular category R.
- 1-cells: relations R ⊆ X×Y (subobjects). 2-cells: entailments (inclusion) between relations.
- Composition: pullback along shared object + image factorization; identities via diagonals.

Properties:
- Po-category enrichment: homs are posets by inclusion; composition monotone.
- Functions embed as left adjoint relations; right adjoint are transposes (converses) subject to unit/counit inequalities.

Connections:
- Graphical regular logic provides a string-diagram calculus for reasoning about these relations.

Sources: [FongSpivak2019], [SEP-CategoryTheory]
# Content
Core definitions and lemmas
- In a regular category R, Rel_R has objects Ob R and morphisms x:r⇸s are subobjects x⊆r×s; composition is via pullback over s and image factorization to r×t. Monoidal structure from ×. [GRL Def 2.7]
- Fundamental lemma: left adjoints in Rel_R are precisely graphs of morphisms in R (x=⟨id_r,f⟩). Hence R ≅ LAdj(Rel_R). [GRL Lem 2.8]
- Regular po-category: a po-category is regular if it is isomorphic to Rel_R for some regular R. Strong monoidal functors between Rel_R arise from regular functors. [GRL Def 2.11, Prop 2.10]

Graphical regular logic links
- Free regular po-category FRg(T)=Rel_{FRg(T)}; shells, wires, breaking, nesting give a calculus for regular formulas (∧, ∃, =, ⊤). [GRL §5]
- Internal relations IntRel_P and internal functions R_P recover a regular category from an ajax P: FRg(T)→Poset. [GRL §6–7]

Sources
- [FongSpivak2019]