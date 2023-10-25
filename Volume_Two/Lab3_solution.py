"""
#Inputs for assignment grades :
print("Welcome to the grade simulator.")
A1=float(input("Please enter your grade for assignment 1 :"))
A2=float(input("Please enter your grade for assignment 2 :"))
A3=float(input("Please enter your grade for assignment 3 :"))
A4=float(input("Please enter your grade for assignment 4 :"))
A5=float(input("Please enter your grade for assignment 5 :"))

Average_Grade= (A1+A2+A3+A4+A5)/5
Average_Grade=int(100 * Average_Grade + 0.5) / 100
print("Your average grade is :",Average_Grade)

if Average_Grade >= 90.00 :
    print("You will get an A in this class.")
if Average_Grade < 90.00 and Average_Grade >= 80.00 :
    print("You will get a B in this class.")
if Average_Grade < 80.00 and Average_Grade >= 70.00:
    print("You will get a C in this class.")
if Average_Grade < 70.00 and Average_Grade >= 60.00 :
    print("You will get a D in this class.")
if Average_Grade <60.00 :
    print("You will get a F in this class.")
 
    
"""

# Initialize variables to store grades and their sum
grade1 = float(input("Please enter your grade for assignment 1: "))
grade2 = float(input("Please enter your grade for assignment 2: "))
grade3 = float(input("Please enter your grade for assignment 3: "))
grade4 = float(input("Please enter your grade for assignment 4: "))
grade5 = float(input("Please enter your grade for assignment 5: "))

# Calculate the average grade
average_grade = (grade1 + grade2 + grade3 + grade4 + grade5) / 5

# Determine the letter grade based on the average grade
if average_grade >= 90.00:
    letter_grade = "A"
elif average_grade >= 80.00:
    letter_grade = "B"
elif average_grade >= 70.00:
    letter_grade = "C"
elif average_grade >= 60.00:
    letter_grade = "D"
else:
    letter_grade = "F"

# Display the results
print(f"Your average grade is {average_grade:.2f}.")
print(f"You will get a {letter_grade} in this class.")
