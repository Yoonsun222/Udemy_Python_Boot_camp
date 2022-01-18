import math

test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5

def paint_calc(height=test_h, width=test_w, cover=coverage):
    return math.ceil(height * width / cover) 

print(f"You'll need {paint_calc(test_h,test_w,coverage)} cans of paint")