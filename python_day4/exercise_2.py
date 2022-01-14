import random

names_string = input("Give me everybody's names, separated by a comma. ")
names = list(names_string.split(", "))

#1
random_number = random.randint(0,len(names)-1)

print(f"{names[random_number]} is going to buy the meal today!")

#2

random_choice = random.choice(names)
print(f"{random_choice} is going to buy the meal today!")