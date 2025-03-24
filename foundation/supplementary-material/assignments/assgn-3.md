# Input Data, If-else, and Loops

## Learning Objectives

- Learn how to prompt the user for input data
- Learn how to use if-else statements
- Learn how to use loops
- Learn how to use the user’s input data for useful calculations

## Overview - Part 1

Write a program that requests grades from the user, computes the average grade, then tells the user their
average and corresponding letter grade. You can assume the user will always enter grades between 0.00 to
100.00 and will enter an indefinite amount of grades. Use a loop that will accept the user’s grade and prompt
the user after each grade if they want to continue to enter grades. If the user enters a `‘y’` (for yes) continue
looping, if the user enters a `‘n’` stop looping. You are required to use loops and must use a different loop for
part 1 and part 2. If you use a while loop in part 2 you must use a for loop for part 1, and vice versa.

```
To display the user’s grade, use the following grading scale:

- A: average grade >= 90.00
- B: 90.00 > average grade >= 80.00
- C: 80.00 > average grade >= 70.00
- D: 70.00 > average grade >= 60.00
- F: 60.00 > average grade
```

## The Program - Part 1

This program will require accepting user input, totaling up those user inputs, averaging them, and using if,
else if, or else statements to display the grade properly. An example execution of the program is below:

```
Welcome to the grade estimator.
Please enter your grade for the assignment: 90.00
Would you like to enter another grade? (y/n): y

Please enter your grade for the assignment: 72.55
Would you like to enter another grade? (y/n): y

Please enter your grade for the assignment: 95.82
Would you like to enter another grade? (y/n): y

Please enter your grade for the assignment: 40.10
Would you like to enter another grade? (y/n): y

Please enter your grade for the assignment: 89.99
Would you like to enter another grade? (y/n): n

Your average grade is 77.69.
You will get a C in this class.
```

## Overview - Part 2

Write a program that lets the user enter their starting weight and how much weight they want to lose per
month, then creates and displays a table showing what their expected weight will be at the end of each
month for the next 6 months. Provide an encouraging statement at the end with the total weight that will be
lost. Ensure the output is formatted in such a way that is visually appealing and easy to understand. You can
use the sample execution as your formatting standard if you like. You are required to use loops and must use
a different loop for part 1 and part 2. If you used a while loop in part 1 you must use a for loop for part 2,
and vice versa.

## The Program - Part 2

This program will require accepting user input, using the user input to output a table, and properly
formatting the output. You may use `“‘\t”` or `“\n”` to ensure your formatting looks neat. An example execution
of the program is below:

```
Enter your starting weight (in lbs): 200.5

Enter how much weight you want to lose per month (in lbs): 2

| Month:| Target Weight:|
|-------|---------------|
|   1   |     198.5     |
|   2   |     196.5     |
|   3   |     194.5     |
|   4   |     192.5     |
|   5   |     190.5     |
|   6   |     188.5     |

You're going to lose 12.0 pounds over the next six months!
You got this!
```

## Task

### Part 1:

- Successfully looped and prompted user for each grade and continuation
- Successfully displayed average grade
- Successfully displayed the proper letter grade for the class

### Part 2:

- Successfully prompted the user form starting weight and weight loss
- Successfully looped and displayed table showing months and weight
- Successfully displayed total weight loss at end and encouraging message
