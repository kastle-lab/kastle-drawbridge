# Knowledge Graphs Module

Welcome to the Knowledge Graph module series. This series of modules takes you from foundational graph theory to querying rich semantic data models. Each module includes an **applied assignments** to test your skills, help you reinforce and apply your learning in meaningful ways.

---

## How to Use This Resource

1. **Follow the modules in order** — Each builds on knowledge from the previous one, i.e. later modules assume prior knowledge.
2. **Click the module titles** – They link directly to the learning content.
3. **Complete each assignment** - Sync with the lab members for review, evaluation and feedback.
4. **Ask questions** - Bring them to weekly lab syncs.

---

## Section 1: Graphs

### [Graphs](01-graphs/01-graphs.md)

**Overview**:  
Start with the foundational concept of graphs, i.e. how entities (nodes) connect via relationships (edges). Understand how real-world knowledge is structured graphically.

**What You'll Learn**:

- Define graphs, nodes, and edges
- Explore directed vs. undirected and weighted vs. unweighted graphs
- Understand real-world graph applications

**Assignment:**

- [Build an Ohio City Graph](01-graphs/01-graphs.md#assignment): Design a graph using five major cities in Ohio and their intercity routes. Determine directionality and explore path connections.
- _Goal:_ Apply graph theory to a real map, then analyze structure and paths.

---

### [Graphs in Turtle (TTL)](01-graphs/02-graphs-ttl.md)

**Overview**:  
Learn how RDF data is expressed using the Turtle (TTL) syntax, a general way to represent triples (subject–predicate–object) in semantic web formats.

**What You'll Learn**:

- Convert natural language into RDF triples
- Write Turtle (.ttl) syntax with prefixes and URIs
- Understand how data is serialized for semantic processing

**Assignment:**

- [RDF Turtle Practice](01-graphs/02-graphs-ttl.md#assignment): Write your own `.ttl` file by converting simple natural language statements into RDF triples.
- _Goal:_ Demonstrate understanding of how semantic data is structured and encoded.

---

## Section 2: Modeling Fundamentals

### [Axioms](02-modeling-fundamentals/03-Axioms.md)

**Overview**:  
Axioms are logic-based rules that define structure, meaning and truth in ontologies. Learn how contraints like subclassing, disjointness, and domain/range rules ensure logical consistency in knowledge graphs.

**What You'll Learn**:

- Use Description Logic and Predicate Logic for axioms
- Apply logical constraints to classes and properties
- Understand OWL axioms like Functional, Inverse, and Scoped constraints

**Assignment:**

- [Axiom Assignment](Supplementary-material/Assignments/Axiom-assign.md): Study the top 17 axioms used in KASTLE Lab ontologies and apply them in examples.
- _Goal:_ Demonstrate your command of logical axioms via real modeling scenarios.

---

## Section 3: Modeling Technologies

### [SPARQL](../knowledge-graphs/03-modeling-technologies/04-sparql.md)

**Overview**:  
Master SPARQL, the query language designed for semantic data. From simple SELECT queries to advanced filters and aggregations, learn to retrieve insights from RDF graphs.

**What You'll Learn**:

- Construct SPARQL queries using PREFIX, SELECT, and WHERE
- Apply and use FILTER, LIMIT, ORDER BY, and COUNT
- Build nested and conditional queries

**Assignment:**

- [SPARQL Query Pack](): Write and test 5 queries over your RDF graph covering filters, counts, ordering, and multiple conditions.
- _Goal:_ Gain fluency in writing expressive SPARQL queries.

---

### [Querying Methods](../knowledge-graphs/03-modeling-technologies/06-querying-methods.md)

**Overview**:  
Explore how to query RDF data both programmatically and via triplestore servers using RDFLib (Python) and Apache Jena Fuseki.

**What You'll Learn**:

- Load `.ttl` files using RDFLib (Python)
- Host knowledge graphs using Apache Zena Fuseki
- Query and test local and remote KGS with SPARQL queries

**Assignment:**

- [Setup & Query Your Knowledge Graph with a Triplestore](../knowledge-graphs/03-modeling-technologies/06-querying-methods.md): Use RDFLib to query your local `.ttl` file, and then deploy the same graph to Fuseki and run remote queries.
- _Goal:_ Practice both programmatic and hosted graph querying.

---

### [Schema Diagrams](../knowledge-graphs/03-modeling-technologies/02-schema-diagrams.md)

**Overview**:  
Learn how to visually model your ontology with schema diagrams using tools like yEd. Understand color and shape conventions standards for KASTLE.

**What You'll Learn**:

- Identify ontology components visually
- Use visual syntax to show class hierarchy and properties
- Create diagrams for documentation and reasoning

**Assignment:**

- [Design Your Own Schema Diagram](./project/project.md): Using yEd, draw a schema diagram with at least 3 classes, 2 properties, and relationships. Apply visual rules from this module.
- _Goal:_ Translate textual ontologies into visual knowledge architecture.

---
