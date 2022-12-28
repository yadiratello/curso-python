#las tuplas son listas inmutables, es decir no se pueden modificar despues de su creacion

#no permiten añadir, eliminar, mover elementos etc
#ventajas: son mas rapidas, ocupan menos espacio, formatean Strings, pueden utilizarse como claves en un diccionario


#Definiendo una tupla
miTupla = ("Yadira",12,12,2022)

print(miTupla)


#Convertir una tupla a una lista usamos el metodo list
miLista = list(miTupla)

print(miLista)


#Convertir una Lista a una Tupla usamos el metodo tuple
miNuevaTupla = tuple(miLista)

print(miNuevaTupla)


#ver si hay elementos
print("Yadira" in miTupla)
print(123 in miLista)

#count: averigua cuantos elementos se encuentran dentro de mi tupla
print(miTupla.count("Yadira"))

#len: permite averiguar la cantidad de elementos de una tupla
print(len(miTupla))

#desempaquetado de tuplas: consiste en asignar los elementos de mi tupla como valor de mis variables
nombre, dia, mes, anio = miTupla

print(nombre,dia,mes,anio)