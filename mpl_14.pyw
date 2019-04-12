import matplotlib.pyplot as plt

datos = [23, 12, 32, 77, 38]
plt.pie(datos)
plt.pie(datos, labels =['Ana','Eva','Juan','Marta','Javier'], shadow = True, labeldistance= 0.7 )
plt.show()
