"""
Una compañía de seguros está abriendo un departamento de
finanzas y estableció un programa para captar clientes, que consiste
en lo siguiente: Si el monto por el que se efectúa la fianza es menor
que $50.000 la cuota a pagar será por el 3% del monto, y si el monto
es mayor que $50.000 la cuota a pagar será el 2% del monto. La
afianzadora desea determinar cual será la cuota que debe pagar al
cliente.

@author: Leonardo Natera
"""

amount = float(input("Ingrese el monto de la fianza: "))
if(amount <= 0):
    print("⛔️ El monto ingresado no es válido")
    exit()

additional = 0.03
if(amount >= 5e4): additional = 0.02

quota_value = amount * additional

print(f"\nValor de la Cuota: ${quota_value:,}")