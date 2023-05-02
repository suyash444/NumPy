# join array
import numpy as np

x1 = np.array([1, 2, 9, 3, 2])
x2 = np.array([3, 4, 5, 1, 2])

# use of concatenate function()
result = np.concatenate((x1, x2))
print(result)

# concatenation of 2-d array:

c1 = np.array([[1, 3], [3, 5], [2, 9], [1, 3]])
c2 = np.array([[4, 2], [5, 2], [2, 3], [0, 1]])

ans = np.concatenate((c1, c2))
print(ans)

# if you want to concatenate in axis =1 then :
ans = np.concatenate((c1, c2), axis=1)
print(ans)
# output
# [[1 3 4 2]
#  [3 5 5 2]
#  [2 9 2 3]
#  [1 3 0 1]]

# Stack function

v1 = np.array([2, 3, 4])
v2 = np.array([3, 4, 2])

output = np.stack((v1, v2), axis=1)
print(output)
# it will form the array in 2d way:
# output
# [[2 3]
#  [3 4]
#  [4 2]]

# if you want to stack row wise then:

output = np.hstack((v1, v2))  # hstcak it will stack in row wise
print(output)

# output
# [2 3 4 3 4 2]

# if you want to stack column wise then :

output1 = np.vstack((v1, v2))  # vstack is use to stack in column wise
print(output1)

# output
#
# [[2 3 4]
#  [3 4 2]]

# if you want to stack height wise then:

output2 = np.dstack((v1, v2))  # dstack is use to stack in height wise
print(output2)

# output
# [[[2 3]
#   [3 4]
#   [4 2]]]

# split function()

var = np.array([1, 2, 3, 4, 5, 6])
print(var)

ar = np.array_split(var, 2)  # you have to give the number like how many time you want to split this like i gave 2
print(ar)

var1 = np.array([2, 12, 33, 442, 11, 42])


ab = np.array_split(var1, 3)
print(ab)
# output
# [array([ 2, 12]), array([ 33, 442]), array([11, 42])]