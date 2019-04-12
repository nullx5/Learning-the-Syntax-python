import matplotlib.pyplot as plt

X = list(range(11))
Y1 = [x*75 for x in X]
Y2 = [x*58 for x in X]
plt.subplot2grid((1,2), (0,0))
plt.title("HOMBRES")
plt.xlabel('Número de hombres')
plt.ylabel('Peso acumulado medio')
plt.plot(X, Y1)
plt.subplot2grid((1,2), (0,1))
plt.title("MUJERES")
plt.xlabel('Número de mujeres')
plt.plot(X, Y2)
plt.show()
