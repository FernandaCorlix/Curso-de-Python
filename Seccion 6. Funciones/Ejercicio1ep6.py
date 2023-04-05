'''
Desarrollar un programa que pueda calcular el valor
del tipo de cambio de moneda (de tu moneda - hacia dolar y viceversa
'''

def cambio_pesos_a_dolares(pesos):
    return pesos/18
def cambio_dolares_a_pesos(dolar):
    return dolar*18

while True:
    print("""\t.:Menu:. 
    1. Convertir de Pesos a Dolares 
    2. Convertir de Dolares a Pesos
    3. Salir""")
    opcion = int(input("Digite una opcion:\n "))
    print()

    if opcion == 1:
        pesos = float(input("Digite la cantidad de pesos:\n"))
        cambio_pesos_a_dolares(pesos)
        print(f"La conversion es de {cambio_pesos_a_dolares(pesos)}\n")
    elif opcion == 2:
        dolares = float(input("Digite la cantidad de dolares:\n"))
        cambio_dolares_a_pesos(dolares)
        print(f"La conversion es de {cambio_dolares_a_pesos(dolares)}\n")
    elif opcion == 3:
        print("Adios")
        break

