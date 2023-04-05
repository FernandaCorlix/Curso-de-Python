'''
Hacer un programa para ingresar el radio de un circulo y se
reporte su area  y la longitud de la circunferencia
'''
import math

radio = 0
area = 0
longitud = 0

radio = float(input("Ingresa el radio: "))

area = math.pi * radio**2

longitud = 2 * math.pi * radio

print(f"El radio es de: {radio}")
print(f"El area del circulo es de: {area}")
print(f"La longitud del circulo es de: {longitud}")


