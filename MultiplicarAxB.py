numA= int(input("Ingresa el primer numero: "))
numB= int(input("Ingresa el segundo numero: "))
resultado = 0
contador = 0
suma_str = ""

while contador < numB:
    resultado += numA
    suma_str += str(numA)
    if contador < numB - 1:
        suma_str += "+"
    contador += 1

print(f"{suma_str} = {resultado}")

