# Introduction

SPARQL Protocol and RDF Query Language (SPARQL - pronounced "sparkle") is a database query language that is explicitly used for data stored in the format of Resource Description Framework (RDF).

# Concepts

More information about these concepts can be explored using the links in the "Resources" section at the bottom of this page.

## Resource Descriptive Framework (RDF)

RDF is the standard for representing web data. This standard was set by the World Wide Web Consortium (W3C), a non-profit international organization that creates standards for developing the World Wide Web (Web).

RDF data is in a directed labeled graph format and is structured in the form of RDF triples: `subject-predicate-object` (s-p-o) to describe the relationship between things. RDF Triples are also referred to as "semantic triple", "statements", or "triple." To further break down the concept of a triple, think of it in the following way:

- `Subject` -> entity identifier
- `Predicate` -> attribute name
- `Object` -> attribute value

## Uniform Resource Identifier (URI)

RDF uses Uniform Resource Identifier (URI) to identify resources such as webpages, material objects, or other concepts.
URIs provide users with the information needed to find and access the source of the data. Think of URIs as references.

# Query Syntax

Below is a simple example of a SPARQL query. To summarize, this query will return all subjects linked by the predicate `klab:member` to any object.

```sql
PREFIX klab: <https://kastle-lab.org/ontology/>

SELECT ?kastle_member
WHERE{
  ?kastle_member klab:member ?something .
}
```

Let's further break down the components of the example query.

### Prefixes

Prefixes are used to shorten URIs via an abbreviation.

Our prefix in the example above allows us to use `klab:member` in lieu of inputting the entire URI. If we didn't use a prefix, this is what the query from above would look like.

```sql
SELECT ?kastle_member
WHERE{
  ?kastle_member <https://kastle-lab.org/ontology/member> ?something .
}
```

If your data set contains several URIs, typing each one out multiple times would be quite tedious, which is why it is standard practice to use prefixes.

### Select

SELECT defines the variables returned from your query results. In the primary example , `?kastle_member` is the variable we want returned, which is placed in the `subject` part of the `triple pattern`.

### Where

This is where the triple pattern that you want to search for goes.

## Advanced

### Filter

### Limit

### OrderBy

### Count

## Query Pattern

## Modifiers

# Resources

### Sparql

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

### OWL

- [Wikipedia - OWL](https://en.wikipedia.org/wiki/Web_Ontology_Language)

### Ontology

- [Wikipedia - Ontology](<https://en.wikipedia.org/wiki/Ontology_(information_science)>)
