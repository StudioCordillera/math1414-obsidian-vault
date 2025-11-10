Conjunctive Queries and Databases (CQ) — Bridge to Regular Logic

Essentials
- Conjunctive queries correspond to regular formulas (∧, ∃, =). Query containment aligns with entailment in regular logic.
- Composition of relations via ∃-conjunction matches CQ joins/projections; diagrams in GRL provide an intuitive calculus for containment proofs.

Key points
- CQ containment (Chandra–Merlin): decidable via homomorphism test; relates to diagrams/allegories/bicategories of relations.
- Database schemas as finitely presented categories; instances as functors; CQ as limits/colimits/adjunction patterns in categorical databases.

Use in corpus
- Translate GRL diagrams to CQ operations for examples and exercises; connect to IntRel_P and syntactic categories to view CQs as internal relations.

Source trail
- [FongSpivak2019] Related work section; connections to Chandra–Merlin and Carboni–Walters
- External background (not in folder): Chandra–Merlin 1977; categorical database literature

Open tasks
- Add a worked translation: a small CQ containment example and its GRL diagram.
- Add page/section refs in [FongSpivak2019].
# Content
Bridge to databases
- Conjunctive queries correspond to regular formulas; containment corresponds to entailment. Chandra–Merlin decidability; formalized via bicategories of relations (Carboni–Walters). [GRL Related work]
- Sketch example: Query q1(x,z): ∃y R(x,y) ∧ S(y,z); containment q1 ⊆ q2 visualized as a breaking morphism in GRL diagrams.

Sources
- [FongSpivak2019]