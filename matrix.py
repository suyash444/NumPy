import numpy as np

arr1 = np.matrix([[1, 2], [3, 4]])
arr2 = np.matrix([[1, 2], [3, 4]])
result = arr1 * arr2
print(result)

print(type(result))

# output
# [[ 7 10]
#  [15 22]]
# <class 'numpy.matrix'>

# transpose of a matrix

x1 = np.matrix([[1, 2, 3, 4], [3, 4, 5, 6]])
ans = np.transpose(x1)
print(ans)

# output
# [[1 3]
#  [2 4]
#  [3 5]
#  [4 6]]
