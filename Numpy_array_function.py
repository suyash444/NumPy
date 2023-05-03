# shuffle () function :
import numpy as np

arr = np.array([1, 2, 5, 0, 9, 4])
np.random.shuffle(arr)
print(arr)

# [5 4 1 0 2 9] if we run again and again  the data will be changing(shuffling).
# [0 5 9 4 2 1] everytime the output will be different as it will shuffle the values.

# unique() function:

x = np.array([1, 1, 3, 4, 3, 5, 9, 1, 9, 4, 2, 5, 9])
res = np.unique(x)
print(res)

# unique() -- it will not give the duplicate values as it will give you only the values which came once
# output
# [1 2 3 4 5 9]


# Resize() function:

z = np.array([1, 2, 3, 4, 5, 6])
ans = np.resize(z, (2, 3))
print(ans)

# output ....
# [[1 2 3]
#  [4 5 6]]

# resize() : function is used to resize the array like: if its single dimension array, and you pass (2,3) then
# it will convert the array to two-dimensional aaray: