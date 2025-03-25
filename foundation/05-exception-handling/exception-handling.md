# Exception Handling

Exceptions are used to handle errors in a program when they occur, and to prevent the program from crashing. In python the try-except block is used to handle exceptions.

## Try-Except Block

```py
import os

# This function will attempt to find a file within a specified directory and subdirectories. Then it will return the absolute path of that file.
def Find_File(fileName, desiredDirectory):

  # This code in the try block will attempt to run. If an exception occurs the "except" blocks will run depending on the type of exception that occurs.
  try:
    for root, dirs, files in os.walk(desiredDirectory):
      if fileName in files:
        print("File found!")
        return os.path.join(root, fileName)

  # This except block will run if the file is not found.
  except FileNotFoundError:
    print(f"\nError: '{fileName}' not found.")

  # This except block will run if the user does not have permission to access the file.
  except PermissionError:
    pass # A placeholder until the desired code is implemented

  # This exception will resolve all other unspecified exceptions.
  except Exception as e:
    print(f"\nError: An unknown error occured: {e}")

```

Python has built in exceptions like the ones above: `FileNotFoundError`, `PermissionErrror` and `Exception`. The try except blocks prevent the user from seeing the traceback errors (typically meant for developers) and instead allows for customized messages that let the user know an error occurred.

The `pass` statement seen in the `PermissionError` exception will result in no message or traceback response. This is typically used as a placeholder until a desired task is implemented. Other exceptions exist and can be explored in the following resources below.

## Assignment

Read and complete [this assignment](/foundation/supplementary-material/assignments/assgn-6.md) to practice using exceptions and data structures (list).

## Resources

- [PyDocs on Exceptions](https://docs.python.org/3/library/exceptions.html)
- [PyDocs on Errors](https://docs.python.org/3/tutorial/errors.html)
- [Geeks for Geeks](https://www.geeksforgeeks.org/python-exception-handling/)
- [W3 School](https://www.w3schools.com/python/python_try_except.asp)
