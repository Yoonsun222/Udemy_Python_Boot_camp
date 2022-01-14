import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''


game_list = [rock, paper, scissors]
answer = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))


if answer >= 3 or answer < 0:
    print("You typed an invalid number, you lose")
else:
    print(f"You choice: \n{game_list[answer]}")
    computer = random.randint(0,len(game_list)-1)
    print(f"computer choice: \n{game_list[computer]}")
    if computer == 0 and answer == 2:
        print("You Lose")
    elif computer == 2 and answer == 0:
        print("You Win")
    elif computer < answer:
        print("You win")
    elif computer > answer:
        print("You Lose")    
    elif computer == answer:
        print("Draw")
