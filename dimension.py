import numpy as np

x = np.array([[[1, 2, 3, 4], [3, 4, 5, 6], [9, 1, 2, 3]]])
print(x)
print(x.ndim)

# to create multidimensional array use the function ndmin  and pass the value
arr = np.array([1, 2, 3, 4], ndmin=8)
print(arr)
print(arr.ndim)
