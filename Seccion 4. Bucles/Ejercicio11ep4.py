'''
Hacer un programa que simule una agenda de contactos. Crear un diccionar donde la clave
sea el nombre del usuario y el valor sea el telefono, el programa tendra el siguiente menu de opciones:

1. Nuevo contacto
2. Borrar contacto
3. Ver contactos existentes
4. Salir

'''

agenda = {}

while True:

    print("\t.:Menu de Agenda de contactos:.")
    print("1. Nuevo contacto")
    print("2. Borrar contacto")
    print("3. Ver contactos existentes")
    print("4. Salir")
    opcion = int(input(" Digite una opcion de menu: \n"))

    print()

    if opcion == 1:
        nombre = input("Ingrese el numbre del usuario:\n")
        telefono = input("Ingrese el numero de telefono:\n")

        if nombre not in agenda:
            agenda[nombre] = telefono
            print("Contacto agregado correctamente")
        else:
            print("Ese nombre de contacto ya existe")

    elif opcion == 2:
        nombre = input("Ingrese el numbre del usuario:\n")
        if nombre in agenda:
            del(agenda[nombre])
            print("Contacto eliminado")
        else:
            print("No se encontre el elemento a borrar")
    elif opcion == 3:
        print(f"Agenda de contactos --> \n")
        for clave, valor in agenda.items():
            print(f"Nombre: {clave}, \ntelefono: {valor}")
            print("----------------------------------------")
    elif opcion == 4:
        print("Gracias por utilizar su agenda de contactos")
        break
    else:
        print("Error, numero no encontrado")

print("----------------------------------------------------------")
