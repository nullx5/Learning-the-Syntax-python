
def numeros(num1, num2, num3):
    print("El primer número es:  ", num1)
    print("El segundo número es: ", num2)
    print("El tercer número es:  ", num3, "\n")

def main():
    numeros(1,2,3)
    numeros(num3 = 10, num2 = 15, num1 = 2)
    numeros(100, num3= 200, num2 = 1)
    numeros(7, 8, num3 = 9)

    print("Introduce tres números: ")
    a = eval(input("Numero1: "))
    b = eval(input("Numero2: "))
    c = eval(input("Numero3: "))
    numeros(a, num3 = b, num2 = c)

main()

