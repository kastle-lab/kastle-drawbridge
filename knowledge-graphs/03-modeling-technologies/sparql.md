# Introduction

SPARQL Protocol and RDF Query Language (SPARQL - pronounced "sparkle") is a database query language that is explicitly used for data stored in the format of Resource Description Framework (RDF).

- W3C Standards
- 3 part statements

  - subject - entity identifier
  - Predicate - attribute name
  - Object - attribute value

- Uniform Resource Identifiers (URIs) "identifiers"
  - Prefixes
    - @prefix customName <http://www.ontology-reference.com> (ttl syntax)

# Concepts

### RDF

# Syntax

### Prefix

### Query Pattern

### Modifiers

### Advanced

# Examples

```sql
SELECT ?thing
WHERE
{
  ?thing predicate object .
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
