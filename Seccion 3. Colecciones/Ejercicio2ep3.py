'''
Escriba un programa que tenga 2 listas y que
cree las siguientes listas (no debe de haber repeticiones)
-Lista de elmentos que aparecen en las dos listas
-Listas de elementos que aparezcan en la primera lista, pero no en la segunda
-Lista de elementos que aparecene n la segunda lista, pero no en la primera
-Lista de elementos que aparecen en ambas listas
'''

Lista1 = [1,2,3,4,5]
Lista2 = [2,4,6,8,10]

ll = set(Lista1)
ll2= set(Lista2)

print("Lista de elmentos que aparecen en las dos listas")
union = list(ll | ll2)
print(union,"\n")
print("Listas de elementos que aparezcan en la primera lista, pero no en la segunda")
SoloEnA = list(ll - ll2)
print(SoloEnA,"\n")
print("Lista de elementos que aparecene n la segunda lista, pero no en la primera")
SoloEnB = list(ll2 - ll)
print(SoloEnB,"\n")
print("Lista de elementos que aparecen en ambas listas")
Ambas = list(ll & ll2)
print(Ambas,"\n")