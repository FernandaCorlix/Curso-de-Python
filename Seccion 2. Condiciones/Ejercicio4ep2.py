'''

Construir un programa que simule el funcionamiento de
una calculadora que pueda realizar las cuatro operaciones
aritmeticas basicas ( suma, resta, multiplicacion, division).
El usuario debe especificar la operacion con el
primer caracter del nombre de la operacion

S , s -Suma
R, r - Resta
P, p, M, m - Multiplicacion
D, d - Division

'''

Letra = input("Ingresa la letra de la operacion que desees realizar\nS,s -Suma\nR,r -Resta"
                  "\nP, p M, m -Multiplicacion\nD,d -Division\n")

if Letra == "S" or Letra == "s":
    print("*** Vas a realizar suma ***")
    num1 = int(input("Ingresa un numero: "))
    num2 = int(input("Ingresa un numero: "))
    suma = num1 + num2
    print(f"La suma de {num1} + {num2} = {suma} ")

if Letra == "R" or Letra == "r":
    print("*** Vas a realizar resta ***")
    num1 = int(input("Ingresa un numero: "))
    num2 = int(input("Ingresa un numero: "))
    resta = num1 - num2
    print(f"La suma de {num1} - {num2} = {resta} ")

if Letra == "P" or Letra == "p" or Letra == "M" or Letra == "m":
    print("*** Vas a realizar multiplicacion ***")
    num1 = int(input("Ingresa un numero: "))
    num2 = int(input("Ingresa un numero: "))
    Multiplicacion = num1 * num2
    print(f"La suma de {num1} * {num2} = {Multiplicacion} ")

if Letra == "D" or Letra == "d":
    print("*** Vas a realizar una division ***")
    num1 = float(input("Ingresa un numero: "))
    num2 = float(input("Ingresa un numero: "))
    division = num1 / num2
    print(f"La division de {num1} / {num2} = {division} ")




