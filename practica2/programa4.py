"""
Docstring for programa4
"""

sueldo = int(input("Ingrese el sueldo de la persona: "))

if sueldo < 1000:
    impuesto = 0
else:
    if sueldo <= 2000 :
        impuesto = sueldo * 0.10
        neto = sueldo - impuesto
    else:
        impuesto = sueldo * 0.20
        neto= sueldo - impuesto

print("Impuesto a pagar:", impuesto)
print("Sueldo neto después de impuestos:", neto)


