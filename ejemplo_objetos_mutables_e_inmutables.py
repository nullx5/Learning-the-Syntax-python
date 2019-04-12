
class FichaEmpleado:
    def __init__(self):
        self.nombre = None
        self.edad = None
        self.antiguedad = None
        self.__cualificacion = None
    def __sueldo(self):
        return(1000 + self.antiguedad * 25 + self.__cualificacion * 100)
    def setCualificacion(self, cualif:int):
        if cualif == 1 or cualif == 2 or cualif == 3 or cualif == 4 or cualif == 5:
            self.__cualificacion = cualif
    def getCualificacion(self):
        return(self.__cualificacion)
    def getSueldo(self):
        return(self.__sueldo())

def aumentaAntiguedad(objeto, antiguedad):
    objeto.antiguedad += 1
    antiguedad += 1

def main():
    a = FichaEmpleado()
    a.nombre = "Javier"
    a.edad = 21
    a.setCualificacion(3)
    antiguedad = eval(input("Introduce la  de Javier: "))
    a.antiguedad = antiguedad
    print("Antes del aumento de antigüedad, el campo antiguedad para Javier es:   ", a.antiguedad, \
    " y la variable antiguedad es: ", antiguedad)

    aumentaAntiguedad(a, antiguedad)

    print("Después del aumento de antigüedad, el campo antiguedad para Javier es: ", a.antiguedad, \
    " y la variable antiguedad es: ", antiguedad)

main()
