# Persona Module Lists

This readme contains the list of topics assigned for each persona.

### Structure

The structure of the tuples in the lists are as follows
`module,submodule,topic`

**Example**:

```py
exampleList =  [(1,1,1), (2,3,5)]
```

`Element 0` = foundation->data-types->data-types-and-variables.md

`Element 1` = knowledge-graphs->modeling-technologies->querying-methods.md

# Lists

**Note**:

- `(2,2,x)` -> Need Protege topic in Modeling Fundamentals.

- `(2,3,x)` -> Need Materialization topic in Modeling Technologies.

## Beginner

Assume no solid coding and ontology knowledge; no/weak logic.

```py
begList = [
(1,1,1), (1,2,1), (1,2,2),
(1,3,1), (1,4,1), (1,5,1),
(2,1,1), (2,1,2), (2,2,1),
(2,2,2), (2,2,'x'), (2,2,3),
(2,2,4), (2,2,5), (2,3,1),
(2,3,2), (2,3,'x'), (2,3,3),
(2,3,4), (2,3,5)
]
```

## Beginner/Intermediate

Can code and familiar with general ideas behind logic.

```py
beg_inter = [
(2,1,1), (2,1,2), (2,2,1),
(2,2,2), (2,2,'x'), (2,2,3),
(2,2,4), (2,2,5), (2,3,1),
(2,3,2), (2,3,'x'), (2,3,3),
(2,3,4), (2,3,5)
]
```

## Intermediate

Can make a schema, knows how to use YED.

```py
inter = [
(2,2,'x'), (2,2,3), (2,2,4),
(2,2,5), (2,3,'x'), (2,3,3),
(2,3,4), (2,3,5)
]
```

## Intermediate/Expert

Needs to learn evaluation, but knows most things about ontologies.

**Note**: may want to better define difference between this and expert...

```py
interExp = [
  (2,2,3), (2,2,4), (2,2,5),
  (2,3,3), (2,3,4), (2,3,5)
]
```

## Expert

Can create schema, ontology, and knows methods other than MoMo, Can use query languagues, but not sparql

```py
exp = [
  (2,2,4), (2,2,5), (2,3,3),
  (2,3,4), (2,3,5)
]
```
