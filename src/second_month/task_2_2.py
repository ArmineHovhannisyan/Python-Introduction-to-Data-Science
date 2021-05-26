# task 2.2
import numpy as np

# 1. Write a NumPy program to compute the multiplication of two given matrices

m1 = np.random.rand(3, 3)
m2 = np.random.rand(3, 3)
print(m1)
print(m2)

result = np.dot(m1, m2)
print(result)


# 2.Write a NumPy program to compute the determinant of an array

arr = np.array([[[1, 2], [3, 4]], [[1, 2], [2, 1]], [[1, 3], [3, 1]]])
print(arr)

det = np.linalg.det(arr)
print('det: ' + str(det))


# 3. Write a NumPy program to compute the sum of the diagonal element of a given array

m = np.random.rand(4, 4)
print(m)

diagonal_elements = np.diagonal(m)
diagonal_sum = np.sum(diagonal_elements)
print('sum of diagonal elements' + str(diagonal_sum))


# 4. Write a NumPy program to compute the inverse of a given matrix

m = np.random.rand(4, 4)
print(m)

inverse = np.linalg.inv(m)
print('inverse: '+ str(inverse))
