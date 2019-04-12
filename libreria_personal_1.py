
class FichaEmpleado:
    def __init__(self, nombre : str):
        self.nombre = nombre
        self.__cualificacion = None
    def setCualificacion(self, cualif:int):
         if cualif == 1 or cualif == 2 or cualif == 3\
         or cualif == 4 or cualif == 5:
            self.__cualificacion = cualif
    def getCualificacion(self):
        return(self.__cualificacion)

class FichaFabricacion(FichaEmpleado):
    def __init__(self, nombre : str, art_mes : float):
        super().__init__(nombre)
        self.articulos_mes = art_mes

class FichaTecnico(FichaEmpleado):
    def __init__(self, nombre : str):
        super().__init__(nombre)
        self.estrellas = "*"

def inicializar_cualificacion(objeto):
    objeto.setCualificacion(1)

def dar_datos(objeto):
    print("Nombre: ", objeto.nombre)
    print("Cualificación: ", objeto.getCualificacion())
    if isinstance(objeto, FichaFabricacion):
      print("Media de artículos manufacturados al mes:", objeto.articulos_mes)
    elif isinstance(objeto, FichaTecnico):
      print("Número de estrellas del departamento técnico:", objeto.estrellas)
    print("")

def main():
    a = FichaEmpleado("Pepe")
    b = FichaFabricacion("Juan", 10)
    c = FichaTecnico("Javier")
    inicializar_cualificacion(a)
    inicializar_cualificacion(b)
    inicializar_cualificacion(c)
    dar_datos(a)
    dar_datos(b)
    dar_datos(c)

