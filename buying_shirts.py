"""
Hacer un algoritmo que calcule el total a pagar por la compra de
camisas. Si se compran tres camisas o mas se aplica un descuento
del 30% sobre el total de la compra y si son menos de tres camisas
un descuento del 10%.

@author: Leonardo Natera
"""

shirts = int(input("Ingrese la cantidad de camisetas a comprar: "))
if(shirts <= 0):
    print("Debe comprar al menos una camiseta para continuar")
    exit()

discount = 0.1
if(shirts >= 3): discount = 0.3

shirts_price = float(input("Ingrese el valor de las camisetas: "))

subtotal = shirts_price * shirts
total_discount = subtotal * discount
total_pay = subtotal - total_discount

print(f"\nSubtotal: ${subtotal:,}")
print(f"Discount: ${total_discount:,}")
print(f"Total: ${total_pay:,}")