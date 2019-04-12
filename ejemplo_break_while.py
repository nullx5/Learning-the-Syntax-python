
suma = 0
print("El programa irá pidiendo números y los irá sumando hasta que la suma supere el valor 100")
while True:
    numero = eval(input("Introduce un número: "))
    suma = suma + numero
    if suma > 100:
        break
print ("La suma total al superar los 100 ha sido: ", suma)
