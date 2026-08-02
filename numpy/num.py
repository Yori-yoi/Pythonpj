import numpy as np
array = np.array([[2020,2022,2029],
                 [2023,2024,2030],
                 [  2025,2026,2031],
                 [2027,2028,2032]])
x=np.array([1,2,3,4,5,6,7,8,9,10,11,12,13])
print(array.ndim)
print(array.shape)
print(array[0][1])
print(array[0,1])#multidimensional indexing 
print(array[0,1]+array[1,1]+array[1,0])
print((array[0,1])*2)
print(array*2)
print(array[::1])
print(array[:,0])#row,column to select 0th column from every row
print("slicing")
print(array[:,0:1])
print(array[0:2,1:3])



