'''
Hacer un programa que identifique cuales son las vocales
'''

vocal = input("Ingresa una letra: ")

if vocal == "A" or vocal =="E" or vocal =="I" or vocal == "O" or vocal == "U" or \
        vocal == "a" or vocal == "e" or vocal == "i" or vocal == "o" or vocal == "u":
    print(f"Ingresaste la vocal {vocal}")
else:
    print(f"La letra {vocal} no es una vocal")