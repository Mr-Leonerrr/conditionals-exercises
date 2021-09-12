"""
En una fábrica de computadoras se planea ofrecer a los clientes un
descuento que dependerá del número de computadoras que compre.
Si las computadoras son menos de cinco se les dará un 10%
de descuento sobre el total de la compra; si el número de
computadoras es mayor o igual a cinco pero menos de diez se le
otorga un 20% de descuento; y si son 10 o más se les da un 40%. El
precio de cada computadora es de $11.000.

@author: Leonardo Natera
"""

print("CANTIDAD A COMPRAR")
computers = int(input("Ingrese el número de computadoras a comprar: "))

discount = 0.1
if(computers >= 5 and computers < 10): discount = 0.2
elif(computers >= 10): discount = 0.4

subtotal = computers * 11000
total_discount = subtotal * discount
total_pay = int(subtotal - total_discount)

print("\nRESULTADO")
print(f"Subtotal: ${subtotal:,}")
print(f"{int(discount * 100)}% Descuento: ${total_discount:,}")
print(f"Total: ${total_pay:,}")