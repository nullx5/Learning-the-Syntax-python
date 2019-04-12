import os
import shelve

def muestra_datos():
    fichero = shelve.open(r"C:\Users\flop\Desktop\Ficheros_Python\ejemplo_shelve.dat")
    print("Los nombres almacenados son: ", fichero["nombres"])
    print("Las edades almacenadas son: ", fichero["edades"])
    print("El gasto individual almacenado es: ", fichero["gasto"])
    suma = 0
    for i in fichero["gasto"]:
        suma = suma + i
    print("El gasto total en todo el fichero es: ", format(suma,".2f"))
    fichero.close()

def menu():
    op_ok = False
    while op_ok == False:
        print("\nIntroduce la operacion a realizar: ")
        print("1.- Introducir nuevo registro.")
        print("2.- Borrar un registro.")
        print("3.- Buscar nombre.")
        print("4.- Salir.")
        op = input("Operacion: ")
        if op =='1' or op =='2' or op == '3' or op =='4':
            return op

def anadir_registro():
    fichero = shelve.open(r"C:\Users\flop\Desktop\Ficheros_Python\ejemplo_shelve.dat", writeback = True)
    nom = input("Introduce Nombre:")
    ed = eval(input("Introduce edad:"))
    gas = eval(input("Introduce gasto:"))
    fichero["nombres"].append(nom)
    fichero["edades"].append(ed)
    fichero["gasto"].append(gas)
    fichero.close()

def borrar_registro(num):
        fichero = shelve.open(r"C:\Users\flop\Desktop\Ficheros_Python\ejemplo_shelve.dat", writeback = True)
        tamano  = len(fichero["nombres"])
        if num <= tamano:
            del fichero["nombres"][num - 1]
            del fichero["edades"][num - 1]
            del fichero["gasto"][num - 1]
        else:
            print("El registro indicado no existe")
        fichero.close()

def buscar_nombre():
    nombre = input("Introduce el nombre a busca:")
    fichero = shelve.open(r"C:\Users\flop\Desktop\Ficheros_Python\ejemplo_shelve.dat")
    res = nombre in fichero["nombres"]
    if res == True:
        print("\nEl nombre", nombre, "sí está en el fichero.")
    else:
        print("\nEl nombre", nombre, "no está en el fichero.")
    fichero.close()

def main():
    nombres = ["Ana", "Javier", "Eva", "Francisco", "Marta"]
    edades= [28, 32, 45, 21, 34]
    gasto = [1023.44, 534.67, 52.34, 489.65, 3213.45]
    fichero = shelve.open(r"C:\Users\flop\Desktop\Ficheros_Python\ejemplo_shelve.dat")
    fichero["nombres"] = nombres
    fichero["edades"] = edades
    fichero["gasto"] = gasto
    fichero.close()

    os.system('cls')
    muestra_datos()
    opcion = menu()

    while opcion != '4':
        if opcion == '1':
            anadir_registro()
        if opcion == '2':
            try:
                num = eval(input("Introduce numero de registro a eliminar"))
            except:
                print("\nEl dato indicado no es correcto")
            else:
                if isinstance(num, int) == True:
                    borrar_registro(num)
        if opcion == '3':
            buscar_nombre()
        os.system('cls')
        muestra_datos()
        opcion = menu()

main()


