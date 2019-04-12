import random
import time
aciertos = 0
num_elementos = eval(input("Introduce número de elementos de la lista original:"))
milista = list(range(num_elementos))
print("Desordenando lista")
random.shuffle(milista)
print("Fin de desordenacion de la lista\n")

miconjunto = set(milista)
mitupla = tuple(milista)
midiccionario = {}.fromkeys(milista, 1)

inicio_tiempo = time.time()
for i in range(num_elementos):
    if i in milista: aciertos += 1
fin_tiempo = time.time()
tiempo_computo = int((fin_tiempo - inicio_tiempo) * 1000)
print(tiempo_computo, "milisegundos para testear", num_elementos, "elementos mediante listas")
print("Aciertos = ", aciertos, "\n")

aciertos = 0
inicio_tiempo = time.time()
for i in range(num_elementos):
    if i in mitupla: aciertos += 1
fin_tiempo = time.time()
tiempo_computo = int((fin_tiempo - inicio_tiempo) * 1000)
print(tiempo_computo, "milisegundos para testear", num_elementos, "elementos mediante tuplas")
print("Aciertos = ", aciertos, "\n")

aciertos = 0
inicio_tiempo = time.time()
for i in range(num_elementos):
    if i in miconjunto: aciertos += 1
fin_tiempo = time.time()
tiempo_computo = int((fin_tiempo - inicio_tiempo) * 1000)
print(tiempo_computo, "milisegundos para testear", num_elementos, "elementos mediante conjuntos")
print("Aciertos = ", aciertos, "\n")

aciertos = 0
inicio_tiempo = time.time()
for i in range(num_elementos):
    if i in midiccionario : aciertos += 1
fin_tiempo = time.time()
tiempo_computo = int((fin_tiempo - inicio_tiempo) * 1000)
print(tiempo_computo, "milisegundos para testear", num_elementos, "elementos mediante diccionario")
print("Aciertos = ", aciertos, "\n")


