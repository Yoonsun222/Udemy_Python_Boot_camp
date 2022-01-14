
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))

BMI = int(weight/(height)**2)


if BMI >= 35:
    print("clinically obese")
elif BMI >= 30:
    print("obese")
elif BMI >= 25:
    print("overweigiht")
elif BMI >= 18.5:
    print("normal weight")
else:
    print("underweight")