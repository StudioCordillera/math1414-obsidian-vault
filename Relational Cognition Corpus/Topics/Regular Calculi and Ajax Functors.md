Regular Calculi and Ajax Functors

Essentials (from Fong–Spivak 2019)
- Regular calculus: a pair (T, P) with P: FRg(T) → Poset an ajax (adjoint-lax) 2-functor.
- Ajax functor: lax monoidal with laxators as right adjoints. Consequence: preserves adjoint monoids; sends contexts to meet-semilattices of predicates.
- Adjoint monoids: objects bearing both comonoid and monoid with μ, η right adjoint to δ, ε. In Poset, adjoint monoids ≅ meet-semilattices; in Rel_R, each object has a canonical adjoint monoid.

Why this matters
- Encodes regular logic semantics: P(Γ) is the poset of predicates in context Γ with ∧, ⊤; substitution/pullback and ∃/image appear as adjoints.
- Bridges syntax and semantics: via internal relations IntRel_P and internal functions R_P.

Key results
- Sub_R ∘ ⟨−⟩: FRg(Ob R) → Poset is ajax (Theorem 3.16). Each P(Γ) is a meet-semilattice (Cor. 3.17).
- Adjoint monoids in Rel_R correspond to unique (co)monoid structures per object; strong link to hypergraph/category structure.

Links
- [Free Regular Category FRg(T)](./Free%20Regular%20Category%20FRg(T).md)
- [Predicates Functor prd and syntactic functor syn](./Predicates%20Functor%20prd%20and%20syntactic%20functor%20syn.md)
- [Regular Logic and Graphical Regular Logic - Key Results](./Regular%20Logic%20and%20Graphical%20Regular%20Logic%20-%20Key%20Results.md)

Source trail: [FongSpivak2019] §§3–4
# Content
Regular calculi
- A regular calculus is (T, P) with P: FRg(T)→Poset ajax (adjoint-lax: laxators right adjoints). Ajax functors preserve adjoint monoids; in Poset, adjoint monoids ≅ ∧-semilattices. [GRL Def 1.1; Prop 3.6–3.8]
- Each context Γ maps to a meet-semilattice P(Γ); true and ∧ induced by right adjoints (explicit via ρ, λ and δ, ε). [GRL Eq (18)]

Bridges
- prd(R) = (Ob R, Sub_R∘⟨-⟩) is ajax; syn(T,P) reconstructs a regular category. [GRL §4.3, §8]

Sources
- [FongSpivak2019]