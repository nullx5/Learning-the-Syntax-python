﻿
def calculo_dos_datos_2(num1, num2):
        res = ((num1 - num2) ** 2 ) + 1
        return(res)


def main():
    for i in range(0,3):
        numero_1 = eval(input("Introcuce el primer número: "))
        numero_2 = eval(input("Introcuce el segundo número: "))
        resultado = calculo_dos_datos_2(numero_1, numero_2)
        print ("\nEl primer número introducido ha sido: ", numero_1)
        print ("El segundo número introducido ha sido: ", numero_2)
        print ("La diferencia entre ellos elevada al cuadrado y luego sumado uno es: ", resultado)

main()

