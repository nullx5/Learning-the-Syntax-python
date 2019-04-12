
milista = []
for i in range(5):
    dato = input()
    milista.append(dato)

todos_los_datos = input()
datos = todos_los_datos.split()
milista_2 = [eval(x) for x in datos]

for i in range(5):
    print(milista[i]," ",end='')

print("")

for i in range(len(milista_2)):
    print(milista_2[i]," ",end='')