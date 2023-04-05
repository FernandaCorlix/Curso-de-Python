'''
Hacer un programa que simule un cajero automatico con un saldo inicial de 1000$ y entra el siguiente menu
de opciones:

1. Ingresar dinero en la cuenta
2. Retirar dinero de la cuenta
3. Mostrar dinero disponible
4. Salir
'''

saldo_inicial = 1000

while True:
    print("\n")
    print("\t.:Menu:.")
    print("1. Ingresar dinero en la cuenta")
    print("2. Retirar dinero de la cuenta")
    print("3. Mostrar dinero disponible")
    print("4. Salir")
    opcion = int(input("Digite un numero opcion de menu:\n"))

    print()

    if opcion ==1:
        extra = float(input("Cuando dinero deseas ingresar -->"))
        saldo_inicial += extra
        print(f"Dinero en la cuenta es de: -> ${saldo_inicial}")
    elif opcion==2:
        retirar = float(input("Cuanto dinero deseas ingresar -->"))
        if retirar > saldo_inicial:
            print("No tiene esa cantidad de dinero")
        else:
            saldo_inicial -= retirar
            print(f"Dinero en la cuenta es  de: --> ${saldo_inicial}")
    elif opcion==3:
        print(f"El dinero en la cuenta es de: --> ${saldo_inicial}")
    elif opcion==4:
        print("Gracias por utilizar su cajero automatico")
        break
    else:
        print("Error, se equivoco de opcion de menu")

print()
