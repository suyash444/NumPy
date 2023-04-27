import numpy as np

arr1 = np.ones(3)
print(arr1)

# create a matrix of 4 row and 4 column using ones function

arr2 = np.ones((4, 4))
print(arr2)

# create an empty array
arr3 = np.empty(4)
print(arr3)

# as empty function uses the memory of last output that we ran

# Range
arr4 = np.arange(5)
print(arr4)

# arange function works as same as like range function we use in for loop like (n-1)

# create an array diagonal element filled with ones

arr5 = np.eye(3)
print(arr5)

# output
# [[1. 0. 0.]
#  [0. 1. 0.]
#  [0. 0. 1.]]

arr6 = np.eye(2,4)
print(arr6)
#output:
# [[1. 0. 0. 0.]
#  [0. 1. 0. 0.]]

# linespace

arr7 = np.linspace(1,30,num = 20)
print(arr7)

# output:
# [ 1.          2.52631579  4.05263158  5.57894737  7.10526316  8.63157895
#  10.15789474 11.68421053 13.21052632 14.73684211 16.26315789 17.78947368
#  19.31578947 20.84210526 22.36842105 23.89473684 25.42105263 26.94736842
#  28.47368421 30.        ]

# as (1,30,num =20) means that it will start from  1 to 30 and total elememts will be 20