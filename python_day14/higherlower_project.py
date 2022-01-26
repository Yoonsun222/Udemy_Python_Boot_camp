from random import randint
from unicodedata import name
import art
from game_data import data
import random

def choice(a_follower_count,b_follower_count):
        choice = input("Who has more follwers? Type 'A' or 'B':" ).lower()
        if choice == a:
            choice_person = a_follower_count
            not_choice = b_follower_count
        elif choice == b: 
            choice_person = b_follower_count
            not_choice = b_follower_count

def compare():
    if choice_person > not_choice:
        




    

def game():

    visited = []
    state = True

                
    a_number = random.randint(0,len(data))
    visited.append(a_number)
    a_lst = list(data[a_number].values())
    
    while state:

        b_number = random.randint(0,len(data))
        b_lst = list(data[b_number])

        print(f'Compare A: {a_lst[0]}, {a_lst[2]}, from {a_lst[3]}')
        print(art.vs)
        print(f'Compare A: {b_lst[0]}, {b_lst[2]}, from {b_lst[3]}')

        choice(a_lst[1], b_lst[1])



game()