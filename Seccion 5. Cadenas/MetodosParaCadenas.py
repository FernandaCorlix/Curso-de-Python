
cadena = "Hola mundo"


'''
#Con el upper se pone todo en mayuscula
'''
print(cadena.upper())

#El capitalize te pone la primer letra en mayuscula
cadena2 = "hola mundo".capitalize()

print(cadena2)

#Se pone en mayusculas la primera letra de cada palabra
cadena3 = "hola mundo".title()

print(cadena3)

#Con esto te cuenta, cuantas veces salio una letra en este caso o salio 2 veces
#Tambien se puede hacer con palabras largas tipo 'Hola'
cadena4 = "Hola mundo".count('o')

print(cadena4)

#Con el metodo find te busca un caracter

cadena5 = "s Hola mundo mundo mundo s".find('s')
print(cadena5)

#Con el .rfind te dice la ultima coincidencia

cadena5 = "s Hola mundo mundo mundo s".rfind('u')
print(cadena5)

#Con el isdigit pregunta si son todos los caracteres numericos y te regresa un true o un false

n = "1000".isdigit()

print(n)

#Comprueba si todos los caracteres son alfabeticos
n = "Aaa".isalpha()
print(n)

#Comprueba si tienes caracteres alfabeticos o numericos
n = "1000aAaa".isalnum()
print(n)

#Te dice si esta todoo en minuscula
n = "aaaaa".islower()
print(n)

#Te dice si esta todoo en mayuscula
n = "AAA".isupper()
print(n)
#Te dice si es un titulo
n = "hola mundo".istitle()
print(n)

#Te dice si la cadena esta compuesta por espacios

cadena = "      ".isspace()
print(cadena)

#Metodo para retornar un valor booleano

cadena = "hola mundo".startswith('h')
print(cadena) #Te dice si la cadena empieza con h y te da un true

#Su contrario seria el .endswith
cadena = "hola mundo".endswith('o')
print(cadena)

print("---")

#Te separa los elementos en una lista
cadena = "hola mundo".split()
print(cadena)

#El metodo join te los separa y con lo que le pongas

cadena = "->".join("Fernanda")
print(cadena)

#te quita los espacios inecesarios

cadena = "     Arbol de manzanas".strip()
print(cadena)

#El metodo replace

cadena = "Hola mundo".replace('o','O')

print(cadena)
