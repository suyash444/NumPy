# indexing and slicing
import numpy as np

arr = np.array([1, 2, 3, 4, 5])
# as index starts from (0 , 1 ,2 ,3 ,4 )
# as negative index from(-5,-4,-4,-2,-1)

print(arr[1:4])
# suppose we want the full array list from starting value then,
print(arr[0:])

# formula for slicing [start_value: stop_value: step_miss_value]

print(arr[0:4:2])  # as it will skip one number

# take 2 -dimensional array

arr1 = np.array([[1, 2, 3, 9, 2], [4, 5, 6, 11, 22], [10, 11, 12, 11, 10]])
# suppose we want the value only [4 6 22]

print(arr1[1, 0:5:2])
# if you want to get the index value 1 and the value only [4 6 22] -then write this - [1, 0:5:2]

# index number -     0             1              2              3
arr3 = np.array([[1, 2, 3, 4], [2, 3, 4, 5], [3, 1, 4, 5], [9, 8, 7, 5]])
print(arr3.ndim)
# as it is a 2 dimensional array, to check whether which dimensional array it is use ndim function.
# now do slicing and indexing
print(arr3[2, 0:4:2])
# as I took 2 index number so 2 index number is :[3,1,4,5]
