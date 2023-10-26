def add_nums(x, y):
    z = x + y
    print("{0:.1f} + {1:.1f} = {2:.1f}".format(x, y, z))
    return z

def subtract_nums(x, y):
    z = x - y
    print("{0:.1f} - {1:.1f} = {2:.1f}".format(x, y, z))
    return z

def mult_nums(x, y):
    z = x * y
    print("{0:.1f} * {1:.1f} = {2:.1f}".format(x, y, z))
    return z

def div_nums(x, y):
    z = x / y
    print("{0:.1f} / {1:.1f} = {2:.1f}".format(x, y, z))
    return z

def mod_nums(x, y):
    z = x % y
    print("{0:.1f} % {1:.1f} = {2:.1f}".format(x, y, z))
    return z

def input_file(f):
    output = open("output.txt", 'w')
    file = open(f, 'r')

    op = file.readline().rstrip("\n")

    while op != '':
        x = float(file.readline().rstrip("\n"))
        y = float(file.readline().rstrip("\n"))
        z = 0

        #print(op, x, y)

        if op == 'a':
            z = add_nums(x, y)
        elif op == 's':
            z = subtract_nums(x, y)
        elif op == 'm':
            z = mult_nums(x, y)
        elif op == 'd':
            z = div_nums(x, y)
        elif op == 'o':
            z = mod_nums(x, y)

        op = file.readline().rstrip("\n")

        output.write(str(z))
        output.write("\n")
        
        
    file.close()
    output.close()

def main():
    print("Welcome to my calculator! Here are the following choices:")
    print("a - addition")
    print("s - subtraction")
    print("m - multiplication")
    print("d - division")
    print("o - modulo")
    print("i - input from file")
    print("q - quit program")

    userInput = ''

    while userInput != 'q':
        userInput = input("Enter the mathematical operation [a, s, m, d, o, i, q]: ")

        if userInput == 'a':
            x = float(input("Enter the first number in the operation: "))
            y = float(input("Enter the second number in the operation: "))
            add_nums(x, y)
        elif userInput == 's':
            x = float(input("Enter the first number in the operation: "))
            y = float(input("Enter the second number in the operation: "))
            subtract_nums(x, y)
        elif userInput == 'm':
            x = float(input("Enter the first number in the operation: "))
            y = float(input("Enter the second number in the operation: "))
            mult_nums(x, y)
        elif userInput == 'd':
            x = float(input("Enter the first number in the operation: "))
            y = float(input("Enter the second number in the operation: "))
            div_nums(x, y)
        elif userInput == 'o':
            x = float(input("Enter the first number in the operation: "))
            y = float(input("Enter the second number in the operation: "))
            mod_nums(x, y)
        elif userInput == 'i':
            filename = input("Enter the name of the file: ")
            input_file(filename)
        elif userInput == 'q':
            print("")
        else:
            print("Invalid input!")

if __name__ == "__main__":
    main()
