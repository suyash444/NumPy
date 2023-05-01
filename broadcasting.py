import numpy as np

a1 = np.array([[1], [2]])  # -- (2, 1) matrix
a2 = np.array([[1, 2, 3], [3, 4, 5]])  # -- (2, 3) matrix
result = a1 + a2
print(a1.shape)
print(a2.shape)

print(result)

# second example

x1 = np.array([1, 2, 3])  # (1,3) -- matrix
x2 = np.array([[1], [4], [5]]) # (3,1) -- matrix

print(x1.shape)
print(x2.shape)

print(x1+x2)