
f= open(r"C:\Users\flop\Desktop\Ficheros_Python\ejemplo_ficheros_9.txt", "w")
num = eval(input("Introduce un número entero o real. Si es el 0 se terminará la serie:"))
while num != 0:
    f.write(str(num))
    f.write(' ')
    num = eval(input("Introduce un número entero o real. Si es el 0 se terminará la serie:"))
f.close()
