import numpy as np

x = np.array([1, 2, 3, 4])
print(x.dtype)

y = np.array([1.3, 3.4, 4.5, 9.4])
print(y.dtype)

z = np.array(([1, 2, 4, 5, 'A', 'B', 'C']))
print(z.dtype)

# to convert int to float

arr = np.array([1, 2, 3, 4], dtype=float)
print(arr)
print(arr.dtype)

# to convert int to String
arr1 = np.array([1, 2, 3, 4], dtype='U')
print(arr1)
print(arr1.dtype)

# use of astype
x3 = np.array([1, 2, 3, 4])
new_x3 = x3.astype(float)
print(x3)
print(new_x3)
