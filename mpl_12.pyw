﻿import matplotlib.pyplot as plt

eje_y = list(range(10,20))
eje_x = [23, 4, 7, 77, 81, 43, 45, 90, 12, 68]
eje_x2 = [45, 10, 3, 67, 65, 24, 32, 21, 38, 56]
plt.ylim(9,20)
plt.barh(eje_y, eje_x, color = 'red', align = 'center')
plt.barh(eje_y, [-eje_x2[i] for i in range(len(eje_x2))], color = 'yellow', align = 'center')
plt.show()
