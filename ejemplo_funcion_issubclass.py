
from libreria_personal_1 import *

class FichaDirectivo:
    def __init__(self, codigo: str):
        self.codigosecreto = codigo

class FichaDirectivo2(FichaDirectivo):
    def __init__(self, codigo: str, bonificacion : bool):
        super().__init__(codigo)
        self.bonificacion = bonificacion

def dar_datos(objeto):
    if issubclass(type(objeto), FichaEmpleado):
        print("Nombre: ", objeto.nombre)
        print("Cualificación: ", objeto.getCualificacion())
        if isinstance(objeto, FichaFabricacion):
            print("Media de artículos manufacturados al mes:", objeto.articulos_mes)
        elif isinstance(objeto, FichaTecnico):
            print("Número de estrellas del departamento técnico:", objeto.estrellas)
    elif issubclass(type(objeto), FichaDirectivo):
        print("El código secreto del directivo es: ", objeto.codigosecreto)
    print("")

def main():
    a = FichaEmpleado("Pepe")
    b = FichaFabricacion("Juan", 10)
    c = FichaTecnico("Javier")
    d = FichaDirectivo("BGD21")
    e = FichaDirectivo2("HJB98", True)
    inicializar_cualificacion(a)
    inicializar_cualificacion(b)
    inicializar_cualificacion(c)
    dar_datos(a)
    dar_datos(b)
    dar_datos(c)
    dar_datos(d)
    dar_datos(e)

main()
