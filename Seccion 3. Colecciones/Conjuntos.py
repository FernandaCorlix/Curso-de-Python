#Conjuntos

'''
Los elementos se agregan de forma desordenada
no puede a ver elementos repetidos
'''

conjunto = set()
conjunto = {1,2,3,4,"Hola",45.2,1,2,3}

#Para agregar elementos
conjunto.add(5)
conjunto.add(9)
conjunto.add(15)
conjunto.add("OA")

print(conjunto)
# Para eliminar elementos

conjunto.discard("OA")


print(conjunto)
print(3 in conjunto,"\n\n")


a = {1,2,3}
b = {3,4,5}

#Como hacer igualdades con conjuntos
print(a==b)
'''
Este es el conjunto = | 
'''
c = a | b
print(c)
c = a & b
print(c)
c= a - b
print(c)
print(a.issubset(c))

print(a.isdisjoint(b))