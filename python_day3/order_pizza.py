pizza_size = input("What size do you want? (S/M/L)")
add_pepperoni = input("add pepperoni? (Y/N)")
extra_cheese = input("Extra cheese? (Y/N)")
bill = 0

if pizza_size == "S":
    bill += 15
elif pizza_size == "M":
    bill += 20
else: 
    bill += 25


if add_pepperoni == "Y":
    if pizza_size == "S":
        bill += 2
    else:
        bill += 3

if extra_cheese == "Y":
    bill += 1




print(f"Your total bill is ${bill}")