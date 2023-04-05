'''
Hacer un programa para detectar si una frase introducida por el usuario
finaliza con un punto "." o no, Deberas imprimir por la consola una de las siguientes
opciones:
"Termina con un punto" o por el contrario "No termina con un punto"
'''

cadena = input("Ingresa una palabra: \n")

if cadena.endswith('.'):
    print(f"La palabra {cadena} termina con un punto")
else:
    print("No termina con un punto")
