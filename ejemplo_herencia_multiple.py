
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

class FichaTecnicoYComercial(FichaTecnico, FichaComercial):
        def __init__(self):
            super().__init__()
            self.horasdetecnico = None
            self.horasdecomercial = None

def main():
    e = FichaTecnicoYComercial()
    e.nombre = "Carlos"
    e.edad = 48
    e.antiguedad = 15
    e.setCualificacion(4)
    print("Empleado:", e.nombre)
    print("\tSueldo:", e.getSueldo())
    print("\tNúmero de estrellas:", e.getEstrellas() )
    print("\tCliente principal:", e.getCliente() )
    e.setNumClientes(78)
    print("\tNúmero de clientes:", e.getNumClientes() )
    e.horasdetecnico = 54
    e.horasdecomercial = 42
    print("\t", e.horasdetecnico, " horas de técnico y ", \
    e.horasdecomercial, " horas de comercial", sep='')

main()

