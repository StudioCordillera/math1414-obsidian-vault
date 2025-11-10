Title: Node Specification for the Mathematical Relational Vault

Purpose
- Provide a consistent, content-first structure for all knowledge nodes (topics, definitions, theorems, examples, proofs, publications)
- Leverage Obsidian features: Properties (frontmatter), tags, typed link relations, and Dataview indexing

Node Types
- topic: Aggregates content from multiple sources into a single conceptual page
- definition: A canonical definitional entry (often appears inside a topic, but can be standalone if reused)
- theorem: A formal statement, optionally with proof
- example: An illustrative instance linked to a topic/theorem/definition
- proof: A proof object linked to a theorem
- publication: A bibliographic entry for a book or article (maps cite keys to local files)

Required Properties (Frontmatter)
- type: topic | definition | theorem | example | proof | publication
- status: seeded | in-progress | reviewed | canonical | needs-citation
- tags: array of topical tags (see Tag Taxonomy)
- sources: array of cite keys (e.g., [FongSpivak2019, LawvereSchanuel2009])
- pages: list of page anchors: objects of form {key: FongSpivak2019, pages: "12–17"}
- created: ISO date
- updated: ISO date

Core Relations (Frontmatter typed link properties)
- broader: [links] — parent concept(s)
- narrower: [links] — contained sub-concepts
- related: [links] — lateral connections
- requires: [links] — prerequisites
- supports: [links] — consequences/applications
- defined_by: [links] — definitions that define this node
- defines: [links] — concepts this node defines
- proved_by: [links] — proofs that prove theorems on this page
- proves: [links] — theorems proven by attached proofs
- examples: [links] — example notes exemplifying this concept
- used_in: [links] — courses/lessons/projects using this node

Naming and IDs
- Filename should be human-readable; avoid redundant qualifiers
- Optional: id slug in frontmatter for stable references: id: regular-logic-grl

Note Structure (for topic nodes)
1. Summary
2. Definitions (inline or links to definition nodes)
3. Key Results (theorems/lemmas with short statements; link to theorem nodes if detailed)
4. Constructions/Calculus (procedures, graphical rules)
5. Examples
6. Connections (bridges to other topics; CQ/DB, logic bridges, etc.)
7. Source Trail (cite keys + page anchors)

Note Structure (for theorem nodes)
1. Statement
2. Proof (inline or linked proof node)
3. Consequences/Corollaries
4. Examples/Applications
5. Source Trail

Publication Nodes
- type: publication
- fields: authors, year, title, venue/publisher, edition, file, citeKey
- links: topics covered (supports), key definitions/theorems (defines/proves)

Conventions
- Content-first: Topics may aggregate multiple sources; single-source only if content uniquely belongs there
- Keep statements concise; move long expositions to subpages or collapsible sections
- Use tags from the taxonomy; avoid inventing ad-hoc tags without adding to Tag Taxonomy
- Maintain updated and pages on edits

Dataview Patterns
- Index topics by status
- Validate missing properties (e.g., no sources, no broader)
- Surface relation graphs (requires/supports)

Validation Checklist
- Has required properties
- At least one tag
- At least one relation (broader OR requires OR related)
- Source Trail includes at least one cite key
