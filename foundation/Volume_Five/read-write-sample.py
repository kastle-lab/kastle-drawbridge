def main():
    fileName = input("Enter a name for the new file: ")
    name = input("What is your name: ")
    gpa = float(input("What is your GPA: "))
    creds = int(input("How many credit hours have you taken: "))
   
    myFile = open(fileName, 'w')

    myFile.write(name)
    myFile.write("\n")
    
    myFile.write(str(gpa))
    myFile.write("\n")    
    myFile.write(str(creds))
    myFile.write("\n")
    
    myFile.close()

    myFile = open(fileName, 'r')

    name = myFile.readline().rstrip("\n")
    gpa = float(myFile.readline().rstrip("\n"))
    creds = int(myFile.readline().rstrip("\n"))

    myFile.close()

    print("This person's name: {0}".format(name))
    print("This person's gpa: {0}".format(gpa))
    print("This person's credit hours: {0}".format(creds))
    print("This person's credit hours minus 100: {0}".format(creds-100))
    

if __name__ == "__main__":
    main()
