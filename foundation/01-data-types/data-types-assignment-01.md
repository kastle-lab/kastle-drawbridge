# Datatypes (Types)

Python does not require explicit declaration of data types unlike Java or C-based languages. MORE INFO ON DATA TYPES HERE...

## Numeric Types

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

- <u><strong>String</strong></u>: a series of letters.
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

- <u><strong>List</strong></u>: Lists store data of any type and are created using brackets.
  - Ordered
  - Changeable
  - Duplicates Allowed
  ```py
  companies = ["Microsoft", "Apple", "Dell"]
  numbers = [1, 3, 17, 25, 12]
  bools = [False, True, True]
  multi = ["Text", True, 15, 23.4, 15]
  ```
- <u><strong>Tuple</strong></u>: Tuples are created using parenthesis.
  - Ordered
  - Unchangeable
  - Duplicates Allowed

### Mapping Type

### None Type

# Assignment

Read and implement [the attached assignment](https://github.com/kastle-lab/kastle-drawbridge/blob/master/foundation/supplementary-material/assignments/cs1160-lab02.pdf) such that your output and calculations match the assignment reading's.

Remember that the numeric datatype affects mathematical calculations. For instance, performing `1/2` rounds down and results in `0`; whereas, `1.0/2.0` evaluates to `0.5`. What happens if we mix datatypes together (i.e., performing `1/2.0` or `1.0/2`?

# Resources

- [Python Documentation](https://docs.python.org/3/library/stdtypes.html)
- [W3School](https://www.w3schools.com/python/python_datatypes.asp)
