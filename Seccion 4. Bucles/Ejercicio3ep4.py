'''
Pide numeros y metelos en una lista, cuando el usuario meta un 0 ya dejaremos de
insertar. Por ultimo, muestra los numeros ordenados de menor a mayor
'''

lista = []

salir = False;

'''Mientras no salir'''
while not salir:
    numero = int(input("Digite un numero: "))
    if numero==0:
        salir=True
    else:
        lista.append(numero)

'''Mostrar los numeros de mayor a menor'''

lista.sort()

print(f"La lista ordenada: \n{lista}")

