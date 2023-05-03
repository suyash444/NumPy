# use of where() function in python
import numpy as np

x1 = np.array([1, 3, 2, 13, 2, 4, 5, 2])
result = np.where(x1 == 2)
print(result)
# where() function is used to find the INDEX LOCATION OF THE ELEMENTS   YOU WANT TO FIND..

# sort(): in python

z1 = np.array([1, 22, 33, 10, 3, 2, 98, 12])
print(np.sort(z1))
# output
# [ 1  2  3 10 12 22 33 98]

# it can sort the alphabets also

z2 = np.array(['N', 'E', 'D', 'K', 'Z', 'A'])
print(np.sort(z2))
# output
# ['A' 'D' 'E' 'K' 'N' 'Z']

# we can sort the 2-d or 3-d array

z3 = np.array([[2, 1], [1, 4], [2, 1], [3, 2]])
answer = np.sort(z3)
print(answer)