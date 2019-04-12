
f = open(r"C:\Users\flop\Desktop\Ficheros_Python\clientes.dat", "wb+")
f.write(b"Alfredo   Parrado   Diez      1234.39   AP32      ")
f.write(b"Julia     Garrido   Panadero  1089.00   JG11      ")
f.write(b"Xavi      Puig      Gonzalez  1890.77   XP01      ")
f.write(b"Jaime     Daroca    Lopez     987.32    JD01      ")

suma = 0
col = eval(input("Introducir el número de la columna a extraer (1-4): "))
while col!=1 and col!=2 and col!=3 and col!=4:
    col = eval(input("Número erróneo. Introducir de nuevo número de columna a extraer:"))
num = eval(input("Introducir el número de registros a extraer: "))
for i in range(num):
    if i == 0:
        f.seek((col-1)*10,0)
    else:
        f.seek(( (col-1)*10 + 50 * i ), 0)
    dato = f.read(10)
    if dato != b'':
        print(dato)
        if col == 4:
            suma += float(dato)
    else:
        print("Hemos llegado al final del fichero")
        break
if col == 4:
    print("La suma es de todos los registros indicados es:", suma)
f.seek(1, 0)
print("El contenido del todo el fichero en forma de lista es:\n ", list(f))

f.close()
