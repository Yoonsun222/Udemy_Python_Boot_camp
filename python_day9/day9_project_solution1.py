from art import logo
import os

print(logo)

money = {}

state = True
max_price = 0
name_lst = []

while state:
    name = input("What is your name? ")
    price = int(input("What is yout bid? $"))

    money[name] = price
    
    
    if max_price < price:
        name_lst = []
        max_price = price
        name_lst.append(name)
    elif max_price == price:
        name_lst.append(name)

    
    game_continue = input("Are there any other bidders? Type 'yes or no ").lower()
    if game_continue == 'yes':
        os.system('cls')
    else:
        state = False


print(f"Winner is {', '.join(name_lst)} with a bids of ${max_price}")