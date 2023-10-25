def isXWithinRange(x):
    return (x>10 and x<20) and not(x == 15)

def multiplyBy2And10(y):
    return y * 2, y * 10

def main():
    userInput = int(input("Enter a number greater than 10, less than 20, and not equal to 15: "))

    while(not isXWithinRange(userInput)):
        print("Oops! You did not meet the condition!")
        userInput = int(input("Enter a number greater than 10, less than 20, and not equal to 15: "))

    a, b = multiplyBy2And10(userInput)
    
    print("Thank you! {0}x2={1} and {0}x10={2}".format(userInput,a,b))

if __name__ == "__main__":
    main()
