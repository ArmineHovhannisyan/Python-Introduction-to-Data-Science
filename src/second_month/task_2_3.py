# task 2.3
import numpy as np
from numpy import newaxis

# 1. Find min and max in NumPy array

m = np.random.rand(5, 4)
print(m)

_min = np.min(m)
_max = np.max(m)
print('minimum value: ' + str(_min))
print('maximum value: ' + str(_max))

# Create a numpy array
arr = np.array([[0, 1],
                [2, 3]])

# 2. Find min and max in NumPy array by second axis

_max2 = np.amax(m, 1)
_min2 = np.amin(m, 1)


print('minimum value: ' + str(_min2))
print('maximum value: ' + str(_max2))


# 3. Find Median

_median= np.median(m)

print('median: ' + str(_median))


# 4. multiple 1d and 2d np arrays

arr1 = np.array([1,  5, 8, -8])
arr2 = np.array([[8, 3], [98, -9]])


arr1 = arr[:, newaxis]
mul = arr1 * arr2
print(mul)




