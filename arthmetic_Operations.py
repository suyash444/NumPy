import numpy as np

x = np.array([1, 2, 3, 4, 5])
ans = x + 3
print(ans)

x1 = np.array(([1, 2, 3, 4, 5, 6]))
x2 = np.array([2, 3, 4, 5, 6, 7])

result = x1 + x2
print(result)

result1 = np.add(x1, x2)
print(result1)

arr1 = np.array([2, 4, 5, 6, 7])
arr2 = np.array([5, 1, 4, 3, 4])

result2 = arr1 * arr2
print(result2)


a1 = np.array([2,3,4])
res = a1/3
print(res)