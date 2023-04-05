#Diccionarios

'''
Tienen 2 elementos por posicion
'''

diccionario = {"azul":"blue","rojo":"red","verde":"green"}

print(diccionario["azul"])

diccionario["amarillo"] = "yellow"

print(diccionario)

'''
Para eliminar una clave se pone del
'''

del(diccionario["verde"])
print(diccionario)

'''
Creando una agenda
'''

agenda = {"Fernanda":[21,1.60],"Cordova":[22,1.67],"Felix":[25,1.36]}
print(agenda)
print(agenda["Fernanda"])
print()
equipo = {10:"Paulo Dybala",11:"Douglas Costa",7:"Cristiano Ronaldo"}
print(equipo.get(10,"No existe un jugador con ese  dorsal"))
print(equipo.get(1,"No existe un jugador con ese  dorsal"))

print(11 in equipo)

#Para que muestre solo los dorsales
print(equipo.keys())
#Para que muestren solo los nombres
print(equipo.values())
#Para que muestre todo
print(equipo.items())
#Tambien con un print normal
print(equipo)
#Para que diga cuantos elementos hay
print(len(equipo))
#Para limpiar el equipo
equipo.clear()
print(equipo)