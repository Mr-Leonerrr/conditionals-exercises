"""
Una persona se encuentra con un problema de comprar un automóvil o un terreno, los cuales cuestan exactamente lo mismo.
Sabe que mientras el automóvil se devalúa, con el terreno sucede lo contrario.
Esta persona comprará el automóvil si al cabo de tres años la devaluación de este no es mayor que la mitad del incremento del valor del terreno. Ayúdale a esta persona a determinar si debe o no comprar el automóvil.

@author: Leonardo Natera
"""

print("PRECIOS")
price = float(input("Ingrese el precio del terreno y automóvil: $"))

print("\nINCREMENTO Y DEVALUACIÓN ANUAL")
annual_increase = float(input("Ingrese el incremento anual del terreno: %"))
annual_devaluation = float(input("Ingrese la devaluación anual del automóvil: %"))

increase = (((price * annual_increase) / 100) * 3) / 2
devaluation = ((price * annual_devaluation) / 100) * 3

print(f"\nLa mitad del incremento de la casa en 3 años es: ${increase:,}")
print(f"La devaluación del automóvil en 3 años es: ${devaluation:,}")

if (devaluation < increase): print("🚗 Es conveniente comprar el automóvil.")
else: print("🌱 Es conveniente comprar el terreno.")
