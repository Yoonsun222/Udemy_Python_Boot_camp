from art import logo
import random 
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
give_card = [0 for _ in range(13)] 
user_card = []
computer_card = []
card_lst = [user_card, computer_card]

def blackjack():
    for card in card_lst:
        count = 0
        for _ in range(14):
            idx = random.randrange(0,10)
            if give_card[idx] != 4:
                card.append(cards[idx])
                give_card[idx] += 1
                count += 1
            elif give_card[idx] == 4:
                continue
            if count == cnt:
                break
    
    print(f'Your cards: {user_card}, current score: {sum(user_card)}')
    print(f'computer first card: {computer_card[0]}')

    input



    return

state = True

while state:

    
    yes_or_no = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()

    if yes_or_no == 'y':
        state = True
    else:
        state = False
        break


    print(logo)
    blackjack()
        
