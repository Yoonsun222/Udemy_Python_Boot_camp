age = int(input("What is your current age? :"))

left_age= 90-age

days = 365*left_age

week = 52*left_age

month = 12*left_age
message= f"You have {days} days, {week} weeks, {month} month left."
print(message)
