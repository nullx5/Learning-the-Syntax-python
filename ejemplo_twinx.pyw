﻿import matplotlib.pyplot as plt

X = list(range(50))
Y1 = [1/(x+5) for x in X]
Y2 = [x**2 for x in X]
fig = plt.figure()
ax1= fig.add_subplot(111)
ax1.plot(X,Y1, color ="magenta")
ax1.set_xlabel("Eje comun")
ax1.set_ylabel("Curva magenta")
ax2 = ax1.twinx()
c2, = ax2.plot(X,Y2)
c2.set_color("green")
ax2.set_ylabel("Curva verde")
plt.show()
