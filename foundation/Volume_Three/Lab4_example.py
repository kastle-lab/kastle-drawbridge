#Note : If you dont wish to run all of the programs at the same time, run them in separate code files or use ' """ '  at the start and end of each functiuon you do not with to run.
# Prompt the user for their age
age = int(input("Please enter your age: "))
print(f"You entered: {age} years old.")

#Prompt the user for the length of a table
length=float(input("Please enter the length of the table:"))
print(f"The length is : {length}.")

# Check if a number is even or odd
number = int(input("Enter a number: "))

if number == 0:
    print("The number is zero.")
else:
    print(f"The number is {number}.")

    
# Print numbers from 1 to 5 using a for loop
for num in range(1, 6):
    print(num)
    num+=1
    

#For loop example from lecture
list = [1, 2, 3, 4, 5]
for num in list:
    print(num, "", end='')
    print("")

#While loop example from class
username = input("Username:")
password = input("Password:")
secretPassword = "ABCD1234"
while password != secretPassword:
    password = input("Incorrect password! Please enter again:")
    print("Success! You are logged in.")

# Calculate the area of a rectangle
length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))

area = length * width
print(f"The area of the rectangle is {area:.2f} square units.")

#Another example from the lecture
grade = float(input("Input your grade (enter -1 to stop): "))
total = 0
count = 0
average = 0
while(grade != -1):
    total += grade
    count += 1
    average = total/count
    grade = float(input("Input your grade (enter -1 to stop): "))
    print("You had {0} assignments for an average of {1} grade.".format(count, average))
