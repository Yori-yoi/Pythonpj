import numpy as np
array = np.array([[2020,2022,2029],
                 [2023,2024,2030],
                 [  2025,2026,2031],
                 [2027,2028,2032]])
x=np.array([1,2,3,4,5,6,7,8,9,10,11,12,13])
#scalar math fn
print((x+1)**5)
print(array**2)

#vectorised math fn
print(np.sqrt(array))
print(np.ceil(np.sqrt(array)))
print(np.pi)
#print(array+x) doesnt work as we need both arrays to have same shape
print(array>2022)
array[array<2024]=0
print(array)
