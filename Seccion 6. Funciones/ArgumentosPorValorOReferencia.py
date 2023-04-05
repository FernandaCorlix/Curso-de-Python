#Argumentos por valor o por referencia

#Este es el argumento por valor
def doblar_valor(numero):
    return numero *2

n = 5
n = doblar_valor(n)

print(n)

print()
#Argumentos por referencia

print("\tArgumentos por referencia")
def doblar_valores(numeros):
    for i,n in enumerate(numeros):
        numeros[i] *=2

n = [5,10,15,20]
#Para quedarte con los valores originales se pone
doblar_valores(n[:])
#Los valores doblados
doblar_valores(n)
print(n)
