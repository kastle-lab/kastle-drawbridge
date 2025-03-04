# Exception Handling

Exceptions are used to handle errors in a program when they occur, and to prevent the program from crashing. In python the try-except block is used to handle exceptions.

## Try-Except Block

```py
import os
# This function will attempt to find a file within a specified directory and subdirectories. Then it will return the absolute path of that file.
def Find_File(fileName, desiredDirectory):
  try:
    for root, dirs, files in os.walk(desiredDirectory): # Search for file
      if fileName in files:
        print("File found!")
        return os.path.join(root, fileName)
    print(f"File '{fileName} not found!") # File not found output
  except FileNotFoundError:
    print(f"\nError: '{fileName}' not found.")
  except PermissionError:
    pass
  except Exception as e:
    print(f"\nError: An unknown error occured: {e}")

```

Python has built in exceptions like the ones above: `FileNotFoundError`, `PermissionErrror` and `Exception`. The try except blocks prevent the user from seeing the traceback errors (typically meant for developers) and instead allows for customized messages that let the user know an error occurred.

The `pass` statement seen in the `PermissionError` exception will result in no message or traceback response. This is typically used as a placeholder until a desired task is implemented.

## Resources

- [PyDocs on Exceptions](https://docs.python.org/3/library/exceptions.html)
- [PyDocs on Errors](https://docs.python.org/3/tutorial/errors.html)
- [Geeks for Geeks](https://www.geeksforgeeks.org/python-exception-handling/)
- [W3 School](https://www.w3schools.com/python/python_try_except.asp)
