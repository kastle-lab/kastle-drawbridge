

def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    return celsius

def main():
    while True:
        print("Menu:")
        print("1. Convert Celsius to Fahrenheit")
        print("2. Convert Fahrenheit to Celsius")
        print("q. Quit")
        
        choice = input("Please enter your choice (1/2/q): ")

        if choice == '1':
            celsius = float(input("Enter a temperature in Celsius: "))
            result = celsius_to_fahrenheit(celsius)
            print(f"{celsius} degrees Celsius is equal to {result} degrees Fahrenheit")
        elif choice == '2':
            fahrenheit = float(input("Enter a temperature in Fahrenheit: "))
            result = fahrenheit_to_celsius(fahrenheit)
            print(f"{fahrenheit} degrees Fahrenheit is equal to {result} degrees Celsius")
        elif choice == 'q':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

# Modulo Reminder :
x=5
y=2
m=x % 2
print(m)
