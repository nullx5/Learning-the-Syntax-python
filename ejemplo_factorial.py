
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)
def main():
    n = eval(input("Introcuce un entero positivo para calcular su factorial "))
    print("El factorial de ", n, "es: ", factorial(n))

main()