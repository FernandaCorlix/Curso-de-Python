
Lista = []
Lista = [1,2,3,4,5,5,5,4,6,7,8,9,10]

print(f"Esta es la lista inicial:\n{Lista}")

conjunto = set(Lista)
print("Eliminando los conjuntos repetidos")
Lista = list(conjunto)
print(conjunto)

