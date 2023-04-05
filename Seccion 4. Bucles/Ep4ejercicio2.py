'''
Llenar una lista con los numeros del 1 al 10.
luego modificar los elementos de la lista
multiplicandolos por un valor que el usuario
digite
'''

lista =list(range(1,11))

print("Lista original ")

for i in lista:
    print(i,end="-")

valor = int(input("\nDigite un valor a multiplicar"))

#Multiplicar todos los elementos de la lista
indice = 0
for i in lista:
    lista[indice] *= valor
    indice+= 1

print(f"\nLista final con los elementos multiplicados por: {valor}")
for i in lista:
    print(i,end="-")