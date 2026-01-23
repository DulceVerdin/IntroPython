import math, os

os.system("cls")

print("Operaciones:\n1.- suma\n2.- resta\n3.- multiplicacion\n4.-divison\n")

opcion = int(input("Seleccione alguna de las opciones (anteriores): "))

if opcion == 1:
    num1 = int(input("Ingrese el primer numero: "))
    num2 = int(input("Ingrese el segundo numero: "))
    sum = num1 + num2
    print ("El resultado de la suma es :", sum)

if opcion == 2:
    num1 = int(input("Ingrese el primer numero: "))
    num2 = int(input("Ingrese el segundo numero: "))
    resta = num1 - num2
    print ("El resultado de la resta es: ", resta)

if opcion == 3:
    num1 = int(input("Ingrese el primer numero: "))
    num2 = int(input("Ingrese el segundo numero: "))
    multiplicacion = num1 * num2
    print ("El resultado de la multiplicacion es: ", multiplicacion)

if opcion == 4:
    num1 = int(input("Ingrese el primer numero: "))
    num2 = int(input("Ingrese el segundo numero: "))
    division = num1 / num2
    print ("El resultado de la resta es: ", division)
    opcion = int(input("Seleccione alguna de las opciones (1,2,3,4): "))


