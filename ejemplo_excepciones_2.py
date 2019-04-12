
try:
    a = 10
    a = al + 1
    print("El valor de a es:", a)
except NameError:
    print("Error en el nombre de alguna variable")
except:
    print("Error genérico")
else:
    print("Bloque try ejecutado sin problemas")
finally:
    print("Bloque finally ejecutado")

print("Seguimos con el programa")