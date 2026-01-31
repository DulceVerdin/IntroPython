'''
pedir 5 sueldos agregar a lista e imprimir
'''

sueldos=[]
cont = 0
total = 0
promedio = 0

while cont<=4:
    tem=float(input("dame el sueldo"+str([cont+1])))
    sueldos.append(tem)
    cont+=1
    total += tem
    
print("Los sueldos son: ", str (sueldos))

promedio = promedio + total / 5

print("El promedio de los sueldos es: ", promedio)

Mayor=max(sueldos)
Menor=min(sueldos)
print("El sueldo mayor es: ",Mayor)
print("El sueldo menor es: ",Menor)



