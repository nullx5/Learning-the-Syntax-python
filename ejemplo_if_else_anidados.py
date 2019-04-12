#-------------------------------------------------------------------------------
# Name:        module1
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
        print("El número es mayor que cero")
    else:
        if numero == 0:	                            # Recordamos que el operador relacional de
            print("El número es cero.")         	#igualdad se escribe' =='. Distinguirlo del de
        else:	                                    # asignación, que se escribe '='.
            print("El número es menor que cero")

if __name__ == '__main__':
    main()
