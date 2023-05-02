# copy ---
import numpy as np

arr = np.array([1, 2, 4, 9, 3])
res = arr.copy()  # it will copy the exact same value given in the array
print(arr)
print(res)
# but suppose we change the original value of the array let's see:
arr[1] = 20  # we change the index value of 1 to 20 ,earlier it was 2
print(arr)
# [ 1 20  4  9  3] # new array now do the copy function:
print(res)
# [1 2 4 9 3] see the original data is different and the data we get was from older so changes made in the copy data
# does not reflect in the original array:

# -----------------------

# view

x = np.array([1, 3, 2, 9])
print(x)
x1 = x.view()
print(x1)

# now changing the value of the original array
x[2] = 5 # in terms of index value 2 =2 replacing it with 5

print(x)
print(x1)
# [1 3 5 9] # as we can see the change array.
# [1 3 5 9] # now view copies the original array as we change the original array so view copies exact same.
