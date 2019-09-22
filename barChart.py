import pandas as pd
from matplotlib import pyplot as plt

#A bar chart is for comparing discrete variables
#A histogram is to represent a frequency distribution of continous variables

x = [2, 4, 6, 8, 10]
y = [1, 4, 9, 5, 7]

x2 = [1 ,3, 5, 9, 10]
y2 = [7, 2, 6, 10, 1]


plt.bar(x, y, label="Bars", color="r")
plt.bar(x2, y2, label="Bars2", color="c")

#label on the x and y side graph
plt.xlabel("x")
plt.ylabel("y")

plt.legend()


plt.title("Wow!! \nInteresting graph")
plt.show()