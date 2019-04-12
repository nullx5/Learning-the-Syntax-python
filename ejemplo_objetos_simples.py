
class Ficha_empleado:
    def __init__(self):
        self.nombre = None
        self.edad = None

def main():
    a = Ficha_empleado()
    a.nombre = "Javier"
    a.edad = 21

    b = Ficha_empleado()
    b.nombre = "Fernando"
    b.edad = 32

    b = a
    print(b.nombre)
    print(b.edad)

    b.nombre = "Fernando"
    print(a.nombre)

main()
