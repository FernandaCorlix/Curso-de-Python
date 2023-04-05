'''
Desarrollar un programa que permita sumar los digitos de un numero
con ayuda de una funcion recursiva
'''

def sumaa(num):
   if num==0:
       resultado = 0
   else: #Caso Recursivo
       resultado = sumaa(int(num/10)) + (num%10)

   return resultado

valor = sumaa(160)
print(valor)