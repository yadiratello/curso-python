#Un diccionario es una estructura de datos q nos permite almacenar valores de diferentes tipo e incluso listas y otros diccionarios

#los datos se almacenan asociados a una clace de tal forma que se crea una asociacion clave:valor para cada elemento almacenado

miDiccionario = {"Alemania":"Berlin",
                "Francia":"Paris",
                "Peru":"Lima",
                "Colombia":"Bogota"}

#acceder a un elemento
print(miDiccionario["Peru"])


#Agregar mas elementos a mi diccionario
miDiccionario["Italia"]="Lisboa"
print(miDiccionario)

#modificar el valor de una clave
miDiccionario["Italia"]="Roma"
print(miDiccionario)

#como eliminar elementos
del miDiccionario["Italia"]
print(miDiccionario)

miDiccionario2 = {"Mexico":"Mexico DC", 23:"Jordan", "Mosqueteros":3}

print(miDiccionario2)


#desempaquetando de una tupla a un diccionario
mitupla = ["España","Francia","Chile","Bolivia"]

miDiccionario3 = {mitupla[0]:"Madrid",
                  mitupla[1]:"Paris",
                  mitupla[2]:"Santiago",
                  mitupla[3]:"Sucre"}

#acceder al valor de España
print(miDiccionario3["España"])


#creando un diccionario que contiene 1 diccionario y este tiene dentro una tupla
miDiccionario4 = {23:"Jordan",
                  "nombre":"Michael",
                  "equipo":"Chicago",
                  "anillos":{"temporadas":[1991,1992,1993,1996,1997,1998]}
                  }

print(miDiccionario4["anillos"])

#las claves
print(miDiccionario4.keys())
#los valores
print(miDiccionario4.values())
#longitud del diccionario
print(len(miDiccionario4))