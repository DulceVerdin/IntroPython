import os
op=0
while op!=5:
    os.system("cls")
    print("1.- suma\n2.- resta\n3.- multiplicacion\n4.- division\n5.- salir")
    op=int(input("seleccionauna opcion (1-5):"))
    if op==1:
        num1=int(input("ingresa el primer numero:"))
        num2=int(input("ingresa el segundo numero"))
        print("la suma de {}+{}".format(num1,num2,num1+num2))
        input("presiona Enter para continuar...")
    if op==2:
        num1=int(input("ingresa el primer numero:"))
        num2=int(input("ingresa el segundo numero"))
        print("la resta de {}-{}".format(num1,num2,num1-num2))
        input("presiona Enter para continuar...")
    if op==3:
        num1=int(input("ingresa el primer numero:"))
        num2=int(input("ingresa el segundo numero"))
        print("la multiplicacion de {}*{}".format(num1,num2,num1*num2))
        input("presiona Enter para continuar...")
    if op==4:
        num1=int(input("ingresa el primer numero:"))
        num2=int(input("ingresa el segundo numero"))
        print("la multiplicacion de {}/{}".format(num1,num2,num1/num2))
        input("presiona Enter para continuar...")
    else:
        print("error: No se puede dividir entre cero.")
        input("Presiona Enter para continuar...")