"""
Leer tres números diferentes e imprimir el número mayor de los tres.

@author: Leonardo Natera
"""

first_number = float(input("Ingrese el primer número: "))
second_number = float(input("Ingrese el segundo número: "))
third_number = float(input("Ingrese el tercer número: "))

print(f"\nNÚMEROS INGRESADOS: \n{first_number}, {second_number} y {third_number}")

print("\nRESULTADO")
if(first_number > second_number):
    if(first_number > third_number):
        print(f"El número mayor es {first_number}")
    else: print(f"El número mayor es {third_number}")
elif(second_number > third_number): print(f"El número mayor es {second_number}")
else: print(f"El número mayor es {third_number}")