
class FichaEmpleado:
    def __init__(self):
        self.nombre = None
        self.edad = None
        self.antiguedad = None
        self.__cualificacion = None
    def __sueldo(self):
        return(1000 + self.antiguedad * 25 + self.__cualificacion * 100)
    def setCualificacion(self, cualif:int):
         if cualif == 1 or cualif== 2 or cualif == 3 or cualif == 4 or cualif == 5:
            self.__cualificacion = cualif
    def getCualificacion(self):
        return(self.__cualificacion)
    def getSueldo(self):
        return(self.__sueldo())

class FichaFabricacion(FichaEmpleado):
    def __init__(self, art_mes : float):
        super().__init__()
        self.__articulos_mes = art_mes
    def incArticulos(self, suma : float):
        self.__articulos_mes += suma
    def getArticulos(self):
        return (self.__articulos_mes)
    def setCualificacion(self):
        print("Introduce cualificación para",self.nombre, ":")
        cualific = eval(input())
        if cualific == 1 or cualific == 2 or cualific == 3 or cualific == 4 or cualific == 5:
            super().setCualificacion(cualific)

def main():
    g = FichaFabricacion(78.5)
    g.nombre = "Elena"
    g.setCualificacion()
    print("La cualificación de", g.nombre, "es:",g.getCualificacion())

main()
