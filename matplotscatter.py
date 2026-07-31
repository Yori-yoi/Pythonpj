import matplotlib.pyplot as plt
import numpy as np
x=np.array([2020,2022,2023,2025,2026,2027,2029,2031,2033])
x1=np.array([2021,2023,2025,2026,2027,2028,2030,2031,2032])
y=np.array([12,14,6,5,7,8,9,12,14])
y1=np.array([1,6,7,3,2,0,0,9,15])
plt.scatter(x,y,color="black",label="Class A")
plt.scatter(x1,y1,color="red",label="Class B")
plt.title("Passes")
plt.xlabel("Years")
plt.ylabel("passed")
plt.legend()
plt.show()
