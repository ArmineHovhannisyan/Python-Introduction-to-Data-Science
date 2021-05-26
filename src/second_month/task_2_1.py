# task 2.1
import numpy as np

# 1.Write a NumPy program to convert a list of numeric values into a one-dimensional NumPy array.

l = [6.3, -3.45, 10542, 39.3]
arr = np.array(l)
print(arr)

# 2.Write a NumPy program to create a NumPy array with values ranging from 2 to 10.

arr = np.arange(2, 11)
print(arr)

# 3.Write a NumPy program to create a null vector of size 10 and update sixth to eight values to 11.

arr = np.zeros(10)
for i in range(6, 9):
    arr[i] = 11
print(arr)


# 4.Write a NumPy program to test whether each element of a 1-D array is also present in a second array.

arr1 = np.array([0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55])

arr2 = [2, 3, 5, 7, 11, 17, 19, 23, 29, 31, 37]

print(np.in1d(arr1, arr2))

