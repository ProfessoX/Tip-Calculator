print("Welcome to the tip calculator.")
#What was the total bill? 
bill_total = float(input("What was the total bill?\n$"))
#What percentage tip would you like to give? 10, 12, or 15? 
tip = input("What percentage tip would you like to give? 10, 12, or 15?\n")
tip_pct = int(tip) / 100
tip_bill = (bill_total * tip_pct)
#How many people to split the bill/? 
split = int(input("How many people to split the bill/?\n"))
person =round((bill_total + tip_bill) / split, 2)
#Each person should pay:
print(f"Each person should pay: ${person}")