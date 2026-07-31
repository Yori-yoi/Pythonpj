import numpy as np
import matplotlib.pyplot as plt
marks = np.random.normal(loc=70, scale=10, size=1000)
plt.hist(marks)
plt.xlabel("Marks")
plt.ylabel("Number of Students")
plt.grid(axis="y")
plt.show()