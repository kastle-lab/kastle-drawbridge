import math

def main():
    userInput = float(input("Enter a number to square root: "))

    result = math.sqrt(userInput)

    print("The square root of {0:.4f} is {1:.4f}.".format(userInput, result))

if __name__ == "__main__":
    main()
