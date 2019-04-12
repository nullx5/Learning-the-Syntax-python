
class Ficha_empleado:
    def __init__(self):
        self.nombre = None
        self.edad = None
        self.antiguedad = None
        self.cualificacion = None

def main():
    import pickle

    a = Ficha_empleado()
    a.nombre = "Javier"
    a.edad = 21
    a.antiguedad = 2
    a.cualificacion = 1

    b = Ficha_empleado()
    b.nombre = "Fernando"
    b.edad = 32
    b.antiguedad = 9
    b.cualificacion = 4

    f = open(r"C:\Users\flop\Desktop\Ficheros_Python\ejemplo_pickle_2.dat", "wb")
    pickle.dump(a, f)
    pickle.dump(b, f)
    f.close()

    f = open(r"C:\Users\flop\Desktop\Ficheros_Python\ejemplo_pickle_2.dat", "rb")
    print("Contenido del fichero:")
    for i in range(2):
        c1 = pickle.load(f)
        print("\nFicha número", i + 1, ":")
        print("Nombre: ", c1.nombre)
        print("Edad: ", c1.edad)
        print("Antigüedad: ", c1.antiguedad)
        print("Cualificación: ", c1.cualificacion)
    f.close()

main()