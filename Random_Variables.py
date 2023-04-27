# Rand()  function
import numpy as np
x = np.random.rand(5)
print(x)
# [0.8385862  0.71013536 0.74472919 0.48982878 0.47662104]
#Rand() --  it will give you the positive values from 0 to 1

#Randn() -- function
#randn() -- it will give you the values from zero to one and will be both (+ve) and (-ve)
y = np.random.randn(5)
print(y)
# output
# [ 1.16309964 -0.96393267  1.29066605  1.17306416  0.72535754]

# Ranf() -- it will include the range from close to zero but it will be less than 1 ,therefore it will not include 1
z = np.random.ranf(5)
print(z)
# output
# [0.25575793 0.73005773 0.70749576 0.77103751 0.84909529]

#Randint() -- the function is used to generate a random numbers between a given range
# np.random.randint(min,max,total_values)
d = np.random.randint(2,20,5)
print(d)
# output
# [11 13  3  5  8]