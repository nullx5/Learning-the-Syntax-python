﻿
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

class FichaTecnico(FichaEmpleado):
    def __init__(self):
        super().__init__()
        self.__estrellas = "*"

    def incEstrellas(self):
        self.__estrellas += "*"

    def disEstrellas(self):
        if self.__estrellas =="**":
                self.__estrellas ="*"
        if self.__estrellas =="***":
                self.__estrellas = "**"
        if self.__estrellas =="****":
                self.__estrellas = "***"
        if self.__estrellas =="*****":
                self.__estrellas = "****"

    def getEstrellas(self):
        return (self.__estrellas)

class FichaComercial(FichaEmpleado):
    def __init__(self):
        super().__init__()
        self.__cliente_principal = "TecnoWorld2000"
        self.__num_clientes = None

    def getCliente(self):
        return (self.__cliente_principal)

    def getNumClientes(self):
        return (self.__num_clientes)

    def setCliente(self, cli : str):
        self.__cliente_principal = cli

    def setNumClientes(self, num : int):
        self.__num_clientes = num

def main():
    c = FichaTecnico()
    c.nombre = "Mónica"
    c.edad = 32
    c.antiguedad = 12
    c.setCualificacion(4)
    print("El sueldo de", c.nombre, "es:",c.getSueldo())
    print("El número de estrellas inicial de", c.nombre, "es:", c.getEstrellas() )
    c.incEstrellas()
    c.incEstrellas()
    print("Tras dos incrementos, el número de estrellas de", c.nombre, "es:", c.getEstrellas() )
    c.disEstrellas()
    print("Tras un decremento, el número de estrellas de", c.nombre, "es:", c.getEstrellas(),"\n" )

    d = FichaComercial()
    d.nombre = "Eva"
    d.edad = 24
    d.antiguedad = 2
    d.setCualificacion(2)
    print("El sueldo de", d.nombre, "es:",d.getSueldo())
    print("El cliente principal inicial de", d.nombre, "es:", d.getCliente() )
    print("\nEmpleado/a : ", d.nombre)
    cliente = input("Introduce cliente principal:")
    d.setCliente(cliente)
    print("El cliente principal actual es:", d.getCliente() )
    numero_cli = eval(input("Introcude número de clientes"))
    d.setNumClientes(numero_cli)
    print("El número de clientes actuales es:", d.getNumClientes() )

main()