import numpy as np
array = np.array([[2020,2022,2029],
                 [2023,2024,2030],
                 [  2025,2026,2031],
                 [2027,2028,2032]])
x=np.array([1,2,3,4,5,6,7,8,9,10,11,12,13])
arr=array[((array>=2024) & (array<2030)) | (array%4==0)] #flattens the data not preserving the shape
preserved=np.where((((array>=2024) & (array<2030)) | (array%4==0)),array,0)
#np.where(condition,array,replacement of values that do not meet the condition)
print(preserved)
print(arr)


