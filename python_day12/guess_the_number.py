import random
from art import logo

def choose_difficulty():
    choose = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    if choose == 'easy':
        return 10
    elif choose == 'hard':
        return 5
    else:
        return

def game(count, correct_number):
    while count:
        print(f'You have {count} attempts remaining to guess the number')
        guess = int(input('Make a guess: '))

        if guess == correct_number:
            return print(f'You got it! The answer was {correct_number}')
        elif guess > correct_number:
            print("Too high")
        else:
            print("Too low")
        
        count -= 1
    return print("You've run out of guesses, you lose.")

print(logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100")

correct_number = random.randint(1,100)

print(f"psst, the correct answer is {correct_number}")


choose = choose_difficulty()
game(choose, correct_number)