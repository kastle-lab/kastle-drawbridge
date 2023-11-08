def printMembers(memberList):
    ## MAX - Function needed for printing tabular member data
    print("")
    print("-------------Current YMCA Membership Data--------------")
    print("|Name: \t\tAge: \tActive: \tBill:")
    print("-------------------------------------------------------")

    for member in memberList:
        print("|{0}, {1}\t|{2}\t|{3}\t\t|${4:,.2f}".format(member[1], member[0], member[2], member[3], member[4]))

    print("")

def sumBills(memberList):
    ## MAX - Function needed for calculating total bill, average bill, of all active members
    total = 0
    average = 0
    activeCount = 0

    for member in memberList:
        if member[3]:
            total += member[4]
            activeCount += 1

    try:
        average = total / activeCount
    except ZeroDivisionError:
        print("There are no active members")

    return total, average, activeCount
    

def main():
    print("Welcome to the YMCA Database")

    ## MAX - Must use 2D list
    members = []
    userInput = ""
    userCount = 0
    
    while userInput != 'n':
        firstName = input("First Name: ")
        lastName = input("Last Name: ")

        ## MAX - Must do exception handling for any possible exceptions
        
        try:
            age = int(input("Age: "))
        except ValueError:
            print("Age was invalid")
            continue

        ## MAX - Converting string to bool is not straightforward
        isActive = input("User's Account is Active: ")
        
        if isActive == "False":
           isActive = False
        elif isActive != "True":
            print("Active was invalid")
            continue;

        try:
            bill = float(input("Monthly Bill: $"))
        except ValueError:
            print("Bill was invalid")
            continue

        ## MAX - Every member has first name, lastname, age, active, and monthly bill
        members.append([firstName, lastName, age, isActive, bill])

        userInput = input("Would you like to enter another YMCA member? (y/n) ")

    total, average, activeCount = sumBills(members)
    printMembers(members)

    ## MAX - Printing this information outside of the "printMembers" function is acceptable
    print("Revenue from Active Members: ${0:,.2f}".format(total))
    print("Average Revenue from Active Members: ${0:,.2f}".format(average))
    print("Total of Members: {0}".format(len(members)))
    print("Total of Active Members: {0}".format(activeCount))
    
if __name__ == "__main__":
    main()
