
class exceso_peso(RuntimeError):
    def __init__(self, suma):
        super().__init__()
        self.cantidad = suma

try:
    num1 = eval(input("Introzca el peso del objeto 1:"))
    num2 = eval(input("Introzca el peso del objeto 2:"))

    total = num1 + num2
    if (total) > 100:
        raise exceso_peso(total)
except exceso_peso as obj_error:
    print("No se han guardado los datos.")
    print("Motivo: El peso total excede el valor máximo (100kg) en",obj_error.cantidad-100,"Kg.")
except:
    print("Los datos no se han introducido correctamente y no se han guardado.")
else:
    print("Los datos han sido correctamente guardados.")
finally:
    print("Cláusula finally ejecutada correctamente.")

print("Seguimos son el flujo del programa.")