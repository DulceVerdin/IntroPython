 mimportath, os


os.system("cls")


print("+-----Grupos  ICO201-9, ICO201 ")


num1=input("ingrese el primer numero:")
num2=input("ingreseel segundo numero:")

suma=int(num1) +int(num2)
print("la suma es: ", suma)

resta = num1 - num2 
print("la resta de {} - {} = {}".format(num1, num2,resta))
multiplicacion = num1 * num2
print("la multiplicacion de {} * {}= {}".format(num1, num2,multiplicacion))
division = num1 / num2
print("la division de {} / {}= {}".format(num1, num2,division ))

potencia = num1 ** num2


print("la potencia de{} con {} es:{}".format(num1, num2, potencia))

print("Operaciones basicas:\n1.- Suma\n2.- Resta\n3.- Multiplicacion\n4.- Division\n")
opcion=input("ingresela opcion a realizar (1/2/3/4):")

val1=3
val2=5

temp=val1>val2
temp=val1<val2
temp=val1==val2
temp=val1<=val2
temp=val1>=val2
temp=val1!=val2

print("El valor de la comperacion")

print("El valor de la comparacion es: ", temp)
tem2= not(val1>val2) and (val1<val2)

print("El valor de la comparacion con NOT es: ", tem2)