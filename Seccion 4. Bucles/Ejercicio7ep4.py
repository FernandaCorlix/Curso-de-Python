'''
Realizar un juego para adivinar un numero. Para ello generar un numero aleatorio entre 0 - 100
luego ir pidiendo numeros indicando si es mayor o menor, segun sea mayor  o menor con respecto a N.
El proceso termina cuando el usuario acierta y mostrar el numero de intentos

'''
import random

intentos = 0
contador = 0
aleatorio = random.randint(0,100) #Aqui se genera un numero aleatorio

print("\t.:Juego adivina el numero:.")

while True:
    numero = int(input("Digite un numero: "))
    contador += 1
    if numero > aleatorio:
        print("\tNo es el numero, digita un numero menor")
    elif numero < aleatorio:
        print("\tNo es el numero, digita un numero mayor")
    else:
        print("\t**Felicidades, Adivinaste el numero**")
        break

print(f"\n Numero de intentos: {contador}")


