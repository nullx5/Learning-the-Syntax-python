def funcion_decoradora_A(funcion_parametro_B):
    def funcion_interior_C(*args):
        print("Realizando calculos...")

        funcion_parametro_B(*args)

        print("Calculos realizados...")

    return funcion_interior_C


@funcion_decoradora_A
def suma(num1, num2, num3):
    print(num1 + num2 + num3)

@funcion_decoradora_A
def resta(num1, num2):
    print(num1 + num2)


suma(1, 2, 3)
resta(5, 3)