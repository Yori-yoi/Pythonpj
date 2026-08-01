import numpy as np
array = np.array([[2020,2022,2029],
                 [2023,2024,2030],
                 [  2025,2026,2031],
                 [2027,2028,2032]])
x=np.array([1,2,3,4,5,6,7,8,9,10,11,12,13])
print(np.sum(x))
print(np.min(x))
print(np.mean(x))
print(np.max(x))
print(np.var(x))
print(np.argmin(x))
print(np.argmax(x)) 
#to print position of the max or min use arg min or argmax and std for standard deviation and var for variance 
array.sum(axis=1)
array.mean(axis=0)
array.max(axis=0)
array.min(axis=1)
array.std(axis=0)
#rule if Shape = (4,6,8,5,7) sum(axis=2) removes the 8 and becomes (4,6,5,7), axis removes=n removes the nth axis froms sum
# for 2 dimensions axis 0 is column and axis 1 