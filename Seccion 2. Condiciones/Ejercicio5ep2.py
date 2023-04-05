'''
Hacer un programa que simule un cajero automatico
con un saldo inicial de $1000 y entra el siguien
menu de opciones:

1. Ingresar dinero en la cuento
2. Retirar dinero de la cuenta
3. Mostrar dinero disponible
4. Salir

'''

saldo_inicial = 1000

print("Ingrese un numero para realizar la operacion que desee:")
print("1. Ingresar dinero en la cuenta")
print("2. Retirar dinero de la cuenta")
print("3. Mostrar dinero disponible")
print("4. Salir")
numero = int(input("Digite el numero: "))

if numero == 1:
    print("¿Cuanto dinero deseas agregarle a la cuenta?")
    ingresar = float(input("-->"))

    saldo = saldo_inicial + ingresar
    print(f"El nuevo saldo es de: {saldo}")

if numero == 2:
    print("¿Cuanto dinero deseas retirar?")
    retirar = float(input("-->"))

    saldo = saldo_inicial - retirar
    print(f"El nuevo saldo es de: {saldo}")

if numero == 3:
    print(f"El saldo disponible es de: {saldo_inicial}")
if numero == 4:
    exit("Haz salido del cajero")


