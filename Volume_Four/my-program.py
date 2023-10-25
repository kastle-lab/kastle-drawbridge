import table

def main():
    savings = float(input("Savings balance: "))
    amt = float(input("Saved per week: "))
    weekCount = int(input("Number of weeks: "))
    
    table.printTable(savings, amt, weekCount)

if __name__ == "__main__":
    main()
