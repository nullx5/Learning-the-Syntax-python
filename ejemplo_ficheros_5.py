﻿
f = open(r"C:\Users\flop\Desktop\Ficheros_Python\ejemplo_ficheros_5.txt", "w+")
num_car = f.write("Ana : 28\nJavier : 32\nEva : 45\nCarlos : 29\n")
print("Los cuatro primeros registros escritos correctamente.")
print("Número de caracteres escritos (incluidos caracteres de cambio de línea): ", num_car ,"\n")
f.seek(0)
c1 = f.readlines()
print("Usando readlines() obtenemos la lista de cadenas siguiente:")
print(c1)
limite = f.tell()
num_car = f.write("Marta : 41\nAlfonso : 21\nLaura : 27\nDiego : 19\n")
print("\nLos cuatro siguientes registros escritos correctamente.")
print("Número de caracteres escritos (incluidos caracteres de cambio de línea): ", num_car ,"\n")
f.seek(limite,0)
c1 = f.readlines()
print("Usando readlines() desde el final de los 4 primeros registros (usando seek y tell) obtenemos:")
print(c1)
f.close()
