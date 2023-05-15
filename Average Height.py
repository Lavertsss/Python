student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
print(student_heights)
# 72 70 65 64 67 76
print(len(student_heights))
print(sum(student_heights))
average = sum(student_heights)/len(student_heights)
rounded_average = round(average, 0)
print(int(rounded_average))
