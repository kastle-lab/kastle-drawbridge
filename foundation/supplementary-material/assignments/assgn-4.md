# Functions and Menus

## Learning Objectives

- Learn how to write menu-driven programs
- Learn how to write functions

## Overview

Your “main” function will ask the user to pick a mathematical operation to perform, and then prompt the
user for two numbers. Use a loop with input validation to check that the user has entered a valid input. Use if
and elif statements in your “main” to call the function for the corresponding character input. Your program
will have 5 functions, `“addNums”`, `“subtractNums”`, `“multNums”`, `“divNums”`, `“modNums”`. These functions
should print the result of the corresponding operation inside the function (your functions should not return a
value).

## The Program

This program will require accepting user input for which mathematical operation the user wants to perform
and the numbers to perform the operation on. If the user enters an invalid mathematical operation selection,
the program should ask the user to reenter a selection until it is valid. The program should loop until the user
wants to quit. An example execution of the program is below:

```
Welcome to my calculator! Here are the following choices:

a - addition
s - subtraction
m - multiplication
d - division
o - modulo
q - quit program

Enter the mathematical operation [a, s, m, d, o, q]: k
Invalid input!

Enter the mathematical operation [a, s, m, d, o, q]: a
Enter the first number in the operation: 4.5
Enter the second number in the operation: 9
4.5 + 9.0 = 13.5

Enter the mathematical operation [a, s, m, d, o, q]: m
Enter the first number in the operation: 10
Enter the second number in the operation: 5
10.0 x 5.0 = 50.0

Enter the mathematical operation [a, s, m, d, o, q]: q
```

## Task

- Successfully displayed list of operations
- Successfully validated the operation selection
- Successfully calculated each mathematical result
- Successfully loop until user quit the program
