import math, os

os.system("cls")

print("Operaciones:\n1.- triangulo\n2.- cuadrado\n3.-circulo\n4.-pentagono\n5.-sali\n")

opcion = int(input("Seleccione alguna de las opciones (anteriores): "))

if opcion == 1:
    num1 = int(input("Ingrese el primer numero: "))
    num2 = int(input("Ingrese el segundo numero: "))
    area = num1 * num2/2
    print ("El resultado de la area es :", area)

if opcion == 2:
    num1 = int(input("Ingrese el primer numero: "))
    num2 = int(input("Ingrese el segundo numero: "))
    area = num1 * num2
    print ("El resultado de la area es: ", area)

if opcion == 3:
    num1 = int(input("Ingrese el primer numero: "))
    area = 3.1416 * num1*num1 
    print ("El resultado de la area es: ", area)

if opcion == 4:
    num1 = int(input("Ingrese el primer numero: "))
    num2 = int(input("Ingrese el segundo numero: "))
    area= num1 * num2/2
    print ("El resultado de la area es: ", area)

if opcion == 5:
    int(input("salir: "))
    opcion = int(input("Seleccione alguna de las opciones (anteriores): "))


