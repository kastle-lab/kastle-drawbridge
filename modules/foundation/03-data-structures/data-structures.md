# Data Structures

Data structures are a fundamental aspect of computer science, allowing developers to organize, manage, and store data efficiently. In Python, several built-in data structures provide versatile and efficient tools for different programming tasks.

## Lists (Arrays)

A list is an ordered, mutable collection that can store a variety of data types, including other lists.

Key Features:

- Ordered: Maintains the order of elements.

- Mutable: Elements can be changed after creation.

- Heterogeneous: Can store different data types in the same list.

```py
# Creating a list
fruits = ["apple", "banana", "cherry"]

# Accessing elements
print(fruits[1])  # Output: banana

# Modifying elements
fruits[0] = "grape"
print(fruits)  # Output: ['grape', 'banana', 'cherry']

# Appending elements
fruits.append("orange")
print(fruits)  # Output: ['grape', 'banana', 'cherry', 'orange']
```

## Dictionaries

Dictionaries store data as key-value pairs, allowing fast lookups by keys.

Key Features:

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

## Sets

A set is an unordered collection of unique elements.

Key Features:

- Unordered: No specific order of elements.

- Unique: Duplicate elements are automatically removed.

- Mutable: Can add or remove elements.

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

## Tuples

A tuple is an ordered, immutable collection of elements.

Key Features:

- Ordered: Maintains the order of elements.

- Immutable: Cannot be changed after creation.

- Can store heterogeneous data types.

```py
# Creating a tuple
coordinates = (10, 20, 30)

# Accessing elements
print(coordinates[1])  # Output: 20

# Tuples are immutable, so the following line would raise an error
# coordinates[1] = 40
```
