def choiceA():
    print("You selected choice A!")

def choiceB():
    print("You selected choice B!")

def choiceC():
    print("You selected choice C!")

def choiceD():
    print("You selected choice D!")

def main():
    userInput = ''
    while userInput != 'q':
        userInput = input("What do you want to do in this program (A, B, C, D)? (q for quit)")

        while userInput != 'A' and userInput != 'B' and userInput != 'C' and userInput != 'D' and userInput != 'q':
            userInput = input("What do you want to do in this program (A, B, C, D)? (q for quit)")

        if userInput == 'A':
            choiceA()
        elif userInput == 'B':
            choiceB()
        elif userInput == 'C':
            choiceC()
        elif userInput == 'D':
            choiceD()
        elif userInput == 'q':
            return
        

if __name__ == "__main__":
    main()
