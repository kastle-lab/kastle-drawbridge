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
