# File Input/Output

## Introduction to File I/O in Python

File I/O (Input/Output) operations are essential when working with data stored in files. Python provides built-in functions to read from and write to files using various methods. Below, we cover the most common techniques for reading and writing files in Python.

### Reading a File (Input)

Reading from a file involves opening the file, processing its content, and then closing it (if necessary). Here are two common methods:

#### **Method 1: Using `open()` and `close()`**

```python
file_name = "some_name.txt"
inpF = open(file_name, 'r')  # Open the file in read mode

# Read and process the file content
content = inpF.read()  # Reads the entire content of the file
print(content)

inpF.close()  # Close the file when done
```

**Note:** Failing to close the file may lead to resource leaks.

#### **Method 2: Using `with` Context Manager**

```python
file_name = "some_name.txt"
with open(file_name, 'r') as inpF:  # Automatically closes the file when done
    content = inpF.read()  # Reads the entire content
    print(content)
```

**Why Use `with`?**

- Automatically handles file closing, even if exceptions occur.
- Cleaner and more Pythonic.

#### Additional Reading Functions

- `read(size)`: Reads `size` bytes from the file.
- `readline()`: Reads a single line from the file.
- `readlines()`: Reads all lines and returns them as a list.

Example using `readlines()`:

```python
with open(file_name, 'r') as inpF:
    lines = inpF.readlines()
    for line in lines:
        print(line.strip())  # Remove newline characters
```

### Writing to a File (Output)

Writing to a file allows you to save data for later use. Be cautious when using write operations, as they can overwrite existing data.

#### **Method 1: Using `open()` and `close()`**

```python
file_name = "output.txt"
outF = open(file_name, 'w')  # Open the file in write mode

outF.write("Hello, World!\n")  # Write a line to the file

outF.close()  # Close the file
```

#### **Method 2: Using `with` Context Manager**

```python
file_name = "output.txt"
with open(file_name, 'w') as outF:
    outF.write("Hello, World!\n")  # Write a line to the file
```

**Why Use `with` for Writing?**

- Ensures the file is properly closed.
- Cleaner code structure.

#### Writing Modes

- `'w'`: Write (overwrites the file if it exists).
- `'a'`: Append (adds new content without deleting existing content).
- `'x'`: Create (fails if the file already exists).

Example using append mode:

```python
with open(file_name, 'a') as outF:
    outF.write("Appended text.\n")
```

### Tips for File I/O

- Always handle exceptions using `try-except` blocks to manage potential errors.

```python
try:
    with open("non_existent_file.txt", 'r') as f:
        print(f.read())
except FileNotFoundError:
    print("File not found.")
```

- Use file paths carefully; consider using the `os` module for cross-platform compatibility.

By mastering these file I/O techniques, you can efficiently handle data storage and retrieval in your Python applications.

# Assignment

Read and implement [the attached assignment](../supplementary-material/assignments/assgn-5.md) such that your output and calculations match the assignment reading's. After the Python scripts run, an `output.txt` file should be generated.

## Extension to Assignment

Originally, the assignment's `output.txt` contains the evaluated solution of two values with a mathematical operator from an input file, `testnums.txt`. Can you figure out how to include the mathematical function to each respective solution when running the calculator without an input file?
For example, an input that appears as:

```
Enter the mathematical operation [a, s, m, d, o, i ,q]: a
Enter the first number in the operation: 4.5
Enter the second number in the operation: 9
4.5 + 9 = 13.5
```

would write to an `output.txt` as:

```
4.5 + 9 = 13.5
```

rather than just the `13.5`?
