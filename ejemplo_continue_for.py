
suma = 0
for i in range(101):
    if i == 3 or i == 19 or i == 32:
        continue
    suma = suma + i
print ("La suma con continue (sin sumar 3, 19 y 32) ha sido: ", suma)
suma = 0

for i in range(101):
    suma = suma + i
print ("La suma sin continue (sumando todos) ha sido: ", suma)
