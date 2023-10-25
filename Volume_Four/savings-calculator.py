savings = float(input("What is the current balance in your savings account: "))
change = float(input("How much will you save per week: "))
weeks = int(input("How many weeks will you save for: "))
totalSaved = 0.0;

print("\nWeek:\tSavings Account:")
print("-----------------------")

for week in range(1, weeks+1):
    savings += change
    totalSaved += change
    print("{0}\t| ${1:,.2f}".format(week, savings))
    #print("")

print("\nCongrats! Total saved is ${0:,.2f}".format(totalSaved))
