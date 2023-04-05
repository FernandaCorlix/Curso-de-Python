'''
Una tienda ofrece un  descuento del 15% sobre el total de la compra
y un cliente desea saber cuando debera pagar finalmente por su compra
'''

precio = float(input("Ingresa el precio del producto: "))
descuento = precio * 0.15

total = precio - descuento

print(f"El precio final a pagar es de ${total:2f}")