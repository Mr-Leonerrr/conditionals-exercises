"""
En un supermercado se hace una promoción, mediante  la  cual  el
cliente obtiene  un  descuento  dependiendo  de un  número  que  se
escoge al azar. Si el número escogido es menor que 74 el descuento
es del  15%  sobre  el  total  de  la  compra,  si es mayor  o  igual  a  74  el
descuento es del 20%. Obtener cuanto dinero se le descuenta.

@author: Leonardo Natera
"""
import random

number = random.randint(1, 99)
total_purchase = float(input("Ingrese el valor total de la compra: "))

discount = 0.15
if(number >= 74): discount = 0.20

total_discount = total_purchase * discount
total_pay = total_purchase - total_discount

print(f"\nRandom number: {number}")
print(f"Subtotal: ${total_purchase:,}")
print(f"%{int(discount * 100)} Discount: ${total_discount:,}")
print(f"Total: ${total_pay:,}")