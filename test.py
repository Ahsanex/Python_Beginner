import numpy as np


#array = np.zeros(5)
#for i in range(5):
    #array[i] = int(input())
#array_arranged = np.sort(array)   
#print(f" {array_arranged}")
#array_linespace = np.linespace(array)


len_array = int(input("Enter The size of array You Want: "))
array = np.zeros(len_array)

print(f"ENTER {len_array} numbers")

for i in range(len_array):
    array[i] = int(input())

print(array)