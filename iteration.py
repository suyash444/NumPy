import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6])
for i in arr:
    print(i)
# iterating for a single dimensional array


# iteration for two-dimensional array, so we will use -:(two for loops:)

arr2 = np.array([[1, 2, 3, 4, 9], [4, 5, 2, 1, 5], [1, 2, 3, 4, 5]])
print(arr2.ndim)
print(arr2.shape)

# to iterate it now we will use two for loops

for i in arr2:
    for j in i:
        print(j)

# iteration for 3 dimensional array:

arr3 = np.array([[[1, 2, 3, 4, 9], [4, 5, 2, 1, 5], [1, 2, 3, 4, 5]]])
print(arr3.ndim)
print(arr3.shape)

print("nditer() function iterator:")
for ar in np.nditer(arr3):
    print(ar)  # we can use this function also to iterate the data instead of using for loop three times
print("for loop iteration:")
for i in arr3:
    for j in i:
        for k in j:
            print(k)

# as we will use three loops for iterating the three-dimensional array

# instead of using for loop every time we can use nditer() function to iterate  the array

x1 = np.array([[1, 2, 3, 4], [2, 3, 4, 5]])
print(x1.ndim)  # to check which type of array is: 2-d or 3d
for i in np.nditer(x1):
    print(i)

# to get the index value with the iteration we will use ndenumerate() function -:

z = np.array([[2, 2], [2, 1], [4, 3]])

for i, j in np.ndenumerate(z):
    print(i, j)

# so as it will update you the index number also with the iteration
# output:
# (0, 0) 2
# (0, 1) 2
# (1, 0) 2
# (1, 1) 1
# (2, 0) 4
# (2, 1) 3