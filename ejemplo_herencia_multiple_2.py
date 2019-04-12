
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

class FichaFabricacion(FichaEmpleado):
    def __init__(self, art_mes : float):
        super().__init__("***")
        self.__articulos_mes = art_mes
    def incArticulos(self, suma : float):
        self.__articulos_mes += suma
    def getArticulos(self):
        return (self.__articulos_mes)

class FichaTecnico(FichaEmpleado):
    def __init__(self, num_estrellas : str):
        super().__init__()
        self.__estrellas = num_estrellas
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

class FichaTodosDepartamentos(FichaFabricacion, FichaTecnico, FichaComercial):
        def __init__(self):
            super().__init__(10.5)
            self.horasdefabrica = 0.0
            self.horasdecomercial = 0.0
            self.horasdecomercial = 0.0

def main():
    f = FichaTodosDepartamentos()
    f.nombre = "Ana"
    f.edad = 41
    f.antiguedad = 12
    f.setCualificacion(5)
    print("Empleado:", f.nombre)
    print("\tMedia artículos manufacturados al mes :", f.getArticulos())
    print("\tSueldo:", f.getSueldo())
    print("\tNúmero de estrellas:", f.getEstrellas() )
    print("\tCliente principal:", f.getCliente() )
    f.setNumClientes(78)
    print("\tNúmero de clientes:", f.getNumClientes() )
    f.horasdefabrica = 15.5
    f.horasdetecnico = 54.8
    f.horasdecomercial = 42.4
    print("\t", f.horasdefabrica, " horas de fábrica, ", \
    f.horasdetecnico, " horas de tecnico y ", \
    f.horasdecomercial, " horas de comercial", sep='')

main()

