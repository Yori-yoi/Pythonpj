import matplotlib.pyplot as plt
import numpy as np
line_style=dict(marker=".",markersize=10,linestyle="-.",linewidth=2)
x=np.array([2020,2022,2023,2025])
y=np.array([12,14,6,5])
y1=np.array([10,9,3,2])
plt.xlabel("Year",fontsize=15,color="#000000")
plt.ylabel("number of people passed",fontsize=16,color="#231983")
plt.title("pass vs year",family="Arial",fontweight="bold",fontsize=20,color="#349390")
plt.xticks([2020, 2022, 2023, 2025])
plt.grid(axis="y",linewidth=2,color = "gray",linestyle="dashed")
plt.plot(x,y,**line_style) #unpack the dict
plt.plot(x,y1,color="black",**line_style)
plt.show()
