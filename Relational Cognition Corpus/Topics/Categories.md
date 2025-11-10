# Categories

Aliases: category; objects and morphisms

Core ideas
- A category consists of objects, morphisms between objects, identity morphisms, and associative composition.
- Morphisms compose when codomain/domain align; identity laws hold.

Key structures
- Mono, epi, iso; initial/terminal objects; products, coproducts.

Examples
- Set, Rel (sets and relations), Poset (as thin categories), Grp, Vect_k.

Diagrams
- Commutative triangles and squares; universal property of product.

Source trail
- [Lawvere & Schanuel 2009], ch. 1–2; [Peter Smith 2026], ch. 1; [SEP Category Theory]
- Cross-links: [[Functors and Natural Transformations]], [[Universal Properties and Limits]]
# Key structures


Universal properties
- Product X×Y: projections π1, π2 with unique ⟨f,g⟩. Dual: coproduct with injections.
- Equalizer/pullback: limiting cones with universal arrows; characterize monos as equalizers where applicable.

Relational viewpoint
- Rel: objects are sets; morphisms R⊆X×Y; composition via relational composition; identities as diagonals Δ_X.
- Functions embed into Rel via their graphs; left adjoints in Rel correspond to total functional relations.
