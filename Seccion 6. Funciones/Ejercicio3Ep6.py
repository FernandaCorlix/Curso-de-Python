'''

Crear un programa que tenga una lista de clientes, cada cliente tiene
su Nombre, Apellido y DNI. El programa tendra el siguiente menu de opciones:
1. Agregar nuevo cliente
2. Mostrar todos los clientes
3. Mostrar por DNI
4. Eliminar Cliente
5. Salir
'''

def agg_cliente(clientes, nombre, apellido, dni):
    cliente = {}
    cliente['nombre'] = nombre
    cliente['apellido'] = apellido
    cliente['dni'] = dni
    clientes.append(cliente)

def showclientes(clientes):
    for i in clientes:
        print(f"Nombre: {i['nombre']}, Apellido: {i['apellido']}, DNI: {i['dni']}")

def showdni(clientes,dni):
    for i in clientes:
        if i['dni'] == dni:
            print(f"El DNI del cliente {i['nombre']}, es: {i['dni']}")
        return False

def delete(clientes, nombre):
    for i in clientes:
        if i['nombre'] == nombre:
           clientes.remove(i)
           return True
    return False


clientes = []

while True:
    print("\t.: Menu de clientes : .")
    print("""
    1. Agregar nuevo cliente
    2. Mostrar todos los clientes
    3. Mostrar por DNI
    4. Eliminar Cliente
    5. Salir""")
    opciones = int(input("Ingresa opcion a realizar: "))
    print()

    if opciones == 1:
        nombre = input("Nombre del cliente -> ")
        apellido = input("Apellido de cliente -> ")
        DNI = input("DNI de cliente ->")
        agg_cliente(clientes,nombre,apellido,DNI)
    elif opciones == 2:
        showclientes(clientes)
        print()
    elif opciones == 3:
        dni = input("Ingresa el dni que buscas --> ")
        if showdni(clientes,DNI):
            showdni(clientes,DNI)
        else:
            print("Cliente no encontrado")
        print()
    elif opciones == 4:
        nombre = input("Ingresa el nombre del cliente a eliminar -> ")
        if delete(clientes,nombre):
            delete(clientes,nombre)
        else:
            print("No se encontro el cliente que se buscaba eliminar")
        print()
    elif opciones == 5:
        print("Adios")
        break
