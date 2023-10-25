
# This program allows the user to select items from a restaurant menu.

# Menu programs : A type of computer program where the user interacts with
# the program by choosing options from a menu displayed on the screen.
# These options represent different actions or functions that the program can perform.

# Function definitions : A reusable block of code that performs a specific task.
# Functions help in organizing code, making it easier to go through.

def display_menu():
    print("Welcome to Our Restaurant!")
    print("1. Burger")
    print("2. Pizza")
    print("3. Pasta")
    print("q. Exit")
   

def order_burger():
    print("You've ordered a burger.")

def order_pizza():
    print("You've ordered a pizza.")

def order_pasta():
    print("You've ordered pasta.")
def main():
    while True:
        display_menu()
        choice = input("Please enter your choice (1/2/3/q): ")

        if choice == '1':
            order_burger()
        elif choice == '2':
            order_pizza()
        elif choice == '3':
            order_pasta()
        elif choice == 'q':
            print("Thank you for dining with us!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()


# Reminder : modulo is the remainder when you divide two numbers.
# In python, modulo of two numbers can be displayed like this : m = num1 % num2

