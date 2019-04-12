
palabras = ["Uno", "Dos", "Tres"]
with open(r"C:\Users\flop\Desktop\Ficheros_Python\mitexto.txt", "w") as f:
    for palabra in palabras:
        f.write(palabra + "\n")

with open(r"C:\Users\flop\Desktop\Ficheros_Python\mitexto.txt", "r") as f:
    for linea in f:
        print(linea, end='')
        print("----")
