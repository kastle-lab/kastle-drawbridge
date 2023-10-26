# Function to add two numbers
def addNums(num1, num2):
    result = num1 + num2
    print(f"{num1} + {num2} = {result}")

# Function to subtract two numbers
def subtractNums(num1, num2):
    result = num1 - num2
    print(f"{num1} - {num2} = {result}")

# Function to multiply two numbers
def multNums(num1, num2):
    result = num1 * num2
    print(f"{num1} x {num2} = {result}")
"""
# Function to divide two numbers
def divNums(num1, num2):
    if num2 == 0:
        print("Error: Division by zero!")
    else:
        result = num1 / num2
        print(f"{num1} / {num2} = {result}")
"""
def divNums(num1,num2):
    if num2==0:
        print("Error, Divizion by zero!")
    num1=num2
    while rem >= num2:
        rem-=num2
    return rem

# Function to calculate the remainder of two numbers
def modNums(num1, num2):
    if num2 == 0:
        print("Error: Division by zero!")
    else:
        result = num1 % num2
        print(f"{num1} % {num2} = {result}")


# Main function
def main():
    print("Welcome to my calculator! Here are the following choices:")
    print("a - addition")
    print("s - subtraction")
    print("m - multiplication")
    print("d - division")
    print("o - modulo")
    print("q - quit program")

    while True:
        operation = input("Enter the mathematical operation [a, s, m, d, o, q]: ").lower()

        if operation == 'q':
            break
        elif operation not in ['a', 's', 'm', 'd', 'o']:
            print("Invalid input!")
        else:
            try:
                num1 = float(input("Enter the first number in the operation: "))
                num2 = float(input("Enter the second number in the operation: "))

                if operation == 'a':
                    addNums(num1, num2)
                elif operation == 's':
                    subtractNums(num1, num2)
                elif operation == 'm':
                    multNums(num1, num2)
                elif operation == 'd':
                    divNums(num1, num2)
                elif operation == 'o':
                    modNums(num1, num2)
            except ValueError:
                print("Invalid input! Please enter valid numbers.")

if __name__ == "__main__":
    main()
