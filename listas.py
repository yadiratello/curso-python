miLista=["Yadira","Pedro","Carmen","Luna",123, False]

print(miLista[:])#lista todos los elementos de mi lista
print(miLista[1])#lista el elemento 2

#porcion de lista(acceder a untrozo de mi lista)

print(miLista[0:3])#lista los 3 primeros elementos de mi lista
print(miLista[:3])

print(miLista[3:])#lista desde el indice 2 hasta el final)

#Agregar elementos a mi lista

#Agregar al final de mi lista
miLista.append("Juan Gabriel")

#Agregar 1 elemento en cualquier lugar de lista 
miLista.insert(1,"Lucia")

#Agregar varios elementos a mi lista
miLista.extend(["Norma","Sonia","Rubi"])

print(miLista[:])#lista todos los elementos de mi lista


#mostrar el indice de un elemento
print(miLista.index("Pedro"))

#comprobar si un elemento se encuentra o no en una lista
print("Yadira" in miLista)


#verificar si existe un elemnto en esa posicion
print(miLista[7])

#Eliminar un elemento de mi lista
miLista.remove(123)

#Eliminar el ultimo elemento de mi lista
miLista.pop()

print(miLista[:])#lista todos los elementos de mi lista


#Unir 2 listas
miLista1=[12,22,33]
miLista2=[99,88,77]
miLista3 = miLista1 + miLista2

print(miLista3[:])

#repetir 3 veces mi lista3
print(miLista3[:]*3)



