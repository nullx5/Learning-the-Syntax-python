﻿import matplotlib.pyplot as plt

X = list(range(50))
Y1 = [1/(x+5) for x in X]
Y2 = [x**2 for x in X]

plt.rcParams['toolbar'] = 'None'
fig = plt.figure(frameon = True, facecolor = '1')
fig.canvas.set_window_title("Gráficos en Matplotlib ")
ax1= fig.add_subplot(121)
ax1.tick_params(width = 0)
ax1.spines["top"].set_visible(False)
ax1.spines["right"].set_visible(False)
ax1.set_title("Primera función", loc = "left", color = "b")
ax1.plot(X,Y1)
ax2 = fig.add_subplot(122)
ax2.tick_params(width = 0)
ax2.spines["top"].set_visible(False)
ax2.spines["right"].set_visible(False)
ax2.set_title("Segunda función", loc = "right", color = "g")
ax2.grid(True, axis = "both", ls = '-.', color ='0.3')

c2, = ax2.plot(X,Y2)
c2.set_color("green")
ax1.annotate('y = 1/(x+5)', xytext = (25, 0.10), xy = (15, 0.05), ha = 'left',  va = 'top',\
              arrowprops = dict(arrowstyle = '->', linewidth = 1.5, connectionstyle = 'angle3',\
                                color = (0.5,0.5,0.5)))
ax2.annotate('y = x**2', xytext = (20, 1200), xy = (30, 890), ha = 'right', va = 'bottom',color = "blue",\
              arrowprops = dict(arrowstyle = '<->', linewidth = 2, connectionstyle = 'angle',\
                                color = (0.7,0.1,0.9)))

plt.show()
