"""
Una empresa quiere hacer una compra de varias piezas de la misma
clase a una fábrica de refacciones. La empresa, dependiendo del
monto total de la compra, decidirá que hacer para pagar al fabricante.
Si el monto total de la compra excede de $500.000 la empresa tendrá
la capacidad de invertir de su propio dinero un 55% del monto de la
compra, pedir prestado al banco un 30% y el resto lo pagará
solicitando un crédito al fabricante. Si el monto total de la compra no
excede de $500.00 la empresa tendrá capacidad de invertir de su
propio dinero un 70% y el restante 30% lo pagará solicitando crédito
al fabricante.
El fabricante cobra por concepto de interes un 20% sobre la cantidad que se le pague a crédito.
Obtener la cantidad a invertir, valor del préstamo, valor del crédito y los intereses.

@author: Leonardo Natera
"""

print("TOTAL PIEZAS")
pieces = int(input("Ingrese el total de piezas a comprar: "))
price = float(input("Ingrese el valor de cada pieza: $"))

subtotal = pieces * price

bank = 0
if(subtotal > 5e5): # 5e5 = 500.000
    investment = subtotal * 0.55
    bank = subtotal * 0.30
    credit = subtotal * 0.15
else:
    investment = subtotal * 0.70
    credit = subtotal * 0.30

interests = credit * 0.20

print("\nRESULTADO")
print(f"Cantidad a invertir: ${round(investment):,}")
if(bank > 0): print(f"Valor préstamo del banco: ${bank:,}")
print(f"El crédito a pagar es de: ${credit:,}")
print(f"El dinero a pagar por intereses del crédito es: ${interests:,}")
