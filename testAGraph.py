import pandas as pd
from matplotlib import pyplot as plt

x = [1, 2, 3, 4, 5]
y = [1, 4, 9, 5, 7]

x2 = [1, 2, 3]
y2 = [10, 56, 43]

#different lines that will be represented
#label that will be added to the legend
plt.plot(x, y, label="line 1")
plt.plot(x2, y2, label="line 2")

#label on the x and y side graph
plt.xlabel("Plot number")
plt.ylabel("Important var")

plt.legend()


plt.title("Wow!! \nInteresting graph")
plt.show()