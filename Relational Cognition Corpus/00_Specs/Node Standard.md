---
Type: Spec
Title: Node Standard (Relational Cognition Corpus)
Version: 0.1
Status: draft
Tags: [#spec, #workflow]
---

Purpose
- Define a consistent, content-first standard for notes (“nodes”) across the corpus
- Make topics the primary unit; sources enrich topics but don’t fragment them
- Leverage Obsidian features: Properties (YAML), tags, links, Dataview, backlinks, and typed relations via properties

Node types
- Topic: central concept (e.g., Regular Categories, Graphical Regular Logic)
- Publication: bibliographic record for a book/article linking to local PDF(s)
- Definition: a precise notion (term) with formal/intuitive versions
- Claim: theorem/lemma/proposition/corollary with status and proof sketch
- Example: worked instance, counterexample, or pattern
- Question/Exercise: prompts for understanding or practice

Mandatory properties by type
- Common (all):
  - type: Topic | Publication | Definition | Claim | Example | Question
  - tags: array of tags from the taxonomy
  - status: draft | in-progress | stable | needs-review
  - importance: 1–5 (relative pedagogical or structural importance)
  - sources: [cite keys, e.g., FongSpivak2019]
  - source_refs: mapping source→page/section anchors (e.g., {FongSpivak2019: "§3, pp. 12–18"})
  - relations: object of typed links (see Relations Spec):
    - broader, narrower, related, depends_on, used_by
    - defines, defined_in, proves, about, formalizes, exemplifies, instance_of, generalizes, specializes, contradicts, equivalent_to
  - aliases: array of alternate titles
  - review: {last: ISO date, next: ISO date}

- Topic-specific:
  - summary: short description
  - problems: optional links to Questions/Exercises

- Publication-specific:
  - cite_key, title, authors, year, venue (if any)
  - file_paths: array of local paths
  - topics: linked topics covered

- Definition-specific:
  - term, formal, intuition, examples

- Claim-specific:
  - statement, status: theorem|lemma|prop|cor|conjecture
  - proof_sketch, dependencies (links), consequences (links)

- Example-specific:
  - setup, walkthrough, takeaway

- Question-specific:
  - prompt, difficulty (1–5), solution (optional), related_topics

Granularity rules
- Prefer one Topic per distinct concept; aggregate multi-source content into the same Topic
- Split when a section is routinely referenced independently or has substantial substructure
- Claims and Definitions live separately when they are reusable or central; otherwise inline in Topic with block refs

Tags standard (see Tags Taxonomy)
- Node type tags: #node/topic, #node/publication, #node/definition, #node/claim, #node/example, #node/question
- Domain tags: #domain/category-theory, #logic/regular, #db/conjunctive-queries, etc.
- Status tags: #status/draft|in-progress|stable|needs-review

Relations standard (see Relations/Relation Types)
- Use Properties ‘relations’ field to hold typed links; each key has a list of [[Note]] links
- Keep directionality as defined; avoid cycles for taxonomy edges (broader/narrower)

Source trails
- Use ‘sources’ and ‘source_refs’ for cite keys and pages; use Citations & Source Trail note to register keys
- PDF annotations can be summarized into Claim/Definition/Example nodes and linked back with page anchors

Dataview conventions
- Use ‘type’, ‘status’, ‘importance’, ‘sources’, ‘relations’ for queries
- Dashboards provide live tables/graphs (see Dashboards folder)

File naming and aliases
- Topic: Topics/Regular Categories.md; aliases: [Regular categories, RegCat]
- Publication: Publications/Fong & Spivak 2019 - Graphical Regular Logic.md
- Definition/Claim/Example: prefixed with the type for clarity, or grouped under Topics with block references

Review cadence
- Set review.next for important nodes; update review.last when edited

Change policy
- Backward-compatible additions to properties; breaking changes require bumping Version and updating Templates