﻿import matplotlib.pyplot as plt

X = list(range(50))
Y1 = [1/(x+5) for x in X]
Y2 = [x**2 for x in X]
fig = plt.figure()
ax1= fig.add_subplot(121)
ax1.plot(X,Y1)
ax2 = fig.add_subplot(122)
ax2.plot(X,Y2)
plt.show()
