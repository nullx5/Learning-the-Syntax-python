
import random

datos = []
for i in range(3):
    datos.append([])
    for j in range(3):
        datos[i].append([])
        for k in range(3):
            datos[i][j].append(random.randint(0,50))

for i in range(3):
    for j in range(3):
        for k in range(3):
           print("Las ventas del comercial", i+1,\
                 "en el mes", j+1, "del artículo ",\
                  k+1, "han sido", datos[i][j][k])

print ("\nLos datos completos del comercial 1 son:", datos[0])
print ("Los datos del comercial 1 en el mes 1 son:", datos[0][0])
print ("El dato de ventas del comercial 1 en el mes 1 del artículo 1 son:", datos[0][0][0])

