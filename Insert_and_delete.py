# how to do insertion in a given array
import numpy as np

x = np.array([1, 2, 3, 4, 5])
ans = np.insert(x, 2, 20)
print(ans)

# so the syntax is-- np.insert(x, 2, 20), first pass the variable name and then the index value in which you want to add
# the value and then the value which you want to replace in that place..

# how to delete a data in a given array
y = np.array([2, 4, 5, 9, 1, 10])
result = np.delete(y, 2)
print(result)

# output
# [ 2  4  9  1 10] -- as we can see the data has been deleted in the index value of 2 ,so this is how we
# delete the data in numpy
