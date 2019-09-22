from matplotlib import pyplot as plt

#A bar chart is for comparing discrete variables
#A histogram is to represent a frequency distribution of continous variables

population_ages = [22, 50, 60, 23, 110, 34, 4, 121, 34, 65, 34, 87, 14, 64, 74, 35]

bins = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130]
ids = [x for x in range(len(population_ages))]

plt.hist(population_ages, bins, histtype="bar", rwidth=0.8)

#label on the x and y side graph
plt.xlabel("x")
plt.ylabel("y")

plt.legend()


plt.title("Wow!! \nInteresting graph")
plt.show()