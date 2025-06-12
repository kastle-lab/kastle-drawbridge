# SPARQL Tutorial

An example RDF dataset is used in this tutorial to demonstrate how a SPARQL query operates. The following picture contrasts RDF data in Turtle syntax (on the right) with a SPARQL query (on the left):

- Colours indicate mapping of the data ot the turtle file to how the query looks for it.

![Sparql mapping query to data](../../images/sparql-mapping.png)

## Step 1: Prefix Declaration

```sparql
PREFIX klab: <https://kastle-lab.org/ontology/>
```

We define the namespace prefix `klab` for convenience, so we can write `klab:member` instead of the full URI `https://kastle-lab.org/ontology/member`.

## Step 2: A SPARQL Query (example)

```sparql
SELECT ?kastle_member ?age
WHERE {
  ?kastle_member klab:member ?something .
  ?kastle_member klab:age ?age .
  FILTER (?age > 25)
}
ORDER BY DESC(?age)
```

### What does this query do?

- `SELECT ?kastle_member ?age`

  - We want to retrieve a kastle lab member and their respective age.

- `WHERE { ... }`

  - Defines the conditions that must be met in our turtle file to retrieve them.

- `?kastle_member klab:member ?something`

  - This means: "Find all subjects that have `klab:member` as a prefix"

- `?kastle_member klab:age ?age`

  - This links the same subject (?klab member) to their respective value.

- `FILTER (?age > 25)`

  - We are interested in results where the age is greater than 25.

- `ORDER BY DESC(?age)`
  - We can sort the results from oldest to youngest.

## RDF Data Example (Turtle Format from an example turtle file)

```turtle
@prefix klab: <https://kastle-lab.org/ontology/> .

<http://example.org/kastle_member1> klab:member <http://example.org/something1> ;
                                     klab:age 30 .

<http://example.org/kastle_member2> klab:member <http://example.org/something2> ;
                                     klab:age 28 .
```

### Breakdown

- Two individuals (`kastle_member1` and `kastle_member2`) are members of "something".
- Both have age values: 30 and 28, respectively.

## Query Execution Result

Based on the query and data, this is what would be returned:

| kastle_member                     | age |
| --------------------------------- | --- |
| http://example.org/kastle_member1 | 30  |
| http://example.org/kastle_member2 | 28  |

Only members older than 25 are included, and the results are sorted in descending order by age.

# Exercise:

- When you are done building your KG, use your competency questions you defined in advance and transform them into SPARQL queries and showcase those results.
