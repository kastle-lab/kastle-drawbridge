# For loop example :

Savings=float(input("Please enter the number of your savings : "))
Money_to_Save_per_Month=float(input("How much money you want to save per month ? :"))


total_money_Saved=0
print("Month:| Savings_Target:")
print("-"*30)
months=12
for month in range(months):
    Savings_Target=Savings+month*Money_to_Save_per_Month
    total_money_Saved+=Money_to_Save_per_Month
    print(f"{month:<12} | {Savings_Target:.1f}")
print(f"You will save {total_money_Saved:.1f} over the next 12 months.")
    

# While loop example :

print("Welcome to word search!")

while True:
    sentence = str(input("Enter one sentence of your choice: "))
    
    # Check if "and" is in the sentence
    if "and" in sentence:
        print("The word 'and' was found in the sentence.")
        break
    else:
        print("The word 'and' was not found in the sentence.")
    
   

