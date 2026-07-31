import matplotlib.pyplot as plt
import numpy as np
line_style=dict(marker=".",markersize=10,linestyle="-.",linewidth=2)
months=np.array(["june","July","August","september"])
numbers=np.array([12,14,6,5])
plt.title("students passed")
plt.xlabel("Months")
plt.ylabel("students")
plt.bar(months,numbers,color="black")
plt.show()

