def readFile():
    fileName = input("What is the name of the file: ")

    myFile = open(fileName, 'r')

    line = myFile.readline().rstrip('\n')

    while line != '':
        print(line)
        line = myFile.readline().rstrip('\n')
    
    myFile.close()

def main():
    fileName = input("What is the name of the file: ")
    myFile = open(fileName, 'a')

    name = input("Enter a name or type QUIT to stop: ")

    while name != "QUIT":
        myFile.write(name)
        myFile.write("\n")
        name = input("Enter a name or type QUIT to stop: ")

    myFile.close()

    readFile()
    
if __name__ == "__main__":
    main()
