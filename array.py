import numpy as np
print("enter 5 integerss")
array1= np.zeros(5, dtype=int)
for i in range(5):
 num = input(f" ENTER  THE {i} NUMBER")
 num = int(num)
 array1[i] = num

for i in range(5):
    if i == 0:
        print(f"1st Number of the Array is: {array1[i]}")
    elif i == 1:
        print(f"2nd Number of the Array is: {array1[i]}")
    elif i == 2:
        print(f"3rd Number of the Array is: {array1[i]}")
    else:
        print(f"{i+1}th Number of the Array is: {array1[i]}")


