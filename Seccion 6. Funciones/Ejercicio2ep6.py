'''
Hacer un programa que pida la anchura y altura de un rectangulo y con
ayuda de una funcion lo dibuje con *
'''

def dibujar(ancho,alto):
    for i in range(alto):
        for j in range(ancho):
            print("* ",end="")
        print()

ancho = int(input("Ingresa la anchura:\n"))
altura = int(input("Ingresa la altura:\n"))
dibujar(ancho,altura)


