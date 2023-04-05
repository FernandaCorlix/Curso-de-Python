
#Escribir la siguiente expresion en forma de expresion algoritmica

a = 0
b = 0
c = 0

a = float(input("Digita un numero: "))
b = float(input("Digita un numero: "))
c = float(input("Digita un numero: "))

resultado = (a**3 * (b**2 - 2*a*c))/(2*b)

print(f"El resultado es : {resultado}")