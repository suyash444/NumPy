# to use shape function it tell which matrix is it like now its (2*2) matrix

import numpy as np

arr = np.array([[1, 2], [3, 4]])
print(np.shape(arr))

arr1 = np.array(([[1, 2, 3, 4], [3, 4, 3, 1]]))
print(np.shape(arr1))
# so it is a (2*4) matrix
# it means 2 rows and 4 columns

# Reshape()
x = np.array([1, 2, 3, 4])
print(x.reshape(2, 2))
# output:
# [[1 2]
#  [3 4]]

# it means reshape the matrix in 2 rows and 6 columns
y = np.array(([[1, 2, 3, 4, 5, 6], [4, 3, 5, 4, 3, 5]]))
print(y.reshape(2, 6))

# output
# [[1 2 3 4 5 6]
#  [4 3 5 4 3 5]]
