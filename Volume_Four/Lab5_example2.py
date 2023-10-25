# This program demonstrates a menu-program that does some calculations on a non-negative numbers.
def display_menu():
    print("Menu:")
    print("1. Calculate the square of a number")
    print("2. Calculate the cube of a number")
    print("3. Calculate the square root of a number")
    print("q. Quit")

def calculate_square(num):
    return num ** 2

def calculate_cube(num):
    return num ** 3

def calculate_square_root(num):
    if num < 0:
        return "Invalid input. Please enter a non-negative number."
    return num ** 0.5
def main():
    while True:
        display_menu()
        choice = input("Please enter your choice (1/2/3/q): ")

        if choice == '1':
            number = float(input("Enter a number: "))
            result = calculate_square(number)
            print(f"The square of {number} is {result}")
        elif choice == '2':
            number = float(input("Enter a number: "))
            result = calculate_cube(number)
            print(f"The cube of {number} is {result}")
        elif choice == '3':
            number = float(input("Enter a number: "))
            result = calculate_square_root(number)
            print(f"The square root of {number} is {result}")
        elif choice == 'q':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
if __name__ == "__main__":
    main()
