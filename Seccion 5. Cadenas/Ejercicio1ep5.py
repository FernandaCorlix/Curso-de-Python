'''
Hacer un programa donde se debera imprimir por la consola
la palabra con mas caracteres de dos palabras dadas. En el caso de que ambas
palabras tengan la misma cantidad de caracteres, deberas mostrar el mensaje
"Son iguales"
'''

cadena1 = input("Digita una palabra: ")
cadena2 = input("Digita otra palabra: ")


if len(cadena1) > len(cadena2):
    print(f"La palabra {cadena1} es mas larga")
elif len(cadena2) > len(cadena1):
    print(f"La palabra {cadena2} es mas larga")
else:
    print("Son iguales")

