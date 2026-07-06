import numpy as np

pass_marks = int(input("ENTER THE PASSING MARKS: "))
number_of_students = int(input("ENTER THE NUMBER OF NUMBER OF STUDENTS THERE ARE: "))
array = np.zeros(number_of_students)
print("ENTER MARKS OF EVERY NUMBER:")
for i in range(number_of_students):
   array[i] = input()

for i in range(number_of_students):
    if(array[i] >= pass_marks):
       print(f"Student Number {(i+1)} is passed ")
    else:
        print(f"Student Number {(i+1)} is failed ")

