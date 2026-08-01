import numpy as np
a = np.array([
    [1,2,3],
    [4,5,6]
])
b = np.array([10,20,30])

print(a + 10)
print(a+b)
#for broadcasting the corresponding dimension should either match or one of them be 1 as that 1 can be stretched
print(a*b) #ex: a is 2,3 and b is 1,3 : first is 1 and the second are equal so it can be broadcasted
#not a matrix multiplication but element wise multiplication according to position
print(a.shape,b.shape)
