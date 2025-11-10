
---

# Automated Content Quality Validator

## **Quality Validation Queries**

### **1. Node Standard v2.0 Compliance Check**
```dataview
TABLE file.name AS "Node", type, status, importance, tags
FROM "Relational Cognition Corpus"
WHERE (file.name != "00_Specs") AND (contains(string(this.file.frontmatter), "dv_type") OR contains(string(this.file.frontmatter), "dv_domain"))
SORT file.name ASC
```

### **2. Deprecated Tag Namespace Detection**
```dataview
TABLE file.name AS "Node", tags
FROM "Relational Cognition Corpus" 
WHERE contains(string(tags), "node/") OR contains(string(tags), "domain/")
SORT file.name ASC
```

### **3. Required Field Validation**
```dataview
TABLE file.name AS "Node", type, status, importance
FROM "Relational Cognition Corpus"
WHERE (file.name != "00_Specs") AND (!type OR !status OR !importance)
SORT file.name ASC
```

### **4. Source Documentation Completeness**
```dataview
TABLE file.name AS "Node", type, sources, source_refs
FROM "Relational Cognition Corpus"
WHERE type IN ["Definition", "Claim"] AND (!sources OR !source_refs)
SORT type, file.name ASC
```

### **5. Relationship Link Integrity**
```dataview
TABLE file.name AS "Node", type, relations
FROM "Relational Cognition Corpus"
WHERE type AND (!relations OR length(keys(relations)) = 0)
SORT type, file.name ASC
```

## **Quality Metrics Dashboard**

### **Standards Compliance Score**
- **v2.0 Compliant Nodes**: `= length(filter(file.lists.type, (x) => x != null AND !contains(string(file.frontmatter), "dv_type")))` / `= length(file.lists.type)` × 100%
- **Current Tag Namespace Usage**: `= length(filter(file.lists.tags, (x) => !contains(string(x), "node/") AND !contains(string(x), "domain/")))` / `= length(file.lists.tags)` × 100%
- **Complete Documentation**: `= length(filter(file.lists, (x) => x.sources != null AND x.source_refs != null))` / `= length(filter(file.lists, (x) => x.type = "Definition" OR x.type = "Claim"))` × 100%

### **Quality Gate Thresholds**
- **A+ Grade (98-100%)**: All nodes v2.0 compliant, complete documentation, bidirectional relationships
- **A Grade (95-97%)**: <5% deprecated elements, >95% complete documentation  
- **A- Grade (90-94%)**: <10% deprecated elements, >90% complete documentation
- **B+ Grade (85-89%)**: <15% deprecated elements, >85% complete documentation

## **Automated Validation Checklist**

### **✅ Phase 3 Quality Standards**
- [ ] **Zero deprecated `dv_type` fields** across all content nodes
- [ ] **Zero deprecated `dv_domain` fields** across all content nodes  
- [ ] **Zero deprecated tag namespaces** (`node/*`, `domain/*`)
- [ ] **100% required field completion** (type, status, importance)
- [ ] **95% source documentation** for Definition/Claim nodes
- [ ] **90% relationship completion** for all concept nodes
- [ ] **Template compliance verification** against Node Standard v2.0
- [ ] **Bidirectional relationship validation** (links point both ways)

### **⚡ Automation Triggers**
- **Daily**: Run compliance check queries 
- **Weekly**: Full quality metrics dashboard update
- **Monthly**: Comprehensive validation against all quality gates
- **On-demand**: Standards conflict detection for new content

---
**Last Updated**: 2025-11-04  
**Quality System**: Node Standard v2.0 + Automated Validation  
**Target Grade**: A (95/100) → A+ (98/100)