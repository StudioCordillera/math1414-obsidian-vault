---
frontmatter:
  type: topic
  status: in-progress
  tags:
    - topic
    - truth
    - logic
  sources:
    - LawvereSchanuel2009
  pages: []
  created: 2025-10-16
  updated: 2025-10-16
  broader:
    - "[[Categories and Functors - Core]]"
  related:
    - "[[Orders and Lattices]]"
    - "[[Propositional and Predicate Logic]]"
  requires:
    - "[[Sets and Functions]]"
    - "[[Categories and Functors - Core]]"
  supports:
    - "[[Regular Categories]]"
    - "[[Regular Logic and Graphical Regular Logic]]"
  defined_by: []
  defines:
    - "[[Equalizers]]"
---
Subobject Classifier and Truth Values (Ω)

Scope: Parts/subobjects, inverse image along a map, images, and the truth-value object Ω; how substitution corresponds to pullback and how logical structure emerges in a topos-like setting.

Key content
- Parts/Subobjects as monomorphisms i: U ↪ X; stability under pullback (inverse image). 
- Inverse image: Given f: X → Y and a part i: V ↪ Y, the inverse image f* i ↪ X satisfies x ∈ f* i iff f x ∈ i. This is substitution of conditions along f.
- Image: For g: W → X, an image i: im(g) ↪ X s.t. (1) g factors through i and (2) i is minimal w.r.t. “g is in i.” In regular/adequate settings, every map factors as epi then mono.
- Truth-value object Ω with “true” v: 1 → Ω classifies subobjects: for each part i ↪ X there is a unique χ_i: X → Ω with i ≅ χ_i^*(v). χ_i is the characteristic map; χ_i(x) is the truth value “x ∈ i.”
- Pullback/substitution as Ω^X action: any f: X → Y induces Ω^Y → Ω^X by precomposition, representing inverse image on parts.

Lawvere–Schanuel essentials (Conceptual Mathematics, Art. VI, Sess. 32–33)
- Stable conditions: “x ∈ g” means ∃w. x = g w; stability under reindexing; when i is mono, images link “in g” to “in im(g).”
- Equalizers as inverse images of the diagonal Δ: Y → Y×Y via ⟨f1, f2⟩.
- Existence of Ω forces rich algebra on parts: meets, joins, implication, quantifiers (when available), differing from linear/group contexts.
- In Sets, Ω = 1+1; in cohesive categories (graphs, dynamical systems) Ω carries more structure (e.g., right ideals for monoid actions).

Connections
- Regular logic: subobject lattices interpret predicates; f_! ⊣ f^* adjunctions (images vs pullbacks) instantiate ∃ vs substitution.
- Graphical Regular Logic: predicates-as-subobjects, meets by pullback, existential via image factorization.

Source trail
- [LawvereSchanuel1997-2009] Article VI; Sessions 32–33 (Subobject, logic, and truth; Toposes)
- [SEP-CategoryTheory] subobjects and classifiers overview
- [FongSpivak2019] Section 2 (Sub functor), Prop. 2.6; Thm 3.16 (Sub is ajax)

Open tasks
- Add worked examples: characteristic maps in Sets; Ω in right M-actions; equalizer via Δ.
- Add page/section refs per source.
# Content
Framework and key facts
- Sub functor Sub_R: R → LAdj(Poset) sends each object to a meet-semilattice; ajax structure (laxators right adjoints) yields true and ∧ operations (GRL §3.1–3.3). [FongSpivak2019]
- In Poset, adjoint monoids ≅ meet-semilattices; hence each P(Γ) is a ∧-semilattice when P is ajax. [FongSpivak2019 Prop 3.8]
- In Lawvere–Schanuel, Ω is the truth-value object (subobject classifier) with true:1→Ω; inverse image along f corresponds to substitution; equalizers as inverse images of diagonal; images factor epi→mono. [L&S 2009, Article VI; Sessions 32–33]

Key constructions (topic-centric)
- Inverse image: given f:X→Y and part i↪Y, the inverse image j↪X is defined by: x∈j iff f x∈i. Stability and Beck–Chevalley properties link to ajax laws. [L&S 2009; GRL Prop 2.6, Rem 3.19]
- Images: regular epis stable under pullback; image factorization unique up to iso; in GRL internal calculus, im(θ)=ε* # θ; regular epi iff φ2 ⊢ im(θ). [GRL §7.3]

Bridges and examples
- Sets: Ω=2, subobjects ≅ predicates; inverse image is preimage; equalizer as fiber equality. [L&S]
- Actions (presheaf toposes): Ω = right ideals (for monoid actions); points vs components functors and adjunction chain F ⊣ I ⊣ G ⊣ J. [L&S Session 33–35]

Sources
- [FongSpivak2019]
- [LawvereSchanuel2009]