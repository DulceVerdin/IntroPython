contador=1
suma = 0

while contador <= 5:
    calificacion =int(input("ingrese la calificacion{}:"))
    suma+= calificacion
    contador += 1
promedio = suma / 5
print("El promedio de las 5 calificaciones es:",promedio)


