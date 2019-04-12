
i = 1	                                        # i lleva la cuenta de números introducidos.
suma = 0	                                    # En suma se va almacenando la suma de
print("Introduce una serie de números. \
Si es 0 entenderemos que has \
terminado la lista.", end ="\n")

print("Número", i, ": ",end = '')	            # Usamos el parámetro end para que no
numero = eval(input())	                        # cambie de línea.
print(numero)	                                # Sacamos el número introducido por pantalla.
suma = suma + numero                        	# Sumanos el primer numero a suma.

while numero != 0:	                            # La condición para pedir otro número es que
    i = i + 1	                                # sea distinto de cero. E incrementamos i
    print("Número", i, ": ", end = "")       	# dentro del bucle, a la vez que sumamos
    numero = eval(input())	                    # cada número a la variable suma.
    print(numero)
    suma = suma + numero

print("La suma de todos los números es:", suma)	# Al salir del while ya tendremos el valor
                                                    # total de la suma.

