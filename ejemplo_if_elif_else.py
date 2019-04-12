#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      flop
#
# Created:     23/05/2016
# Copyright:   (c) flop 2016
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    numero = eval(input("Introduce un número: "))
    if numero > 0:
        print("El número es mayor que cero")
    elif numero == 0:
        print("El número es cero.")
    else:
        print("El número es menor que cero")

if __name__ == '__main__':
    main()
