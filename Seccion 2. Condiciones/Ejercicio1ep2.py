'''
Hacer un programa que pida 2 numeros y se de cuenta cual
de ellos es par, o si ambos lo son
'''

numero1 = int(input("Digite un numero: "))
numero2 = int(input("Digite otro numero:"))

if numero2 %2==0 and numero1%2==0 :
    print(f"Los numeros {numero1} y {numero2} ambos son pares")
elif numero2 % 2 != 0 and numero1 % 2 == 0:
    print(f"El {numero1} es par")
elif numero2 % 2 == 0 and numero1 % 2 != 0:
    print(f"El {numero2} es par")

else:
    print("Ninguno es par")