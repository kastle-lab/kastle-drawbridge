def main():
    x = 12
    accounts = [["Max", 1000, "a", "car"],
                ["Ziggy", 5, "z", "bike"],
                ["Jack", x, "i", "subway"]]

    nums = [1, 2, 3, 0, -5, 20, -100]

    for i in range(0, len(nums)):
        print("nums[{0}] = {1}".format(i, nums[i]))

    for i in range(0, len(accounts)):
        for j in range(0, len(accounts[0])):
            print(accounts[i][j])

    for entry in accounts:
        print("Name:", entry[0], "\tMileage:", entry[1], "\tAccount Type:", entry[2], "\tTransportation:", entry[3])

    print("Name:", accounts[1][0], "\tMileage:", accounts[1][1], "\tAccount Type:", accounts[1][2], "\tTransportation:", accounts[1][3])

if __name__ == "__main__":
    main()
