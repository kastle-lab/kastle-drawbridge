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

### Sequence Types

- <u><strong>List</strong></u>: Lists store data of any type and are created using brackets. Each element is separated by a comma and can be accessed via an index value (beginning at 0).
  - Ordered
  - Changeable
  - Duplicates Allowed
  ```py
  companies = ["Microsoft", "Apple", "Dell"]
  numbers = [1, 3, 17, 25, 12]
  bools = [False, True, True]
  multi = ["Text", True, 15, 23.4, 15]
  ```
- <u><strong>Tuple</strong></u>: Tuples are created using parenthesis. They are similar to lists in many ways, with one key difference being that they are immutable.

  - Ordered
  - Unchangeable
  - Duplicates Allowed

  ```py
  gamesTuple = ("The Legend of Zelda: Breath of the Wild", "Escape from Tarkov", "Battlefield V") # A tuple containing strings of video game names

  print(gamesTuple[1])
  # Returns
  # Escape from Tarkov
  ```

There are over a dozen different types in Python, and it is recommended that this topic be further explored for a more advanced understanding. See the Resources section below for more information about data types in Python.

# Assignment

Read and implement [the attached assignment](../supplementary-material/assignments/assgn-1.md) such that your output and calculations match the assignment reading's.

Remember that the numeric datatype affects mathematical calculations. For instance, performing `1/2` rounds down and results in `0`; whereas, `1.0/2.0` evaluates to `0.5`. What happens if we mix datatypes together (i.e., performing `1/2.0` or `1.0/2`)?

# Resources

- [W3school - Python Variables](https://www.w3schools.com/python/python_variables.asp)
- [Python Guides - What are variables?](https://pythonguides.com/python-variables/)
- [G4G - Data Types in Programming](https://www.geeksforgeeks.org/data-types-in-programming/)
- [Python Official Documentation - Types](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)
- [W3School - Types](https://www.w3schools.com/python/python_datatypes.asp)
