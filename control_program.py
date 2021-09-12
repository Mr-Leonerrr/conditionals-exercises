"""
Una fábrica ha sido sometida a un programa de control de contaminación
para lo cual se efectúa una revisión de los puntos de contaminación generados por la fábrica.
El programa de control de contaminación consiste en medir los puntos que emite la fábrica
en cinco días de una semana y si el promedio es superior a los 170 puntos
entonces tendrá la sanción de parar su producción por una semana
y una multa del 50% de las ganancias diarias cuando no se detiene la producción.
Si el promedio obtenido de puntos es de 170 o menos entonces no tendrá ni sanción ni multa.
El dueño de la fábrica desea saber cuanto dinero perderá después de ser sometido a la revisión.

@author: Leonardo Natera
"""

print("MEDICIONES")
day_one = float(input("Ingrese la medición para el 1er día: "))
day_two = float(input("Ingrese la medición para el 2do día: "))
day_three = float(input("Ingrese la medición para el 3er día: "))
day_four = float(input("Ingrese la medición para el 4to día: "))
day_five = float(input("Ingrese la medición para el 5to día: "))

average = (day_one + day_two + day_three + day_four + day_five) / 5

print("\nGANANCIAS")
day_one_earnings = float(input("Ingrese las ganancias para el 1er día: $"))
day_two_earnings = float(input("Ingrese las ganancias para el 2do día: $"))
day_three_earnings = float(input("Ingrese las ganancias para el 3er día: $"))
day_four_earnings = float(input("Ingrese las ganancias para el 4to día: $"))
day_five_earnings = float(input("Ingrese las ganancias para el 5to día: $"))

total_earnings = day_one_earnings + day_two_earnings + \
    day_three_earnings + day_four_earnings + day_five_earnings

penalty_fee = 0
if (average > 170): penalty_fee = total_earnings * 0.5

print("\nRESULTADOS")
print(f"El promedio de las mediciones es: {average} puntos")
print(f"Ganancias totales de la semana: ${total_earnings:,}")
print(f"Perdidas por la revisión: ${penalty_fee:,}")
