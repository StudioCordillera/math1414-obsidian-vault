# Relation Types (controlled vocabulary)

Use these typed relations in frontmatter (relations: []) and/or in-body Relation blocks.

- broader: Parent topic or more general concept
- narrower: Child topic or more specific concept
- related: Lateral association without hierarchy
- depends_on: Prerequisite concept/result needed to understand or prove
- defines: Definition node that defines a concept/topic
- defined_in: Topic/page where a definition is housed
- proves: Claim node that establishes a result about a topic
- about: Topic(s) that a claim/result concerns
- uses: Concept/result/tool used inside a proof or construction
- exemplifies: Example that instantiates a definition/result
- equivalent_to: Logical or categorical equivalence between concepts/claims
- contradicts: Incompatible statements (rare; use carefully)
- part_of: Structural inclusion (e.g., rule is part_of calculus)
- has_part: Inverse of part_of

Usage patterns
- Definition ↔ Topic: (Definition) defines → (Topic); (Topic) defined_in → (Definition) [optional]
- Claim ↔ Topic: (Claim) proves → (Topic); (Claim) about → (Topic)
- Claim ↔ Claim: (Claim A) depends_on → (Claim B) when B is used in proof of A
- Topic hierarchy: broader/narrower to maintain content-first structure
- Cross-cutting: related for lateral links; uses for proof ingredients

Conventions
- Prefer minimal, meaningful edges; avoid redundant cycles
- Keep relations directional as specified; add inverse only when queried often
- For multi-topic claims, include all major about targets
- Review cadence: status/review.next fields drive weekly audits via dashboards