Yoneda and Representables

Essentials
- Representable functor for an object A: hom(A, -) or hom(-, A). Yoneda lemma: Nat(hom(A,-), F) ≅ F(A); fully faithful embedding of C into Set^{C^op}.
- Natural transformations encode structure-preserving data; proofs often reduce to componentwise checks via Yoneda.

Use in corpus
- Equivalence of categories: fully faithful + essentially surjective functor; Yoneda underlies many proofs (e.g., uniqueness via representables).
- In regular logic: predicates correspond to subobjects; representables clarify how contexts/variables embed into presheaf settings.

Key points
- Yoneda reduces universal property reasoning to elementwise arguments in presheaves.
- Many “free-forgetful” adjunctions can be studied via representables and colimits.

Source trail
- [PeterSmith2026] chs on Yoneda; [SEP-CategoryTheory]; [GowersCompanion]; [LawvereSchanuel1997-2009] App. I–II

Open tasks
- Add explicit Yoneda proof sketch; examples in Set and Grph; use to justify uniqueness up to unique iso for products/pullbacks.
# Content
Highlights
- Yoneda perspective appears in Lawvere–Schanuel (Appendix I; Sessions 34): Cayley–Yoneda for actions; elements as maps from representable; maps determined by values on representables. [L&S 2009]
- In GRL, representability underlies free regular categories FRg(T) and context shells; though not explicit Yoneda, free constructions reflect ‘elements via maps’. [GRL §4–5]

Sources
- [LawvereSchanuel2009]
- [FongSpivak2019]