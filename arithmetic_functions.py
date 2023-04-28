import numpy as np
# to find the min value
arr = np.array([1,2,3,0,5])
print("Minimum value :=", min(arr))

# to find the maximum value:
print("Maximum Value =:", max(arr))

# to find the index value of the min value use argmin function

print("Minimum value :=", min(arr),"Index Value :=", np.argmin(arr))

#To find the index value of the maximum number

print("Maximum Value =:", np.max(arr),"Index Value: =", np.argmax(arr))
# to find the cosine function:
print(np.cos(arr))

# to find the sin() function
print(np.sin(arr))

# to find the cumsum()
print(np.cumsum(arr))