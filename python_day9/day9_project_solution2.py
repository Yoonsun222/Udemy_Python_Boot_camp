from art import logo
import os

print(logo)

money = {}

state = True

def find_max_value(dic):
    max_price = 0
    winner = ''
    for name in dic:
        price = dic[name]
        if price > max_price:
            max_price = price
            winner = name
    print(f"Winner is {winner} with a bids of ${max_price}")

while state:
    name = input("What is your name? ")
    price = int(input("What is yout bid? $"))

    money[name] = price
    
    
    
    
    game_continue = input("Are there any other bidders? Type 'yes or no ").lower()
    if game_continue == 'yes':
        os.system('cls')
    else:
        state = False


find_max_value(money)