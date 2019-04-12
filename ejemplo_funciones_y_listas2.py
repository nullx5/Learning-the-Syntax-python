
def elevar_2(numero : int , lista = [1, 2, 3]):
    for i in range(0, len(lista)):
        lista[i] = lista[i] **2
    numero = numero ** 2
    print("El número dentro de la función elevar_2 es:", numero)
    print("La lista dentro de la función elevar_2 es:", lista)

def main():
    numero = 10
    elevar_2(numero)
    print("El número en el programa principal es:", numero,"\n")

    elevar_2(numero)
    print("El número en el programa principal es:", numero,"\n")

    elevar_2(numero,[5, 5, 5, 5, 5])
    print("El número en el programa principal es:", numero,"\n")

main()

