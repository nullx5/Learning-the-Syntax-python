import os.path

if os.path.isfile(r"C:\Users\flop\Desktop\Ficheros_Python\ejemplo_ficheros_1.txt"):
    f = open(r"C:\Users\flop\Desktop\Ficheros_Python\ejemplo_ficheros_1.txt", "r")
    contador = 0
    linea = f.readline()
    while(linea != ''):
        for caracter in linea:
            if ((caracter != ' ') and (caracter != '\n')):
                contador += 1
        linea = f.readline()
    print("El total de caracteres del fichero es:", contador)
    f.close()
else:
    print("El fichero que estás queriendo leer no existe.")