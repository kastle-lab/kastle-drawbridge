# Introduction

SPARQL Protocol and RDF Query Language (SPARQL - pronounced "sparkle") is a database query language that is explicitly used for data stored in the format of Resource Description Framework (RDF).

# Concepts

More information about these concepts can be explored using the links in the "Resources" section at the bottom of this page.

## Resource Descriptive Framework (RDF)

RDF is the standard for representing web data. This standard was set by the World Wide Web Consortium (W3C), a non-profit international organization that creates standards for developing the World Wide Web (Web).

RDF data is in a directed labeled graph format and is structured in the form of RDF triples: 'subject-predicate-object'. RDF Triples are also referred to as "Semantic triple" or "triple."

RDF uses Uniform Resource Identifier(URI) to identify resources such as webpages, material objects, or other concepts. URIs provide users with the information needed to find and access the original data source. Think of URIs as references.

## SPARQL

SPARQL is the query language used to retrieve information from databases that use the RDF format.

### Syntax

- Select
- Where
- Filter
- Limit
- OrderBy
- Count
  (;, , , . , limit, order by, count, filter)

### Prefix

### Query Pattern

### Modifiers

### Advanced

# Examples

```sql
SELECT ?thing1 ?thing2 ?thing3
WHERE
{
  ?thing1 .
  ?thing2 .
  ?thing3
}
```

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
