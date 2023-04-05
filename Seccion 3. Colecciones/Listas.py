
# Listas

#Lista vacia
lista = []

lista = ["Lunes","Martes","Miercoles", "Jueves", "Viernes"]
print(lista)

#Para imprimir una ubicacion en especifico
print(lista[4])

#El indice -1 indica el ultimo elemento
print(lista[-1])

#Se puede trabajar con sub listas
print(lista[0:3])

#Con la funcion len te da el tamaño
print(len(lista))

lista2 = [1,2,3,4,5]

#Como agregarle elementos ala lista

lista2.append(6)
print(lista2)

#Agregar un elemento en una  ubicacion especifica

lista2.insert(2,9)
print(lista2)

#Con el metodo extend se ponen al ultimo elementos

lista2.extend([6,7,10])
print(lista2)

lista3 = lista + lista2
print(lista3)

#Como se sabe si algun elemento se encuentra en la lista

print(10 in lista2)

#Para saber en que indice se encuentra el elemento

print(lista3.index(4))

#Para que te diga cuantas veces sale algo
print("Salio")
print(lista3.count(10))

#Para eleminar

lista2.pop(2)

print(lista2)

lista.remove("Martes")
print(lista)

#Para eliminar TODOS los elementos de la lista
lista.clear()

