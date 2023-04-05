'''
Llenar una lista con los numeros del 1 al 50,
luego mostrar la lista con un bucle for, los
elementos deben mostrarse de la manera
siguiente 1-2-3-4-5-...-50
'''
#Creamos la lista
lista = []
#Iniciamos en 1
i = 1
while i<=50:
    lista.append(i)
    i+=1

for i in lista:
    print(i,end="-")
