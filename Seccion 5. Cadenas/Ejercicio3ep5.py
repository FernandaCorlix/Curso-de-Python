'''
Hacer un programa que determine si una palabra o frase es palindroma.
Una cadena palindroma se lee igual de izquierda a derecha de derecha a izquierda
'''

cadena = input("Digite una frase: ")

#Le quitamos los espacios en blanoc
cadena = cadena.replace(" ","")
#Invertimos la cadena
cadena2 = cadena[::-1]

print(f"La cadena invertida es: {cadena2}")

if cadena == cadena2:
    print("La cadena es un palindromo")
else:
    print("La cadena no es palindromo")
