print("Welecome to the tip caclultor.")
total_bill = float(input("What was the total bill? $"))

percent = float(input("Wath percentage tip would you like to give?"))/100

print(percent)
bill = total_bill * (1 + percent)

person = int(input("How many people to split the bill?"))
Each_Bill = bill / person


print("Each person should pay: $" ,round(Each_Bill,2))