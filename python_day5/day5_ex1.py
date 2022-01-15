
student_heights = list(map(int,input("Input a list of student heights ").split()))
student_sum = 0
for n in student_heights:
    student_sum +=n

print(round(student_sum/len(student_heights)))