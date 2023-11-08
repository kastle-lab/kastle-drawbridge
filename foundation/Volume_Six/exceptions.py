
def main():
    isValid = False

    while not isValid:
        try:
            myNum = int(input("Enter a number: "))
            isValid = True
        except TypeError as error:
            print("That was not a number!")
            #print("Official Error Message: \n", error)
            isValid = False
        else:
            print("Thank you for entering a valid input!!!")
        finally:
            print("Thanks for your attempt!")

    #num = 5 / 0

    try: 
        reciprocal = 1 / myNum
    except ZeroDivisionError:
        print("You tried to divide by 0!!!")
        return

    print(reciprocal)

if __name__ == "__main__":
    main()
