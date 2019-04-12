
try:
    a = 10
    a = al + 1
    b = 1 /0
    print("El valor de a es:", a)
except BaseException as obj_error:
    print("Error en la ejecución")
    print("Motivo del error: ",obj_error)
else:
    print("Bloque try ejecutado sin problemas")
finally:
    print("Bloque finally ejecutado")

print("Seguimos con el programa")