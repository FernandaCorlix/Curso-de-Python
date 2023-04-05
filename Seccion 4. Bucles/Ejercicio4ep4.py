'''
Hacer un programa para sumar numeros pares dentro de un rango
Ejemplo suma numeros pares del 2 - 30
suma = 240
'''

a = int(input("Digite de donde se empieza a sumar: "))
b = int(input("Digite hasta donde quiere dejar de sumar: "))

suma = 0
for i in range(a,b+1):
    if i%2==0: #Si el numero es par
        suma += i

print(f"\nLa suma es: {suma}")