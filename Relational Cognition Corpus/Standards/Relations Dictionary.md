Title: Typed Relations Dictionary

Purpose
- Define and standardize the meaning of link relations used in frontmatter and inline annotations.

Conventions
- Relations are expressed in frontmatter as arrays of wikilinks, e.g.:
  broader: ["[[Regular Logic and Graphical Regular Logic]]", "[[Regular Categories]]"]
- Inline, you may annotate links with relation tags using the syntax [[Target Note|label]] ^rel:requires

Relations
- broader: Parent concept(s) that subsume this node.
- narrower: Subconcepts fully contained within this node’s scope.
- related: Lateral associations without prerequisite entailment.
- requires: Prerequisite knowledge needed to understand or apply this node.
- supports: Concepts, topics, or results that this node enables.
- defined_by: Definition nodes that formally define a key term on this page.
- defines: Concepts or terms that this node introduces/defines.
- proves: Theorems that are proven in this note (topic or proof node).
- proved_by: Proof notes providing a proof of a theorem on this page.
- examples: Example notes illustrating this concept.
- used_in: Course modules, lessons, or projects that use this node.

Examples
- Regular Logic is broader than Graphical Regular Logic; GRL requires Regular Categories and Relations.
- Subobject Classifier supports Truth Values, which supports Regular Logic’s ∧, ∃ semantics.

Dataview Usage
- You can query forward or inverse relations to build dashboards (e.g., show all nodes that require this one).
