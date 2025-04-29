# Introduction

SPARQL Protocol and RDF Query Language (SPARQL - pronounced "sparkle") is a database query language that is explicitly used for data stored in the format of Resource Description Framework (RDF).

# Concepts

More information about these concepts can be explored using the links in the [Resources](#Resources) section at the bottom of this page.

## Resource Descriptive Framework (RDF)

RDF is the standard for representing web data. This standard was set by the World Wide Web Consortium (W3C), a non-profit international organization that creates standards for developing the World Wide Web (Web).

RDF data is in a directed, labeled graph format and is structured in the form of RDF Triples: `subject-predicate-object` (s-p-o) to describe the relationship between things. RDF Triples are also referred to as "semantic triples", "statements", or "triples." To further break down the concept of a triple, think of it in the following way:

- `Subject` -> entity identifier
- `Predicate` -> attribute name
- `Object` -> attribute value

## Uniform Resource Identifier (URI)

RDF uses Uniform Resource Identifier (URI) to identify resources such as webpages, material objects, or other concepts.
URIs provide users with the information needed to find and access the source of the data. Think of URIs as references.

# Query Syntax

Below is a simple example of a SPARQL query. To summarize, this query will return all subjects, under the variable `?kastle_member`, linked by the predicate `klab:member` to any object.

```sparql
PREFIX klab: <https://kastle-lab.org/ontology/>

SELECT ?kastle_member
WHERE{
  ?kastle_member klab:member ?something .
}
```

Let's further break down the components of a SPARQL query.

### Punctuation

Punctuation is vital in SPAQRL as it gives language specific instructions and makes queries more condensed and readable.

- `.` - Period: Means the `end` of a triple pattern or statement.
- `,` - Comma: Used to save space when the `subject` and `predicate` are the same for multiple variables.
- `;` - Semicolon: Used to save space when the `subjects` are the same between multiple variables.

### Prefixes

Prefixes are used to shorten URIs via an abbreviation and are defined using `PREFIX`. Prefixes are always declared at the top of the query.

Our prefix in the example above allows us to use `klab:member` in lieu of inputting the entire URI. If we didn't use a prefix, this is what the query from above would look like:

```sparql
SELECT ?kastle_member
WHERE{
  ?kastle_member <https://kastle-lab.org/ontology/member> ?something .
}
```

If your data set contains several URIs, typing each one out multiple times would be quite tedious, which is why it is standard practice to use prefixes.

### Select

`SELECT` defines the variables returned from your query results. In the primary example , `?kastle_member` is the variable we want returned, which is placed in the `subject` part of the triple pattern.

### Where

This is where the defined triple patterns you want to search for go.

# Advanced Queries

There are many expressions to further refine your SPARQL query. We will go over the most common ones below. However, there are many other expressions that can be explored in the W3C SPARQL documentation from the [Resources](#Resources) section at the bottom of this page.

### Filter

`FILTER` will restrict query results to return results equal to `True` based on the filter expression.

The example below filters for results of `?kastle_members` who are above the age of twenty-five with the `?age` variable.

```sparql
PREFIX klab: <https://kastle-lab.org/ontology/>

SELECT ?kastle_member ?age
WHERE{
  ?kastle_member klab:member ?something ;
                 klab:age ?age .
  FILTER (?age > 25)
}
```

### Count

`COUNT` is a SPARQL set/aggregate function that counts the number of elements returned in the results. It is frequently used with the `GROUP BY` modifier but can also be used standalone by using `COUNT(*)`; this counts all results. The results from the `COUNT` function can be given their own variable, as seen in the example below.

```sparql
PREFIX klab: <https://kastle-lab.org/ontology/>

SELECT ?kastle_member ?age (COUNT(?kastle_member) as ?member_count)
WHERE{
  ?kastle_member klab:member ?something;
                 klab:age ?age .
  FILTER (?age > 25)
}
```

## Modifiers and Clauses

Query results are typically unordered, but SPARQL has many modifiers that can be used to structure how the results are returned. Modifiers and clauses are declared after the `WHERE` block.

### Limit

The `LIMIT` clause will trigger results to display to the user once the declared limit has been reached or the search has been fully completed.

The example below will display results to the user once 5 results for the `?kastle_member` variable have been gathered.

```sparql
PREFIX klab: <https://kastle-lab.org/ontology/>

SELECT ?kastle_member
WHERE{
  ?kastle_member klab:member ?something .
}
LIMIT 5
```

### Order By

The `ORDER BY` modifier will change the sequence in which the results are returned. You can order the variables in ascending or descending order. The order by modifier defaults to ascending order. Descending order must be declared.

The example below will display the results in descending order of the `?age` variable.

```sparql
PREFIX klab: <https://kastle-lab.org/ontology/>

SELECT ?kastle_member ?age
WHERE{
  ?kastle_member klab:member ?something .
  ?kastle_member klab:age ?age .
  FILTER (?age > 25)
}
ORDER BY DESC(?age)
```

# Resources

### SPARQL

- [SPARQL Dev - Learn SPARQL](https://sparql.dev/)
- [SPARQL Dev - Tutorial Video](https://youtu.be/FvGndkpa4K0?si=Nr09D5x3k0qDZr4d)
- [Wikipedia - SPARQL](https://en.wikipedia.org/wiki/SPARQL)
- [W3C - SPARQL Documentation](https://www.w3.org/TR/sparql11-query/)

### RDF

- [Eye on Tech - What is RDF?](https://www.youtube.com/watch?v=NzzAxEPpuJQ&ab_channel=EyeonTech)
- [Wikipedia - RDF](https://en.wikipedia.org/wiki/Resource_Description_Framework)
- [W3C - RDF Standards](https://www.w3.org/RDF/)
- [W3C - RDF Documentation](https://www.w3.org/XML/9711theory/concepts.html)

### URI

- [Wikipedia - URI](https://en.wikipedia.org/wiki/Uniform_Resource_Identifier)


### SPARQL Tutorial

- [SPARQL Tutprial step by step](../03-modeling-technologies/sparql-tutorial.md)