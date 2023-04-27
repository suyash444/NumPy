from timeit import timeit
import numpy as np

x = [1, 2, 3, 4, 5]
y = np.array(x)

print(y)

# create an empty list
list = []
# pass the range till which you have to pas the number as range works (n-1) so it will take 5 numbers
for i in range(6):
    x = int(input("Enter the number:"))
    # append the list to the values that you passed to the variable x
    list.append(x)
# convert the list to array with help of numpy
print(np.array(list))

x = ([[[1, 2, 3, 4], [3, 4, 5, 6], [9, 1, 2, 3]]])
print(x)
