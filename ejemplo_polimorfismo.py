
class FichaEmpleado:
    def __init__(self):
        self.nombre = None
        self.cualificacion = None
    def setCualificacion(self, cualif:int):
         if cualif == 1 or cualif== 2 or cualif == 3\
         or cualif == 4 or cualif == 5:
            self.cualificacion = cualif
    def getCualificacion(self):
        return(self.cualificacion)

class FichaFabricacion(FichaEmpleado):
    def __init__(self, art_mes : float):
        super().__init__()
        self.__articulos_mes = art_mes

class FichaTecnico(FichaEmpleado):
    def __init__(self):
        super().__init__()
        self.__estrellas = "*"
    def getCualificacion(self):
         salida = "La cualificación del empleado técnico "\
          + self.nombre + " es: " + str(self.cualificacion)
         return(salida)

def dar_cualificacion(objeto):
    print(objeto.getCualificacion())

def main():
    a = FichaEmpleado()
    b = FichaFabricacion(10)
    c = FichaTecnico()
    a.nombre = "Pepe"
    b.nombre = "Juan"
    c.nombre = "Javier"
    a.setCualificacion(5)
    b.setCualificacion(3)
    c.setCualificacion(1)
    dar_cualificacion(a)
    dar_cualificacion(b)
    dar_cualificacion(c)

main()
