def printTable(savings, change, weeks):
    totalSaved = 0.0
    print("\nWeek:\tSavings Account:")
    print("-----------------------")

    for week in range(1, weeks+1):
        savings += change
        totalSaved += change
        print("{0}\t| ${1:,.2f}".format(week, savings))

    print("\nCongrats! Total saved is ${0:,.2f}".format(totalSaved))
