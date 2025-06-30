print("Welcome to the tip calculator!")
total_bill = float(input("What was the total bill? $"))
tip = int(input("How much tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill? "))
bill_with_tip = total_bill + (tip/100)*total_bill
individual_bill = bill_with_tip / people
print(f"Each person should pay: ${individual_bill:.2f}")