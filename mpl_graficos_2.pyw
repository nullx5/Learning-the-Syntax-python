import matplotlib.pyplot as plt
import random

plt.rcParams['toolbar'] = 'None'
plt.rcParams['font.size'] = '10'

X = list(range(1, 11))
Y1 = []
Y2 = []
Y3 = []
Y4 = []
for y in range(10):
    Y1.append(10)
    Y2.append(random.randint(1,50))
    Y3.append(random.randint(1,50))
    Y4.append(random.randint(1,50))

nombres = ["Ajos", "Patatas", "Lechugas","Berzas", "Fresas",\
           "Lechugas", "Puerros", "Tomates", "Pimientos", "Coles"]
colores = ['b' , 'g' , 'r', '0.65', 'c', 'm' , '0.85', 'y' , 'w' , (0.7,0.1,0.3) ]

fig = plt.figure(figsize = (12, 10),frameon = False)
fig.canvas.set_window_title("Gráfico tipo tarta")
fig.suptitle("Número de productos pedidos", fontsize = 15, color = "blue")

ax1= fig.add_subplot(221)
ax1.set_title("Colores por producto", color = 'k')
ax1.pie(Y1, labels = nombres, shadow = True, colors = colores,\
        explode = [0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1])

ax2= fig.add_subplot(222)
ax2.set_title("Cliente: Manolo", color = 'r')
ax2.pie(Y2,autopct= '%d' , shadow = True, colors = colores,\
        explode = [0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1])

ax3= fig.add_subplot(223)
ax3.set_title("Cliente: Ana", color = 'b')
ax3.pie(Y3,autopct= '%d', shadow = True, colors = colores,\
        explode = [0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1])

ax4= fig.add_subplot(224)
ax4.set_title("Cliente: Laura", color = 'm')
ax4.pie(Y4,autopct= '%d' , shadow = True, colors = colores,\
        explode = [0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1])

plt.show()
