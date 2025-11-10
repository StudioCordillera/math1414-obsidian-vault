# Functors and Natural Transformations

Core ideas
- Functor: structure-preserving mapping between categories.
- Natural transformation: components η_X: F(X) → G(X) natural in X; naturality square commutes.

Key results
- Yoneda lemma (to be added in detail).
- Equivalences of categories via fully faithful and essentially surjective functors.

Diagrams
- Naturality squares; whiskering and vertical/horizontal composition.

Source trail
- [Lawvere & Schanuel 2009], ch. 3–5; [Peter Smith 2026]; [SEP]
- Cross-links: [[Categories]], [[Universal Properties and Limits]], [[Adjunctions and Monads]]
# Key results
Key results
- Yoneda lemma: Nat(C(-,A), F) ≅ F(A); consequences: representable functors are determined up to unique isomorphism by their representing objects; embeddings via Yoneda.
- Equivalence of categories: F ⊣ G with unit/counit isos; or F fully faithful + essentially surjective ⇒ equivalence.
- Functors preserve isos, initial/terminal objects, products, and pullbacks (when limits exist and F preserves them).

Bridges to relational topics
- Graphs of morphisms embed functions into relations: left adjoints in Rel_C correspond to morphisms in C (fundamental lemma).
- Regular functors preserve finite limits and regular epis; induce strong monoidal po-functors on relation bicategories.

Status
- Scaffold complete; ✚ add page/section refs from [LawvereSchanuel2009], [Smith2026], [SEP-CategoryTheory].