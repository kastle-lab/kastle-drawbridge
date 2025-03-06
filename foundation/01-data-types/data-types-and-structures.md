# Data types (Types)

Data types give context to a value for a computer to store in memory. As an example, the value 21 without a data type can be a string, integer, or float (more on this later). Without context, the computer will be unsure of how to interact with this data, as each data type will be processed differently. So, how do we give this value context in Python?

First, you need to give it a variable name. Think of a variable name as a label for the value we are about to store. For example, this code

```py
number = int(21)
```

assigns the <u><strong>`value`</strong></u> 21 to the <u><strong>`data type`</strong></u> of <u><strong>`Integer`</strong></u>, which we have given the <u><strong>`variable`</strong></u> name of "`number`". This gives the developer an easy way to manipulate this data later in the code and gives context for the computer to process the data properly.

Python does not require explicit declaration of data types unlike Java or C-based languages. Python will automatically assign a variable a data type based on the syntax. See below for an example.

```py
number = 21   # Integer data type
number = 21.0 # Float data type because of the decimal
number = "21" # String data type because of the quotes
```

## Numeric Types

Numeric data types have a numeric value and can be used in mathematical operations.

- <u><strong>Integer</strong></u>: whole numbers

  ```py
  num = 5       # Variable without type specification
  num = int(5)  # Variable specifying type as an integer
  ```

- <u><strong>Float</strong></u>: similar to a `double` and, as such, can represent decimal values.
  ```py
  dec = 5.32
  dec = float(12.3)
  ```

## Non-Numeric Representation

### Text Sequence Type

- <u><strong>String</strong></u>: a sequences of Unicode characters.
  ```py
  phrase = "This is a string type."
  phrase2 = 'This is also a string type.'
  phrase3 = str("Specify a string type by using str()")
  ```

### Boolean Type

- <u><strong>Boolean</strong></u>: representation of 0 and 1 as `True` and `False` (the `T` and `F` casing matters)
  ```py
  isAlive = False
  isHere = bool(True)
  ```

## Data Structures

Data structures store, organize, and define relationships between data elements. They also provide ways of accessing, interacting with, and modifying the data.

- <u><strong>List</strong></u>: Lists store data of any type and are created using brackets. Each element is separated by a comma and can be accessed via an index value (beginning at 0).
  - Ordered: Maintains the order of elements.
  - Mutable: Elements can be changed after creation.
  - Heterogeneous: Can store different data types in the same list.
  - Duplicates Allowed
  ```py
  companies = ["Microsoft", "Apple", "Dell"]
  numbers = [1, 3, 17, 25, 12]
  bools = [False, True, True]
  multi = ["Text", True, 15, 23.4, 15]
  ```
- <u><strong>Tuple</strong></u>: Tuples are created using parenthesis. They are similar to lists in many ways, with one key difference being that they are immutable.

  - Ordered: Maintains the order of elements.
  - Immutable: Cannot be changed after creation.
  - Can store heterogeneous data types.
  - Duplicates Allowed

  ```py
  gamesTuple = ("The Legend of Zelda: Breath of the Wild", "Escape from Tarkov", "Battlefield V") # A tuple containing strings of video game names

  print(gamesTuple[1])
  # Returns
  # Escape from Tarkov
  ```

* <u><strong>Dictionaries</strong></u>: Dictionaries store data as key-value pairs, allowing fast lookups by keys.

  - Unordered (prior to Python 3.7) and insertion-ordered (from Python 3.7 onwards).

  - Mutable.

  - Keys must be unique and immutable.

  ```py
  # Creating a dictionary
  person = {"name": "Alice", "age": 30, "city": "New York"}

  # Accessing elements
  print(person["name"])  # Output: Alice

  # Modifying values
  person["age"] = 31
  print(person)  # Output: {'name': 'Alice', 'age': 31, 'city': 'New York'}

  # Adding new key-value pairs
  person["profession"] = "Engineer"
  print(person)  # Output: {'name': 'Alice', 'age': 31, 'city': 'New York', 'profession': 'Engineer'}
  ```

* <u><strong>Sets</strong></u>: A set is an unordered collection of unique elements.

  - Unordered: No specific order of elements.

  - Unique: Duplicate elements are automatically removed.

  - Mutable: Can add or remove elements.

  - Duplicates not allowed

  ```py
  # Creating a set
  numbers = {1, 2, 3, 3, 4}
  print(numbers)  # Output: {1, 2, 3, 4}

  # Adding elements
  numbers.add(5)
  print(numbers)  # Output: {1, 2, 3, 4, 5}

  # Removing elements
  numbers.remove(2)
  print(numbers)  # Output: {1, 3, 4, 5}
  ```

There are over a dozen different types in Python, and it is recommended that this topic be further explored for a more advanced understanding. See the Resources section below for more information about data types in Python.

# Assignment

ASSIGNMENT GOES HERE!

# Resources

- [W3school - Python Variables](https://www.w3schools.com/python/python_variables.asp)
- [Python Guides - What are variables?](https://pythonguides.com/python-variables/)
- [G4G - Data Types in Programming](https://www.geeksforgeeks.org/data-types-in-programming/)
- [PyDocs - Types](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)
- [PyDocs - Data Structures](https://docs.python.org/3/tutorial/datastructures.html#tuples-and-sequences)
- [W3School - Types](https://www.w3schools.com/python/python_datatypes.asp)
