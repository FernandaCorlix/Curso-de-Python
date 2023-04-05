'''
Hacer un programa donde el usuario ingrese una frase. se le devolvera la misma frase
pero sin espacios en blanco y ademas un contador de cuantos caracterres tiene la frase
(sin contar los espacios en blanco)

'''

frase = input("Digita una frase: ")
frase2 = ""
contador = 0

for i in frase:
    if i != " ":
        frase2 += i

frase = frase2

print(f"\nLa frase sin espacios es {frase}")
print(f"Numero de caracteres: {len(frase)}")