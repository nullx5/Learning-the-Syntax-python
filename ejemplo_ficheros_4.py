
f = open(r"C:\Users\flop\Desktop\Ficheros_Python\ejemplo_ficheros_4.txt", "w")
num_car = f.write("Ana : 28\nJavier : 32\nEva : 45\nCarlos : 29")
print("Primeros 4 registros escritos correctamente.")
print("Número de caracteres escritos:", num_car)
f.close()

f = open(r"C:\Users\flop\Desktop\Ficheros_Python\ejemplo_ficheros_4.txt", "a")
num_car = f.write("\nTexto añadido al final del fichero en una sola línea")
print("\nTexto añadido al final del fichero escrito correctamente.")
print("Número de caracteres escritos:", num_car)
f.close()

f = open(r"C:\Users\flop\Desktop\Ficheros_Python\ejemplo_ficheros_4.txt", "r")
c1 = f.read()
print("\nEl contenido del fichero es:")
print(c1)
f.close()
