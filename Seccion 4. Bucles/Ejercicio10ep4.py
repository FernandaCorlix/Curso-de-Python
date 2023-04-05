'''
Hacer un programa que pida una cadena por teclado, luego meta los caracteres en una lista sin repetir
caracteres
'''

cadena = input("Digite la cadena: ")

lista = []

for i in cadena:
    if i not in lista: #Si el caracter aun no esta en la lista
        lista.append(i) #Lo agregamos en el la lista


print(f"La cadena en la lista quedo: {lista}")

