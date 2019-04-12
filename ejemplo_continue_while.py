
suma = 0
i = 0
while i < 10 :
   i = i + 1
   suma = suma + i
print ("La suma del 1 al 10 inclusive es: ", suma)
suma = 0
i = 0
while i < 10 :
   i = i + 1
   if i % 4 == 0:
        continue
   suma = suma + i
print("La suma del 1 al 10 inclusive salvo los múltiplos de 4 es:", suma)
