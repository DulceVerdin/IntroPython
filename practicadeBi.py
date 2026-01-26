import os
num= int(input("Ingresa un numero entre 1 y 100:"))
while num < 1 or num > 100:
    print("Numero no  valido")
    num= int(input("Ingresa de nuevo un numero entre 1 y 100"))
print("Numero valido:numero")
if num == -7 or num < 1 or num > 100:
        print("Número no válido")
binario = 0
potencia = 1
while num > 0:
    resto = num % 2
    binario = binario + resto * potencia
    potencia = potencia * 10
    num = num // 2
print("El número en binario es:", binario)