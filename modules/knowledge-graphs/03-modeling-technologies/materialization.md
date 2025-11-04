# Materialization

Materialization is the term used to describe the process of applying the axioms from an ontology to a knowledge graph, reasoning over the data, and explicitly populating the graph with triples formed from the raw data. The result is a materialized graph, which can then be queried more efficiently and thoroughly.

In simple terms, it means applying reasoning rules from your ontology to your knowledge graph so that you take your initial data, apply the logic defined in your schema (like “every Person is also an Agent”), and expand your graph with all the facts that follow from that logic.

This process helps you query your data more efficiently and with more accurate results, since all inferred relationships are already materialized in the graph.

This can be achieved by extending and building on top of the [RDFLib starter code](../../../resources/rdflib-starter.py) to fit to your usecase.

## Why is it important
 - Materialization makes implicit facts explicit.
 - Without it, your queries only “see” directly stated facts from your data.
 - With it, your graph includes all facts that logically follow from your ontology, even those not originally in your raw data.

##### Example
Say if your data has a fact which says: `dog` is an `Animal`

But your ontology has rules like:
 - `Animal` is a `Living Organism`
 - `Living Organism` has `Habitat`

Then without materialization your graph will only have "`dog` is an `Animal`", but with materialization, it will have
 - `dog` is an `Animal`
 - `dog` is an `Living Organism`
 - `dog` has `Habitat`

## What is a materialized graph?
A materialized graph is the original graph that is obtained by extracting the knowledge from all of your available data according to the designed schema/ontology and then explicitly being added to the graph.

##### Example
If your ontology says `ex:Person rdfs:subClassOf ex:Agent` and you have a triple `ex:Cogan rdf:type ex:Person` from your data and in your knowledge graph, then materialization adds: `ex:Cogan rdf:type ex:Agent`.

## What is a fully materialized graph?
A fully materialized graph is a materialized graph that is closed under the chosen rule set (i.e. materialized graph plus all triples that logically follow from the ontology axioms that have been actually asserted) such that all possible consequences of the chosen inference rules have already been added. This means that if you take the resulting graph and re-apply the same inference rules (e.g., simple RDFS rules) on it, no new triples can be produced, i.e. it already contains every fact that can be logically derived from the asserted data and ontology.

## Pros and Cons of Materialization
Even though materialization enables completeness of the designed knowledge graph, it also has some benefits and downsides:

### ✅ Benefits
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;\+ Explicit declaration of inferred data<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;\+ Faster and efficient querying<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;\+ More complete results<br>

### ⚠️ Downsides
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;\- Increased storage requirements<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;\- Mitigation: Can split large materialized graphs into multiple output files or graph DBs that support compression or lazy materialization<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;\- Longer preprocessing times<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;\- Mitigation: Can retort to Incremental Materialization (triplfying subsets of data in phases and loading to a store)

### ❗Important Step before begining Materialization
Make sure your data is clean and normalized before loading it into RDFLib. This is crucial for error-free materialization.
Typical steps include:
 - Remove inconsistent entries in your CSV/TXT sources. (e.g., drop rows with missing or mismatched identifiers and addressing typos)
 - Standardize names, URIs, and formats. (e.g., ensure all URIs use lowercase and a consistent namespace pattern.)
 - Ensure consistent prefix usage and association to data. (e.g., prefixes like `ex:` and `rdf:` must align across datasets.)
 - Verify your ontology (e.g., check that subclass and domain/range rules are applied to the correct data entities, not just class names.).


## RDF Materialization With Example:
We will illustrate materialization with a simple example. Here, we will proceed with:
 1. Loading some original triples into a graph (can already added by the [RDFLib starter code](../../../resources/rdflib-starter.py))<br>This step helps you 1. initialize an RDF graph, 2. Bind namespace prefixes and 3. Add a few example triples.<br>
    ```python
        kastle_members = ["Cogan", "Andrea", "Brandon"]
        for x in kastle_members:
            graph.add( (pfs["ex"][x], a, pfs["ex"]["Person"]) ) # Adds the triples for Cogan, Andrea and Brandon
    ```
    So the original triples added in the initial RDF knowledge graph will be as follows:
    ```bash
        # Original Triples
        ex:Cogan   rdf:type  ex:Person .
        ex:Andrea  rdf:type  ex:Person .
        ex:Brandon rdf:type  ex:Person .
    ```

 2. Adding an ontology axiom, for instance lets take Axiom 1 (Subclass) `?Class_1 rdfs:subClassOf ?Class_2` and define a rule in our ontology: every `Person` is also an `Agent`.
    ```bash
    # Sample Ontology Axiom 1 (we add this explicitly to the same graph)
    ex:Person  rdfs:subClassOf  ex:Agent .
    ```
 3. Materialize by adding the inferred rdf:type for each instance via chosen Axiom rules. For Axiom 1, the RDFS rule used (informally) is: `If ?X rdfs:subClassOf ?Y and ?x rdf:type ?X, then add ?x rdf:type ?Y.`
 After full materialization over the graph instances across all rules, new triples can be inferred.
    ```bash
    # Inferred Triples (after materialization)
    ex:Cogan   rdf:type  ex:Agent .
    ex:Andrea  rdf:type  ex:Agent .
    ex:Brandon rdf:type  ex:Agent .
    ```
