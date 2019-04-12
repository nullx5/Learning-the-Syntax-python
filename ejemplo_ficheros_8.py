import os.path

if os.path.isfile(r"C:\Users\flop\Desktop\Ficheros_Python\ejemplo_ficheros_1.txt"):
    f = open(r"C:\Users\flop\Desktop\Ficheros_Python\ejemplo_ficheros_1.txt", "r")
    cont_eb = 0
    num_txt = ''
    total = 0
    for linea in f:
        for caracter in linea:
            if cont_eb != 2:
                if caracter == ' ':
                    cont_eb += 1
            else:
                if caracter != '\n':
                   num_txt += caracter
        total += int(num_txt)
        cont_eb = 0
        num_txt = ''
    f.close()
    print("El total de edades de las cuatro personas es:", total)
else:
    print("El fichero que estás queriendo leer no existe.")