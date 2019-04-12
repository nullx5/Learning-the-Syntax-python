import matplotlib.pyplot as plt

eje_x = list(range(1,13))
eje_y = [23, 4, 32, 77, 48, 93, 75, 90, 32, 28, 21, 18]
plt.xlim(0.5, 12.5)
plt.ylim(0, 100)
plt.xticks([x for x in range(1,13)], ["Enero", "Febrero", "Marzo", "Abril"," Mayo" ,\
                                      "Junio","Julio","Agosto","Septiembre","Octubre",\
                                      "Noviembre","Diciembre"], fontsize = 7)
plt.yticks([10*x for x in range(11)])
plt.bar(eje_x, eje_y, color = 'cyan', align = 'center', width = 1)
plt.show()
