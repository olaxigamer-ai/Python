import matplotlib.pyplot as plt

days=['Mon','Tues','Wed','Thur','Fri','Sat','Sun']
score=[30,40,32,10,70,20,90]
plt.plot(days,score)
plt.show()

plt.plot(days,score,color="green", marker="o", linestyle="dashed",linewidth=4)
plt.grid(True)
plt.title("Score Tracker:")
plt.xlabel("Days")
plt.ylabel("Score")
plt.show()

plt.bar(days,score)
plt.show()

plt.bar(days,score,color="red")
plt.grid(True)
plt.title("Bar Score Tracker")
plt.xlabel("Days")
plt.ylabel("Score")
plt.show()