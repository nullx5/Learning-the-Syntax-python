#-------------------------------------------------------------------------------
# Name:        module2
# Purpose:
#
# Author:      flop
#
# Created:     20/05/2016
# Copyright:   (c) flop 2016
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    numero = eval(input("Introduce un número: "))
    if numero > 0:
        print("El número es positivo y distinto de cero")
    else:
        print("El número es negativo o cero")

if __name__ == '__main__':
    main()
