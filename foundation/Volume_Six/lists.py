def writeList(myList):
    f = open("list.txt", 'w')

    for number in myList:
        f.write(str(number))
        f.write("\n")

    f.close()
    print("List was written to file successfully!")

def readList(myList):
    f = open("list.txt", 'r')

    line = f.readline()
    while line != '':
        myList.append(int(line))
        line = f.readline()

    f.close()
    print("List was read from file successfully!")
    print(myList)

def averageList(myList):

    if len(myList) == 0:
        print("Error: cannot calculate the average of empty list!")
        return
    
    total = 0

    for number in myList:
        total += number

    return total / len(myList)

def main():
    nums0 = []

    readList(nums0)
    
    nums1 = nums0.copy()

    for number in nums0:
        nums1.append(number)

    nums0[0] = 1000

    average = averageList(nums0)

    print("nums0 =",nums0)
    print("nums0 average value =", average)
    print("nums1 =",nums1)

    writeList(nums0)

if __name__ == "__main__":
    main()
