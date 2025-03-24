# Reading and Writing with Files

## Learning Objectives

- Learn how to read files in Python
- Learn how to write files in Python

## Overview

Your “main” function will ask the user to pick a mathematical operation to perform, and then prompt the
user for two numbers. Use a loop with input validation to check that the user has entered a valid input. Use if
and elif statements in your “main” to call the function for the corresponding character input. Your program
will have 6 functions, `“addNums”`, `“subtractNums”`, `“multNums”`, `“divNums”`, `“modNums”`, `“inputFile”`. These functions should print the result of the corresponding operation inside the function. All of these functions must return the correct mathematical result (excluding inputFile) but you can still print the result to the screen inside the function. The math functions from the previous assignment can remain unchanged other than including a return statement.

For the inputFile function you will pass a filename (string) as an input argument. The inputFile function needs
to open the “input” file, as well as an output file called “output.txt”. The input file will contain at least one set of mathematical operations and numbers, which are on individual lines. For example at a minimum the input
file may contain:

```
a
25
80
```

Read the file in a loop, processing each set of operators and numbers, and call your mathematical functions
with the information read from the file. Each time you perform a calculation using the loop, write the result
to the output file. Using the previous example, the “output.txt” file will contain:

```
105
```

You are not required to write any manual outputs to “output.txt”. For example, if the user selects option ‘m’
manually, and not using a file, you do not have to write the result of the multiplication to the file.

## The Program

This program will require accepting user input for which mathematical operation the user wants to perform
and the numbers to perform the operation on, and/or accepting an input file. If the user enters an invalid
mathematical operation selection, the program should ask the user to reenter a selection until it is valid. If
the user wants to input operations from a file, ask for a filename, calculate all the operations in the file, and
output each mathematical result to an output file. The program should loop until the user wants to quit. An
example execution of the program is below:

```
Welcome to my calculator! Here are the following choices:

a - addition
s - subtraction
m - multiplication
d - division
o - modulo
i - input from file
q - quit program

Enter the mathematical operation [a, s, m, d, o, i, q]: k
Invalid input!

Enter the mathematical operation [a, s, m, d, o, i, q]: a
Enter the first number in the operation: 4.5
Enter the second number in the operation: 9
4.5 + 9.0 = 13.5

Enter the mathematical operation [a, s, m, d, o, i, q]: m
Enter the first number in the operation: 10
Enter the second number in the operation: 5
10.0 * 5.0 = 50.0

Enter the mathematical operation [a, s, m, d, o, i, q]: i
Enter the name of the file: testnums.txt
1.0 + 2.0 = 3.0
5.0 * 10.0 = 50.0
50.0 - 25.0 = 25.0
0.5 * 2.0 = 1.0
10.0 / 5.0 = 2.0
5.0 % 2.0 = 1.0
0.2 + 0.5 = 0.8

Enter the mathematical operation [a, s, m, d, o, i, q]: q
```

### output.txt:

```
3.0
50.0
25.0
1.0
2.0
1.0
0.75
```

## Task

- Successfully read and executed all operations and operands from input file
- Successfully wrote all mathematical results to output file
- Successfully calculated each mathematical result with manual entry
- Successfully loop until user quit the program
