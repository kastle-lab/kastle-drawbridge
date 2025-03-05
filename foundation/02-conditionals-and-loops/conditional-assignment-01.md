# Conditionals in Python

Conditionals help programs make decisions. They check if something is true or false and then run different parts of the code based on that check. This helps make programs more flexible and useful.

Python has three main conditional statements: `if`, `elif`, and `else`. These help the program decide what to do depending on different conditions.

## If-Else Statement
```py
# Check if a condition is true
if condition:
    # Do something if the condition is True
    pass
else:
    # Do something else if the condition is False
    pass
```

### Example:
```py
# Assign a number to 'value'
value = 10

# Check if 'value' is greater than 5
if value > 5:
    print("Value is greater than 5")
else:
    # If not, print this message
    print("Value is 5 or less")
```

## Using Conditionals within the  rdflib starter code

When building a Knowledge Graph, conditionals assist when we want to make sure the data we are using are satisfying certain conditions we define. Below there is a snippet of the rfdlib starter code with a modification that uses conditions, that demonstrates how conditionals are used when adding data to our graph.

```py
from rdflib import Graph, URIRef, RDF, Namespace

# Create an RDF graph
graph = Graph()

# Define a namespace (like a category for data)
ex = Namespace("https://example.com/")

# List of names to add to the graph
data_entries = ["Alice", "Bob", "Charlie"]

# Go through each name in the list
for name in data_entries:
    # Create a unique reference for each name
    person_uri = ex[name]
    
    # If the name starts with 'A', mark it as 'SpecialPerson'
    if name.startswith("A"):  
        graph.add((person_uri, RDF.type, ex["SpecialPerson"]))
    else:
        # Otherwise, mark it as 'RegularPerson'
        graph.add((person_uri, RDF.type, ex["RegularPerson"]))
```

## Assignment
Read and complete [this assignment](https://github.com/kastle-lab/kastle-drawbridge/blob/master/foundation/supplementary-material/assignments/cs1160-lab03.pdf) to practice using conditionals.

## Resources
- [Python If Statements](https://docs.python.org/3/tutorial/controlflow.html#if-statements)
- [Python Conditions - W3Schools](https://www.w3schools.com/python/python_conditions.asp)
- [RDFlib Documentation](https://rdflib.readthedocs.io/en/stable/)

