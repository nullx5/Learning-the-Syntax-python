import os.path

if os.path.isfile(r"C:\Users\flop\Desktop\Ficheros_Python\ejemplo_ficheros_1.txt"):
    f = open(r"C:\Users\flop\Desktop\Ficheros_Python\ejemplo_ficheros_1.txt", "r")
    contador = 0
    for linea in f:
        for caracter in linea:
            if ((caracter != ' ') and (caracter != '\n')):
                contador += 1
    print("El total de caracteres del fichero es:", contador)
    f.close()
else:
    print("El fichero que estás queriendo leer no existe.")