At this point, under this simple rule set, the graph is fully materialized. Applying the same subclass rule again won’t yield any new triples (no further superclasses were asserted)

### Implementation with RDFLib
This can be achieved by modifying the [RDFLib starter code](../../../resources/rdflib-starter.py) with applicable axiom codes.<br>
<b>Note: You’ll need to modify and extend this starter code for your own use case. It’s just a template to get you going.</b>

The current starter code already gives you:
 - Bound namespaces (e.g., `pfs["ex"], pfs["rdfs"]`, and `a = pfs["rdf"]["type"]`)
 - An initialized graph and three `ex:Person` instances

You can add the axiom and then materialize with a simple pass.
```python
# Add a tiny ontology axiom
graph.add( (pfs["ex"]["Person"], pfs["rdfs"]["subClassOf"], pfs["ex"]["Agent"]) )

# Materialize via the RDFS subclass rule: if x a Person and Person ⊑ Agent, add x a Agent
for s, _, _ in graph.triples( (None, a, pfs["ex"]["Person"]) ):
    graph.add( (s, a, pfs["ex"]["Agent"]) )
```

You can save your materialized graph as a `.ttl` (Turtle) file:
```python
graph.serialize(destination="<materialized_graph_file_name>.ttl", format="turtle")
```
❌ Without proper materialization, you ttl file will have only raw data triples and will look like this:
```ttl
@prefix ex: <http://example.org/> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

ex:Cogan   rdf:type         ex:Person .
ex:Andrea  rdf:type         ex:Person .
ex:Brandon rdf:type         ex:Person .
```

✅ But with full materialization, your saved file will look like this:
```ttl
@prefix ex: <http://example.org/> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

ex:Person  rdfs:subClassOf  ex:Agent .
ex:Cogan   rdf:type         ex:Person, ex:Agent .
ex:Andrea  rdf:type         ex:Person, ex:Agent .
ex:Brandon rdf:type         ex:Person, ex:Agent .
```

Similarly, you can expand this pattern with other axioms according to your ontology modeling and design. 
``` bash
# Domain (Axiom 3)
if ?p rdfs:domain ?X and (s, p, o) occurs, add s rdf:type X.

# Range (Axiom 5)
if ?p rdfs:range ?X and (s, p, o) occurs, add o rdf:type X.
```

Each time upon finishing a materialization pass, it adds all missing consequences as explicit triples, and you will have a materialized graph. If another pass adds nothing new, it is now a fully materialized graph (w.r.t. the rules (axioms) chosen).


## Advanced Considerations
 ### Materialization vs. Query-Time Reasoning
 Materialization is not the only way to infer all triples. You can also perform query time reasoning to achieve similar results. Below are some tradeoffs for each:

    | Aspect        | Materialization                | Query-Time Reasoning          |
    | ------------- | ------------------------------ | ----------------------------- |
    | Preprocessing | High (reasoning done up front) | Low                           |
    | Query speed   | Fast (no runtime inference)    | Slower (reasoning on the fly) |
    | Storage       | Larger (all inferred triples)  | Smaller                       |
    | Best use case | Read-heavy, static datasets    | Frequently changing datasets  |
 
 ### Common Pitfalls and their fixes

    | Pitfall                                                   | How to Fix                                                |
    | --------------------------------------------------------- | --------------------------------------------------------- |
    | Forgetting to clean input data                            | Always preprocess CSV/TXT files before loading            |
    | Overconsideration for duplicate triples in materializtion | Triplestores handle for duplicate and maintain uniqueness |
    | Wrong namespaces                                          | Double-check bound prefixes in your graph setup           |
    | Large dataset performance issues                          | Use incremental or lazy materialization                   |

## Quick Recap:
 - Materialization = reasoning applied once upfront -> explicit, fast, complete graph
 - Fully materialized = all logical consequences added -> no more new triples
 Always normalize and clean data first, modify the starter code for your own rules, and verify your results with .ttl output.

# References
 - [Oxford Semantic Tech](https://www.oxfordsemantic.tech/glossary/materialisation)
 - [RDFLib Documentation](https://rdflib.readthedocs.io/)