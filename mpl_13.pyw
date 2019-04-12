﻿import matplotlib.pyplot as plt

eje_x = list(range(1,11))
for i in range(len(eje_x)):
    eje_x_2 = [x + 1/3 for x in eje_x]
for i in range(len(eje_x)):
    eje_x_3 = [x + 2/3 for x in eje_x]
eje_y = [23, 4, 32, 77, 8, 43, 45, 90, 12, 68]
eje_y2 = [45, 10, 3, 7, 65, 4, 32, 21, 38, 6]
eje_y3 = [11, 98, 42, 71, 12, 67, 4, 9, 2, 52]
plt.xlim(1-1/6, 11-1/6)
plt.ylim(0, 100)
plt.grid(linestyle = '--', axis = 'y')
plt.bar(eje_x, eje_y, width = 1/3, color = 'green', align = 'center')
plt.bar(eje_x_2, eje_y2, width = 1/3, color = 'blue', align = 'center')
plt.bar(eje_x_3, eje_y3, width = 1/3, color = 'yellow', align = 'center')
plt.show()
