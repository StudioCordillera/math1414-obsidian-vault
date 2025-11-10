# Relational Cognition Corpus — Framework

Purpose
- Build topic-centric notes from books and scholarly articles in the Relational Cognition Library.
- Organize by concepts and problems (content), not by source. A topic may aggregate multiple sources; only create source-only notes if a concept appears uniquely in a single source.

Scope of sources (initial)
- Category Theory (SEP)
- Conceptual Mathematics (Lawvere & Schanuel, 1997/2009)
- Graphical Regular Logic (Fong & Spivak, 2019)
- Higher-Dimensional Categories: Illustrated (Cheng & Lauda)
- Introducing Category Theory (Peter Smith, 2026)
- Sets for Mathematics (Lawvere & Rosebrugh, 2003)
- The Princeton Companion to Mathematics (ed. Gowers)
- Real Analysis (Carothers, 2000)
- The Algebra of Logic Tradition (Stanford/compiled)
- The Origins of the Concept Mapping Tool (Novak & Cañas)

Organization
- Publications.md: canonical list of books/articles and file pointers
- Topics/: topic notes where content is synthesized across sources
- Topics/_Index.md: high-level map of topics

Note types
- Topic Note: single concept or cluster (e.g., Functors; Regular Logic)
  - Core ideas (definitions, propositions, examples)
  - Diagrams / schemas (string diagrams, universal properties)
  - Cross-links to related topics
  - Source trail (citations list; page/section references as we extract)
- Framework Note (this file): conventions and structure

Conventions
- Topic-first: content resides under Topics/. Sources are linked at the bottom of each topic in a Source trail list.
- Citations: inline cite keys in square brackets (e.g., [Lawvere & Schanuel 2009, ch. 1]). Exact pages added during extraction.
- Cross-links: Obsidian wiki links between topics (e.g., [[Functors and Natural Transformations]]).
- Vocabulary: prefer standard terms; add aliases as needed at the top of topic notes.

Initial workflow
1) Identify publications (done — see Publications.md)
2) Create topic scaffold (done — see Topics/_Index.md)
3) Iterative extraction pass per source: capture definitions, statements, key diagrams into existing Topics/* notes
4) Reconcile overlaps and refine cross-links

Status
- v0.1 scaffold created; content to be filled during extraction passes.
