
f = open(r"C:\Users\flop\Desktop\Ficheros_Python\ejemplo_ficheros_1.txt", "w")
num_car = f.write("Ana : 28\nJavier : 32\nEva : 45\nCarlos : 29")
print("Fichero escrito correctamente. Número de caracteres escritos: ", num_car ,"\n")
f.close()

f = open(r"C:\Users\flop\Desktop\Ficheros_Python\ejemplo_ficheros_1.txt", "r")
c1 = f.read()
print("Usando read() nos devuelve la siguiente cadena (incluye tres cambios de línea):")
print(c1)

f.seek(0)
c2 = f.readline()
print("\nUsando readline() nos devuelve la cadena (incluye un cambio de línea):")
print(c2)

f.seek(0)
c3 = f.readlines()
print("Usando readlines() obtenemos la lista de cadenas siguiente:")
print(c3)

f.seek(0)
c4 = list(f)
print("\nUsando list(f) obtenemos la lista de cadenas siguiente:")
print(c4)

f.close()
