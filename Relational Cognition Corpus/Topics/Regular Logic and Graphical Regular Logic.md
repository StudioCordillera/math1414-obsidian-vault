# Regular Logic and Graphical Regular Logic

Aliases: regular categories; string diagrams for logic

Core ideas
- Regular logic: ⊤, ∧, ∃ with equality; interpretations in regular categories.
- Graphical Regular Logic (GRL): string-diagrammatic calculus (Fong–Spivak) for regular logic proofs.

Elements
- Subobjects and images; pullbacks; regular epimorphisms; kernel pairs.
- Diagrammatic composition and contraction rules.

Source trail
- [Fong & Spivak 2019], entire; [Lawvere & Schanuel 2009] (regular categories); [Gowers Companion] for background.
- Cross-links: [[Categories]], [[Universal Properties and Limits]], [[Diagrams and Commutativity]]
# Core ideas
Core ideas
- Regular logic fragment: equality, ⊤, ∧, ∃; no ∨, ¬, or →. Formulas denote subobjects of finite products.
- Interpretation in a regular category C: contexts as finite products; predicates as subobjects; existential as image factorization; conjunction as pullback-intersection.
- GRL provides a sound and complete graphical calculus for the regular fragment, enabling equational reasoning via string diagrams.

Graphical rules (Fong–Spivak)
- Monotonicity: weakening/strengthening respecting entailment.
- Nesting and breaking: boxes can be nested or split while preserving meaning (reflects associativity and stability of image/pullback constructions).
- Contraction/duplication via diagonals; deletion via terminal maps; equality wires for variable identification.
- Composition of relations = existential composition: R;S(x,z) ≡ ∃y. R(x,y) ∧ S(y,z).

Key structures
- Regular categories: finite limits + stable image factorizations (reg epi–mono).
- Bicategory of relations Rel_C: objects of C; 1-cells as subobjects of X×Y; composition via pullback+image.
- Left adjoints in Rel_C correspond to graphs of morphisms in C.

Status
- ✔ Core rules outlined; ✚ Add page/section refs from [FongSpivak2019].
# Content
Essentials
- Regular logic: fragment with =, ⊤, ∧, ∃; composition of relations via ∃-conjunction R#S = {(x,z) | ∃y. R(x,y) ∧ S(y,z)}. [GRL §1]
- Graphical regular logic: shells (contexts), wires (variables), white dots (support), operations: nesting (composition), breaking (entailment), juxtaposition (⊗). [GRL §5]

Use
- Reason about internal relations, images, pullbacks, and limits directly in the diagrammatic calculus; prove R_P is regular. [GRL §6–7]

Sources
- [FongSpivak2019]