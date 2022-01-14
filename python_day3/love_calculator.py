print("welecome to the love calculator!")
name1 = input("What is your name?").lower()
name2 = input("what is their name?").lower()

name = name1 + name2
true = "true"
love = "love"
true_count = 0
love_count = 0
for i in true:
    true_count += name.count(i)


for i in love:
    love_count += name.count(i)



score = int(str(true_count) + str(love_count))

if score >= 90 or score <= 10:
    print(f"Your score is {score}, you go thgether like coke and mentos.")
elif score >= 40 and score <= 60:
    print(f"Your score is {score}, ou are alright together")
else:    
    print(f"Your score is {score}")