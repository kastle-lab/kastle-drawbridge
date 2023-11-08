data_list = []  # Initialize an empty list to store the data

while True:
    # Get user input for name, age
    name = input("Enter the name: ")
    grade = int(input("Enter the age: "))
    

    # Create a new data set (e.g., a tuple) with the entered information
    data = (name, grade)

    # Add the data set to the list
    data_list.append(data)

    another_entry = input("Do you want to add another entry? (yes/no): ")
    if another_entry.lower() != "yes":
        break  # Exit the loop if the user doesn't want to add more data

# Print the collected data
for data in data_list:
    name, grade = data
    print(f"Name: {name}, Grade: {grade}")
