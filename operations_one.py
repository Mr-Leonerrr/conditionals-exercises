"""
Leer 2 números; si son iguales que los multiplique, si el primero es
mayor que el segundo que los reste y sino que los sume.

@author: Leonardo Natera
"""

first_number = float(input("Ingrese el primer número: "))
second_number = float(input("Ingrese el segundo número: "))

print(f"\nNúmeros ingresados: {first_number} y {second_number}")

print("\nRESULTADO")

if(first_number == second_number):
    result = first_number * second_number
    print(f"{first_number} es igual a {second_number}, su producto es: {result}")
elif(first_number > second_number):
    result = first_number - second_number
    print(f"{first_number} es mayor a {second_number}, su resta es: {result}")
else:
    result = first_number + second_number
    print(f"{first_number} es menor a {second_number}, su suma es: {result}")
