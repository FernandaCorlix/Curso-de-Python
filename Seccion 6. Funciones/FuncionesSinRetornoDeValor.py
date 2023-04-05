#Funciones sin retorno de valor
print("Funciones sin retorno de valor\n")
#Como crear una funcion
def saludar():
    print("Holaa")

#Como llamar una funcion
saludar()

#Crear una funcion con parametro
def saludar(nombre):
    print(f"Holaa {nombre}")

#Como llamar una funcion
saludar("Luis")

def tabla_multiplicar(num):
    print("Tabla de multiplicar del num")
    for i in range (1,11):
        print(f"{num}*{i} = {num*i}")

tabla_multiplicar(5)

print()
print("\tFunciones con retorno de valor")

#Funciones con retorno de valor

def multiplicar(num1, num2):
    mult = num1 * num2
    return mult

#Puedes imprimirlo asi
print(multiplicar(5,2))
#Tambien asi
mult = multiplicar(5,2)

def prueba():
    return "Hola",45,[1,2,3]

#Se puede almacenar asi
print(prueba())
#Tambien asi
c,n,l = prueba()

print(c)
print(n)
print(l)


