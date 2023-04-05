'''
Hacer un programa donde se reemplacen, todos los espacios de una cadena por asteriscos y ademas cada palabra comience
por mayusculas
'''

cadena = input("Ingresa una cadena: ")


cadena = cadena.replace(" ","*")
cadena = cadena.title()

print(cadena)