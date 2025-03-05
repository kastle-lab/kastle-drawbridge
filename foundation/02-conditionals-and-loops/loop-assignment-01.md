# Looping in Python

In programming, a loop is a tool that allows you to repeat the same block of code multiple times without writing it out each time. This is especially useful when working with tasks that need to be done repeatedly, such as handling data. When having to go through large data sources to add, retrieve or delete etc, looping saves time. Instead of writing separate instructions for each piece, a loop enables you to automatically process all of them in one go.

## For Loop
A `for` loop repeats a set number of times or goes through a list of items.

```py
# Loop through numbers 0 to 2
for i in range(3):
    print("Iteration:", i)
```

## While Loop
A `while` loop runs as long as a condition is true.

```py
i = 0
while i < 3:
    print("Iteration:", i)
    i += 1
```

## Using Loops with rdflib

When building a Knowledge Graph, loops assist when we want to iterate through out data and add them to our graph without doing so manually. Below there is a snippet of the rfdlib starter code that uses a for loop when adding data into the graph.
```py
from rdflib import Graph, URIRef, RDF, Namespace
# Initialization shortcut
def init_kg(prefixes=pfs):
    kg = Graph()
    for prefix in pfs:
        kg.bind(prefix, pfs[prefix])
    return kg
# rdf:type shortcut
a = pfs["rdf"]["type"]
# Initialize an empty graph
graph = init_kg()

kastle_members = ["Cogan", "Andrea", "Brandon"]
for x in kastle_members: # adds all members iteratively
    # Add a specific triple
	# g.add( (subject_node, predicate_node, object_node) )
	graph.add( (pfs["ex"][x], a, pfs["ex"]["Person"]) )
```

## Assignment
Read and complete [this assignment](https://github.com/kastle-lab/kastle-drawbridge/blob/master/foundation/supplementary-material/assignments/cs1160-lab03.pdf) to practice using loops in Python.

## Resources
- [Python Loops - W3Schools](https://www.w3schools.com/python/python_loops.asp)
- [RDFlib Documentation](https://rdflib.readthedocs.io/en/stable/)

