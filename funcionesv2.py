print("Funciones Version 2")
print("Victor Aleman")

# Zona de listas, tuplas, set y dicionario
celulares = ["Samsung a52", "Iphone 11", "Chafa"]
LenguajesProgramaticos = ("Python", "Javascript", "Java", "C++", "C#")
PlantasExoticas = {"Planta de Hielo", "Nopal Serrero", "Hierba Nudosa Japonesa", "Fallopia baldschuanica", "Altamisa"}
canciones = {
    "Hasta que llegue el alba": "Pepe Aguilar",
    "Ahora te puedes marchar": "Luis Miguel",
    "Noviembre sin ti": "Reik",
    "Cuando Me Enamoro": "Enrique Iglesias_Juan Luis Guerra"
}

# Zona de funciones
def verlista(telefonos):
    for uncelular in telefonos:
        print (uncelular)

def vertupla(lenguajes):
    for unLenguaje in lenguajes:
        print(unLenguaje)

def verSet(plantas):
    for unaPlanta in plantas:
        print(unaPlanta)

def verDiccionario(canciones):
    for unaCancion in canciones:
        print(unaCancion, "----" ,canciones[unaCancion])

#Llamadas a funciones
print("Imprime celulares de una lista")
verlista(celulares)

print("Imprime Lenguajes de Programacion de una tupla")
vertupla(LenguajesProgramaticos)

print("Imprime Plantas exoticas de un conjunto (set)")
verSet(PlantasExoticas)

print("Imprime Canciones con su Autor de un diccionario")
verDiccionario(canciones)