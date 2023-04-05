 #Tuplas

'''
LAS TUPLAS NO SE MODIFICAN
'''

tupla = (4,"hola",6.78,[1,2,3],9)
print(tupla)

'''
Con las tuplas se pueden buscar
'''

print(4 in tupla)
print(tupla.index("hola"))
print(tupla.count(7))

#Transformar tuplas en listas

lista = list(tupla)

print(lista)
