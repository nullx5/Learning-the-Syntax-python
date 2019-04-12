
def elevar_2(numero : int , lista = [1, 2, 3]):
    print("La variable lista antes de ejecutar la función es:", lista)
    for i in range(0, len(lista)):
        lista[i] = lista[i] **2
    numero = numero ** 2
    return lista, numero

def main():
    numero = 10

    print("La variable número antes de ejecutar la función es:", numero)
    lista, numero = elevar_2(numero)
    print("La variable número después de ejecutar la función es:", numero)
    print("La variable lista después de ejecutar la función es: ", lista,"\n")

    print("La variable número antes de ejecutar la función es:", numero)
    lista, numero = elevar_2(numero)
    print("La variable número después de ejecutar la función es:", numero)
    print("La variable lista después de ejecutar la función es: ", lista,"\n")

    print("La variable número antes de ejecutar la función es:", numero)
    lista, numero = elevar_2(numero,[5, 5, 5, 5, 5])
    print("La variable número después de ejecutar la función es:", numero)
    print("La variable lista después de ejecutar la función es: ", lista)

main()

