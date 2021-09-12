"""
Un proveedor de estéreos ofrece un descuento del 10% sobre el
precio sin IVA, de algún aparato si este cuesta $2000 o más.
Además, independientemente de esto, ofrece un 5% de descuento si la marca es NOSY.
Determinar cuanto pagará, con IVA incluido, un cliente cualquiera por la compra de su aparato. IVA es del 16%.

@author: Leonardo Natera
"""

print("VALOR DEL ESTÉREO")
price = float(input("Ingrese el valor del estéreo: $"))
brand = input("¿Qué marca es el estéreo?: ")

vat = 0.16
discount = 0
if(brand.lower().strip() == "nosy" and price >= 2000): discount = 0.15
elif(price >= 2000): discount = 0.1

total_discount = round(price * discount)
subtotal = int(price - total_discount)
total_with_vat = round(subtotal * 0.16)
to_pay = subtotal + total_with_vat

print("\nRESULTADO")
print(f"Subtotal: ${price:,}")
if(discount > 0.1): print(f"{int(discount * 100)}% Descuento: ${total_discount:,}")
print(f"El IVA aplicado es: ${total_with_vat:,}")
print(f"Total: ${to_pay:,}")
