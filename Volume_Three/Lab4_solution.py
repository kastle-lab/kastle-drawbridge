#Part1

# Initialize variables to store grades and their sum
# Initialize variables to store grades and their sum
total_grade = 0.0
num_grades = 0

# Welcome message
print("Welcome to the grade estimator.")

# Use a while loop with 'y/n' input
user_input = 'y'  # Initialize with 'y' to enter the loop

while user_input == 'y':
    # Input grade
    grade = float(input("Please enter your grade for the assignment: "))
    total_grade += grade
    num_grades += 1

    # Ask the user if they want to continue
    user_input = input("Would you like to enter another grade? (y/n): ")

# Calculate the average grade
if num_grades > 0:
    average_grade = total_grade / num_grades
else:
    average_grade = 0.0

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




#Part2
# Part 1 - Accept user input using a while loop
"""
# Initialize variables
starting_weight = float(input("Enter your starting weight (in lbs): "))
weight_loss_per_month = float(input("Enter how much weight you want to lose per month (in lbs): "))

target_weights = []
month = 1

print("Month: | Target Weight:", end=" ")
while month <= 6:
    target_weight = starting_weight - month * weight_loss_per_month
    target_weights.append(target_weight)
    print(f"{month} |", end=" ")
    month += 1

print("\n" + " " * 7, end=" ")
for weight in target_weights:
    print(f"{weight:.1f}", end=" ")


total_weight_loss = weight_loss_per_month * 6

# Display an encouraging statement with the total weight loss
print(f"\nYou're going to lose {total_weight_loss:.1f} pounds over the next six months! You got this!")
"""

"""
# Get user input for starting weight and weight to lose per month
starting_weight = float(input("Enter your starting weight (in lbs): "))
weight_to_lose_per_month = float(input("Enter how much weight you want to lose per month (in lbs): "))

total_weight_lost = 0

# Print the table header
print("Month: | Target Weight:")
print("-" * 30)

# Use a for loop to calculate and display the target weight for each month
for month in range(1, 7):
    target_weight = starting_weight - month * weight_to_lose_per_month
    total_weight_lost += weight_to_lose_per_month
    # Format the output to align columns and display one decimal place
    print(f"{month:<6} | {target_weight:.1f}")

# Print the total weight lost
print(f"\nYou're going to lose {total_weight_lost:.1f} pounds over the next 6 months.")
"""
