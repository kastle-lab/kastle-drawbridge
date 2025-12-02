# Modeling Fundamentals

## [Knowledge Graph](../01-graphs/01-graphs.md)

- (Node, Edge, Node)
- Nodes as Entities/Classes/Subjects
- Edge as Relationships/Predicates
- `Knowledge Graphs` are a `Directed Graph` that associates Class Entities as `Nodes`/`Vertices` and Relationships as `Edges`.

## Linked Data

Knowledge Graphs are designed with principles inherited from Linked Data, which is a set of best practices for publishing structured data onto the Web.

- The set consists of :
  1. The use of URIs as names for things.
  2. The use of HTTP URIs so that people can look up those names.
  3. When someone looks up a URI, the URI must provide useful information.
  4. Inclusion of links to other URIs to provide further insight on the described domain.

## [Ontology](./02-ontology.md)

An `ontology` is a conventional way of representing data within a specific area of thought or domain.

- "is a branch of philosophy...as it considers how knowledge, language, and perception relate to the nature of reality."
- _onto-_,from the Greek, "being; that which is"
- _-logia_ "logical discourse"

### Types of Ontology:

- **Domain Ontology**: representation of concepts from a realm
- **Upper Ontology**: representation of shared relations and objects generally applicable across a wide range of domains
- **Hybrid Ontology**: combining Domain and Upper Ontology

## [Axioms](./03-Axioms.md)

`Axioms` are _asserted_ constraints to how a knowledge graph can be constructed.

Example:

- Person(Cogan), hasFather(Cogan, Bill)
  The above example is written in `First Order Predicate Logic`. In the above example, we assert that Cogan is a Person. It is also asserted that Cogan has a father, and that father is Bill.

### Closed World Assumptions

- Implies that attributes outside the ontology that are not explicitly stated are considered 'False'.

### Open World Assumptions

- Implies that attributes outside the ontology CAN be 'True' (implied).

### Common Axioms and their descriptions

The below illustrates in `Figure 2` common axioms written in Description Logic syntax (discussed in the next section). The numbered list in this depiction describes the axioms in natural language.

![17 axioms](https://github.com/kastle-lab/kastle-drawbridge/assets/70174975/8d3d557f-059a-44cc-a806-068f0222dc5c)

## [Description Logic](https://corescholar.libraries.wright.edu/cse/185/)

> "Description logics (DLs) is a family of knowledge representation (KR) languages which represent knowledge in a domain of interest using formal, logic-based semantics through knowledge bases (KBs) containing general assertions of describing relevant concepts - hence, the term description - and specific assertions about individuals and relationships among them." (Krisnadhi, 2014)

Description Logic, as a set of knowledge representation languages, encompasses the formal representation of knowledge with admittances of _truths_ in the world.

Knowledge can be formally defined with the concepts of TBox and ABox where:

- TBox is a set of axioms constraining terminology definitions (`concepts` or `roles`)
- ABox is a set of axioms constraining `named individuals` (First-Order Logic(R(a,b))

Additionally, Description Logic includes another concept, RBox where:

- RBox is a set of axioms constraining `roles`

> "A description logic (DL) models `concepts`, `roles` and `individuals`, and `their relationships`." - [Wikipedia](https://en.wikipedia.org/wiki/Description_logic)

These asserted admittances are broken down from concept and role constructors:

1. Top and Concept, represented respectively by Tautology(⊤,up tack, falsum, \tee) and Contradiction((⊥, down tack, verum, \bot)
2. nominal
3. Intersection and Union
4. Complements (Negation)
5. Universal Restrictions
6. Existential Restrictions
7. Cardinality Restrictions (at minimum, at maximum, exactly)

### From _ALC_ to _SROIQ_

- _ALC_, or Attributed Language with general Complement,
  - _ALC_ provides support from the above list with including admittances for 1, 3, 4, and 7, along with `TBox` axioms (axioms constraining concepts), and `ABox` axioms (axioms constraining named individuals).
- _SHIF_ extends from _ALC_ and adds `Role` admittances
- _SHOIN_ adds from _SHIF_ with including #2 and #7
- _SROIQ_ combines all of the above with `RBox` Axioms and extends additional constraints to `Roles` and applies numeric conditions and qualifications for 5, 6, 7.

## [Competency Questions](../02-modeling-fundamentals/04-Competency-Question.md)

`Competency Questions` (CQs) are questions formatted in natural language that aid in defining the scope and requirements in knowledge representation.

These questions allow ontology engineer(s) to appropriately process and organize the requirements for the ontology, ensuring it is equipped with all of the information it needs. Additonally, it is used for verification of the ontology in the later stages.

## [Key Notions](./05-key-notions.md)

`Key notions` can be thought of as the fundamental ideas that establish the purpose of a Knowledge Graph (KG) [1]. Concepts that overlap within the competency questions

## [Ontology Design Patterns](./06-ontology-design-patterns.md)

Ontology Design Patterns (ODPs) are small, self-contained ontologies that aim to address general problems in ontology design.

## Resources :

- [Github Repo of open-kg-curriculum](https://github.com/KGConf/open-kg-curriculum/tree/master/curriculum/modules)
- [W3 Wiki](https://www.w3.org/wiki/LinkedData)
- [Ontology](<https://en.wikipedia.org/wiki/Ontology_(information_science)>)
- [Axioms](https://people.cs.ksu.edu/~hitzler/pub2/04-axiomatization.pdf)
- [List of Logic Symbols](https://en.wikipedia.org/wiki/List_of_logic_symbols)

## Preliminary knowledge regarding Knowledge Graphs (KGs):

- [Class and Subclass](https://github.com/KGConf/open-kg-curriculum/blob/master/curriculum/modules/Class_and_Subclass/Class_and_Subclass.md)
- [Description Logic](https://github.com/KGConf/open-kg-curriculum/blob/master/curriculum/modules/Description_Logic/Description_Logic.md)
- [What is a KG](https://github.com/KGConf/open-kg-curriculum/blob/master/curriculum/modules/What_is_a_Knowledge_Graph/What_is_a_Knowledge_Graph.md)
- [What is a Taxonomy](https://github.com/KGConf/open-kg-curriculum/blob/master/curriculum/modules/What_is_a_Taxonomy/What_is_a_Taxonomy.md)
- [What is an Identifier](https://github.com/KGConf/open-kg-curriculum/blob/master/curriculum/modules/What_is_an_Identifier/What_is_an_Identifier.md)
- [What is an Ontology](https://github.com/KGConf/open-kg-curriculum/blob/master/curriculum/modules/What_is_an_Ontology/What_is_an_Ontology.md)
- [What is Metadata](https://github.com/KGConf/open-kg-curriculum/blob/master/curriculum/modules/What_is_Metadata/What_is_Metadata.md)
- [Axioms](https://github.com/KGConf/open-kg-curriculum/blob/master/curriculum/modules/Open_World_Assumption_vs_Closed_World_Assumption/Open_World_Assumption_vs_Closed_World_Assumption.md)
