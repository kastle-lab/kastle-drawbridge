# Functions

Functions are reusable blocks of code that perform a specific task. Each programming language comes with their own collection of built in functions, but developers frequently create their own custom functions to suit their needs. However, instead of writing your own functions and "reinventing the wheel," it is common practice to use other predefined functions that others have created for public use. This is done by importing libraries, more on this later.

## User defined functions

Use the keyword `def` to <i>def</i>ine a function and assign it an identifier.

```py
def functionName():
    # Function code goes here
```

Functions typically have information (values) passed into them to process. This is done in the form of arguments: positional or keyword.

- Positional arguments are
- Keyword arguments are

```py
def functionName(argument1, argument2):
    # Function code goes here
```

```py
# This function takes in two numbers and returns the average as a float. **Note**: This function can take in either floats and or integers, but will always return a float due to the syntax for division ("/").
def numAverage(number1, number2):
    average = (number1 + number2) / 2
    return average

# Create variables
num1 = 10 # Dynamically typed as a integer
num2 = 15.5 # Dynamically typed as a float

# Call the user defined function
average = numAverage(num1, num2)

# Print is a built in function that will print the input parameter to the console
print(average)

```

Passing info.

Arguments and Params.

Passing args.

keyword args

Imported functions from library

# Examples

# Resources

[PyDocs - Built-in Functions](https://docs.python.org/3/library/functions.html)

[G4G - Functions](https://www.geeksforgeeks.org/python-functions/)

[w3school - Functions](https://www.w3schools.com/python/python_functions.asp)
