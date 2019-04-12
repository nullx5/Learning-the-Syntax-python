import matplotlib.pyplot as plt

X = list(range(11))
Y1 = [x*75 for x in X]
Y2 = [x*58 for x in X]
plt.subplot2grid((1,2), (0,0))
plt.title("HOMBRES")
plt.xlabel('Numero de hombres')
plt.ylabel('Peso acumulado medio')
plt.plot(X, Y1)
ejes1_tupla = plt.axis()
plt.subplot2grid((1,2), (0,1))
plt.title("MUJERES")
plt.xlabel('Numero de mujeres')
plt.plot(X, Y2)
ejes2_tupla = plt.axis()
if ejes1_tupla[3] > ejes2_tupla[3]:
    ejes2_lista = list(ejes2_tupla)
    ejes2_lista[3] = ejes1_tupla[3]
    plt.axis(ejes2_lista)
else:
    ejes1_lista = list(ejes1_tupla)
    ejes1_lista[3] = ejes2_tupla[3]
    plt.subplot2grid((1,2), (0,0))
    plt.axis(ejes1_lista)
    plt.xlabel('Numero de hombres')
    plt.ylabel('Peso acumulado medio')
    plt.plot(X, Y1)
plt.show()
