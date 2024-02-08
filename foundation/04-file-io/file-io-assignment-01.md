# File Input/Output

## Reading a file (input)
1. Method 1
```py
fileName = "someName"
inpF = open(fileName, 'r')

# do something
```

2. Method 2
```py
with(open([filename], 'r')) as inpF:
    # do something
    pass
```

## Writing to a file (output)
1. Method 1
```py
fileName = "someName"
inpF = open(fileName, 'w')

# do something
```

2. Method 2
```py
with(open([filename], 'w')) as outF:
    # do something
    pass
```

# Assignment
Read and implement [the attached assignment](https://github.com/kastle-lab/kastle-drawbridge/blob/master/foundation/supplementary-material/assignments/cs1160-lab06.pdf) such that your output and calculations match the assignment reading's. After the Python scripts run, an `output.txt` file should be generated.

## Extension to Assignment
Originally, the assignment's `output.txt` contains the evaluated solution of two values with a mathematical operator from an input file, `testnums.txt`.  Can you figure out how to include the mathematical function to each respective solution when running the calculator without an input file?
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
