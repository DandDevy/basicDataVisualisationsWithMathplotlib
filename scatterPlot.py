from matplotlib import pyplot as plt

x = [1, 2, 3, 4 ,5, 6, 7, 8, 9]
y = [3, 6, 7, 9, 4, 7, 5, 8, 2]

plt.scatter(x, y, label="skitscat", color="k", marker="*", s=100)
#label on the x and y side graph
plt.xlabel("x")
plt.ylabel("y")

plt.legend()


plt.title("Wow!! \nInteresting graph")
plt.show()