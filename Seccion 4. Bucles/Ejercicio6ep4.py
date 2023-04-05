'''
Hacer un programa que pida un numero por teclado y guarde en una lista su tabla de  multiplicar hasta el 10
Por ejemplo:
Si se digita el 5 la lista tendria 5,10,15,20,25,30,35,40,45
'''

numero = int(input("Digite un numero:  "))

lista = []

#Aqui ya tenemos la lista
for i in range(1,10):
    lista.append(i*numero)

print(f"\nLa tabla de multiplicar es {lista}")