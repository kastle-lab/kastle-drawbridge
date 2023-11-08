# Make a list :
numbers = [1, 2, 3, 4, 5]
print(numbers)
for n in numbers:
    print(n)

# Add a new element to a list :
numbers2=[1,2,3]
print(numbers2)
numbers2.append(4)
print(numbers2)

# Extracting specific element from the list depending on the position. First element is 0 . :
first_number=numbers2[0]
third_number=numbers2[2]
print(first_number)
print(third_number)

# Handle value errors :
try:
    user_input = int(input("Enter a number: "))
    print("You entered:", user_input) 
except ValueError:
    print("Invalid input. Please enter a valid number.")

# Handle index error, i.e. when you want to access a list element but you enter the wrong position for it :

numbers = [1, 2, 3]
try:
    element = int(input("Enter the position of the element you want to access :"))
    print(numbers[element])
except IndexError:
    print("Index out of range.")

# Handle a zero division error :
try:
    number=int(input("Enter the number the result should be divided by : "))
    result = 1 / number
except ZeroDivisionError:
    print("Division by zero is not allowed.")

